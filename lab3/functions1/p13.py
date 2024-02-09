import random
def inter(num,num1):
    i=0
    x=random.randint(num,num1)
    print(x,"\n")
    m=input()
    if m=="Your guess is too low. Take a guess.":
        inter(x,20)
        i+=1
    elif m=="Your guess is too high. Take a guess.":
        inter(1,x)
        i+=1
    elif m=="Good job, KBTU! You guessed my number":
        return
        

    
a=input()
if a=="Hello! What is your name?":
    print("KBTU\n")
b=input()
if b=="Well, KBTU, I am thinking of a number between 1 and 20. Take a guess.":
    inter(1,20)
