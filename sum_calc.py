# Sum Calculator Script

# Function to calculate the sum of all numbers from 1 to n using a loop
def sum_of_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Ask the user for the value of n
n = int(input("Enter a number n to find the sum of numbers from 1 to n: "))

# Calculate the sum and display the result
result = sum_of_numbers(n)
print(f"The sum of numbers from 1 to {n} is: {result}")
