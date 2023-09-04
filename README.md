<h1 align="center"> 🏡 RealEstateMate: WhatsApp Group Management Bot </h1>
<div align="center">
  <a href="mailto:ahmadzee26@gmail.com">
    <img alt="Gmail" width="30px" src="https://edent.github.io/SuperTinyIcons/images/svg/gmail.svg" />
    <code>ahmadzee26@gmail.com</code>
  </a>
  <span> ┃ </span>

  <a href="https://t.me/zeeshanahmad4">
    <img alt="Telegram" width="30px" src="https://edent.github.io/SuperTinyIcons/images/svg/telegram.svg" />
    <code>@zeeshanahmad4</code>
  </a>
  <span>┃</span>
  
  <a href="https://discord.com">
    <img alt="Discord" width="30px" src="https://cdn.jsdelivr.net/npm/simple-icons@v5/icons/discord.svg" />
    <code>zee#2655</code>
  </a>
  <span>┃</span>
  
  <a href="https://www.upwork.com/freelancers/zeeshanahmad291">
    <img alt="Upwork" width="80px" src="https://github.com/Zeeshanahmad4/Zeeshanahmad4/blob/main/upwork.svg" />
    <code>Zeeshan Ahmad</code>
  </a>
  
  <br />
  <strong>For discussion, queries and freelance work. Do reach me.👆👆👆</strong>
</div>


<br />

<!-- TABLE OF CONTENTS -->
## Table of Contents

- [Project Overview](#project-overview-)
- [Features](#features-)
  - [Future Features (To-Do)](#-future-features-to-do)
- [Requirements](#requirements-)
- [Usage Examples](#usage-examples-)
  - [Setup and Installation Instructions](#setup-and-installation-instructions-)
- [Troubleshooting Tips](#troubleshooting-tips-)
- [Contribution Guidelines](#contribution-guidelines-)

## Project Overview 📖

**RealEstateMate** is a comprehensive WhatsApp group bot designed to streamline and automate the interactions within real estate-focused WhatsApp groups. It aids in user categorization, message verification, and ensures a smooth, spam-free experience for all group members.

## Features ✨

- **User Type Identification:** Categorize users into Realtors, Sellers or Lessors, and Buyers or Tenants.
- **Message Verification:** Vet every message's content and the sender's phone number.
- **User Authentication:** Ensure users are authorized to send specific types of content.
- **Payment Status Check:** Permit only users with active payments to send messages.
- **Notification Feature:** Alert the group if a message gets deleted and tag the violating user.
- **Activity Report:** Generate reports detailing group activity metrics.
- **Database Integration:** Sync with an external database for real-time payment status checks.
- **Scheduled Messages:** Dispatch messages at predetermined times.
- **Prohibited Words Filter:** Screen out messages containing unwanted or irrelevant words/phrases.

### 🌟 Future Features (To-Do):

- **Voice Message Analysis:** Analyze voice notes for prohibited content.
- **User Feedback System:** Allow users to report issues or provide feedback directly.
- **Advanced Analytics:** Dive deeper into group metrics and offer insights.
- **Multilingual Support:** Support for multiple languages to cater to a global audience.

## Requirements 🛠️

- Python 3.x
- SQLite (for the database operations)
- WhatsApp Business API access


## Usage Examples 📝
```# Example of processing a new message
from main import process_message
process_message("+1234567890", "Hello, I am looking to buy a property.")
```

### Setup and Installation Instructions 🚀

```git clone https://github.com/your_username/RealEstateMate.git```


Navigate to the project directory:
```cd RealEstateMate```

Install the required packages:
```pip install -r requirements.txt```

- Set up the database (details provided in `database_integration.py`).
- Run the `main.py` script to start the bot:

```python main.py```


## Troubleshooting Tips 🔍

- Ensure you have the correct Python version installed.
- Double-check database connectivity and permissions.
- Validate your WhatsApp Business API credentials.
- For message sending errors, ensure the bot has the necessary group permissions.


## Contribution Guidelines 🤝

1. Fork the project.
2. Create your feature branch: `git checkout -b feature/YourFeatureName`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature/YourFeatureName`
5. Open a pull request.


