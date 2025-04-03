import re

class User:
    """
    Represents a user with attributes
    """
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    def __init__(self, email, name, role):
        self.email = email.strip() # Remove leading/trailing whitespaces
        self.name = name.strip()
        self.role = role.strip()

    def is_valid(self):
        """
        Validates the user attributes.
        """
        return self.is_valid_email() and self.name and self.role

    def is_valid_email(self):
        """
        Validates if the user's email is in a valid email format.
        """
        return re.match(self.email_regex, self.email) is not None

    def __repr__(self):
        return f"User(email={self.email}, name={self.name}, role={self.role})"