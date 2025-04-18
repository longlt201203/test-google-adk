from typing import Union
from fastapi import FastAPI
from .dto import CreateSessionDto, InteractDto
from supa_coder_agent.helpers import create_session as agent_create_session, interact as agent_interact
import asyncio

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/create-session")
def create_session(dto: CreateSessionDto):
    session_id = agent_create_session(user_id=dto.userId)

    return { "session_id": session_id }

@app.post("/interact")
async def interact(dto: InteractDto):
    result = await agent_interact(
        user_id=dto.userId,
        session_id=dto.sessionId,
        query=dto.message
    )

    return { "result": result }

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
