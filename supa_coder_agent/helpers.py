import uuid
from global_vars import APP_NAME
from .agent import session_service, root_runner
from google.genai import types
import asyncio

def create_session(user_id: str):
    session_id = uuid.uuid4().__str__()

    session_service.create_session(
        session_id=session_id,
        user_id=user_id,
        app_name=APP_NAME
    )

    return session_id

async def interact(user_id: str, session_id: str, query: str):
    content = types.Content(role='user', parts=[types.Part(text=query)])

    final_response_text = "Agent did not produce a final response."

    async for event in root_runner.run_async(user_id=user_id, session_id=session_id, new_message=content):
        if event.is_final_response():
            if event.content and event.content.parts:
                # Assuming text response in the first part
                final_response_text = event.content.parts[0].text
            elif event.actions and event.actions.escalate: # Handle potential errors/escalations
                final_response_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
                # Add more checks here if needed (e.g., specific error codes)
            break

    return final_response_text