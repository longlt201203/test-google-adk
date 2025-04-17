from google.adk.agents import Agent
from .prompts import instructions
from .sub_agents import ba_agent
from google.adk.tools.agent_tool import AgentTool

AGENT_MODEL = "gemini-2.0-flash"

root_agent = Agent(
    name="supa_coder",
    description="An expert in coding and debugging",
    model=AGENT_MODEL,
    instruction=instructions,
    tools=[AgentTool(ba_agent)]
)