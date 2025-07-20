# Number Comparison Script

# Function to compare two numbers
def compare_numbers(num1, num2):
    if num1 > num2:
        return f"{num1} is larger than {num2}"
    elif num1 < num2:
        return f"{num1} is smaller than {num2}"
    else:
        return f"{num1} and {num2} are equal"

# Ask the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the numbers and display the result
result = compare_numbers(num1, num2)
print(result)
