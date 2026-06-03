"""  functions with parameters 

def sum(a,b):
    print(a+b)
sum(2,3)
   
   function with return type
def add(a,b):
    return a+b
print(add(2,3))

((((((((            types of arguments        )))))))))

------->position argument 
def sum(a,b):
    print(a,b)
sum(2,3)

-------> keyword argument
def sum(a,b):
    print(a,b)
sum(a=2,b=3)

------->default argument
def student(result="pass"):
    print(result)
student()

 ------> variable length arguments 
def number(*n):
    print(n)
number(1,2)



(((((((((((((                 modules           )))))))))))))

Any file with .py extension is considered as a module.
in first file (( module1.py  ))
"""
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if(b==0):
        return "divion error"
    else:
        return a/b


