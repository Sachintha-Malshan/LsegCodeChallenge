# LSEG Code Challenge

This project is a Python-based application that reads user data from a CSV file and sends user creation requests to an API. It includes robust logging, environment variable management, and CSV validation.

---

## Features

- Reads user data from a CSV file.
- Sends HTTP POST requests to create users via an API.
- Logs successes and failures to a log file (`error_log.txt`).
- Validates CSV files for required fields and structure.
- Uses environment variables for configuration.

---

## Prerequisites

- Python 3.8 =<
- A virtual environment
- Required Python packages (`requirements.txt`)

---

## Installation

1. Clone the repository:
```bash
   git clone <repository-url>
   cd LsegCodeChallenge
```
2. Create and activate a virtual environment
```bash
    python -m venv venv
    venv\Scripts\activate
```
3. Install dependencies
```bash
   pip install -r requirements.txt
```
4. Create a .env file in the root directory and configure the following environment variables
```bash
    API_URL=<Your API URL>
    INPUT_FILE_PATH=data/users.csv
    ERROR_FILE_PATH=error_log.txt
```

---

## Usage
1. Place your CSV file with user data in the data directory (e.g., users.csv).
2. Run the application:
```bash 
    python run.py 
```
3. Check the logs for results:
    - Success and error logs will be displayed in the console.
    - Errors will also be logged in error_log.txt.

---

## CSV File Format
The CSV file should have the following headers:
- email: email address (required)
- name: name (required)
- role: role (required)

---

## Project Structure

LsegCodeChallenge/
├── data/                
│   └── users.csv        # Example input file
├── logs/
│   └── error_log.txt    # Error logging file 
├── logging_setup.py     # Logging config
├── validate.py          # Validation utilities
├── user.py              # User class
├── run.py               # Main script
├── input_read.py        # Read CSV
├── data_processing.py   # Sending HTTP requests 
├── requirements.txt     # Python dependencies
├── .gitignore           # Git ignore file
└── README.md            # Project doc
