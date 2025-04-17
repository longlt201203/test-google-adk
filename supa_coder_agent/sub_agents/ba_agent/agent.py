from google.adk.agents import Agent
from .prompts import instructions
from .tools import analyze_project_design_tool

AGENT_MODEL = "gemini-2.0-flash"

root_agent = Agent(
    name="ba_agent",
    description="Agent that acts as a BA in a project",
    model=AGENT_MODEL,
    instruction=instructions,
    tools=[analyze_project_design_tool],
)