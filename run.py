import requests
import dotenv
import os
import logging
from logging_setup import setup_logging
from validate import validate_environment_variables, is_valid_email
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
    processed_emails = set()  # To track already processed email addresses
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            user_email = row.get("email").strip() # Strip whitespace
            user_name = row.get("name").strip()
            user_role = row.get("role").strip()

            # Validate required fields
            if not user_email or not user_name or not user_role:
                logging.error("Skipping user creation for row %s: missing required data", row)
                continue

            # Validate email format
            if not is_valid_email(user_email):
                logging.error("Skipping user creation for row %s: invalid email format (%s)", row, user_email)
                continue

            # Check for duplicate email
            if user_email in processed_emails:
                logging.warning("Skipping user creation for row %s: duplicate email (%s)", row, user_email)
                continue

            # Send user creation request
            try:
                response = requests.post(api_url, json=row)
                if response.status_code == 201:
                    logging.info("User creation successful: %s", user_email)
                    processed_emails.add(user_email)  # Add email to the processed set
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