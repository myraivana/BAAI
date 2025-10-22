#
# Myra, 2025/10/15
# File: Myra_Mini_Project.py
# Mini Project: Product Discount Calculator
#

# 1. Input

# Project Requirements
products = [
    {"name": "Laptop", "price": 1200, "category": "Electronics"},
    {"name": "Shirt", "price": 45, "category": "Clothing"},
    {"name": "Phone", "price": 800, "category": "Electronics"},
    {"name": "Shoes", "price": 120, "category": "Clothing"},
    {"name": "Tablet", "price": 350, "category": "Electronics"},
    {"name": "Jacket", "price": 95, "category": "Clothing"},
    {"name": "Book", "price": 25, "category": "Books"},
    {"name": "Headphones", "price": 150, "category": "Electronics"}
]

# Initialize Tracking Variables
total_original = 0
total_discount_amount = 0
total_final = 0
discount_amounts = []
discount_percentages = []
category_counts = {}
final_prices = []

print("=== PRODUCT DISCOUNT CALCULATOR ===\n")

# 2. Process

for product in products:
    name = product["name"]
    price = product["price"]
    category = product["category"]

    # Determine Discount (Based on Category and Price)
    if category == "Electronics":
        if price >= 1000:
            discount = 20
        elif price >= 500:
            discount = 15
        else:
            discount = 10
    elif category == "Clothing":
        if price >= 100:
            discount = 25
        else:
            discount = 15
    elif category == "Books":
        discount = 10

    # Calculate Final Prices
    discount_amount = price * (discount / 100)
    final_price = price - discount_amount

    # Clearance Tag if Discount >= 20%
    clearance_tag = " (Clearance)" if discount >= 20 else ""

# 3. Output

# A. Output per Product
    # Print Product Details
    print(f"Product: {name}{clearance_tag}")
    print(f"Category: {category}")
    print(f"Original Price: ${price:.2f}")
    print(f"Discount: {discount}%")
    print(f"Discount Amount: ${discount_amount:.2f}")
    print(f"Final Price: ${final_price:.2f}\n")

    # Update Totals
    total_original += price
    total_discount_amount += discount_amount
    total_final += final_price

    # Tracking for Bonus Challenges
    discount_amounts.append((name, discount_amount))
    discount_percentages.append(discount)
    final_prices.append((name, final_price))
    category_counts[category] = category_counts.get(category, 0) + 1

#B. Output Final Summary
# Print Summary
total_products = len(products)
print("=== SUMMARY ===")
print(f"Total Products: {total_products}")
print(f"Total Original Price: ${total_original:.2f}")
print(f"Total Discount: ${total_discount_amount:.2f}")
print(f"Total Final Price: ${total_final:.2f}")

# Bonus Level 1
# Find and display the product with the highest discount amount
# Calculate the average discount percentage across all products
highest_discount_product = max(discount_amounts, key=lambda x: x[1])
average_discount_percentage = sum(discount_percentages) / len(discount_percentages)
print("\n--- BONUS LEVEL 1 ---")
print(f"Highest Discount Product: {highest_discount_product[0]} (${highest_discount_product[1]:.2f})")
print(f"Average Discount Percentage: {average_discount_percentage:.2f}%")

# Bonus Level 2
# Count how many products are in each category
# Find the most expensive and cheapest product after discount
most_expensive_product = max(final_prices, key=lambda x: x[1])
cheapest_product = min(final_prices, key=lambda x: x[1])
print("\n--- BONUS LEVEL 2 ---")
print("Category Counts:")
for cat, count in category_counts.items():
    print(f"{cat}: {count}")
print(f"Most Expensive Product After Discount: {most_expensive_product[0]} (${most_expensive_product[1]:.2f})")
print(f"Cheapest Product After Discount: {cheapest_product[0]} (${cheapest_product[1]:.2f})")

# Bonus Level 3
# Add a special “Clearance” tag for products with discount >= 20%
# Calculate total savings for the customer
print("\n--- BONUS LEVEL 3 ---")
print("Clearance Tag was added to products with discount >= 20% in the above list.")
print(f"Total Savings for Customer: ${total_discount_amount:.2f}")