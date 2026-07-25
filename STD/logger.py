# logger.py

# import date time modules
from datetime import datetime

# import log file path from config.py
from config import LOG_FILE

# Function
def write_log(message):
    # Get Current Time
    current_time = datetime.now()

    # Conver date and time into redable format
    current_time = current_time.strftime("%d-%m-%y %I:%M:%S %p")
    with open(LOG_FILE,"a")as file:
        #Write date, time and activity
        file.write(f"[{current_time}] {message}\n")
