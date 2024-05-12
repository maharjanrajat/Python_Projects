# Display list
game_list = [0,1,2]

def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)
    
# take position choice from user    
def position_choice():
    
    choice = 'wrong'
    
    while choice not in ['0','1','2']:
        
        choice = input("pick a position (0,1,2): ")
        
        if choice not in ['0','1','2']:
            print("Sorry, invalid choice!")
            
    return int(choice)

# Take replace choice from user
def replacement_choice(game_list,position):
    
    user_placement = input("Type a string to place at position: ")
    
    game_list[position] = user_placement
    
    return game_list

# Ask if keep playing or not
def gameon_choice():
    
    choice = 'wrong'
    
    while choice not in ['Y','N']:
        
        choice = input("Keep playing? ('Y','N') ")
        
        if choice not in ['Y','N']:
            print("Sorry, I dont understand, please choose Y or N")
            
    if choice == "Y":
        return True
    else:
        return False

# Final result
game_on = True
game_list = [0,1,2]

while game_on:
    
    display_game(game_list)
    
    position = position_choice()
    
    game_list = replacement_choice(game_list,position)
    
    display_game(game_list)
    
    game_on = gameon_choice()
    
