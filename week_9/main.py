from ticket import create_ticket
from display import display_ticket


def main():
    print("=== IT Helpdesk Ticket System ===")
    ticket = create_ticket()
    print()
    display_ticket(ticket)


if __name__ == "__main__":
    main()
