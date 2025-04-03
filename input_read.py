import csv
import logging

def read_csv(file_path):
    """
    Reads CSV file and returns its rows as a list of dictionaries.
    Args:
        file_path (str): Path to the CSV file.
    Returns:
        list: List of rows as dictionaries.
    """
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        logging.critical("CSV file not found: %s", file_path)
        exit(1)
    except Exception as e:
        logging.critical("Error reading CSV file: %s", str(e))
        exit(1)
