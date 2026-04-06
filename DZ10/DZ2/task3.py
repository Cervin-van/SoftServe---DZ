class Employee:
    """This class represents an employee with a name and a salary."""
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    @classmethod
    def display_total_employees(cls):
        print(f"Total number of employees: {cls.total_employees}")

    def display_info(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary}")

if __name__ == "__main__":
    emp1 = Employee("Alice", 50000)
    emp2 = Employee("Bob", 60000)

    emp1.display_info()
    emp2.display_info()
    Employee.display_total_employees()

    print("\n--- Class Information ---")
    print(f"__base__: {Employee.__base__}")
    print(f"__dict__: {Employee.__dict__}")
    print(f"__name__: {Employee.__name__}")
    print(f"__module__: {Employee.__module__}")
    print(f"__doc__: {Employee.__doc__}")
