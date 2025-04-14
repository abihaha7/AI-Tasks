from functools import reduce

def factorial_recursive(n):
    """Recursively calculates factorial of n."""
    if n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    """Calculates factorial using an iterative loop."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_reduce(n):
    """Calculates factorial using functools.reduce()."""
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)

def factorial_generator(n):
    """Yields step-by-step factorial calculations."""
    product = 1
    for i in range(1, n + 1):
        product *= i
        yield product  # Yielding intermediate factorial results

def main():
    """Main function to handle user input and factorial calculations."""
    print("Factorial Calculation Methods:")
    print("1. Recursive")
    print("2. Iterative (Loop)")
    print("3. Functional (Reduce)")
    print("4. Generator (Step-by-Step Calculation)")
    
    try:
        choice = int(input("Choose a method (1-4): "))
        num = int(input("Enter a number: "))

        if num < 1:
            print("❌ Error: Please enter a positive integer.")
            return

        if choice == 1:
            print(f"Factorial ({num}!) using Recursion: {factorial_recursive(num)}")
        elif choice == 2:
            print(f"Factorial ({num}!) using Iteration: {factorial_iterative(num)}")
        elif choice == 3:
            print(f"Factorial ({num}!) using Reduce: {factorial_reduce(num)}")
        elif choice == 4:
            print(f"Factorial ({num}!) using Generator (Step-by-Step):")
            for step, value in enumerate(factorial_generator(num), start=1):
                print(f"Step {step}: {value}")
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 4.")

    except ValueError:
        print("❌ Error: Please enter a valid number.")

if __name__ == "__main__":
    main()
