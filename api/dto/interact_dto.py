from pydantic import BaseModel

class InteractDto(BaseModel):
    userId: str
    sessionId: str
    message: str