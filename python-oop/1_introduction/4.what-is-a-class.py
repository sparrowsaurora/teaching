# A class is a blueprint for creating objects.
# It defines the structure (attributes) and behavior (methods) of its objects.
# Example:
    
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(f"{self.name} says woof!")
    
# `__init__` is a special method (constructor) that runs when an object is created.
# `self` refers to the specific object (instance) being created or used.

# here's the bottle class we saw in part 1

class bottle: # <- first we define the blueprint's name
    # now we need to construct / make / initialize the bottle we using the __init__ magic method for this
    # we'll learn more about magic methods and initializations later
    def __init__(self): # <- We define a method like a normal function except we pass in self as an argument
        # all 'self' means right now. is it looks at itself (the instance) and look a the attributes and methods of the bottle
        # so 'self' means "take a look at what the bottle is full of. and what methods it has"
        self.liquid = "water" #this set's the bottls's first attribute and fills it with "water"
    
    # looking at 'self.liquid' we see it's defined similarly to a normal variable.
    # except it starts with self. in this case self just means the current bottle we're looking at
    # variables in procedural programming do this too. but the 'self.' part is hidden becasue it is implied


    def drink(self): #this is out first method. it takes in 'self' meaning it looks at the current bottle.
        print(f"drinking {self.liquid}") #then it prints out the the bottle.
        # but only selects the liquid atrribute to print from the bottle
        # the 'self' syntax might be confusing at first. but i will get simpler over time
        
        # Self looks at the current bottle,
        # the '.' make it look for a specific item in that bottle,
        # then we name the bottle's attribute (variable) we want to look at