from fastapi import APIRouter
import os
from app.config.settings import TEMP_DIR

router = APIRouter()

@router.delete("/cleanup/{file_id}")
async def cleanup(file_id: str):
    path = os.path.join(TEMP_DIR, file_id)

    if os.path.exists(path):
        os.remove(path)

    return {"message": "Deleted"}