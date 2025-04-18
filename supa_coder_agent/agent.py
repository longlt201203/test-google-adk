from google.adk.agents import Agent
from .prompts import instructions
from .sub_agents import ba_agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.sessions import InMemorySessionService
from .disk_artifact_service import DiskArtifactSerivce
from google.adk.runners import Runner
from global_vars import APP_NAME
import os

AGENT_MODEL = "gemini-2.5-flash-preview-04-17"
# AGENT_MODEL = "gemini-2.0-flash"

root_agent = Agent(
    name="supa_coder",
    description="An expert in coding and debugging",
    model=AGENT_MODEL,
    instruction=instructions,
    tools=[AgentTool(ba_agent)],
    sub_agents=[ba_agent]
)

artifact_service = DiskArtifactSerivce(os.path.join(os.getcwd(), "resources/artifacts"))
session_service = InMemorySessionService()

root_runner = Runner(
    app_name=APP_NAME,
    agent=root_agent,
    session_service=session_service,
    artifact_service=artifact_service
)