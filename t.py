def generate_bill(customer_name, customer_phone, products):
    total_amount = 0
    
    # Print bill header
    print("Customer Name:", customer_name)
    print("Phone Number:", customer_phone)
    print("\n=============================")
    print("         YOUR BILL")
    print("=============================")
    print("Product      Quantity    Price")
    print("-------------------------------")

    # Print each product details and calculate total amount
    for product, details in products.items():
        quantity, price = details
        amount = quantity * price
        total_amount += amount
        print(f"{product:<12} {quantity:<10} ${amount:.2f}")

    # Print total amount
    print("-------------------------------")
    print(f"Total Amount: ${total_amount:.2f}")
    print("===============================")

# Example usage
customer_name = "John Doe"
customer_phone = "123-456-7890"
products = {
    "Product A": (2, 10.50),
    "Product B": (1, 5.25),
    "Product C": (3, 8.75)
}

generate_bill(customer_name, customer_phone, products)

print(len('erefed'))