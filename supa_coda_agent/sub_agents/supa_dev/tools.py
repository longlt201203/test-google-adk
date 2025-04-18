import os
import shutil

TEMPLATES_PATH = "resources/templates"
PROJECT_SET_UPS_PATH = "project_set_ups"

def list_project_set_ups():
    """Tool to list the available project set ups"""
    
    path = os.path.join(TEMPLATES_PATH, PROJECT_SET_UPS_PATH)
    return os.listdir(path)

def load_project_set_up(template_name: str, project_path: str):
    """Tool to load a specific project set up. Providing basic project structure
    
    Args:
        template_name (str): Name of the template to use (e.g., 'html_css_js', 'react')
        project_path (str): Path where the project structure will be created
        
    Returns:
        dict: Status information with success or error message
    """
    source_path = os.path.join(TEMPLATES_PATH, PROJECT_SET_UPS_PATH, template_name)
    
    if not os.path.exists(source_path):
        return {"status": "error", "message": f"Template '{template_name}' not found"}
    
    if not os.path.exists(project_path):
        os.makedirs(project_path)
    
    try:
        # Copy all files from template to project path
        for item in os.listdir(source_path):
            source_item = os.path.join(source_path, item)
            dest_item = os.path.join(project_path, item)
            
            if os.path.isdir(source_item):
                shutil.copytree(source_item, dest_item, dirs_exist_ok=True)
            else:
                shutil.copy2(source_item, dest_item)
        
        return {"status": "success", "message": f"Project setup '{template_name}' loaded successfully to {project_path}"}
    except Exception as e:
        return {"status": "error", "message": f"Failed to load project setup: {str(e)}"}

def write_code():
    pass

def copy_file():
    pass