from .supa_anthropic import send_message_with_image as anthropic_send_message_with_image
from .supa_guguru import send_message_with_image as google_send_message_with_image
from typing import Optional
import os

PROJECTS_PATH = "resources/projects"

def find_desgin_file(projectName: str) -> Optional[str]:
    path = os.path.join(PROJECTS_PATH, projectName)
    if not os.path.exists(path):
        return None

    files = os.listdir(path)
    for f in files:
        if f.startswith("design"):
            return os.path.join(path, f)

    return None


def analyze_project_design_tool(projectName: str, query: str):
    """Tool to analyze the project design
    
    Args:
        (projectName): The project name
        (query): The query that user prefer or agent's prediction about the user's idea
    
    """
    design_file_path = find_desgin_file(projectName)
    response = google_send_message_with_image(design_file_path, query)
    return response