from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from app.config.settings import TEMP_DIR
import os

router = APIRouter()


@router.get('/download/{file_id}')
async def download(file_id: str):
    path = os.path.join(TEMP_DIR, file_id)

    if not os.path.exists(path):
        raise HTTPException(
            status_code=404,
            detail='File not found'
        )

    return FileResponse(
        path,
        filename=file_id,
        media_type='application/octet-stream'
    )