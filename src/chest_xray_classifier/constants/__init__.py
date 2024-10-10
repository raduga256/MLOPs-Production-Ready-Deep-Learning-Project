from pathlib import Path

# List of yaml configuration files to be created in the project directory structure.

CONFIG_FILE_PATH = Path("config/config.yaml")   # Convert all paths to Path objects to avoid windows path issues
PARAMS_FILE_PATH = Path("params.yaml")

# print("Configuring constants ..")