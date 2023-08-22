import csv


def read_employees():
    employees = []
    with open('employees.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            employees.append(row)
    return employees


def write_employees(employees):
    fieldnames = employees[0].keys()
    with open('employees.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(employees)


def update_employee(employee_id, field, new_value):
    employees = read_employees()
    for employee in employees:
        if employee['EmployeeID'] == str(employee_id):
            employee[field] = new_value
            break
    write_employees(employees)
    print("Employee record updated successfully.")


# Example usage
update_employee(1, 'Salary', '55000.00')


def insert_employee(employee):
    employees = read_employees()
    employees.append(employee)
    write_employees(employees)
    print("Employee inserted successfully.")


# Example usage
new_employee = {
    'EmployeeID': '3',
    'FirstName': 'Sarah',
    'LastName': 'Johnson',
    'DateOfBirth': '1992-06-05',
    'Gender': 'Female',
    'Email': 'sarah@example.com',
    'Phone': '9876543210',
    'Address': '789 Oak St',
    'DepartmentID': '2',
    'PositionID': '2',
    'HireDate': '2021-02-15',
    'TerminationDate': None,
    'Salary': '65000.00',
    'EmergencyContact': 'Michael Johnson'
}

insert_employee(new_employee)


def delete_employee(employee_id):
    employees = read_employees()
    employees = [employee for employee in employees if employee['EmployeeID'] != str(employee_id)]
    write_employees(employees)
    print("Employee deleted successfully.")


# Example usage
# delete_employee(2)

def search_employee_by_id(employee_id):
    employees = read_employees()
    for employee in employees:
        if employee['EmployeeID'] == str(employee_id):
            return employee
    return None


# Example usage
employee_id = 1
result = search_employee_by_id(employee_id)
if result:
    print("Employee found:")
    print(result)
else:
    print("Employee not found.")
