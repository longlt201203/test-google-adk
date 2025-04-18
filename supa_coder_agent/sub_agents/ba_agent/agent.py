from google.adk.agents import Agent
from .prompts import instructions
from .tools import load_project_design_tool, store_user_image
from google.adk.models.lite_llm import LiteLlm

# AGENT_MODEL = LiteLlm(model="claude-3-5-sonnet-latest")
AGENT_MODEL = "gemini-2.5-flash-preview-04-17"

root_agent = Agent(
    name="ba_agent",
    description="Agent that acts as a Business Analyst in a project",
    model=AGENT_MODEL,
    instruction=instructions,
    tools=[load_project_design_tool, store_user_image],
)