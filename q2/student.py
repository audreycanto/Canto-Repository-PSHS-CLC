class Student:

    def __init__(self, name, age):

        self.__name = name

        self.__age = 0

        self.set_age(age)


    #setter and getter methods for name

    def set_name(self, name):

        self.__name = name


    def get_name(self):

        return "Hello my name is " + self.__name


    #setter and getter methods for age

    def set_age(self, age):

        if age > 0:

            self.__age = age


    def get_age(self):

        return self.__age

s = Student("Aliyah", 14)
s.set_age(-15)
print(s.get_name())
print(s.get_age())
