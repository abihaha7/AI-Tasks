def generate_numbers(n):
    for i in range(1, n + 1):
        yield i

# Example Usage
for num in generate_numbers(5):
    print(num)
