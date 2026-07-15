from customer import get_customer_details
from receipt import print_receipt


def main():
    print("=== Customer Information ===")
    name, food, quantity, price, delivery_choice = get_customer_details()
    print()
    print_receipt(name, food, quantity, price, delivery_choice)


if __name__ == "__main__":
    main()
