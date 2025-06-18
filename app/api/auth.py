# handles all auth-related endpoints: login, callback, logout, etc.

from fastapi import APIRouter, Depends, HTTPException, Response, Cookie
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.session import get_db
from app.db.models import User
import os
import httpx

router = APIRouter()

GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
REDIRECT_URI = os.getenv("GITHUB_REDIRECT_URI") # e.g., "http://localhost:8000/auth/github/callback"

SESSION_COOKIE_NAME = "git_to_blog_user_id"

@router.get('/auth/github/login')
def github_login():
    github_auth_url = (
        f"https://github.com/login/oauth/authorize"
        f"?client_id={GITHUB_CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        f"&scope=repo"
    )
    return RedirectResponse(github_auth_url)


@router.get('/auth/github/callback')
async def github_callback(code: str, db: AsyncSession = Depends(get_db)):
    async with httpx.AsyncClient() as client:
        # Exchange code for access token
        response = await client.post(
            "https://github.com/login/oauth/access_token",
            data={
                "client_id": GITHUB_CLIENT_ID,
                "client_secret": GITHUB_CLIENT_SECRET,
                "code": code,
                "redirect_uri": REDIRECT_URI
            },
            headers={"Accept": "application/json"}
        )
        token_data = response.json()
        access_token = token_data.get("access_token")
        if not access_token:
            raise HTTPException(status_code=400, detail="Failed to get access token from GitHub.")

        # Fetch user info from GitHub
        user_resp = await client.get(
            "https://api.github.com/user",
            headers={"Authorization": f"token {access_token}"}
        )
        if user_resp.status_code != 200:
            raise HTTPException(status_code=400, detail="Failed to fetch user info from GitHub.")
        user_data = user_resp.json()
        github_id = str(user_data["id"])
        name = user_data.get("name") or user_data.get("login")
        email = user_data.get("email") or ""

        # Upsert user in DB
        result = await db.execute(select(User).where(User.github_id == github_id))
        user = result.scalar_one_or_none()
        if user is None:
            user = User(
                github_id=github_id,
                name=name,
                email=email,
                github_access_token=access_token
            )
            db.add(user)
        else:
            user.github_access_token = access_token
            user.name = name
            user.email = email
        await db.commit()

        # Set session cookie
        response = RedirectResponse(url="/") # Redirect to home 
        response.set_cookie(key=SESSION_COOKIE_NAME, value=str(user.id), httponly=True, max_age=60*60*24*7)
        return {"message": "User authenticated", "user_id": user.id}

@router.get('/auth/logout')
async def logout(response: Response, user_id: int = Cookie(), db: AsyncSession = Depends(get_db)):
    if not user_id:
        raise HTTPException(status_code=401, detail="Not logged in.")
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    user.github_access_token = ""
    await db.commit()
    response.delete_cookie(SESSION_COOKIE_NAME)
    return {"message": "Logged out successfully"}