from pydantic import BaseModel

class ProcessRequest(BaseModel):
    file_id: str
    target_size: float
    unit: str
    operation: str