import random

def fun(x):
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
x=10
print("Welcome! lets play 'Guess the Number' where I choose a number and you have to guess it. Afraid? Dont worry at each step i will be giving you hints whether your guess was to high or low. So are you rady? Lets play!" )
fun(x)
