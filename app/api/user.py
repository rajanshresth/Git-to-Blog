# handles user-related endpoint:
#   list repos, select repos, profile, etc.

from typing import List
from fastapi import APIRouter, Body, Cookie, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from app.db.session import get_db
from app.db.models import User, TrackedRepo
import httpx

router = APIRouter()

class RepoSelection(BaseModel):
    id: int
    name: str

@router.get('/user/repos')
async def list_repos(
        user_id: int = Cookie(None,alias="git_to_blog_user_id"),
        db: AsyncSession = Depends(get_db)
    ):
        print(f'[DEBUG]: user_id: {user_id}')
        if not user_id:
            raise HTTPException(status_code=404, detail="User not found")
        # Fetch user from DB
        result = await db.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        # Fetch repos from GitHub
        async with httpx.AsyncClient() as client:
            resp = await client.get(
                "https://api.github.com/user/repos",
                headers={"Authorization": f"token {user.github_access_token}"}
            )
            if resp.status_code != 200:
                raise HTTPException(status_code=400, detail="Failed to fetch repos from GitHub.")
            return resp.json()

@router.post('/user/select-repos')
async def select_repos(
    selected_repos: List[RepoSelection] = Body(...),
    user_id: int = Cookie(None,alias="git_to_blog_user_id"),
    db: AsyncSession = Depends(get_db)
):
    print(f'[DEBUG]: user_id: {user_id}')
    if not user_id:
        raise HTTPException(status_code=401, detail="Not logged in.")
    # Remove old tracked repos
    await db.execute(delete(TrackedRepo).where(TrackedRepo.user_id == user_id))
    # Add new tracked repos
    for repo in selected_repos:
        tracked = TrackedRepo(
            user_id=user_id,
            repo_id=str(repo.id),
            repo_name=repo.name
        )
        db.add(tracked)
    await db.commit()
    return {"message": "Repositories selected"}