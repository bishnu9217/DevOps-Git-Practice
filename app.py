print("Employee Management System")
def search_employee(employees, employee_id):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
    return "Employee not found"
