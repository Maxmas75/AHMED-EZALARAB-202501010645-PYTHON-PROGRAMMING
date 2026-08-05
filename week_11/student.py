def get_student():
    """Collects student access details from the user."""
    name = input("Student Name: ").strip()
    student_id = input("Student ID: ").strip()
    registered = input("Registered for today's lab? (Y/N): ").strip().upper()
    lab_open = input("Is the lab open? (Y/N): ").strip().upper()
    computer_available = input("Computer Available? (Y/N): ").strip().upper()

    return name, student_id, registered, lab_open, computer_available
