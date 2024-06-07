#This program plays the game 'Guess that number'. 
#The objective of the game is to guess the value the computer randomly selects from 1 to 100.
#1.User enters a guess
#2.The function 'validate_input' makes sure user entered an appropriate input
#3.The function 'higher_or_lower' prints if the user's guess is higher or lower than the answer
#4.Steps 1 to 3 are repeated until user guess the correct number.

from random import randint

def validate_input(number, min_value, max_value):
   """This function returns True if the user input is a number and in the valid range
      Args:
        - number: user guess
        - min_value: minimum value of acceptable range
        - max_value: maximum value of acceptable range
    Return:
        -bool: True if valid, False otherwise
   """
   if not(number.isdigit()) or int(number) < min_value or int(number) > max_value: #checks if input is a number then if it is in the valid range
        print(f"Please enter a valid integer from {min_value} to {max_value}")
        return False
   else:
       return True
        
   
def higher_or_lower(guess, answer):
    """This function returns True if user guess is equal to answer and False if guess is higher or lower. 
       It also prints 'lower', if the guess > answer and 'higher' if the guess < answer
       Args:
        - guess: user's guess
        - answer: random generator number
      Returns:
        -bool: True if answer == guess, False otherwise
    """
    if guess > answer:
        print("lower")
    elif guess < answer:
        print("higher")
    elif guess == answer:
        print("Yay you got it")
        return True
    return False


def main():
   min_value = 1
   max_value = 100
   answer = randint(min_value+1, max_value) #random number selected between min_value and max_value
   user_got_it = False

   print("\n\nWelcome! To Guess That Number")
   print(f"The objective of this game to guess a random generated number from {min_value} to {max_value}")
   
   while user_got_it == False: 
        user_guess = input(f"Enter your guess: ")
        if validate_input(user_guess, min_value, max_value) == True:
           guess = int(user_guess)
        else:
            continue
    
        user_got_it = higher_or_lower(guess, answer) #higher_or_lower returns True, then loop can be broken

   print("\n\nThank you for playing Guess That Number")
   print("Hope to see you soon, BYE!")

if __name__ == '__main__':
    main()


