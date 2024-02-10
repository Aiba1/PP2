import random
def ran(x,a,counter):
    if(a == x):
        return counter
    elif(a<x):
        a = int(input("Your guess is too low. Take a guess."))
        return ran(x,a,counter+1)
    elif(a>x):
        a = int(input("Your guess is too high. Take a guess."))
        return ran(x,a,counter+1)
x = random.randint(1,20)
name = input('Hello! What is your name?')
a = int(input('Well, '+name+', I am thinking of a number between 1 and 20.Take a guess.'))
print('Good job, '+name+'! You guessed my number in '+str(ran(x,a,1))+' guesses!')
