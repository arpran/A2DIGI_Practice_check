# Simple Password Validator Script

# Function to check if the password meets basic requirements
def check_password(password):
    min_length = 8  # Minimum length requirement
    
    if len(password) < min_length:
        return f"Password is too short. It must be at least {min_length} characters."
    else:
        return "Password is valid."

# Ask the user for the password
password = input("Enter your password: ")

# Check the password and display the result
result = check_password(password)
print(result)
