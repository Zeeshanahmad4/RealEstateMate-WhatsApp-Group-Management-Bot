# user_identification.py

def classify_user(phone_number):
    if not phone_number:
        return "Unknown"

    # Using the last digit of the phone number to classify the user
    last_digit = phone_number[-1]

    if last_digit == '0' or last_digit == '2':
        return 'Realtor'
    elif last_digit == '1' or last_digit == '3':
        return 'Seller or Lessor'
    else:
        return 'Buyer or Tenant'

