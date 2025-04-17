from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from .sub_agents import db_agent
from .tools import say_hi_tool, update_job_state_tool
from google.adk.tools.agent_tool import AgentTool
from .prompts import instructions

AGENT_MODEL = "gemini-2.0-flash"

root_agent = Agent(
    name="my_agent",
    description="My personal agent",
    model=AGENT_MODEL,
    instruction=instructions,
    tools=[say_hi_tool, AgentTool(agent=db_agent), update_job_state_tool],
    # sub_agents=[db_agent]
)