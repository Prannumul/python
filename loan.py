money_owed=float(input("How much money do you owe,in dollars?\n"))
apr=float(input("What's is the annual percentage rate of loan\n?"))
payments=float(input("How much will you pay off each month in dollars?\n"))
months = int (input ("How many months do you want to see the results for?\n"))
monthly_rate=apr/100/12
for i in range(months):
    interest_paid= money_owed*monthly_rate

    money_owed=(money_owed) + interest_paid
    if(money_owed-payments<0):
        print("The last payment is",money_owed )
        print("You paid off the loan",i+1,"months")
        break
    money_owed=money_owed-payments

    print("Paid",payments,"of which",interest_paid, "was interest", end="")
    print("Now I owe", money_owed)


    
    
