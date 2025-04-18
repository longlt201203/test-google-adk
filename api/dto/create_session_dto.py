from pydantic import BaseModel

class CreateSessionDto(BaseModel):
    userId: str