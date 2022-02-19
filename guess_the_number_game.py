import random

## We guess a number

def guess(x):
    random_number=random.randint(1, x)
    guess = 0 
    while guess != random_number:
        guess = int(input(f'Guess a number 1 and {x}: '))
        if guess > x:
            print(f'Lutfen sadece 1-{x} arasinda tahmin yapiniz')
        elif guess > random_number:
            print('Try a smaller number')
        elif guess < random_number:
            print('Try a bigger number')
        elif guess == random_number:
            print('You found the correct number !!')
        
guess(20)

## We choose a number and Computer try to guess it


def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback!='c' :
        if low != high:
             guess=random.randint(low, high)
        else:
            guess = low        
        feedback = input(f'Is {guess} too high (H), too low (L) or correct (C): ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print('Yes. You are correct')
computer_guess(1000)

