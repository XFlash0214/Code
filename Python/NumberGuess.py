import random
n=random. randint(0,50)
print("I am thinking of a number 0-50. Write a number. I will say higher or lower. You have 5 guesses.")
g=int(input())
if g>n:
    print("Lower")
if g<n:
    print("Higher")
if g==n:
      print("Congratulations, you win!")
      exit()
      
h=int(input())
if h>n:
    print("Lower")
if h<n:
    print("Higher")
if h==n:
      print("Congratulations, you win!")
      exit()
      
j=int(input())
if j>n:
    print("Lower")
if j<n:
    print("Higher")
if j==n:
      print("Congratulations, you win!")
      exit()
          
z=int(input())
if z>n:
    print("Lower")
if z<n:
    print("Higher")
if z==n:
      print("Congratulations, you win!")
      exit()
          
x=int(input())
if x>n:
    print("Lower")
if x<n:
    print("Higher")
if x==n:
      print("Congratulations, you win!")
      exit()
          
print("What is you final answer?")
i=int(input())
if i==n:
    print("Congratulations, you win!")
if i>n or i<n:
    print("Sorry, the answer is "+str(n)+".")
