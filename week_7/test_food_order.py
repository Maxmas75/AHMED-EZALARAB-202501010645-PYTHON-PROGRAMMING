from food_order import calculate_total, food_order


def test_order_total_examples():
    assert calculate_total(10, 2) == 20
    assert calculate_total(10, 3) == 30
    assert calculate_total(20, 5) == 100
    assert calculate_total(10, 1) == 10


def test_invalid_inputs_are_rejected():
    assert calculate_total(-5, 2) == "Invalid price"
    assert calculate_total(10, 0) == "Invalid quantity"
    assert food_order(10, 2) == 20
