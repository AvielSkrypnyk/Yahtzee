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
            keep = check_input_list("Enter dice to keep (e.g., 'Y Y N N Y' for 1st, 2nd, and 5th dice): ", ['Y', 'N'])
            print(keep)
            #keep = input("Enter dice to keep (e.g., 'Y Y N N Y' for 1st, 2nd, and 5th dice): ").split()
            keep = [k == 'Y' for k in keep]
            reroll_dice(keep)
            print_dice()
        
        print_scorecard()
        category = input("Enter the category to score: ")
        score = calculate_score(category)
        update_scorecard(category, score)
        print_scorecard()
        
        turns -= 1
    
    total_score = sum(score for score in scorecard.values() if score is not None)
    print(f"\nGame over! Your total score is: {total_score}")

if __name__ == "__main__":
    main()
