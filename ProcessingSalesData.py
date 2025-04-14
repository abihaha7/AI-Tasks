def apply_discount(prices, discount):
    """Applies a discount percentage to each price in the list."""
    return [round(price * (1 - discount / 100), 2) for price in prices]

def filter_expensive_items(prices, threshold):
    """Finds all items that cost more than the given threshold."""
    return [price for price in prices if price > threshold]

def calculate_total_earnings(prices):
    """Calculates the total earnings from all prices."""
    return sum(prices)

def main():
    """Main function to handle user input and process sales data."""
    try:
        # Input: List of product prices
        prices = list(map(float, input("Enter product prices (comma-separated): ").split(',')))

        # Apply discount
        discount = float(input("Enter discount percentage: "))
        discounted_prices = apply_discount(prices, discount)
        print(f"Discounted Prices: {discounted_prices}")

        # Filter expensive items
        threshold = float(input("Enter threshold price: "))
        expensive_items = filter_expensive_items(discounted_prices, threshold)
        print(f"Items costing more than {threshold}: {expensive_items}")

        # Calculate total earnings
        total_earnings = calculate_total_earnings(discounted_prices)
        print(f"Total Earnings: {total_earnings}")

    except ValueError:
        print("❌ Error: Please enter valid numeric values.")

if __name__ == "__main__":
    main()

