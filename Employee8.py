class Employee:
    def __init__(self, emp_id, name, details):
        self.emp_id = emp_id
        self.name = name
        self.details = details   # tuple (department, salary)

    def show_details(self):
        print("\nEmployee ID:", self.emp_id)
        print("Name:", self.name)
        print("Department:", self.details[0])
        print("Salary:", self.details[1])


# Dictionary to store employees
employees = {}

try:
    # Adding 3 employees
    for i in range(3):
        print(f"\nEnter details of Employee {i+1}")

        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        # store department and salary in tuple
        details = (dept, salary)

        # create object and store in dictionary
        emp = Employee(emp_id, name, details)
        employees[emp_id] = emp

    # Display all employees
    print("\n----- Employee Details -----")
    for emp in employees.values():
        emp.show_details()

except ValueError:
    print("Invalid input! Salary must be a number.")

except Exception as e:
    print("Error occurred:", e)