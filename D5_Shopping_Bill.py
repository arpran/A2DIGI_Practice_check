# Shopping Bill Calculator Script

# Function to calculate the total cost including tax
def calculate_total_cost(item1_price, item2_price, item3_price, tax_percentage):
    subtotal = item1_price + item2_price + item3_price
    total_cost = subtotal + (subtotal * tax_percentage / 100)
    return total_cost

# Ask the user for the prices of the three items
item1_price = float(input("Enter the price of item 1: $"))
item2_price = float(input("Enter the price of item 2: $"))
item3_price = float(input("Enter the price of item 3: $"))

# Ask for the tax percentage
tax_percentage = float(input("Enter the tax percentage: "))

# Calculate the total cost
total = calculate_total_cost(item1_price, item2_price, item3_price, tax_percentage)

# Display the total cost
print(f"\nThe total cost of the items including {tax_percentage}% tax is: ${total:.2f}")
