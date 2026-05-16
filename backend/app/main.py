from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import upload, process, download, cleanup
from app.services.cleanup_service import cleanup_old_files
import threading
import time

app = FastAPI()

origins = [
    "http://localhost:5173",
    "https://file-size-adjuster.onrender.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router)
app.include_router(process.router)
app.include_router(download.router)
app.include_router(cleanup.router)

def cleanup_loop():
    while True:
        cleanup_old_files()
        time.sleep(60)

threading.Thread(target=cleanup_loop, daemon=True).start()

@app.get("/")
async def root():
    return {"message": "File Size Adjuster API"}