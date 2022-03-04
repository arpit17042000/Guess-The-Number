import random

def guess_by_user(x):
    print("Do you want to play Y/N")
    choice=input()
    while choice=='Y':
        random_number=random.randint(1,x)
        print(f"I have chosen a number now guess it and it is between 1 to {x}")
        guess=0
        while guess!=random_number:
            guess=int(input("Guess a number"))
            if guess>random_number:
                print("Sorry! Your guess was too high")
            elif guess<random_number:
                print("Sorry! Your guess was too low")
        print(f"Jackpot! you have guessed the number {random_number} correctly")
        print("Do  you want to play another round Y/N")
        choice = input()
        if choice == 'N':
            return
        print("Fun! Right? Now lets make it more intersting I will be giving you only 5 moves and you have to guess the number in 5 moves")
        random_number=random.randint(1,x)
        print(f"I have chosen a number now guess it and it is between 1 to {x}")
        guess,moves=0,1
        while guess!=random_number and moves<=5:
            guess=int(input("Guess a number"))
            if guess>random_number:
                print("Sorry! Your guess was too high")
            elif guess<random_number:
                print("Sorry! Your guess was too low")
            moves+=1
        if guess==random_number:
            print(f"Jackpot! you have the guess the number {random_number} correctly")
        else:
            print(f" Sorry you were not able to guess the number {random_number}")
        print("See it was so fun! Do you wish to play another game Y/N")
        choice=input()

def guess_by_computer(x):
    print("Oh! you want me to guess your number?! Fine then lest bring it on!")
    low=1
    high=x
    print(f"Remember you have to choose between 1 and {x} and since i am not that 'smart' I need your help. Please give me feed back whther my guess was too high(h) or too low(l) or correct(c).So guess your number")
    low,high,feedback,guess=1,x,'',0
    
    while feedback!='c':
        if low!=high:
            guess=random.randint(low,high)#since randint throws an erorr that is why if else 
        else:
            guess=low
        feedback=input(f"is {guess} too high,too low or correct")
        if feedback == 'h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
    print(f"See i may not be that dumb i guess your number correctly and that is {guess}")


x=10
choice=input("whom do you want to guess the number yourself(me) or the computer(c)")
if choice=='me':
    print("Welcome! lets play 'Guess the Number' where I choose a number and you have to guess it. Afraid? Dont worry at each step i will be giving you hints whether your guess was to high or low. So are you ready?" )
    guess_by_user(x)
else:
    guess_by_computer(x)
print("See you next time")
