# get logger object and test
from chest_xray_classifier import logger


logger.info("Welcome to JEPA research labs and projects!")
logger.info("Welcome to innovative projects!")

# when run 'python demo.py' in terminal, this message will be printed in the logs file
# python-box library will help us to write exceptions

try:
    raise Exception("An error occurred")
except Exception as e:
    logger.error(f"An error occurred: {str(e)}")

