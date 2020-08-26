def test_func():
    try:
        m = 1/0
    except NameError:
        print("Cathc NameError in the sub-function")

try:
    test_func()
except ZeroDivisionError:
    print("Catch error in the main program")
else:
    print("No error found!") #if the except didn't describe the exeception, the program will be terminated