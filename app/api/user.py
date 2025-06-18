# handles user-related endpoint:
#   list repos, select repos, profile, etc.


from fastapi import APIRouter, Depends, HTTPException
import httpx

router = APIRouter()

# Dependency to get current user's access token (implement this for your auth/session system)
def get_current_user_token():
    # TODO: Implement actual user session/token retrieval
    return "user_access_token"

@router.get('/user/repos')
async def list_repo(token: str = Depends(get_current_user_token)):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://api.github.com/user/repos",
            headers={"Authorization": f"token {token}"}
        )
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Failed to fetch repos")
        return response.json()

@router.post("/user/select-repos")
async def select_repos(selected_repos: list, token: str = Depends(get_current_user_token)):
    # TODO: Store selected repos in your database, associated with the user
    print(f'Selected Repos: {select_repos}')
    print(f'token: {token}')
    return {"message": "Repositories selected", "repos": selected_repos}