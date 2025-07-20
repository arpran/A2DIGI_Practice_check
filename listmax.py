# List Maximum Script

# Function to find the largest number in a list without using max()
def find_largest(numbers):
    largest = numbers[0]  # Assume the first element is the largest initially
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Example list of numbers
numbers = [98, 12, 13, 3, 99, 21]

# Find the largest number
largest_number = find_largest(numbers)

# Print the result
print(f"The largest number in the list is: {largest_number}")
