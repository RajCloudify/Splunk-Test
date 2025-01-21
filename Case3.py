# Case 3

import logging

# Configure logging settings
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("/var/log/my_python_app.log"),  # Ensure path is writable
        logging.StreamHandler()
    ]
)

# Success log
logging.info("This is a success log message.")

try:
    # Intentional error: Divide by zero
    result = 10 / 0
except ZeroDivisionError as e:
    # Log the error with stack trace
    logging.error("An error occurred: %s", e, exc_info=True)

# Additional success log
logging.info("This message will still log after the error.")
