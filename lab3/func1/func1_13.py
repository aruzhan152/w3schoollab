import random

print('Guess a number')
def Game():
    target=random.randrange(1,100)
    #print(target)
    n=0
    while True:
        guess=int(input())
        if guess==target:
            print(f'YOU WON!!! \n{n} trials')
            exit()
        if guess>target:
            print('Your guess is too big :(')
            n+=1
        else:
            print('Your guess is too low :(')
            n+=1
            
cn=Game()
            
    
        