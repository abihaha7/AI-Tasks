from collections import namedtuple

# Define a named tuple for products
Product = namedtuple("Product", ["name", "price", "category"])

# Creating product instances
product1 = Product("Laptop", 1200, "Electronics")
product2 = Product("T-shirt", 25, "Clothing")

# Accessing product details
print("Product Name:", product1.name)  
print("Price:", product1.price)
print("Category:", product1.category)

