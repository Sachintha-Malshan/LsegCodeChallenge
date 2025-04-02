#env_validate.py
import os
import logging
import dotenv
import re

# Load environment variables
dotenv.load_dotenv()

def validate_environment_variables():
    """
    Validates required environment variables and file paths.
    Exits the program if validation fails.
    
    Returns:
        tuple: A tuple containing the API URL and input file path.
    """
    api_url = os.getenv("API_URL")
    input_file_path = os.getenv("INPUT_FILE_PATH")

    if not api_url:
        logging.critical("API_URL environment variable is not set. Exiting.")
        exit(1)

    if not input_file_path:
        logging.critical("INPUT_FILE_PATH environment variable is not set. Exiting.")
        exit(1)

    if not os.path.exists(input_file_path):
        logging.error("Invalid file path: %s", input_file_path)
        exit(1)

    return api_url, input_file_path

def is_valid_email(email):
    """
    Validates if the given email is in a valid email format.
    Args:
        email (str)
    Returns:
        bool: True if the email is valid.
    """
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None