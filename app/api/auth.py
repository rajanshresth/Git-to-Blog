# handles all auth-related endpoints: login, callback, logout, etc.

from urllib import response
from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse
import os
import httpx

router = APIRouter()

GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
REDIRECT_URI = os.getenv("GITHUB_REDIRECT_URI") # e.g., "http://localhost:8000/auth/github/callback"

@router.get('/auth/github/login')
def github_login():
    print(f'\n\nredirect_uri: {REDIRECT_URI}\n\n')
    github_auth_url = (
        f"https://github.com/login/oauth/authorize"
        f"?client_id={GITHUB_CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        f"&scope=repo"
    )
    return RedirectResponse(github_auth_url)

@router.get('/auth/github/callback')
async def github_callback(code:str):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://github.com/login/oauth/access_token",
            data={
                "client_id": GITHUB_CLIENT_ID,
                "client_secret": GITHUB_CLIENT_SECRET,
                "code": code,
                "redirect_uri": REDIRECT_URI
            },
            headers={"Accept":"application/json"}
        )
        token_data = response.json()
        access_token = token_data.get("access_token")
        # TODO: Store access_token securely, associate with user session/account
        print(f'access_token: {access_token}')
        return {"access_token": access_token}
