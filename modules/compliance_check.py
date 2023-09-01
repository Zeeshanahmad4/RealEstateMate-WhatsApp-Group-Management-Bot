# compliance_check.py

# Placeholder for compliance rules
COMPLIANCE_RULES = {
    "message_rate_limit": 20,  # Maximum messages per minute
    "prohibited_content": ["spam", "abuse"],  # Prohibited content keywords
    "user_data_protection": True,  # Ensure user data is not stored without encryption
    "third_party_advertising": False  # Ensure no third-party ads are sent to users
}

def check_compliance_rate_limit(messages_sent_last_minute):
    """
    Check if the bot is complying with the message rate limit.
    """
    return messages_sent_last_minute <= COMPLIANCE_RULES["message_rate_limit"]

def check_compliance_content(message_content):
    """
    Check if the message content complies with the rules.
    """
    for prohibited_word in COMPLIANCE_RULES["prohibited_content"]:
        if prohibited_word in message_content:
            return False
    return True

def check_user_data_protection(is_encrypted):
    """
    Check if user data is stored with encryption.
    """
    return is_encrypted == COMPLIANCE_RULES["user_data_protection"]

def check_third_party_advertising(is_advertising):
    """
    Check if the bot is sending third-party ads.
    """
    return not is_advertising

def run_compliance_checks(message_content, messages_sent_last_minute, is_encrypted, is_advertising):
    """
    Run all compliance checks and return the results.
    """
    results = {
        "Rate Limit": check_compliance_rate_limit(messages_sent_last_minute),
        "Content": check_compliance_content(message_content),
        "User Data Protection": check_user_data_protection(is_encrypted),
        "Third Party Advertising": check_third_party_advertising(is_advertising)
    }

    return results

if __name__ == "__main__":
    # Placeholder data for demonstration
    message_content = "This is a test message without spam."
    messages_sent_last_minute = 10
    is_encrypted = True
    is_advertising = False
    
    compliance_results = run_compliance_checks(message_content, messages_sent_last_minute, is_encrypted, is_advertising)
    
    for key, value in compliance_results.items():
        status = "Compliant" if value else "Not Compliant"
        print(f"{key}: {status}")

