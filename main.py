import random
print('Welcome to the perfect guess game...')
print('press 0 to exit this game...')
print('You have to enter the number that computer chose.\nOnce you guess it correctly,the program will show you the number of guesses in which you guessed the number correctly.\nIf you guessed number in less than 5 times,you win, otherwise you lose...')
max =int(input('The computer will guess from 1 to the maximum number that you are going to enter here: '))
computer=random.randint(1,max)

guesses=0


while True:
    
    
    you=int(input('Enter the number: '))
    
    if you<0 or you>max:
        print(f"Error: Please Enter the number within the range of 1 to {max}")
    else:    
        if you==0:
            print('Exiting the game...')
            break
        guesses+=1
        if  you<computer:
            print('Higher Number Please!')
        elif you>computer:
            print('Lower Number Please!')
        elif you==computer:
            print(f'You guessed the number {computer} correctly in {guesses} guess(es)')
            if guesses<=(max/2):
                print('You Win!')
            else:
                print('You Lose!')
            again=input('Want to play game?y/n: ').lower()
            if again=='n':
                print('Exiting the game...')
                break
            elif again=='y':
                guesses=0
                
        


    
    




    

