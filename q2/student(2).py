class Student:
    def __init__(self, name, age):

        self.__name = name

        self.__age = age

    @property
    def name(self):
        return "Hello my name is " + self.__name + "."
    
    @property
    def age(self):
        return " I am " + str(self.__age) + " years old."

    @name.setter
    def name(self, value):
        self.__name = value;

    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        
s = Student("JM", 30)
s.name = "Sir Bern"
s.age = 31
print(s.name + s.age)

