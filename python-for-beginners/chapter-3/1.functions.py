# Functions are reusable blocks of code, that you can write once and use many times

# lets write a function

def function_name(param):
    return 0

# a function has 3 distinct elements
# a 'def' or definition, this says "im about to define a function"
# the name for the function
# and a parameter, this is what the function will take to do some action

# finally when you want to call it


# you simple call it like the "print" function we've used before
var = function_name("hi")

# here is a practical example using what we have learnt so far


def greet_user(name):
    if name == "":  # blank string
        return "Hello, User"
    else:
        return "hello, " + name


print(greet_user("John"))
print(greet_user(""))
