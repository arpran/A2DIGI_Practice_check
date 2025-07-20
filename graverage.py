# Grade Average Script

# Function to calculate the average of 5 test scores and determine pass/fail
def calculate_grade(scores):
    # Calculate the average score
    average_score = sum(scores) / len(scores)
    
    # Determine pass/fail based on the average score
    if average_score >= 50:
        result = "Pass"
    else:
        result = "Fail"
    
    return average_score, result

# Input: 5 test scores
scores = []
for i in range(1, 6):
    score = float(input(f"Enter score for test {i}: "))
    scores.append(score)

# Calculate the average and pass/fail result
average, result = calculate_grade(scores)

# Print the results
print(f"\nAverage Score: {average:.2f}")
print(f"Result: {result}")
