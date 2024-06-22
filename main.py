# main.py
from data import *
from functions import *

def main():
    print(START)
    round_number = 0

    while not is_game_over():
        round_number += 1
        print(f"\n--- Round {round_number} ---\n")
        current_dice = roll_dice()
        display_dice(current_dice)

        roll_count = 0
        while roll_count < 2:
            roll_count += 1
            if roll_count < 3:
                if roll_again():
                    dice_to_keep = choose_dice()
                    current_dice = [current_dice[i - 1] for i in dice_to_keep] + roll_dice(len(dice_to_keep))
                    display_dice(current_dice)

        display_scores()

        category = input("Enter category to score (e.g., 'Ones', 'Three of a kind'): ").strip()
        while category not in scores.keys() or scores[category] is not None:
            print(messages["invalid_category"])
            category = input("Enter category to score (e.g., 'Ones', 'Three of a kind'): ").strip()

        scores[category] = calculate_score(current_dice, category)
        print(messages["score_set"])

    total_score = sum(score if score is not None else 0 for score in scores.values())
    print(messages["total_score"].format(total_score))
    print(messages["game_over"])

if __name__ == "__main__":
    main()


#! Some ideas for main part

# def main():
#     print("Welcome to Yahtzee!")
#     print(START)

#     for round_num in range(13):
#         #* Play a round and get the kept dice
#         kept_dices = play_round(round_num, random)
        
#         #* Display the current score sheet
#         display_score_sheet(scores)
        
#         #* Prompt the player to choose a category and update the score
#         while True:
#             print("Choose a category to score:")
#             for category in scores:
#                 if scores[category] is None:
#                     print(f" - {category}")
#             category = input().strip()
#             if category in scores and scores[category] is None:
#                 message = update_score(category, kept_dices, scores)
#                 print(message)
#                 break
#             else:
#                 print(colored(messages['invalid_category'], "red", attrs=["bold"]))

#     #* Calculate the total score and bonus for the upper section
#     upper_section_score = sum(scores[category] for category in ['Ones', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes'] if scores[category] is not None)
#     if upper_section_score >= 63:
#         print(messages['bonus_earned'])
#         upper_section_score += 35
#     else:
#         print(messages['no_bonus'])

#     #* Calculate the total score
#     total_score = sum(score for score in scores.values() if score is not None)
#     print(messages['total_score'].format(total_score))

#     print(messages["game_over"])
#     print(scores)

# if __name__ == "__main__":
#     main()