class Employee:
    count = 0
    total_salary = 0

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        Employee.count += 1
        Employee.total_salary += salary

    # instance method
    def get_info(self):
        return(f"{self.name} and {self.position}")
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook"]
        return position in valid_positions
    
    @classmethod
    def get_count(cls):
        return f"Total # of employees: {cls.count}"
    
    @classmethod
    def get_average_salary(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_salary / cls.count:.2f}"
    
employee1 = Employee("Martin", "Manager", 5000)
employee2 = Employee("Conny", "Cashier", 2700)
employee3= Employee("Claudia", "Cook", 3500)

employees = [employee1, employee2, employee3]

for employee in employees:
    print(employee.get_info())

print(Employee.is_valid_position("Manager"))

print(Employee.get_count())
print(Employee.get_average_salary())