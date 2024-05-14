import platform, winsound, time, os

def sound():
    
    for i in range(5): #Number of repeats
        for j in range(9): #Number of beeps
            
            winsound.MessageBeep(-1) #Sound played
            
        time.sleep(2) #How long between beeps
        

def alarm(n):
    
    print()
    print("Wait time: ", n, "seconds. ")
    time.sleep(n) #Waits 'n' seconds before playing sound
    
    sound()
    
def input_destinations(user_input):
    
    if user_input == '1':
        
        user_input = int(input("Enter your desired hours: "))
        
        wait_time = (user_input *60)*60
        alarm(wait_time)
    
    elif user_input == '2':
        
        user_input = int(input("Enter your desired minutes: "))
        
        wait_time = user_input *60
        alarm(wait_time)
        
    elif user_input == '3':
        
        user_input = int(input("Enter your desirede seconds: "))
        
        wait_time = user_input
        alarm(wait_time)
        
    elif user_input == '4':
        
        hours = int(input("Hours: "))
        minutes = int(input("Minutes: "))
        seconds = int(input("Seconds: "))
        
        wait_time = ((hours*60)*60) + (minutes*60) + seconds
        print(wait_time)
        alarm(wait_time)
        
    else:
        try:
            os.system('cls') #If the OS is Windows
            main()
        
        except:
            os.system('clear') #If the OS is Linux/Mac
            main()
            
            
def main():
    print("What unit of time do yu want to wait? \n (1) Hours\n (2) Minutes\n (3) Seconds\n (4) Combined")
    main_input = input(": ")
    
    input_destinations(main_input)
    
    return;

main()