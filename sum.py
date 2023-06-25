Number1=input("first number\n")
Number2=input("second number\n")
operation = input("add or mul\n")

if (operation == "add"):
    result=int(Number1)+int(Number2)
elif (operation == "mul"):
    result=int(Number1)*int(Number2)
else:
    print("invalid operation. please enter add or mul")
    exit(0)


#print(type(Number1))

#print(type(sum))
print("Result of the numbers : " + str(result))