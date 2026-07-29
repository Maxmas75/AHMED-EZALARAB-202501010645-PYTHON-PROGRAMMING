from employee import get_employee_details
from salary import calculate_salary_summary
from report import print_report


def main():
    print("=== Employee Information ===")
    employee = get_employee_details()
    summary = calculate_salary_summary(
        name=employee["name"],
        employee_id=employee["employee_id"],
        basic_salary=employee["basic_salary"],
        allowance=employee["allowance"],
        overtime_hours=employee["overtime_hours"],
        years_of_service=employee["years_of_service"],
    )
    print()
    print_report(summary)


if __name__ == "__main__":
    main()
