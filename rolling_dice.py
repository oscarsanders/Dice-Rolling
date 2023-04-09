from random import randint

dice_faces = [ "| · |", "|· ·|", "|···|", "|: :|", "|:·:|", "|:::|"]

while True:
    num_dice = int(input("Number of dices you want to rolling: "))
    
    for i in range(0,num_dice):
        j = randint(0, 5)
        print("")
        print(dice_faces[j]," → " , j+1)
        
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
        print(" You should choose YES or NO ")
        