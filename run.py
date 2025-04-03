
import dotenv
import os
from logging_setup import setup_logging
from validate import validate_environment_variables
from input_read import read_csv
from data_processing import send_req

# Load environment variables
dotenv.load_dotenv()

# Setup logging
error_log_file = os.getenv("ERROR_FILE_PATH", "error_log.txt") # Default to error_log.txt
setup_logging(error_log_file)


def create_users(file_path, api_url):
    """
    Reads a CSV file, processes each row, and sends user creation requests.
    Args:
        file_path (str): Path to CSV file.
        api_url (str): URL for user creation.
    """
    rows = read_csv(file_path)
    processed_emails = set()

    for row in rows:
        send_req(row, processed_emails, api_url)

# Validate environment variables and file paths
api_url, input_file_path = validate_environment_variables()

# Execute the user creation process
create_users(input_file_path, api_url)