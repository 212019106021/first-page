# Python basics lesson 3: functions

# A function is a reusable block of code

def greet(name):
    print("Hello, " + name)


greet("Asha")
greet("Ravi")

# Function with return value

def add(a, b):
    return a + b

result = add(5, 3)
print("Result:", result)

# Function with default value

def welcome(name="friend"):
    print("Welcome, " + name)

welcome()
welcome("Asha")
def make_tea():
    return "Tea is ready"

tea = make_tea()
print(tea)


def make_coffee():
    return "Coffee is not "

coffee = make_coffee()
print(coffee)