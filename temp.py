acroynm=input("What acroynm do u want to add?\n")
defenition=input("What is the defeition?\n")
with open("./fundamentals/vijay1.txt","a")as file:
    file.write(acroynm+"-"+ defenition+"\n")