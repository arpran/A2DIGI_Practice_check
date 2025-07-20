# Name Formatter Script (with Last, Middle, First formats)

# Function to format the name in different formats
def format_name(full_name):
    name_parts = full_name.split()  # Split the full name into individual parts
    
    if len(name_parts) >= 2:
        first_name = name_parts[0]
        last_name = name_parts[-1]
        middle_name = " ".join(name_parts[1:-1]) if len(name_parts) > 2 else ""
        
        formatted_names = {
            "First Middle Last": f"{first_name} {middle_name} {last_name}".strip(),
            "Last, First Middle": f"{last_name}, {first_name} {middle_name}".strip(),
            "Middle Last, First": f"{middle_name} {last_name}, {first_name}".strip(),
            "First Last": f"{first_name} {last_name}",
            "Last, First": f"{last_name}, {first_name}",
        }
        
        return formatted_names
    else:
        return None  # If the name doesn't contain at least two parts (first and last)

# Input: Full name (First Middle Last)
full_name = input("Enter your full name (First Middle Last): ")

# Format the name and display different formats
formatted_names = format_name(full_name)

# Check if the name is formatted correctly
if formatted_names:
    print("\nFormatted Names:")
    for format_type, formatted_name in formatted_names.items():
        print(f"{format_type}: {formatted_name}")
else:
    print("Please enter a valid name with at least a first and last name.")
