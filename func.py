# -------------------------------------- Task 1 -----------------------------------
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def div(x, y):
    return x / y

# TODO: Add definitions of sub(), div(), mult(), exp(), as well as neg() and sqrt().
#       neg() should return the negation of the given number, and sqrt() should
#       return the square root of the given number. 
def neg(x):
    return -x # fill here

def sqrt(x):
    return x^1/2 # fill here

# -------------------------------------- Task 2 -----------------------------------

# TODO: Implement the quadratic formula using *only* the functions defined here.
#       Do not use arithmetic operators directly. 
#       You're allowed to define other functions.
a = 1
b = -3
c = 1

x1 = add((neg(b)), (sub(b ** 2, 4 * a * c) ** 0.5)) # TODO: write a code to compute the first root of the quadratic equation
x2 = sub((neg(b)), (sub(b ** 2, 4 * a * c) ** 0.5)) # TODO: then do the same for the second root
# Note: Make sure to remove the ellipsis (...) when you're writing your code

print("First root:" + str(x1))
print("Second root:" + str(x2))
