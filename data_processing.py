import logging
import requests
from user import User

def send_req(row, processed_emails, api_url):
    """
    Processes a single row by validating and sending a user creation request.
    Args:
        row (dict): A dictionary 
        processed_emails (set): A set of already processed emails
        api_url (str): The API URL for user creation.
    Returns:
    string
    """
    user = User(row.get("email"), row.get("name"), row.get("role"))

    # Validate user attributes
    if not user.is_valid():
        logging.error("Skipping row: Invalid user data: %s", user)
        return 'Failed: Invalid user data'

    # Check for duplicate email
    if user.email in processed_emails:
        logging.warning("Skipping row: Duplicate email: %s", user.email)
        return 'Failed: Duplicate email'

    # Send user creation request
    try:
        response = requests.post(api_url, json=row)
        if response.status_code == 201:
            logging.info("User creation successful: %s", user.email)
            processed_emails.add(user.email)
            return 'Success'
        else:
            logging.error("Error creating user %s: %s", user.email, response.text)
            return f"Failed: {response.status_code} - {response.text}"
    except requests.RequestException as e:
        logging.error("Request failed for user %s: %s", user.email, str(e))
        return f"Failed: RequestException - {str(e)}"