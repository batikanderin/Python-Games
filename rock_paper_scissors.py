import random
## VERSION 1

def game():    
    while True:
        list=['tas','kagit','makas']
        durum=random.choice(list)        
        guess=input('Elinizi oynayiniz: ')
        bilgisayar = durum
        oyuncu = guess        
        
        if bilgisayar == 'tas' and oyuncu=='kagit':
            print(f' bilgisayar: {bilgisayar} ****** oyuncu: {oyuncu}: oyuncu won')
        elif bilgisayar=='tas' and oyuncu=='makas':
            print(f'{bilgisayar}-{oyuncu}: bilgisayar won')
        elif bilgisayar=='kagit' and oyuncu=='makas':
            print(f'{bilgisayar}-{oyuncu}: oyuncu won')
        elif bilgisayar=='kagit' and oyuncu=='tas':
            print(f'{bilgisayar}-{oyuncu}: oyuncu won')
        elif bilgisayar=='makas' and oyuncu=='kagit':
            print(f'{bilgisayar}-{oyuncu}: bilgisayar  won')
        elif bilgisayar=='makas' and oyuncu=='tas':
            print(f'{bilgisayar}-{oyuncu}: oyuncu won')
        elif bilgisayar=='makas' and oyuncu=='makas':
            print(f'{bilgisayar}-{oyuncu}: Kimse kazanmadi')
        elif bilgisayar=='tas' and oyuncu=='tas':
            print(f'{bilgisayar}-{oyuncu}: Kimse kazanmadi')
        elif bilgisayar=='kagit' and oyuncu=='kagit':
            print(f'{bilgisayar}-{oyuncu}: Kimse kazanmadi')
        elif player2=='C':
            break   

game()

## VERSION 2
def play():
    user=input(" 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer=random.choice(['r','p','s'])

    if user == computer:
        return 'It\s a tie'

    if is_win(user, computer):
        return f'{user} {computer} You won!'
    
    return f'{user} {computer} You lost!'

        
def is_win(player,opponent):
    if (player == 'r' and opponent=='s') or (player=='s' and opponent=='p') or (player == 'p' and opponent == 'r'):
        return True

print(play())