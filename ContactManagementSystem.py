# Contact Management System
contacts = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-123-4567"
}

# Adding a new contact
contacts["David"] = "111-222-3333"

# Updating a contact
contacts["Alice"] = "999-888-7777"

# Searching for a contact
name = "Alice"
if name in contacts:
    print(f"{name}'s number: {contacts[name]}")
else:
    print(f"{name} is not found.")

# Removing a contact
contacts.pop("Bob", None)  # Removes Bob if exists, avoids KeyError

# Checking if a contact exists
print("Eve" in contacts)  # False

# Display all contacts
for name, number in contacts.items():
    print(f"{name}: {number}")
