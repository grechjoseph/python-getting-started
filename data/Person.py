class Person:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getAge(self):
        return self.age