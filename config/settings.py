# settings.py

# Database Configuration
DATABASE_CONFIG = {
    'NAME': 'whatsapp_bot.db',
    'USER': '',  # Add user if needed
    'PASSWORD': '',  # Add password if needed
    'HOST': 'localhost',
    'PORT': 'default_port'  # Add port if needed
}

# Compliance settings
MESSAGE_RATE_LIMIT = 20  # Maximum messages per minute

# Prohibited content settings
PROHIBITED_CONTENT = [
    "spam",
    "abuse",
    # ... Add more prohibited words/phrases as needed
]

# User categorization based on phone number's last digit
USER_CATEGORIZATION = {
    '0': 'Realtor',
    '1': 'Seller or Lessor',
    '2': 'Realtor',
    '3': 'Seller or Lessor',
    '4': 'Buyer or Tenant',
    '5': 'Buyer or Tenant',
    '6': 'Buyer or Tenant',
    '7': 'Buyer or Tenant',
    '8': 'Buyer or Tenant',
    '9': 'Buyer or Tenant',
}

# Notification settings
NOTIFICATION_MESSAGE = "@{user_phone_number} - Your message was deleted due to: {reason}"

# Message settings
MIN_MESSAGE_LENGTH = 10

# API Keys and External Configurations
API_CONFIG = {
    "WHATSAPP_API_KEY": "YOUR_WHATSAPP_API_KEY_HERE",
    # ... Add other API keys or external configurations as needed
}

# Other settings can be added as the project evolves...

