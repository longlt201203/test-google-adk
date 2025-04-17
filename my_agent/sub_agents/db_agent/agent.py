from google.adk.agents import Agent
from my_agent.db.users import get_user_info

AGENT_MODEL = "gemini-2.0-flash"

tools = [
    get_user_info
]

root_agent = Agent(
    name="db_agent",
    description="Database agent",
    model=AGENT_MODEL,
    instruction=(
        "You are an agent that provides data from a database. Your only job is to provide the data to the user or the agent that calls you."
    ),
    tools=tools
)