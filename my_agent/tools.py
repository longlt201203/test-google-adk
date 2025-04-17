from google.adk.tools.tool_context import ToolContext

def say_hi_tool(userinfo: dict, tool_context: ToolContext) -> str:
    """Tool to get the say hi message"""

    name = userinfo["name"]
    job = tool_context.state.get("user_job")
    if job:
        return f"Hi {name}, how are you? I know for a fact that you are a/an {job}."

    return f"Hi {name}, how are you?"

def update_job_state_tool(job: str, tool_context: ToolContext):
    """Tool to update the job state"""

    tool_context.state["user_job"] = job