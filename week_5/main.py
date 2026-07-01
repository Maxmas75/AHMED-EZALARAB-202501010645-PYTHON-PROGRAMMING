from utils import MENU_ITEMS, calculate_total, print_receipt


def get_order():
    order = {}

    while True:
        item = input("Enter item name (Coffee/Tea) or 'done': ").strip().lower()

        if item == "done":
            break

        if item not in MENU_ITEMS:
            print("Invalid item. Please choose Coffee or Tea.")
            continue

        while True:
            try:
                quantity = int(input("Enter quantity: "))
                if quantity > 0:
                    break
                print("Quantity must be greater than zero.")
            except ValueError:
                print("Please enter a whole number.")

        order[item] = order.get(item, 0) + quantity

    return order


def main():
    print("Welcome to the Cafe Billing System")
    print("Menu:")
    for item, price in MENU_ITEMS.items():
        print(f"- {item.title()}: RM{price:.2f}")

    order = get_order()

    if not order:
        print("No items selected. Exiting program.")
        return

    total = calculate_total(order)
    print_receipt(order, total)


if __name__ == "__main__":
    main()
