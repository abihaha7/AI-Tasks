def calculate_ticket_price(age, base_price=12):
    """Calculates the movie ticket price based on age."""
    if age < 12:
        return base_price * 0.5  # 50% discount for children
    elif age >= 60:
        return base_price * 0.7  # 30% discount for seniors
    else:
        return base_price  # Regular price

# Example usage
print(f"Ticket for 10-year-old: ${calculate_ticket_price(10)}")  # $6.00
print(f"Ticket for 30-year-old: ${calculate_ticket_price(30)}")  # $12.00
print(f"Ticket for 65-year-old: ${calculate_ticket_price(65)}")  # $8.40
test_ages = [5, 10, 17, 25, 40, 60, 75]
for age in test_ages:
    print(f"Age {age}: ${calculate_ticket_price(age)}")
class Ticket:
    def __init__(self, base_price=12):
        self.base_price = base_price

    def get_price(self, age):
        if age < 12:
            return self.base_price * 0.5
        elif age >= 60:
            return self.base_price * 0.7
        return self.base_price

# Example usage
cinema_ticket = Ticket()
print(f"Ticket for 8-year-old: ${cinema_ticket.get_price(8)}")
print(f"Ticket for 65-year-old: ${cinema_ticket.get_price(65)}")
