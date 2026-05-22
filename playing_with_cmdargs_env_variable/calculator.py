import sys

def add (a,b):
    add = a+b
    return add

def sub (a,b):
    sub = a-b
    return sub

a = float(sys.argv[1])
opr = sys.argv[2]
b = float(sys.argv[3])

if opr == "add":
    result = add(a,b)
    print (result)

