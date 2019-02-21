#lab8, this lab require either user or computer play the guessing number game 
import random

#human guess
def humanGuessing():
    answer = random.randrange(0,101,1)
    guess_time = 0
    print(answer)
    while True:
        if guess_time == 6:
            print("you are out of guess")
            break
        
        guess = input("please enter a number from 1 to 100 you guessed or 'exit' to exit the game: ")
        if guess.lower() == 'exit':
            #the user want to end the game
            print('the user game has end')
            break
      
        guess = int(guess) #must transfer the str input to int
        if guess < 0 or guess > 100:
            print('you guess is out of range, please enter the number from1 to 100.')
            continue
        elif guess > answer:
            print('too high')
        elif guess < answer:
            print('too low')
        else:
            print("Hooray you won!")
            break 
        
        guess_time += 1
        

def computerGuessing():
    start = 0
    end = 101
    
    while True:
        guess = random.randrange(start, end, 1)
        print("Computer Guess:", guess)
        user_prompt = input("")
        guess_time = 0
        
        # computer win
        if user_prompt.lower() == 'win':
            print("Hooray the computer won")
            break         
        elif user_prompt == '+':
            start = guess + 1
        elif user_prompt == '-':
            end = guess-1
        elif user_prompt.lower() == 'exit':
            # game end
            print("the computer game has end")
            break            
        else: #when the input is neither '+','-','exit' and 'win'
            print('user input wrong, please input the correct order.')
            continue
        
            
def main():
    
    while True:
        user_com = input('please enter who guess the number.(Computer or User): ')
        if user_com.lower() == 'user':
            humanGuessing()
        elif user_com.lower() == 'computer':
            computerGuessing()
        else:
            print('wrong order, please enter either computer or user')
            continue
main()
        
            