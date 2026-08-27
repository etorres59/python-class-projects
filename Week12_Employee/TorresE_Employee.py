###
# Name: Evan Torres
# Date: 7/26/27
# Program Name: Employee
# Program Purpose: Defines a Person superclass that stores and manages basic personal information,
# extends it with Employee and Programmer subclasses that add job related details such as salary
# and programming language.The program creates objects from each class, displays their information,
# and demonstrates the use of class variables and methods by applying salary raises to employees.
###

#Person Superclass
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # toString to print full name
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # Person Getters and Setters
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

class Employee(Person):
    def __init__(self, first_name, last_name, age, salary):
        Person.__init__(self, first_name, last_name, age)
        self.salary = salary

    # Employee Raise Variable
    amnt_of_raise = 1.05

    #method for giving raises
    def give_raise(self):
        self.salary = self.salary * self.amnt_of_raise

    # Employee Getters and Setters
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

class Programmer(Employee):
    def __init__(self, first_name, last_name, age, salary,prog_language):
        Employee.__init__(self, first_name, last_name, age, salary)
        self.prog_language = prog_language

    def known_language(self) -> str:
        return f"{self.first_name} {self.last_name} knows {self.prog_language}"

    # Programmer Raise Variable (Overwrites Employee Raise Variable)
    amnt_of_raise = 1.10

    # Programmer Getters and Setters
    @property
    def prog_language(self):
        return self._prog_language

    @prog_language.setter
    def prog_language(self, prog_language):
        self._prog_language = prog_language

def main():
    # Instantiate Objects
    person1 = Person("John", "Doe", 40)
    employee1 = Employee("Jane", "Doe", 37, 30000)
    programmer1 = Programmer("Evan", "Torres", 31, 150000, "Python")


    # Print Objects
    print(person1)
    print(employee1)
    print(programmer1)

    #Prints Programmer1's programming language
    print(programmer1.known_language())

    # Print Salaries Before
    print(f"{employee1.__str__()}'s salary before raise is {employee1.salary}")
    print(f"{programmer1.__str__()}'s salary before raise is {programmer1.salary}")

    # Give Raises
    employee1.give_raise()
    programmer1.give_raise()

    # Print Salaries After Raises
    print(f"{employee1.__str__()}'s salary after raise is {employee1.salary}")
    print(f"{programmer1.__str__()}'s salary after raise is {programmer1.salary}")


if __name__ == "__main__":
    main()









