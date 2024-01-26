class Employee:
    # Class variable to count the number of employees
    employee_count = 0

    def __init__(self, name, family, salary, department):
        # Instance variables
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department

        # Increment the employee count when a new employee is created
        Employee.employee_count += 1

    def display_employee_details(self):
        print(f"Name: {self.name}\nFamily: {self.family}\nSalary: {self.salary}\nDepartment: {self.department}")

    @staticmethod
    def average_salary(salaries):
        # Calculate and return the average salary
        return sum(salaries) / len(salaries)


class FulltimeEmployee(Employee):
    def __init__(self, name, family, salary, department, employment_type):
        # Call the constructor of the parent class (Employee)
        super().__init__(name, family, salary, department)
        # Additional property for FulltimeEmployee
        self.employment_type = employment_type


# Create instances of Employee and FulltimeEmployee
employee1 = Employee("John Doe", "Doe Family", 50000, "HR")
employee2 = Employee("Jane Smith", "Smith Family", 60000, "IT")

fulltime_employee = FulltimeEmployee("Bob Johnson", "Johnson Family", 70000, "Finance", "Full-time")

# Display details of the employees
print("Employee 1 Details:")
employee1.display_employee_details()
print("\nEmployee 2 Details:")
employee2.display_employee_details()
print("\nFulltime Employee Details:")
fulltime_employee.display_employee_details()

# Display the average salary using the static method
salaries = [employee1.salary, employee2.salary, fulltime_employee.salary]
average_salary = Employee.average_salary(salaries)
print(f"\nAverage Salary: {average_salary}")
