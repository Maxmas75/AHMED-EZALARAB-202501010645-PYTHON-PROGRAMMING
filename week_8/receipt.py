def print_receipt(name, food, quantity, price, delivery_choice):
    """Prints the customer receipt with subtotal and delivery charge."""
    subtotal = quantity * price
    service_charge = subtotal * 0.05
    delivery_charge = 5.00 if delivery_choice == "Y" else 0.00
    grand_total = subtotal + service_charge + delivery_charge

    print("=" * 30)
    print("RECEIPT")
    print("=" * 30)
    print(f"Customer : {name}")
    print(f"Food : {food}")
    print(f"Quantity : {quantity}")
    print(f"Price per Item : RM {price:.2f}")
    print(f"Subtotal : RM {subtotal:.2f}")
    print(f"Service Charge (5%): RM {service_charge:.2f}")
    print(f"Delivery Charge : RM {delivery_charge:.2f}")
    print(f"Grand Total : RM {grand_total:.2f}")
    print("=" * 30)

    return grand_total
