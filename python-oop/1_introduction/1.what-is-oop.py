# Definition:
# OOP (Object-Oriented Programming) is a programming paradigm based on the concept of "objects", which are instances of "classes".

# Objects contain data (called attributes) and behaviors (called methods(similar to functions)).

# It is easy to think of objects as "real-world entities" modeled in code.
# Think of a class as a blueprint. in this example - a blueprint of a bottle.
# A bottle can contain a liquid like water <- this is an attribute
# It can also have a lid, or a label.
# This bottle can also be opened, drank from, and refilled <- these are methods

# When making a bottle (initializing) we look at the blueprint and set the variables like we pass into a function.
# Here's a practical example

class bottle: 
    def __init__(self): 
        self.liquid = "water"

    def drink(self): 
        print(f"drinking {self.liquid}")

#we'll cover all the part of this code in the next section