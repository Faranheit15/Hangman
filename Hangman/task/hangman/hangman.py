# Write your code here
import random
print("H A N G M A N")
list=["python","java","kotlin","javascript"]
w=random.choice(list)
i=input("Guess the word "+(w[0:3])+""+("-"*(len(w)-3))+": > ")
if (i.lower()==w):
    print("You survived!")
else:
    print("You are hanged!")