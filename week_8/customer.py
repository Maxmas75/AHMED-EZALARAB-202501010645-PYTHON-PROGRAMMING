def get_customer_details():
    """Collects customer order details from the user."""
    name = input("Customer Name: ").strip()
    food = input("Food Ordered (Cake/Muffin): ").strip()
    quantity = int(input("Quantity: "))
    price = float(input("Price per Item (RM): "))
    delivery_choice = input("Delivery (Y/N): ").strip().upper()

    return name, food, quantity, price, delivery_choice
