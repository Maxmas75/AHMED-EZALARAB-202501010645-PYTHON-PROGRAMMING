def get_employee_details():
    """Collects employee details from the user."""
    name = input("Employee Name: ").strip()
    employee_id = input("Employee ID: ").strip()
    basic_salary = float(input("Basic Salary (RM): "))
    allowance = float(input("Allowance (RM): "))
    overtime_hours = int(input("Overtime Hours: "))
    years_of_service = int(input("Years of Service: "))

    return {
        "name": name,
        "employee_id": employee_id,
        "basic_salary": basic_salary,
        "allowance": allowance,
        "overtime_hours": overtime_hours,
        "years_of_service": years_of_service,
    }
