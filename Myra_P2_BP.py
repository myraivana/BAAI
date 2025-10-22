#
# Myra, 2025/10/17
# File: Myra_P2_BP.py
# [Bonus Project] Project 2: Inventory Reorder System
#

# 1. Input
# The purpose of this line is to import the pandas library for Excel file handling,
# allowing the inventory dataset to be read into a DataFrame and enabling easy calculations and iterations on the data.
import pandas as pd

# The purpose of this line is to read inventory from Excel into a DataFrame.
# Request the Excel filename from the user --> user interaction needed.
filename = input("Please enter the inventory data Excel file name: ")
df = pd.read_excel(filename)

# The purpose of this line is to initialize variables to
# track total reorder cost and store products needing reorder.
total_reorder_cost = 0
products_needing_reorder = []
products_good_stock = []

# The purpose of this line is to print header lines,
# to visually separate the report in the console output.
print("INVENTORY REORDER REPORT")
print("========================")

# 2. Process
# The purpose of this line is to iterate over each product in the DataFrame using iterrows().
for index, row in df.iterrows():
    product = row["Product_Name"]
    current_stock = row["Current_Stock"]
    minimum_stock = row["Minimum_Stock"]
    unit_price = row["Unit_Price"]

    # The purpose of this line is to determine if reorder is needed
    if current_stock < minimum_stock:
        reorder_qty = (minimum_stock - current_stock) + 10                      # Calculate reorder qty = shortage + 10 units (safety buffer)
        reorder_cost = reorder_qty * unit_price                                 # Calculate reorder cost
        total_reorder_cost += reorder_cost                                      # Calculate total reorder cost
        products_needing_reorder.append((product, reorder_qty, reorder_cost))   # Save product reorder details
    else:
        products_good_stock.append(product)     # List of products with stock at or above the minimum

# 3. Output
# The purpose of this line is to display the result for the products needing order.
print("Products Needing Reorder:\n")
for product, qty, cost in products_needing_reorder:
    print(f"{product}: Reorder {qty} units | Cost: ${cost:,.0f}")

# The purpose of this line is to print the total reorder cost to be paid (final summary).
print(f"\nTotal Reorder Cost: ${total_reorder_cost:,.0f}")

# The purpose of this line is to display the result for the products good stock.
if products_good_stock:
    print("Products in Good Stock: ", ', '.join(products_good_stock))