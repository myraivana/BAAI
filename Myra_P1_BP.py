#
# Myra, 2025/10/17
# File: Myra_P1_BP.py
# [Bonus Project] Project 1: Sales Performance Analyzer
#

# 1. Input
# The purpose of this line is to import the pandas library for Excel file handling,
# allowing the sales dataset to be read into a DataFrame and enabling easy calculations and iterations on the data.
import pandas as pd

# The purpose of this line is to read sales data from Excel into a DataFrame
# Request the Excel filename from the user --> user interaction needed.
filename = input("Please enter the sales data Excel file name: ")
df = pd.read_excel(filename)

# The purpose of this line is to initialize the total bonus payout to zero.
# As each employee's bonus is calculated in the loop, it is added to this running total so that, at the end, the overall amount of bonuses to be paid can be displayed.
total_bonus = 0

# The purpose of this line is to print header lines,
# to visually separate the report in the console output.
print("SALES PERFORMANCE REPORT")
print("========================")

# 2. Process
# The purpose of this line is to iterate over each row in the DataFrame using iterrows().
for index, row in df.iterrows():
    name = row["Employee_Name"]     # Retrieve the employee's name
    sales = row["Monthly_Sales"]    # Retrieve monthly sales amount
    target = row["Sales_Target"]    # Retrieve assigned sales target

    # The purpose of this line is to determine if the employee met their sales target or not.
    if sales >= target:
        target_status = "Target MET"       # Status text for meeting the target.
        bonus = sales*0.10                              # Bonus 10% --> if the target successfully met.
    else:
        target_status = "Target NOT MET"   # Status text for not meeting the target.
        bonus = sales*0.05                              # Bonus 5% --> if the target not successfully met.
   
    # 3. Output
    # The purpose of this line is to display the result for the current employee.
    print(f"{name}: {target_status} | Sales: ${sales:,.0f} | Bonus: ${bonus:,.0f}")
    
    # The purpose of this line is to add the current employee's bonus to the running total.
    total_bonus += bonus

# The purpose of this line is to print the total bonuses to be paid (final summary).
print(f"\nTotal Bonuses to Pay: ${total_bonus:,.0f}")