class Employee:
    def __init__(self, emp_id, name, details):
        self.emp_id = emp_id
        self.name = name
        self.details = details   

    def show_details(self):
        
        print("\n Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Department:", self.details[0])
        print("Salary:", self.details[1])



employees = {}

try:

    for i in range(3):
        print(f"\n Enter details of Employee {i+1}")

        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        salary = float(input("Enter Salary: "))


        emp = Employee(emp_id, name, details)
        employees[emp_id] = emp

  
    print("\n----- Employee Details -----")
    for emp in employees.values():
        emp.show_details()

except ValueError:
    print("Invalid input! Salary must be a number.")

except Exception as e:
    print("Error occurred:", e)