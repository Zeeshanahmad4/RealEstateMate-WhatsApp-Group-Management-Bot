
# database_integration.py
import sqlite3

# Setup database connection
DATABASE_NAME = "whatsapp_bot.db"
conn = sqlite3.connect(DATABASE_NAME)
cursor = conn.cursor()

def setup_database():
    """
    Create tables if they don't exist.
    """
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        phone_number TEXT PRIMARY KEY,
        user_type TEXT,
        payment_status BOOLEAN
    )
    ''')
    conn.commit()

def check_payment_status(phone_number):
    """
    Check if a particular user's payment status is up-to-date.
    """
    cursor.execute('SELECT payment_status FROM users WHERE phone_number=?', (phone_number,))
    result = cursor.fetchone()
    if result:
        return result[0]
    return False

def add_user(phone_number, user_type, payment_status):
    """
    Add a user to the database.
    """
    cursor.execute('INSERT INTO users (phone_number, user_type, payment_status) VALUES (?, ?, ?)', 
                   (phone_number, user_type, payment_status))
    conn.commit()

def update_payment_status(phone_number, payment_status):
    """
    Update the payment status of a user.
    """
    cursor.execute('UPDATE users SET payment_status=? WHERE phone_number=?', 
                   (payment_status, phone_number))
    conn.commit()

def close_database():
    """
    Close the database connection.
    """
    conn.close()

if __name__ == "__main__":
    setup_database()
    # Placeholder: Adding a user for testing purposes.
    add_user("1234567890", "Realtor", True)
    print(check_payment_status("1234567890"))  # Expected to return True
    close_database()
