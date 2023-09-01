# helpers.py

import re
from datetime import datetime

def format_phone_number(phone_number):
    """
    Remove non-numeric characters from a phone number.
    
    Args:
    - phone_number (str): The phone number to format.

    Returns:
    - str: A phone number containing only numeric characters.
    """
    return re.sub('[^0-9]', '', phone_number)

def current_timestamp():
    """
    Get the current timestamp in a specific format.
    
    Returns:
    - str: The current timestamp in 'YYYY-MM-DD HH:MM:SS' format.
    """
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def contains_prohibited_content(message, prohibited_list):
    """
    Check if a message contains any words or phrases from a prohibited list.
    
    Args:
    - message (str): The message to check.
    - prohibited_list (list): A list of prohibited words or phrases.

    Returns:
    - bool: True if the message contains prohibited content, False otherwise.
    """
    for word in prohibited_list:
        if word in message:
            return True
    return False

# Additional helper functions can be added as the project evolves...

