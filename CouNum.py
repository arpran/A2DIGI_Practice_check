# Count Numbers Script

# Function to count positive, negative, and zero numbers in a list
def count_numbers(numbers):
    positive_count = 0
    negative_count = 0
    zero_count = 0
    
    for num in numbers:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1
    
    return positive_count, negative_count, zero_count

# Example list of numbers
numbers = [12, -7, 0, 45, -3, 0, -15, 8]

# Count the numbers and display the result
positive, negative, zero = count_numbers(numbers)

print(f"Positive numbers: {positive}")
print(f"Negative numbers: {negative}")
print(f"Zero numbers: {zero}")
