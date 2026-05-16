from fastapi import APIRouter, HTTPException
from app.models.schemas import ProcessRequest
from app.utils.size_utils import convert_to_bytes
from app.config.settings import TEMP_DIR
from app.services.image_service import adjust_image_size
from app.services.pdf_service import adjust_pdf_size
from app.services.docx_service import adjust_docx_size
import os
import uuid

router = APIRouter()

@router.post("/process")
async def process(req: ProcessRequest):
    input_path = os.path.join(TEMP_DIR, req.file_id)

    if not os.path.exists(input_path):
        raise HTTPException(404, "File not found")

    ext = req.file_id.split(".")[-1].lower()

    output_name = f"{uuid.uuid4()}.{ext}"

    output_path = os.path.join(TEMP_DIR, output_name)

    target = convert_to_bytes(req.target_size, req.unit)

    if ext in ["jpg", "jpeg", "png", "webp"]:
        adjust_image_size(input_path, output_path, target, req.operation)

    elif ext == "pdf":
        adjust_pdf_size(input_path, output_path, target, req.operation)

    elif ext == "docx":
        adjust_docx_size(input_path, output_path, target, req.operation)

    else:
        raise HTTPException(400, "Unsupported type")

    return {
        "processed_file_id": output_name,
        "download_url": f"/download/{output_name}",
        "final_size": os.path.getsize(output_path)
    }