balance = 0
last_transaction = []


#for deposting money
def deposit(amount):
    global balance
    global last_transaction

    if amount > 0:
        balance = balance + amount
        last_transaction.append(amount)
    else:
        print(" error !!! Enter correct value")

#for withdrawing money
def withdraw(amount):
    global balance
    global last_transaction

    if balance >= amount:
        if amount != 0:
            balance = balance - amount
            last_transaction.append(-amount)
        else:
            print("!!! invalid task !!!")
    else:
        print("Insufficinet Balance !!!")


#for bank statements
def bank_statements():
   # global last_transaction
    print("-----statements-----")
  
    if len(last_transaction) > 10:
        last_transaction.pop(0)

    if len(last_transaction) == 0:
        print("you don't have any statements")
    else:
        for i in range(len(last_transaction)):
            print("your transaction  -->|{}| is a -->|{}|".format(i+1, last_transaction[i]))
            

#for checking input is intger?
def int_check(amount):
    try:
        int(amount)
        return int(amount)
    except:
        return False

print("Welcome to bhavesh's intractive piggybank")
print("-----Main Manu-----")
print("press 'd' for depositing money")
print("press 'w' for withdrawing money")
print("press 's' for statement")
print("press 'm' for main manu")
print("press 'q' for quite")

action = input("Enter  the charter-->").lower()
while action != 'q':

    if action == 'd':
        amount = input("Enter how much you want to deposit -->")
        amount = int_check(amount)         #converting user's ammount to the intger
        if type(amount) == int:
            deposit(amount)  
        else:
            print("error")
            print("please Enter the correct value") 
    elif action == 'w':
        amount = input("Enter how much you wanto to withdraw-->")
        amount = int_check(amount)         #converting user's amount  to the intger
        if type(amount) == int:
            withdraw(amount)
        else:
            print("error")
            print("please Enter the correct value")
    elif action == 's':
        bank_statements()
    elif action == 'm':
        print("-----Main Manu-----")
        print("press 'd' for depositing money")
        print("press 'w' for withdrawing money")
        print("press 's' for statement")
        print("press 'q' for quite")
    else:
        print("Enter the correct command")
        

    action = input("Enter the charter-->").lower()
else:
    print("Thak you for using bhavesh's Intractive piggybank")