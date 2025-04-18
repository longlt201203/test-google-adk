from google.adk.agents import Agent
from .instruction import instruction
from .tools import analyze_project_design_tool

AGENT_MODEL = "gemini-2.0-flash"

root_agent = Agent(
    name="supa_dev",
    description="Developer Expert",
    model=AGENT_MODEL,
    instruction=instruction,
    tools=[]
)