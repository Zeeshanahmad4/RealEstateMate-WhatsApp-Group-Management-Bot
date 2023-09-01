# activity_report.py

# Placeholder data structures
group_members = [
    {"phone_number": "1234567890", "user_type": "Realtor"},
    {"phone_number": "0987654321", "user_type": "Buyer or Tenant"},
    # ... add more members as needed
]

messages_exchanged = [
    {"sender": "1234567890", "content": "This is a message from a Realtor."},
    {"sender": "0987654321", "content": "This is a message from a Buyer or Tenant."},
    # ... add more messages as needed
]

deleted_messages = [
    {"sender": "0987654321", "reason": "Message too short"},
    # ... add more deleted messages as needed
]

removed_members = [
    {"phone_number": "1122334455", "reason": "Multiple rule violations"},
    # ... add more removed members as needed
]


def generate_activity_report():
    total_members = len(group_members)
    total_messages = len(messages_exchanged)
    total_deleted_messages = len(deleted_messages)
    total_removed_members = len(removed_members)

    user_types = {"Realtor": 0, "Seller or Lessor": 0, "Buyer or Tenant": 0}
    for member in group_members:
        user_types[member["user_type"]] += 1

    report = {
        "Total group members": total_members,
        "Messages exchanged": total_messages,
        "User categorization": user_types,
        "Number of messages deleted": total_deleted_messages,
        "Number of members removed": total_removed_members
    }

    return report


def display_report():
    report = generate_activity_report()
    for key, value in report.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    display_report()
