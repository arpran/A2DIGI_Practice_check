# Initial Extractor Script

# Function to extract initials from a full name
def extract_initials(full_name):
    # Split the full name into parts
    name_parts = full_name.split()
    
    # Extract the first letter from each part and join them
    initials = "".join([name[0].upper() for name in name_parts])
    
    return initials

# Input: Full name
full_name = input("Enter your full name: ")

# Extract initials and display the result
initials = extract_initials(full_name)
print(f"Your initials are: {initials}")
