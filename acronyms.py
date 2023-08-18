def find_acroynms():
    look_up = input("What software acroynm would you like to look up\n")

    found = False
    try:
        with open('./fundamentals/acronymssdfds.txt') as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found=True
                    break
    except FileNotFoundError as e:
        print("file not found")
        return
    
    if not found:
        print("Acroymn is not there")

def add_acroynm():
    acroynm=input("What acroynm do u want to add?\n")
    defenition=input("What is the defeition?\n")
    with open("./fundamentals/acronyms.txt","a")as file:
        file.write( acroynm+"-"+ defenition+"\n")

def main():
    choice= input("Do you want to find an ancroynm(f) or add an ancroynm(a)\n")
    if choice == "f":
        find_acroynms()
    elif choice == "a":
        add_acroynm()
    else:
        print("invalid option")

main()