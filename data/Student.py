from data.Person import Person


class Student(Person):
    def __init__(self, firstName, lastName, age, course):
        super(Student, self).__init__(firstName, lastName, age)
        self.__course = course

    def getCourse(self):
        return self.__course