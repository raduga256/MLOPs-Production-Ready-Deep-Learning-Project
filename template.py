import os
from pathlib import Path
import logging

# This will intiate a project file structure automatically

logging.basicConfig(level= logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "chest_xray_classifier"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

# Create directories using os.makedirs from the list_of_files

for file in list_of_files:
    logging.info(f"Creating directory: {file}")
    Path(os.path.dirname(file)).mkdir(parents=True, exist_ok=True)

logging.info("Project directory structure created successfully.")

for filepath in list_of_files:
    logging.info(f"creating file: {filepath}")
    
    filepath = Path(filepath)   # convert to Path object for better manipulation
    filedir, filename = os.path.split(filepath)
    
    # Check if the directory exists before creating the file directory
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for file: {filepath}")
        
    # Create an empty file
    if(not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"creating file: {filename}")
        
    else:
        logging.info(f"{filename} is already exists. Skipping...")
        
        










# Execute the file in terminal at this stage to create the directory structure
