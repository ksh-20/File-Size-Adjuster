import os
import shutil
from app.config.settings import TEMP_DIR

os.makedirs(TEMP_DIR, exist_ok=True)

def save_upload(file, file_id):
    path = os.path.join(TEMP_DIR, file_id)

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return path