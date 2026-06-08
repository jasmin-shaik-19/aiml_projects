while True:
    n1=int(input("enter the first number :"))
    n2=int(input("enter the second number :"))
    print("pick up your choice \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division\n")
    choice=int(input("enter the choice :"))
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        if(b==0):
            return "Error : Division by zero is not allowed"
        return a/b
    if choice ==1:
        print("result :",add(n1,n2))
    elif choice==2:
        print("result :",sub(n1,n2))
    elif choice==3:
        print("result :",mul(n1,n2))
    elif choice==4:
        print("result :",div(n1,n2))
    else:
        print("invalid! please select a valid operation")
        break