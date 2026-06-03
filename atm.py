balance=int(input("enter your balance "))
transactions=[]
while True:
    print("ATM Menu")
    print("1. check the balance")
    print("2. Deposit money ")
    print("3. Withdraw money")
    print("4. mini statement")
    print("5. Exit")
    choice=int(input("Enter your choice :"))
    def check_balance():
        return balance
    def deposit(amount):
        return amount
    def withdraw(amount):
        if(amount>balance):
            return "insufficient"
        return amount
    if(choice==1):
        print("current Balance: ",check_balance())
    elif(choice==2):
        amount=int(input("enter the amount to deposit:"))
        balance+=deposit(amount)
        transactions.append(f"money deposited is :{amount}")
    elif(choice==3):
        amount=int(input("enter the amount to withdraw :"))
        result=withdraw(amount)
        if result=="insufficient":
            print(result)
        else:
            balance-=result
            print("amount is withdrawed")
            print("current balance is :",balance)
            transactions.append(f"money withdrawed is :{amount}")
    elif(choice==4):
        if(transactions==0):
            print(" no transactions occured ")
        for transaction in transactions:
            print(transaction)
        print("current balance ",balance)
    elif(choice==5):
        print("exited succesfully")
        break
    else:
        print("invalid choice! please try year")
        break


