def print_report(summary):
    """Displays a formatted salary report."""
    print("=== SALARY REPORT ===")
    print(f"Employee Name : {summary['name']}")
    print(f"Employee ID : {summary['employee_id']}")
    print(f"Basic Salary (RM) : {summary['basic_salary']:.2f}")
    print(f"Allowance (RM) : {summary['allowance']:.2f}")
    print(f"Overtime Hours : {summary['overtime_hours']}")
    print(f"Overtime Pay (RM) : {summary['overtime_pay']:.2f}")
    print(f"Service Bonus (RM) : {summary['service_bonus']:.2f}")
    print(f"Gross Salary : RM {summary['gross_salary']:.2f}")
    print(f"EPF (11%) : RM {summary['epf']:.2f}")
    print(f"SOCSO (0.5%) : RM {summary['socso']:.2f}")
    print(f"Net Salary : RM {summary['net_salary']:.2f}")
