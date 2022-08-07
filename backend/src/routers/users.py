from fastapi import APIRouter
from fastapi.responses import JSONResponse
router:APIRouter = APIRouter(prefix="/users")

@router.get("/{user_id}")
async def get_user(user_id) -> JSONResponse:
    return JSONResponse(status_code=200, content={"detail":"Implement this"}) # TODO