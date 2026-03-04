# we wont dive into how conditonals actually work under the hood, (as much as i would like to)

# the most basic conditional in python is an 'If statement'
# it checks if a value equals a condition

# here's how you write one

value = 1
CONDITION = 0  # remember that constants use all caps

if value == CONDITION:
    print("Condition met")

# thats it.

# we can also add onto this with the 'else' and 'elif' keywords
# 'elif' means "else if"
elif value is not CONDITION:
    print("Condition not met")
else:
    print("Third option")

# you can also use strings and put the value to check inside of the statement without a variable
operator = '*'
if operator == '*':
    print(2*3)


# please not two things:
#   1. the ':' at the end of the statement with an 'if', 'elif' or 'else'
#   2. the use of two things, words and symbols.
#      we will not cover the difference between using symbols and words in this level of the course

# in this course we will view them as the same as their symbol counterparts.
# henceforth, we will be using only symbols in this course like other languages

# symbols:

# is (==)
# is not (!=)
# in (for lists (iteratables))
