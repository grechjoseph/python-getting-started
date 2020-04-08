""" IMPORTS """
from data.Person import Person
from data.Student import Student

""" VARIABLES """
print("\nVARIABLES:")
string = "abcdefghijklmnopqrstuvwxyz"

# print character at index 5.
print(string[5])

# print from index 1 up to index 5 (index 5 excluded), ie: "bcde".
print(string[1:5])

# print from start up to index 5 (index 5 excluded), ie: "abcde".
print(string[:5])

# print from start to finish, excluding last 2.
print(string[:-2])

""" PLACEHOLDERS """
print("\nPLACEHOLDERS:")
name = "John"
lastname = "Doe"

sentence = "Hello %s"
# print sentence with value of name in placeholder.
print(sentence % name)
# print sentence with hard-coded value in placeholder.
print(sentence % "Tom")

# print sentence with two values for two placeholders.
sentence2 = "Hello %s %s"
print(sentence2 % (name, lastname))

# print sentence with two values for two placeholders.
sentence3 = "%s is %d years old."
print(sentence3 % (name, 50))

""" LISTS """
print("\nLISTS:")
fruit = ["apples", "oranges", "bananas", "kiwi"];
# print element at index 0.
print(fruit[0])
fruit[0] = "cherries"
print(fruit[0])
print(fruit[1])
print(fruit[2])
print(fruit[3])
# print elements from index 0 up to index 2 (index 2 excluded)
print(fruit[0:2])
# print elements from start up to index 2 (index 2 excluded)
print(fruit[:2])

# print all elements in list.
print(fruit)
# delete element at index 1.
del fruit[1]
print(fruit)
# print twice.
print(fruit * 2)

listOfNumbers = [10, 4, 6, 8]
# print maximum from list.
print(max(listOfNumbers))

""" DICTIONARIES """
print("\nDICTIONARIES:")
students = {
    # key : value
    "Bob": 12,
    "Rachel": 13,
    "Emily": 15
}

# Print age of Rachel.
print(students["Rachel"])

# Update age.
students["Rachel"] = 15
print(students["Rachel"])

# Add Student.
students["New"] = 20
print(students["New"])

# Delete Student
print(students)
del students["New"]
print(students)

# Print dictionary size
print(len(students))

""" TUPLES (Immutable Lists) """
print("\nTUPLES:")

# Cannot be changes after being defined.
tup = ("oranges", "apples", "bananas")
print(tup)

# Still accessible as lists
print(tup[:2])
print(len(tup))

# But tuples can be combined.
tup2 = (1, 5, 8)
tup3 = tup + tup2
print(tup3)

# Tuple can be deleted from memory
del tup

""" CONDITIONAL STATEMENTS """
print("\nCONDITIONAL STATEMENTS:")
condition = 2
if (condition == 0):
    print("True Line 1")
    print("True Line 2")
# AND: condition 1 and condition 2
elif (condition == 1 and 1):
    print("Is 1")
    print("Is 1b")
# OR: condition 2 or condition 2
elif (condition == 2 or 1):
    print("Is 2")
    print("Is 2b")
else:
    print("False Line 1")
    print("False Line 2")
print("Done")

""" FOR LOOPS """
print("\nFOR LOOPS:")
items = ["apples", "oranges", "bananas"]

for item in items:
    print(item)

# Iterate i == 0, i < 10 (10 excluded)
for i in range(0, 10):
    print(i)

print()

# Iterate i == 0, i < 10 with an increment factor of 2
for i in range(0, 10, 2):
    print(i)

""" WHILE LOOPS """
print("\nWHILE LOOPS:")
c = 0

# Traditional While Loop.
while c < 5:
    print(c)
    c = c + 1

print()

# Break loop.
c = 0
while c < 5:
    print(c)
    c = c + 1
    if (c == 3):
        break

print()

# Continue loop.
c = 0
while c < 5:
    print(c)
    c = c + 1
    if (c == 3):
        continue
    print("finished")

print()

# Pass - somewhat a pending piece of code.
c = 0
while c < 5:
    print(c)
    c = c + 1
    if (c == 3):
        pass
    print("finished")

""" EXCEPTIONS """
print("\nEXCEPTIONS:")
# Catch an exception using try/except
try:
    if (variableThatDoesNotExist == 3):
        print("doStuff")
except:
    print("There is something wrong with your code.")

""" FUNCTIONS """
print("\nFUNCTIONS:")


# Define a function using def <functionName>(<arg1>, <arg2>, ...)
def Add(num1, num2):
    print(num1 + num2)


Add(1, 2)
Add(1, 3)


# Return result of a function using 'return'.
def CalculateAdd(num1, num2):
    return num1 + num2


print(CalculateAdd(1, 2))
print(CalculateAdd(1, 3))

""" IN-BUILT FUNCTIONS """
print("\nIN-BUILT FUNCTIONS:")

# Absolute number
print()
print(abs(-3))

# Bool (0 = false, any other number = true)
print()
print(bool(0))
print(bool(None))
print(bool(1))
print(bool(2))
print(bool(-1))

# List all functions available to object (eg: String)
print()
print(dir("Hello"))

# Print help for an object's function.
print()
hello = "Hello"
help(hello.upper)

# Evaluate python code in String format.
print()
command = 'print("Hello")'
eval(command)

# Execute python code in String format (ideal for multiple lines of code).
print()
command = 'print("Hello")'
exec(command)

# Changing data types.
print()
a = 1
print(str(a) + str(a))
print(float(a) + float(a))
print(int(a) + int(a))
print(str(a))

""" OBJECT-ORIENTED PROGRAMMING """
# Class and object
print("\nOBJECT-ORIENTED PROGRAMMING:")
p = Person("Joseph", "Grech", 29)
print("%s %s is %d years old." % (p.getFirstName(), p.getLastName(), p.getAge()))

# Inheritance
s = Student("Joseph", "Grech", 29, "Python")
print("%s %s is %d years old, and is reading a %s course." % (s.getFirstName(), s.getLastName(), s.getAge(), s.getCourse()))
