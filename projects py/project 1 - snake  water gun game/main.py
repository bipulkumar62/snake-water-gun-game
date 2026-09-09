'''
1 for snake
-1 for water
0 for gun
'''
import random
computer = random.choice([-1, 0, 1])
you = int(input("Enter 1 for snake, -1 for water, 0 for gun: "))


if(computer== -1 and you==1):
    print("you win")

elif(computer== 1 and you==-1):
    print("you lose")

elif(computer== 0 and you==1):
    print("you win")    

elif(computer== 1 and you==0):
    print("you lose")       

elif(computer== 0 and you==-1):          
    print("you lose")

elif(computer== -1 and you==0):
    print("you win")    

else:
    print("it's a tie")    
