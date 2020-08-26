import os

os.chdir(r'/Users/baixilin/Developer/Python_Learning/Python_Intermediate/IO')
print(os.getcwd()) #

f = open("record.txt", "r")
line = f.readline()
f.close()

f = open("record.txt", "w")
f.write('abc')
f.close()
