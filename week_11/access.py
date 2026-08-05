def check_access(registered, lab_open, computer_available):
    """Returns True only when all access conditions are satisfied."""
    return registered == "Y" and lab_open == "Y" and computer_available == "Y"


def get_reason(registered, lab_open, computer_available):
    """Returns the reason for access denial or welcome message."""
    if registered != "Y":
        return "Student is not registered"
    elif lab_open != "Y":
        return "Computer lab is closed"
    elif computer_available != "Y":
        return "No available computer"
    else:
        return "Welcome to the lab"
