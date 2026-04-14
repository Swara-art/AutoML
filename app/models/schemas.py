from pydantic import BaseModel

class PredictRequest(BaseModel):
    data: dict