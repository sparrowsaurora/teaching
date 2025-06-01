class name:
    def a_function(self):
        print("in the name class")

# Think of an instance as a object made by the blueprints. its an object like any other datatype.
# It can have methods and be used in functions.
# An instance is a tangible version of a class and we can create multiple instances from one class.

# Now we're going to Create an instance. 
# We have the class from the last section above. Now we'll create an instance

# first we assign a the class name to a variable
# we assign the class by stating a variable = the class name (that is called like a function)
class_variable = name()

# now we can use the class's methods as normal functions. that are assigned to that variable
# so we can write the variable. and then called the method linked to the class

class_variable.a_function()
