# Even or Odd Checker Script

# Function to check if a number is even or odd
def check_even_or_odd(number):
    if number % 2 == 0:
        return f"{number} is Even."
    else:
        return f"{number} is Odd."

# Ask the user for a number
number = int(input("Enter a number to check if it's even or odd: "))
print(check_even_or_odd(number))

# List of numbers to check
numbers = [10, 15, 23, 42, 55, 66, 89, 100]

# Check each number in the list
print("\nChecking a list of numbers:")
for num in numbers:
    print(check_even_or_odd(num))
