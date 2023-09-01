# user_authentication.py
from user_identification import classify_user
from message_verification import verify_message_content, verify_sender

def authenticate_user(phone_number, message_content):
    if not phone_number:
        return False, "Phone number is missing"
    
    if not message_content:
        return False, "Message content is missing"

    user_type = classify_user(phone_number)
    is_verified, error = verify_message_content(message_content)
    is_sender_verified = verify_sender(phone_number)
    
    if not is_sender_verified:
        return False, "Invalid phone number format"
    
    if not is_verified:
        return False, error

    return True, f"User is a {user_type} and is authenticated."

