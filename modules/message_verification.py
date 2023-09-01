# message_verification.py

def verify_message_content(message_content):
    if not message_content:
        return False, "Empty message"

    if len(message_content) < 10:
        return False, "Message too short"
    
    if not any(char.isdigit() for char in message_content):
        return False, "Message does not contain any numbers"

    return True, ""

def verify_sender(phone_number):
    if not phone_number or len(phone_number) < 10:
        return False
    return phone_number.isnumeric()

