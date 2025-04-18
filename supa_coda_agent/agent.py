from google.adk.agents import LlmAgent
from .instruction import instruction
from .tools import analyze_project_design_tool
from .sub_agents import supa_ba_agent, supa_dev_agent
from google.adk.tools.agent_tool import AgentTool

AGENT_MODEL = "gemini-2.0-flash"

root_agent = LlmAgent(
    name="supa_coda",
    description="Coding expert",
    model=AGENT_MODEL,
    instruction=instruction,
    # tools=[AgentTool(supa_ba_agent)],
    sub_agents=[supa_ba_agent, supa_dev_agent]
)