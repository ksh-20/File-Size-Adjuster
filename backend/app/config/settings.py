from dotenv import load_dotenv
import os

load_dotenv()

TEMP_DIR = os.getenv("TEMP_DIR", "app/temp")
MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE", 104857600))
CLEANUP_MINUTES = int(os.getenv("CLEANUP_MINUTES", 5))