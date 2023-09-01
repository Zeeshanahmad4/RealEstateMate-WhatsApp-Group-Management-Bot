# main.py
from user_identification import classify_user
from message_verification import verify_message_content, verify_sender
from user_authentication import authenticate_user
from database_integration import check_payment_status
from notifications import send_notification
from payment_status import is_payment_active
from scheduled_messages import schedule_message, run_schedule
from constants import PROHIBITED_WORDS_LIST
from helpers import contains_prohibited_content

def process_message(phone_number, message_content):
    """
    Process incoming messages and apply the necessary checks and operations.

    Args:
    - phone_number (str): The sender's phone number.
    - message_content (str): The content of the message.
    """
    # Verify sender's phone number
    if not verify_sender(phone_number):
        print(f"Invalid sender: {phone_number}")
        return

    # Classify user based on phone number
    user_type = classify_user(phone_number)
    print(f"User {phone_number} is identified as {user_type}")

    # Authenticate user
    is_authenticated, user_or_error = authenticate_user(phone_number, message_content)
    if not is_authenticated:
        print(f"Authentication failed for {phone_number}. Reason: {user_or_error}")
        send_notification(phone_number, user_or_error)
        return

    # Check payment status
    if not is_payment_active(phone_number):
        print(f"User {phone_number} does not have an active payment. Message blocked.")
        send_notification(phone_number, "Inactive payment status")
        return

    # Check for prohibited content
    if contains_prohibited_content(message_content, PROHIBITED_WORDS_LIST):
        print(f"Message from {phone_number} contains prohibited content. Message deleted.")
        send_notification(phone_number, "Message contains prohibited content")
        return

    print(f"Message from {phone_number} processed successfully!")

if __name__ == "__main__":
    # Simulate processing a few messages
    process_message("1234567890", "Hello! I'm interested in buying a property.")
    process_message("1234567891", "spam message content here.")
    process_message("abcdefg", "Invalid phone number test.")

    # Placeholder for scheduled messages (this would run in its own loop or thread in a real-world scenario)
    schedule_message("Scheduled message going out in 5 seconds.", 5)
    run_schedule()

