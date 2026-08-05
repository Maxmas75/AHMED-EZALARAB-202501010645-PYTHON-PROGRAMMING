from student import get_student
from access import check_access, get_reason
from display import print_result


def main():
    print("=== Computer Lab Access ===")
    name, student_id, registered, lab_open, computer_available = get_student()

    is_allowed = check_access(registered, lab_open, computer_available)
    status = "Access Granted" if is_allowed else "Access Denied"
    reason = get_reason(registered, lab_open, computer_available)

    print()
    print_result(name, student_id, status, reason)


if __name__ == "__main__":
    main()
