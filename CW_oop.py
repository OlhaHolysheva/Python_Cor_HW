#Create a class Human, everyone has a name, create a method in the class that displays 
# a welcome message to a each person. Create a class method in the class that returns 
# information that it is a species of "Homosapiens". And also in the class create 
# a static method that returns an arbitrary message. 

# class Human:
#     def __init__(self, name):
#         self.name = name

#     def grating_massege(self):
#         print(f"Hello my dear {self.name}!")

#     def homosapiens_info(self):
#         print("You  are homosapiens")

#     @staticmethod
#     def staticmetod():
#         print("You are the best perdon hole over the world!")

# man = Human("Oleg")
# man.grating_massege()
# man.homosapiens_info()

# print(Human.staticmetod())

###############################################################

class Human:
    # атрибут класу
    species = "Homosapiens"
    # конструктор
    def __init__(self, name):
        self.name = name
    
    #метод екземпляру класу
    def say(self, msg):
        return "{name}>>> {message}".format(name = self.name, message = msg)

    # метод класу
    @classmethod
    def get_species(cls):
        return cls.species

    # статичний метод
    @staticmethod
    def grun():
        return "Static"

    man_1 = Human("Oleg")
    
    print(man_1.say("Hello"))
    print(man_1.get_species())
    print(Human.grun())

#########################################################################

#Create an employee class. Each employee has characteristics such as name and salary. 
# The class should have a counter that calculates the total number of employees, 
# as well as a method that prints the total number of employees 
# and a method that displays information about each employee in particular, namely the name and salary.

#In addition to creating a class, display information about the base classes from which the employee class 
# is inherited (__base__), the class namespace (__dict__), the class name (__name__), 
# the module name in which the class is defined (__module__), the documentation bar ( __doc__) 

class Employee:
    '''General class for all employees.'''
    
    total_counter_employees = 0
    
    def __init__(self, name, age, gender, position, sciense_degree, salery):
        self.name = name
        self.age = age
        self.gender = gender
        self.position = position
        self.sciense_degree = sciense_degree
        self.salery = salery
        
        Employee.total_counter_employees += 1

    def display_total_employees(self):
        return f'Total emploees: {Employee.total_counter_employees}'

    def display_inform_employee(self):
        return f'Name: {self.name} \nAge: {self.age} \nGender: {self.gender} \nPosition: {self.position} \nDegree: {self.sciense_degree} \nSalery: {self.salery}'


emp_1 = Employee('Olga', 28, 'women', 'junior', 'master of manegment', '400')
print(emp_1.display_inform_employee())
print(emp_1.display_total_employees())


print(Employee.__base__) #базові класи від яких наслідується клас працівник 
print(Employee.__dict__) #про простір імен класу
print(Employee.__name__) #ім’я класу 
print(Employee.__module__) #ім’я модуля, в якому визначений клас 
print(Employee.__doc__) #стрічку документації 