#
# Myra, 2025/10/08
# File: Myra_Excel.py
# Calculate sum of column in Excel file.
#

import os
import pandas as pd

# Folder path containing all Excel files
folder_path = r"C:\Users\myrai\OneDrive\Desktop\Myra_AI\BAAI-1"

# Automatically create list of Excel files in the folder
file_list = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

for i, file in enumerate(file_list):
    # 1. Input
    # Read Excel file
    file_path = os.path.join(folder_path, file)
    df = pd.read_excel(file_path)

    # 2. Process
    # Calculate sum of all numeric columns
    sums = df.select_dtypes(include='number').sum()

    # Optionally give a label for the row (e.g., 'Total')
    sums['Name'] = 'Total' # Add a value for the non-numeric column

    # Create a total row DataFrame with the sums
    total_row = pd.DataFrame([sums])

    # Append the total row to the DataFrame
    df_with_total = pd.concat([df, total_row], ignore_index=True)

    # 3. Output
    # Print DataFrame with total row
    print(f"Processed file: {file}")
    print(df_with_total)

    # Save the result into a new Excel file
    output_file = file.replace('.xlsx', '_with_total.xlsx')
    output_path = os.path.join(folder_path, output_file)
    df_with_total.to_excel(output_path, index=False)
    print(f"Saved result to {output_file}\n")

    # Check if this is the last file
    if i == len(file_list) - 1:
        print("This is the last file.")
    else:
        print("Processing next file...\n")