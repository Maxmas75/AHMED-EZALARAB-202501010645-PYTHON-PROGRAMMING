import importlib.util
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from salary import calculate_salary_summary


def test_calculates_salary_with_overtime_and_service_bonus():
    summary = calculate_salary_summary(
        name="Ali",
        employee_id="EMP001",
        basic_salary=3500.0,
        allowance=400.0,
        overtime_hours=6,
        years_of_service=4,
    )

    assert summary["gross_salary"] == 3900.0 + 150.0 + 100.0
    assert summary["epf"] == round((3900.0 + 150.0 + 100.0) * 0.11, 2)
    assert summary["socso"] == round((3900.0 + 150.0 + 100.0) * 0.005, 2)
    assert summary["net_salary"] == round((3900.0 + 150.0 + 100.0) - ((3900.0 + 150.0 + 100.0) * 0.11) - ((3900.0 + 150.0 + 100.0) * 0.005), 2)
    assert summary["service_bonus"] == 100.0
