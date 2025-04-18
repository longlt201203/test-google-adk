from supa_coda_agent.supa_guguru import send_message_with_image as google_send_message_with_image
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
    """Tool to analyze the project design using Google's image analysis capabilities
    
    This function locates a design file for the specified project and sends it to 
    Google's image analysis service along with a query to get insights about the design.
    
    Args:
        projectName (str): The name of the project whose design file should be analyzed
        query (str): The specific question or instruction for analyzing the design image,
                     can be user-provided or agent-generated based on context
    
    Returns:
        str: The analysis response from Google's image analysis service
        
    Raises:
        FileNotFoundError: If no design file can be found for the specified project
    """
    design_file_path = find_desgin_file(projectName)
    response = google_send_message_with_image(design_file_path, query)
    return response