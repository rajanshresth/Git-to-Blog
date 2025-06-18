# handles user-related endpoint:
#   list repos, select repos, profile, etc.

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from app.db.session import get_db
from app.db.models import User, TrackedRepo
import httpx

router = APIRouter()

@router.get('/user/repos')
async def list_repos(user_id: int, db: AsyncSession = Depends(get_db)):
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
async def select_repos(user_id: int, selected_repos: list, db: AsyncSession = Depends(get_db)):
    # Remove old tracked repos
    await db.execute(delete(TrackedRepo).where(TrackedRepo.user_id == user_id))
    # Add new tracked repos
    for repo in selected_repos:
        tracked = TrackedRepo(
            user_id=user_id,
            repo_id=str(repo["id"]),
            repo_name=repo["name"]
        )
        db.add(tracked)
    await db.commit()
    return {"message": "Repositories selected"}