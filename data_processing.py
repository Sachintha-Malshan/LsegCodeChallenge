import logging
import requests
from validate import is_valid_email

def send_req(row, processed_emails, api_url):
    """
    Processes a single row by row and sending user creation requests.
    Args:
        row (dict): A dictionary  .
        processed_emails (set): A set of already processed emails.
        api_url (str): URL for user creation.
    Returns:
        string message.
    """
    user_email = row.get("email").strip() # Remove leading/trailing whitespaces
    user_name = row.get("name").strip()
    user_role = row.get("role").strip()

    # Validate required fields
    if not user_email or not user_name or not user_role:
        logging.error("Skipping row: Missing required data: %s", row)
        return 'Failed: Missing required data'


    # Validate email format
    if not is_valid_email(user_email):
        logging.error("Skipping row: Invalid email format: %s", user_email)
        return 'Failed: Invalid email format'

    # Check for duplicate email
    if user_email in processed_emails:
        logging.warning("Skipping row: Duplicate email: %s", user_email)
        return 'Failed: Duplicate email'

    # Send user creation request
    try:
        response = requests.post(api_url, json=row)
        if response.status_code == 201:
            logging.info("User creation successful: %s", user_email)
            processed_emails.add(user_email)
            return 'User creation successful'
            
        else:
            logging.error("Error creating user %s: %s", user_email, response.text)
            return f"Failed: {response.text}"
    except requests.RequestException as e:
        logging.error("Request failed for user %s: %s", user_email, str(e))
        return f"Failed: {str(e)}"