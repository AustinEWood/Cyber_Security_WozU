class Employee:
    """New superclass for Employee information."""
    def __init__(self, name, salary, hire_date):
        """Initialize of Employee class properties."""
        self.name = name
        self.salary = salary
        self.hire_date = hire_date

    def get_name(self):
        """Method of get name."""
        return "This employee's name is " +  str(self.name) + "."
    
    def get_salary(self):
        """Method of get salary."""
        return "This employees's salary is " + str(self.salary) + "."

    def get_hired_date(self):
        """Method of get hired date"""
        return "This employee's hire date is " + str(self.hire_date) + "."


class Engineer(Employee):
    """Subclass Engineer of superclass Employee"""
    def __init__(self, name, salary, hire_date):
        """Initialize from superclass Employee for subclass Engineer properties"""
        super().__init__(name, salary,hire_date)


main_employee = Employee("joe smo", 5000, "12/12/19")
engineer_employee = Engineer("jack smack", 20000, "12/12/19")

print(main_employee.get_name())
print(engineer_employee.get_salary())
 
#Part 2

class Software_Engineer(Engineer):
    """Subclass Software Engineer of subclass Engineer of superclass Employee."""
    def get_salary(self):
        """Change the get get salary method of Engineer."""
        return "Sorry, this employee's salary is private."

software_engineer_employee = Software_Engineer("sam man", 20000, "12/12/19")

print(software_engineer_employee.get_name())
print(software_engineer_employee.get_hired_date())
print(software_engineer_employee.get_salary())


#Part 3

class Manager(Employee):
    """Subclass of Employee for Managers."""
    def __init__(self, name, salary, hire_date):
        """Initialize from super class Employee."""
        super().__init__(name, salary, hire_date)

    def get_job_description(self):
        """New method for manager of job description."""
        return "This employee manages all of the Software Engineers."

    def get_years_experiance(self):
        """New method for manager of years experiance."""
        return "This employee has 13 years experience."

    def degree_completed(self):
        """New method of manager of degrees completed."""
        return "This employee completed the following degree: Bachelor in Software Engineering from Arizona State University."

    def get_salary(self):
        """Change the get salary method of Employee."""
        return "Sorry, this employee's salary is private."


manager1 = Manager("dan ran", 10000, "12/12/19")

print(manager1.get_name())
print(manager1.get_hired_date())
print(manager1.get_salary())
print(manager1.get_job_description())
print(manager1.get_years_experiance())
print(manager1.degree_completed())

