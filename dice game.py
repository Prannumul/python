import random
    
def roll_dice():
    dicetotal= random.randint(1,6) +random.randint(1,6)
    return dicetotal
player1=input("Enter Player 1's Name ")
player2=input("Enter Player 2's Name ")

roll1 = roll_dice()
roll2 = roll_dice()
print (player1,'rolled',roll1)
print (player2,'rolled',roll2)

if (roll1>roll2):
      print(player1,'wins!')
elif (roll2>roll1):
      print(player2,'wins!')
else:
     print("You tied")