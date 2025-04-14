# Initialize a set to store unique emails
emails = set()

# Function to add an email
def register_email(email):
    if email in emails:
        print(f"{email} is already registered.")
    else:
        emails.add(email)
        print(f"{email} has been registered.")

# Registering emails
register_email("user1@example.com")
register_email("user2@example.com")
register_email("user1@example.com")  # Duplicate, won't be added again

# Check if an email exists
print("user2@example.com" in emails)  # True
print("notregistered@example.com" in emails)  # False

# Removing an email
emails.discard("user2@example.com")  # Safely removes email

# Displaying all unique emails
print("Registered Emails:", emails)
