import os
import base64
from google.adk.tools.tool_context import ToolContext
from google.genai import types

PROJECTS_FOLDER_PATH = "resources/projects"

def load_project_design_tool(project_name: str, tool_context: ToolContext):
    """Tool to load the project design tool to the context"""
    files = tool_context.list_artifacts()

    print(files)
    
    # find design file in project
    design_file = None
    for file in files:
        if file.startswith("design"):
            design_file = file
            break

    # use pillow to analyze design file
    if design_file is None:
        return None

    return tool_context.load_artifact(design_file)

def store_user_image(image: types.Part):
    """
    Tool to handle user image
    """
    print("Handling user image")
    print(image.inline_data.mime_type)
    with os.open("test.img", "w") as f:
        f.write(base64.b64decode(image.inline_data.data))

def get_project_design_tool(project_name: str) -> str:
    """
    Tool to get the project design

    Args:
        project_name (str): Project name

    Returns:
        str: Project design image as base64 string
    """
    project_path = os.path.join(PROJECTS_FOLDER_PATH, project_name)
    if not os.path.exists(project_path):
        return { "status": "error", "message": "Project not found" }
    
    files = os.listdir(project_path)
    if len(files) == 0:
        return { "status": "error", "message": "Project is empty" }
    
    # find design file in project
    design_file = None
    for file in files:
        if file.startswith("design"):
            design_file = file
            break

    # use pillow to analyze design file
    if design_file is None:
        return { "status": "error", "message": "Design file not found" }
        
    design_file_path = os.path.join(project_path, design_file)
    
    with open(design_file_path, "rb") as f:
        encoded = base64.b64encode(f.read())

        return { "status": "success", "message": encoded.decode("utf-8") }