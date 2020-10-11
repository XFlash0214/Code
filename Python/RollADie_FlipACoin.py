import random
import time

x=random.randint(0,1)
z=random.randint(1,6)

print("Choose Heads or Tails, Roll a Die, or Quit.")
y=input()


def prog():
    if y=="Heads or Tails".upper():
        if x==0:
            print("Tails")
        if x==1:
            print("Heads")

    if y=="Roll a Die":
        print(z)
    
    if y=="Quit":
        quit()
        
    
prog()
time.sleep(5)
