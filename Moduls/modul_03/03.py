message = "Hello Mr. "

def greet(name):
    print(message, name)

def greet2(name):
    message = "Good morning Mr. "
    print(message, name)

def greet3(name):
    global message
    message = "Good morning Mr. "
    print(message, name)

greet("Sergiy")

greet2("Max")
print(message)

greet3("Kostja")
print(message)

greet2("Max-2")
print(message)