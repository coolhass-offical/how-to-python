x = y = z = "same"
print(x)
print(y)
print(z)

# Assigning value to constant in Python

'''this will be in the constant.py and main.py'''

# Rules and Naming Convention for Variables and constants

# Constant and variable names should have a combination of letters in lowercase (a to z)
# or uppercase (A to Z) or digits (0 to 9) or an underscore (_).
# If you want to create a variable name having two words, use underscore to separate them.
# like this

my_name = 1

# Use capital letters possible to declare a constant.

PI = 3.14
G = 9.8
MASS = 50
SPEED_OF_LIGHT = 299792458
TEMP = 0

# Never use special symbols like !, @, #, $, %, etc.
# Don't start a variable name with a digit.

# Numeric Literals

# Numeric Literals are immutable (unchangeable).
# Numeric literals can belong to 3 different numerical types:
# Integer, Float, and Complex.

q = 0b1010  # Binary Literals
w = 100  # Decimal Literal
e = 0o310  # Octal Literal
r = 0x12c  # Hexadecimal Literal

# Float Literal
float_1 = 10.5
float_2 = 1.5e2

# Complex Literal
x = 3.14j

print(q, w, e, r)
print(float_1, float_2)
print(x, x.imag, x.real)
