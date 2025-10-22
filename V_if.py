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

total_original = 0
total_discount_amount = 0
total_final = 0

print("=== PRODUCT DISCOUNT CALCULATOR ===\n")

for product in products:
    name = product["name"]
    price = product["price"]
    category = product["category"]

    # Caculate percentage discount
    if category == "Electronics":
        if price >= 1000:
            discount = 0.20
        elif price >= 500:
            discount = 0.15
        else:
            discount = 0.10

    elif category == "Clothing":
        if price >= 100:
            discount = 0.25
        else:
            discount = 0.15

    elif category == "Books":
        discount = 0.10

    else:
        discount = 0.0  # phòng trường hợp category lạ

    # Tính toán
    discount_amount = price * discount
    final_price = price - discount_amount

    # Cập nhật tổng
    total_original += price
    total_discount_amount += discount_amount
    total_final += final_price

    # In chi tiết sản phẩm
    print(f"Product: {name}")
    print(f"Category: {category}")
    print(f"Original Price: ${price:.2f}")
    print(f"Discount: {discount*100:.0f}%")
    print(f"Final Price: ${final_price:.2f}\n")

# In summary
print("=== SUMMARY ===")
print(f"Total Products: {len(products)}")
print(f"Total Original Price: ${total_original:.2f}")
print(f"Total Discount: ${total_discount_amount:.2f}")
print(f"Total Final Price: ${total_final:.2f}")