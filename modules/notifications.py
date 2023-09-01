# notifications.py

def send_notification(user_phone_number, violation_reason):
    """
    Send a notification to the group about a rule violation.
    
    Args:
    - user_phone_number: The phone number of the user who violated the rule.
    - violation_reason: The reason for the rule violation.

    Returns:
    - str: A notification message.
    """
    # Simulate sending a notification by returning a formatted message.
    # In a real-world scenario, this function would use the WhatsApp API to send a message to the group.
    notification_message = f"@{user_phone_number} - Your message was deleted due to: {violation_reason}"
    return notification_message

if __name__ == "__main__":
    # Placeholder: Testing the send_notification function.
    print(send_notification("1234567890", "Message too short"))

