import random

dice_faces = [ "| · |", "|· ·|", "|···|", "|: :|", "|:·:|", "|:::|"]

while True:
    num_dice = int(input("Number of dices you want to rolling: "))
    
    for i in range(0,num_dice):
        print("")
        s = random.choice(dice_faces)
        print(s," → " , dice_faces.index(s) + 1)
        
    choice = input("Continue: Yes(y) ←→ No (n) ").lower()
    
    if choice == "y":
        continue
    elif choice == "n":
        break
    
    try:
        if choice != "n" or num_dice != "y":
            raise ValueError
        pass
        
    except ValueError:
        print(" ******************************* ")
        
        