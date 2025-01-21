#CASE 2 

import logging

# Configure logging settings
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("/var/log/my_python_app.log"),  # Change path if needed
        logging.StreamHandler()
    ]
)

# Example usage
logging.info("This is a success log message.")
logging.error("This is an error log message.")
