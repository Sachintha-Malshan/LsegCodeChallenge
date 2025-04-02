import requests
import dotenv
import os
import logging
from logging_setup import setup_logging
from env_validate import validate_environment_variables
import csv

# Load environment variables
dotenv.load_dotenv()

# Setup logging
error_log_file = os.getenv("ERROR_FILE_PATH", "error_log.txt") # Default to error_log.txt if not set
setup_logging(error_log_file)

def create_users(file_path, api_url):
    """
    Reads a CSV file and sends user creation requests to the API.
    Logs successes and failures.
    """
    
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            user_email = row.get("email")
            user_name = row.get("name")
            user_role = row.get("role")

            # Validate required fields
            if not user_email or not user_name or not user_role:
                logging.error("Skipping user creation for row %s: missing required data", row)
                continue

            # Send user creation request
            try:
                response = requests.post(api_url, json=row)
                if response.status_code == 201:
                    logging.info("User creation successful: %s", user_email)
                else:
                    logging.error(
                        "Error creating user %s: response code %s, response text: %s",
                        user_email, response.status_code, response.text
                    )
            except requests.RequestException as e:
                logging.error("Request failed for user %s: %s", user_email, str(e))

# Validate environment variables and file paths
api_url, input_file_path = validate_environment_variables()

# Execute the user creation
create_users(input_file_path, api_url)