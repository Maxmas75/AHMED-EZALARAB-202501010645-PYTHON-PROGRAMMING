def create_ticket():
    print("=== IT Helpdesk Ticket ===")
    student_name = input("Student Name: ").strip()
    student_id = input("Student ID: ").strip()
    issue = input("Issue Description: ").strip()
    location = input("Location: ").strip()

    priority = ""
    while priority not in ("High", "Medium", "Low"):
        priority = input("Priority (High/Medium/Low): ").strip().title()
        if priority not in ("High", "Medium", "Low"):
            print("Please enter High, Medium, or Low.")

    technician = assign_technician(priority)
    status = "Pending"

    ticket = {
        "student_name": student_name,
        "student_id": student_id,
        "issue": issue,
        "location": location,
        "priority": priority,
        "technician": technician,
        "status": status,
    }

    print("\nTicket created successfully.")
    return ticket


def assign_technician(priority):
    if priority == "High":
        return "Ahmad"
    if priority == "Medium":
        return "Siti"
    return "Ali"
