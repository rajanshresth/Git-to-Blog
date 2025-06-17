import hashlib
import hmac
import os
import logging
from typing import List, Optional
from fastapi import APIRouter, Request, HTTPException, Header, status
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from pydantic import BaseModel, HttpUrl

# Load environment variables
load_dotenv()

# Set up logging
logger = logging.getLogger("webhook")
logging.basicConfig(level=logging.INFO)

router = APIRouter()

# Get webhook secret from environment variable
WEBHOOK_SECRET = os.getenv("GITHUB_WEBHOOK_SECRET")

if not WEBHOOK_SECRET:
    raise RuntimeError("GITHUB_WEBHOOK_SECRET is not set in environment variables.")

MAX_PAYLOAD_SIZE = 1024*1024 # 1MB

class Author(BaseModel):
    name: str
    email: str
    username: Optional[str] = None

class Commit(BaseModel):
    id: str
    message: str
    timestamp: Optional[str]
    author: Optional[Author] = None
    url: Optional[HttpUrl] = None

class Repository(BaseModel):
    full_name: str
    private: bool
    description: Optional[str] = None
    url: Optional[HttpUrl] = None  # This is present in your payload

class WebhookPayload(BaseModel):
    repository: Repository
    commits: List[Commit]
    ref: str
    before: str
    after: str
    created: Optional[bool] = False
    deleted: Optional[bool] = False
    forced: Optional[bool] = False

def verify_signature(payload_body: bytes, signature_header: str) -> bool:
    if WEBHOOK_SECRET is None:
        raise RuntimeError("GITHUB_WEBHOOK_SECRET is not set in environment variables.")

    if not signature_header:
        logger.warning("No signature header provided.")
        return False

    if "=" in signature_header:
        algo, signature = signature_header.split("=")
    else:
        algo="sha256"
        signature = signature_header

    if algo != "sha256":
        logger.warning("Unsupported signature algorithm: %s", algo)
        return False
    
    expected_signature = hmac.new(
        WEBHOOK_SECRET.encode(),
        payload_body,
        hashlib.sha256
    ).hexdigest()

    is_valid = hmac.compare_digest(expected_signature, signature)
    if not is_valid:
        logger.warning("Signature mismatch.")
    return is_valid

@router.post("/webhook")
async def github_webhook(
    request: Request,
    x_hub_signature_256: str = Header(None),
    x_github_event: str = Header(None)
):
    body = await request.body()
    # Limit payload size
    if len(body) > MAX_PAYLOAD_SIZE:
        logger.error("Payload too large: %d bytes", len(body))
        raise HTTPException(status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, detail="Payload too large")

    # Verify signature
    if not verify_signature(body, x_hub_signature_256):
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"error": "Invalid signature"})

    try:
        payload_dict = await request.json()
        payload = WebhookPayload(**payload_dict)
    except Exception as e:
        logger.error("Payload parsing error: %s", str(e))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Payload parsing error: {str(e)}")

    # Log event type
    logger.info("Received event: %s for repo: %s", x_github_event, payload.repository.full_name)

    # Example: handle push event
    if x_github_event == "push":
        commit_messages = [commit.message for commit in payload.commits]
        logger.info("Received %d commits.", len(commit_messages))
        return {
            "message": "Webhook received and verified ✅",
            "repository": payload.repository.full_name,
            "commits": commit_messages
        }
    else:
        logger.info("Unhandled event type: %s", x_github_event)
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": f"Event {x_github_event} received but not handled."})
