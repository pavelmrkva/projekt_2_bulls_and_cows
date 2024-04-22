"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Pavel Mrkva
email: palon@seznam.cz
discord: pavel_58358
"""

import random

def generate_secret_number():
    while True:
        secret_number = ''.join(random.sample('0123456789', 4))
        if secret_number[0] == '0':
            continue
        return secret_number
            
def verification_of_rules(guess):
    if len(guess) != 4 or not guess.isdigit():
        return False
    if guess[0] == '0' or len(set(guess)) < 4:
        return False
    return True

def compare_the_numbers(guess, secret_number):
    bull = 0
    cow = 0
    for i in range(4):
        if guess[i] == secret_number[i]:
            bull += 1
        if guess[i] in secret_number:
            cow += 1 
    cow = cow - bull
    return bull, cow

def final_rating(attempts):
    if attempts <= 3:
        return "Excellently!"
    elif attempts <= 6:
        return "Very good!"
    elif attempts <= 10:
        return "That's good!"
    elif attempts <= 15:
        return "That's average."
    else:
        return "That's not very good."


# GAME
def main_game():
    separator = ("-") * 47
    attempts = 0
    secret_number = generate_secret_number()
    print(
        "Hi there!", separator, 
        "I've generated a random 4 digit number for you.",
        "Let's play a bulls and cows game.", separator, sep="\n"
    )    
    
    print(
        "Rules of the game:",
        "Enter a number that does not start with a zero", 
        "and the digit must not be repeated:",separator, sep="\n"
    )
    #print(secret_number) # test
    while True:
        guess = input(">>> ")
        attempts +=1
        bulls, cows = compare_the_numbers(guess, secret_number)
        rating = final_rating(attempts)
        if not verification_of_rules(guess):
            print("Your assignment is out of the rules!",separator,  sep="\n")
            continue
        
        if bulls == 4:
            attempt_str = str(attempts) + " attempt"
            if attempts != 1:
                attempt_str += "s"
            print("Correct, you've guessed the right number","in " + attempt_str + "!", separator, sep="\n")  
            print(rating)
            break
        else:
            bull_str = str(bulls) + " bull"
            if bulls != 1:
                bull_str += "s"

            cow_str = str(cows) + " cow"
            if cows != 1:
                cow_str += "s"

            print(bull_str + ", " + cow_str, separator, sep="\n")
        
if __name__ == "__main__":
    main_game()