def calculate_total(price, quantity):
    if price <= 0:
        return "Invalid price"
    if quantity <= 0:
        return "Invalid quantity"
    return price * quantity


def food_order(price, quantity):
    return calculate_total(price, quantity)
