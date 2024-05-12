mylist = [' ','O',' ']

from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return(mylist)


def player_guess():
    
    guess = ' '
    
    while guess not in ['0','1','2']:
         
         guess = input("Pick a number: 0,1,2: ")
         
    return int(guess)



def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print("Correct!!")
        
    else:
        print("Wrong Answer!!")
        
        
#intial list
mylist = [' ','O',' ']

#shuffle list
mixedup_list = shuffle_list(mylist)

#user guess
guess = player_guess()

#check guess
check_guess(mixedup_list,guess)

input("prompt:")
