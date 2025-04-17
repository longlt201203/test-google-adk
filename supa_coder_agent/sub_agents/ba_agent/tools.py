import os
from PIL import Image

PROJECTS_FOLDER_PATH = "resources/projects"

def analyze_project_design_tool(project_name: str) -> dict:
    """Tool to analyze the design of a project"""

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
    design_image = Image.open(design_file_path)
    design_image_size = design_image.size
    design_image_format = design_image.format
    # design_image_mode = design_image.mode
    
    return {
        "status": "success",
        "message": "Project design analyzed",
        "data": {
            "size": design_image_size,
            "format": design_image_format,
            # "mode": design_image_mode
        }
    }
