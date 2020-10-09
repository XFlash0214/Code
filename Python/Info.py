import time

print("How old are you?")
x=int(input())
a=17
if x>a:
    print("You are an adult.")
if x<a+1:
    print("You are a kid.")



print("What is your name?")
y=input()
print("Where are you from?")
z=input()
print("Thank you, "+y)
print("Your name is "+y+", you are "+str(x)+" years old, and you are from "+z+".")
time.sleep(3)
