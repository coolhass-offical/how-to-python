# Instructions that a Python interpreter can execute are called statements.
a = 1

# In Python, the end of a statement is marked by a newline character.
# But we can make a statement extend over multiple lines with the line continuation character (\).
b = 1 + 2 + 3 +\
    3 + 4 + 5 +\
    5 + 6 + 7

# In Python, line continuation is implied inside parentheses ( ), brackets [ ], and braces { }.
c = (1 + 2 +
     3 + 4)

# The surrounding parentheses ( ) do the line continuation implicitly. Same is the case with [ ] and { }.
colors = ['green',
          'red',
          'blue']

# We can also put multiple statements in a single line using semicolons.
d = 1
e = 2
f = 3
# ps: vscode putts them in order automaticly.
# like this
g = 1
h = 2
i = 3

print(a, b, c, d, e, f, g, h, i, colors)


#triple quotes can also be used while writing docstrings
def double(num):
    """Function to double the value"""
    return 2*num
print(double.__doc__)
