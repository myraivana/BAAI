#
# Myra, 2025/10/17
# File: Myra_P3_BP.py
# [Bonus Project] Project 3: Customer Segmentation Tool
#

# 1. Input
# The purpose of this line is to import the pandas library for Excel file handling,
# allowing the customer dataset to be read into a DataFrame and enabling easy calculations and iterations on the data.
import pandas as pd

# The purpose of this line is to read customer data from Excel into a DataFrame.
# Request the Excel filename from the user --> user interaction needed.
filename = input("Please enter the customer data Excel file name: ")
df = pd.read_excel(filename)

# The purpose of this line is to initialize
# total VIP revenue tracker and storage for each customer segment.
total_vip_revenue = 0
vip_customers = []
regular_customers = []
new_customers = []

# The purpose of this line is to print header lines,
# to visually separate the report in the console output.
print("CUSTOMER SEGMENTATION REPORT")
print("============================")

# 2. Process
# The purpose of this line is to iterate over each customer in the DataFrame using iterrows().
for index, row in df.iterrows():
    name = row["Customer_Name"]
    total_purchases = row["Total_Purchases"]
    num_orders = row["Number_of_Orders"]

    # The purpose of this line is to calculate average order value.
    avg_order_value = total_purchases / num_orders

    # The purpose of this line is to categorize customers based on total purchases.
    if total_purchases > 10000:
        vip_customers.append ((name, total_purchases, num_orders, avg_order_value))
        total_vip_revenue += total_purchases
    elif total_purchases >= 5000:
        regular_customers.append((name, total_purchases, num_orders, avg_order_value))
    else:
        new_customers.append((name, total_purchases, num_orders, avg_order_value))

# 3. Output
# The purpose of this line is to print the result of VIP customers.
print("VIP Customers:")
for name, total, orders, avg in vip_customers:
    print(f"- {name} | Total: ${total:,.0f} | Orders: {orders} | Avg Order: ${avg:,.2f}")

# The purpose of this line is to print the result of regular customers.
print("\nRegular Customers:")
for name, total, orders, avg in regular_customers:
    print(f"- {name} | Total: ${total:,.0f} | Orders: {orders} | Avg Order: ${avg:,.2f}")

# The purpose of this line is to print the result of new customers.
print("\nNew Customers:")
for name, total, orders, avg in new_customers:
    print(f"- {name} | Total: ${total:,.0f} | Orders: {orders} | Avg Order: ${avg:,.2f}")

# The purpose of this line is to print the total VIP revenue (final summary).
print(f"\nTotal VIP Revenue: ${total_vip_revenue:,.0f}")