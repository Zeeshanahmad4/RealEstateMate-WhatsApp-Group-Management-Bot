# constants.py

# User Types
REALTOR = "Realtor"
SELLER_OR_LESSOR = "Seller or Lessor"
BUYER_OR_TENANT = "Buyer or Tenant"

# Message Types
TEXT = "Text"
IMAGE = "Image"
LINK = "Link"
VIDEO = "Video"  # For future use if needed
AUDIO = "Audio"  # For future use if needed
DOCUMENT = "Document"  # For future use if needed

# Compliance
MAX_MESSAGE_RATE = 20  # Maximum messages per minute
MAX_MESSAGE_SIZE = 2048  # Maximum message size in bytes (For future use if needed)

# Prohibited content
PROHIBITED_WORDS_LIST = [
    "spam",
    "abuse",
    # ... Add more prohibited words/phrases as needed
]

# Notification templates
NOTIFICATION_TEMPLATE = "@{user_phone_number} - Your message was deleted due to: {reason}"

# Error messages
ERROR_INVALID_PHONE_NUMBER = "Invalid phone number format"
ERROR_SHORT_MESSAGE = "Message too short"
ERROR_LARGE_MESSAGE = "Message too large"  # For future use if needed
ERROR_UNSUPPORTED_FORMAT = "Unsupported message format"  # For future use if needed

# Database related constants (For future use if needed)
USER_TABLE_NAME = "users"
MESSAGE_TABLE_NAME = "messages"
PAYMENT_TABLE_NAME = "payments"

# API Endpoints or URLs (For future use if needed)
USER_API_ENDPOINT = "/api/user"
MESSAGE_API_ENDPOINT = "/api/message"
PAYMENT_API_ENDPOINT = "/api/payment"

# Other potential constants
DEFAULT_GROUP_NAME = "WhatsApp Bot Group"  # For future use if needed
MAX_GROUP_SIZE = 256  # Maximum number of users in a group (For future use if needed)
