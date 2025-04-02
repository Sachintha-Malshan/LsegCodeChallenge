#logging_setup.py
import logging

def setup_logging(error_log_file):
    """
    Configures logging for the application.
    Logs INFO level to the console and ERROR level to a file.
    """

    # Console handler for info logs
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    # File handler for error logs
    file_handler = logging.FileHandler(error_log_file)
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logging.getLogger().addHandler(file_handler)