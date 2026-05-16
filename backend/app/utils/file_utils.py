import uuid
import os

def generate_file_id():
    return str(uuid.uuid4())

def get_extension(filename):
    return filename.split(".")[-1]

def safe_filename(filename):
    return filename.replace("/", "").replace("\\", "")