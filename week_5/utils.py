MENU_ITEMS = {
    "coffee": 6.00,
    "tea": 12.00,
}


def calculate_subtotal(price, quantity):
    return round(price * quantity, 2)


def calculate_total(order):
    total = 0.0
    for item, quantity in order.items():
        total += calculate_subtotal(MENU_ITEMS[item], quantity)
    return round(total, 2)


def print_receipt(order, total):
    print("\n===== RECEIPT =====")
    print(f"{'Item':<10} {'Qty':<5} {'Subtotal':<10}")
    print("-" * 30)

    for item, quantity in order.items():
        subtotal = calculate_subtotal(MENU_ITEMS[item], quantity)
        print(f"{item.title():<10} {quantity:<5} RM{subtotal:>7.2f}")

    print("-" * 30)
    print(f"{'Total':<10} {'':<5} RM{total:>7.2f}")
    print("==================")
