from fastapi import APIRouter, Depends, status, Query, HTTPException
from fastapi.responses import JSONResponse

from app.utils import get_current_active_user, get_db_creds
from app.models import FindOneUserModel, User
from app.database import DBManager

db = DBManager(get_db_creds())
router: APIRouter = APIRouter()

@router.get("/")
async def home_root(
    current_user: User = Depends(get_current_active_user),
) -> JSONResponse:
    return JSONResponse(
        content={"user": current_user.username}, status_code=status.HTTP_200_OK
    )

@router.get("/search")
async def home_root_query(_:User = Depends(get_current_active_user), user:str = Query(...)) -> JSONResponse:
    user = await db.db_find_one(FindOneUserModel(user=user), collection="dashboard")
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error":f"User {user} not found"}
        )
    return JSONResponse(
        content={"user":FindOneUserModel(**user).dict()}, status_code=status.HTTP_200_OK
    )