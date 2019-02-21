import random

# generate a random target number
target = random.randrange(1,20)

# initialize the guess chances
guess_time = 0

while True:
    # check if the user use all the chances
    guess_time += 1
    if guess_time>6:
        print("You are out of guesses. The number was "+str(target)+".")
        break
    
    # Avoid non int inputs
    try:
        guess = input("Enter a guess (1-20): ")
        guess = int(guess)
    except ValueError:
        print("Not A Float")
        guess_time-=1
        continue
    
    # check the range of guess
    if (guess<1 or guess>20):
        print("that number is not between 1 and 20 !")
        guess_time-=1
        continue
    
    # game
    if(guess > target):
        print("Too high!")
    elif(guess < target):
        print("Too low!")
    else:
        print("Correct! The number was "+str(target)+".")
        break
