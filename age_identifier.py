# Age Category Checker Script

# Function to determine the age category
def determine_age_category(age):
    if age < 13:
        return "Child"
    elif 13 <= age < 20:
        return "Teenager"
    elif 20 <= age < 60:
        return "Adult"
    else:
        return "Senior"

# Ask the user for their age
age = int(input("Enter your age: "))

# Determine the age category and display the result
category = determine_age_category(age)
print(f"You are classified as: {category}")
