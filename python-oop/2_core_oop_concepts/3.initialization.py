# when we first made our instance. we called it like this

# variable = class_name()

# well since we're calling a class like we do with a function that returns a variable.
# we can also pass into the class a few arguments when we initialise it.
# we do that by creating a method in the class called a magic method (we'll learn more about this soon)
# the magic method we're going to write is called an init method or constructor. in python it looks like this __init__
# Note: the double underscore prefix and suffix is the convention of magic methods in python
# we define it as a normal function. now we can write one

# first we make the class
class initialisation:
    # then we write the __init__ method
    # we can ask for parameters in this function. this is how we will know what to pass into the class when defining it.
    # we also need to pass self, as we do for all other methods in a class
    def __init__(self, name, age):
        # then we assign these parameters to variables in the self 'container'
        self.name = name
        self.age = age
    
    # we access the variables in this class (attributes) by writing 'self.' as a prefix.
    # again, this means look in your own instance
    def show(self):
        print(self.name, self.age)

# now we can make an instance
instance = initialisation("ryan", 18)
instance.show()
