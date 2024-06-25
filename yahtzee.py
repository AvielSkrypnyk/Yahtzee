# main.py
#* Thats one is working version of the game

from data import dice, scorecard
from functions import *

def main():
    print("Welcome to Yahtzee!")
    turns = 13
    
    while turns > 0:
        print(f"\nTurns remaining: {turns}")
        roll_dice()
        print_dice()
        
        for i in range(2):  #* Allow up to 2 rerolls
            keep = check_input_list("Enter dice to keep (e.g., 'Y Y N N Y' for 1st, 2nd, and 5th dice): ", ['Y', 'N'], required=5)
            keep = [k == 'Y' for k in keep]
            reroll_dice(keep)   #* Reroll the dice that the player does not want to keep
            print_dice()    #* Print the updated dice
        
        print_scorecard()
        category = check_input("Enter the category to score: ", list(scorecard.keys())) #* Ask the user to choose a category
        score = calculate_score(category)   #* Calculate the score for the chosen category
        update_scorecard(category, score)   #* Update the scorecard with the new score
        print_scorecard()                #* Print the updated scorecard
        
        turns -= 1
    
    total_score = sum(score for score in scorecard.values() if score is not None)
    print(f"\nGame over! Your total score is: {total_score}")

if __name__ == "__main__":
    main()
