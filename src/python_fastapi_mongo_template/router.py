from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def _():
    return {"message": "hello world"}
