string = "abcdefghijklmnopqrstuvwxyz"

# print character at index 5.
print(string[5])

# print from index 1 up to index 5 (index 5 excluded), ie: "bcde".
print(string[1:5])

# print from start up to index 5 (index 5 excluded), ie: "abcde".
print(string[:5])

# print from start to finish, excluding last 2.
print(string[:-2])

# PLACEHOLDERS
name = "John"
lastname = "Doe"

sentence = "Hello %s"
# print sentence with value of name in placeholder.
print(sentence % name)
# print sentence with hard-coded value in placeholder.
print(sentence % "Tom")

sentence2 = "Hello %s %s"
# print sentence with two values for two placeholders.
print(sentence2 % (name, lastname))

sentence3 = "%s is %d years old."
# print sentence with two values for two placeholders.
print(sentence3 % (name, 50))
