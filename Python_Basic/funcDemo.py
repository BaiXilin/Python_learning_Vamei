def square_sum(a,b):
    c = a**2 + b**2
    return c

print square_sum(3,4)

#Example of passing value to functions
a = 1

def change_integer(a):
    a = a+1
    return a

def change_list(b):
    b[0] = b[0] + 1
    return b

a = 1
b = [1,2,3]

print change_integer(a) # a new var is created to hold the passing var, changing the new var won't affect the origin var
print a

print change_list(b) # a pointer of the list is passed -> origin list will be changed
print b