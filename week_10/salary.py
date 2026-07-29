def calculate_salary_summary(name, employee_id, basic_salary, allowance, overtime_hours, years_of_service):
    """Calculates gross salary, deductions, and net salary for an employee."""
    overtime_pay = overtime_hours * 25
    gross_salary = basic_salary + allowance + overtime_pay

    service_bonus = 100.0 if years_of_service > 3 else 0.0
    gross_salary += service_bonus

    epf = round(gross_salary * 0.11, 2)
    socso = round(gross_salary * 0.005, 2)
    net_salary = round(gross_salary - epf - socso, 2)

    return {
        "name": name,
        "employee_id": employee_id,
        "basic_salary": basic_salary,
        "allowance": allowance,
        "overtime_hours": overtime_hours,
        "years_of_service": years_of_service,
        "overtime_pay": overtime_pay,
        "gross_salary": gross_salary,
        "service_bonus": service_bonus,
        "epf": epf,
        "socso": socso,
        "net_salary": net_salary,
    }
