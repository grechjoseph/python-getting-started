class Person:
    def __init__(self, firstName, lastName, age):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__age = age

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getAge(self):
        return self.__age