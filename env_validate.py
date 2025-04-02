#env_validate.py
import os
import logging
import dotenv

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