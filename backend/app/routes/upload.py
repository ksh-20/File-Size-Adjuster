from fastapi import APIRouter, UploadFile, File, HTTPException
from app.utils.validators import (
    validate_type,
    validate_size
)
from app.utils.file_utils import (
    generate_file_id,
    safe_filename
)
from app.services.file_service import save_upload
import os

router = APIRouter()


@router.post('/upload')
async def upload(file: UploadFile = File(...)):
    if not validate_type(file.content_type):
        raise HTTPException(
            status_code=400,
            detail='Unsupported file type'
        )

    content = await file.read()

    if not validate_size(len(content)):
        raise HTTPException(
            status_code=400,
            detail='File exceeds 100MB limit'
        )

    file.file.seek(0)

    safe_name = safe_filename(file.filename)

    ext = safe_name.split('.')[-1]

    file_id = f'{generate_file_id()}.{ext}'

    path = save_upload(file, file_id)

    return {
        'file_id': file_id,
        'filename': safe_name,
        'size': os.path.getsize(path)
    }