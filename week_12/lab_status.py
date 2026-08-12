def check_computers():
    """Collects the status of 5 computers from the user."""
    computers = []
    for number in range(1, 6):
        status = input(f"Computer {number} Status (A/U/M): ").strip().upper()
        while status not in {"A", "U", "M"}:
            print("Invalid status. Please enter A, U, or M.")
            status = input(f"Computer {number} Status (A/U/M): ").strip().upper()
        computers.append(status)
    return computers


def count_available(computers):
    """Counts how many computers are available."""
    available = 0
    for status in computers:
        if status == "A":
            available += 1
    return available


def display_status(computers, available):
    """Displays the lab status and available computer count."""
    print("\nLAB STATUS")
    for index, status in enumerate(computers, start=1):
        print(f"Computer {index}: {status}")
    print(f"Available Computers: {available}")
