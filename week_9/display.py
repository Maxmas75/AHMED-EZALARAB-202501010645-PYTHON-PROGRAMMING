def display_ticket(ticket):
    print("=== HELP DESK TICKET ===")
    print(f"Student Name : {ticket['student_name']}")
    print(f"Student ID   : {ticket['student_id']}")
    print(f"Issue        : {ticket['issue']}")
    print(f"Location     : {ticket['location']}")
    print(f"Priority     : {ticket['priority']}")
    print(f"Technician   : {ticket['technician']}")
    print(f"Status       : {ticket['status']}")
