# payment_status.py
from database_integration import check_payment_status

def is_payment_active(phone_number):
    """
    Determine if the user with the given phone number has an active payment.
    
    Args:
    - phone_number: The phone number of the user.

    Returns:
    - bool: True if the user has an active payment, False otherwise.
    """
    return check_payment_status(phone_number)

if __name__ == "__main__":
    # Placeholder: Testing the is_payment_active function.
    # Assuming the user "1234567890" was added to the database with an active payment in the previous step.
    print(is_payment_active("1234567890"))  # Expected to return True

