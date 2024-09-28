# Local packages installation file 

#from setuptools import find_packages, setup
import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "MLOPs-Production-Ready-Deep-Learning-Project"
AUTHOR_NAME = "Paul N"
AUTHOR_USER_NAME_GIT = "raduga256"
SRC_REPO = "chest_xray_classifier"
AUTHOR_EMAIL = "ntalops@yahoo.com"

# Setup script for local packages installation
setuptools.setup(
    name= SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME_GIT}/{REPO_NAME}",
    
    project_urls={
        "BugTracker": "https://github.com/{AUTHOR_USER_NAME_GIT}/{REPO_NAME}/issues",
        },
    packages=setuptools.find_packages(where="src"),
    package_dir={"":"src"}
)






# Create conda environment
    # conda create -n waste-dectection python=3.8
    # actiave the env
    
    # Go to setting --> select the correct python version b4 installing requirements.txt
    # install requirements.txt file into the virtual env
    # then run setup.py
    
