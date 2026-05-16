import os
import time
from app.config.settings import TEMP_DIR, CLEANUP_MINUTES

def cleanup_old_files():
    now = time.time()

    for file in os.listdir(TEMP_DIR):
        path = os.path.join(TEMP_DIR, file)

        if os.path.isfile(path):
            age = now - os.path.getmtime(path)

            if age > CLEANUP_MINUTES * 60:
                os.remove(path)