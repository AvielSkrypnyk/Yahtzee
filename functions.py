# functions.py
import random
from data import DICE_ART, messages, scores

def roll_dice():
    """Rolls 5 dice and returns their values."""
    return [random.randint(1, 6) for _ in range(5)]

def display_dice(dice):
    """Displays the dice using ASCII art."""
    for die in dice:
        print(DICE_ART[die - 1])

def choose_dice():
    """Allows the player to choose which dice to keep."""
    valid_choices = ['1', '2', '3', '4', '5']
    while True:
        try:
            choice = input(messages["choose_dice"]).strip()
            if choice.lower() == 'none':
                return []
            chosen_dice = list(map(int, choice.split()))
            if all(str(die) in valid_choices for die in chosen_dice):
                return chosen_dice
            else:
                raise ValueError
        except ValueError:
            print(messages["invalid_dice_choice"])

def roll_again():
    """Asks the player if they want to roll again."""
    while True:
        choice = input(messages["roll_again"]).strip().lower()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print(messages["invalid_input"])

def calculate_score(dice, category):
    """Calculates and returns the score based on the chosen category."""
    if category in ['Ones', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes']:
        return dice.count(int(category[-1])) * int(category[-1])
    elif category == 'Three of a kind':
        for value in set(dice):
            if dice.count(value) >= 3:
                return sum(dice)
        return 0
    elif category == 'Four of a kind':
        for value in set(dice):
            if dice.count(value) >= 4:
                return sum(dice)
        return 0
    elif category == 'Full House':
        if len(set(dice)) == 2 and (dice.count(dice[0]) == 2 or dice.count(dice[0]) == 3):
            return 25
        return 0
    elif category == 'Small Straight':
        if sorted(set(dice)) in [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]:
            return 30
        return 0
    elif category == 'Large Straight':
        if sorted(set(dice)) in [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]:
            return 40
        return 0
    elif category == 'Yahtzee':
        if len(set(dice)) == 1:
            return 50
        return 0
    elif category == 'Chance':
        return sum(dice)

def check_bonus():
    """Checks if the upper section bonus of 35 points is earned."""
    upper_section_total = sum(scores[key] if scores[key] is not None else 0 for key in ['Ones', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes'])
    if upper_section_total >= 63:
        print(messages["bonus_earned"])
        return 35
    else:
        print(messages["no_bonus"])
        return 0

def display_scores():
    """Displays the current scores."""
    print("\nCurrent Scores:")
    for key, value in scores.items():
        print(f"{key}: {value if value is not None else '-'}")
    print("")

def is_game_over():
    """Checks if the game is over (all categories are filled)."""
    return all(value is not None for value in scores.values())






#! Some new ideas for game

# #* Function to prompt a question and validate the answer
# def question_with_answer(question, expected_answers):
#     while True:
#         end_answer = input(f"{question} You can answer with ({', '.join(expected_answers)}): ").lower()
#         if end_answer not in [answer.lower() for answer in expected_answers]:
#             print(colored(f"{messages['invalid_input']}\n", "red", attrs=["bold"]))
#         else:
#             return end_answer

# #* Function to roll dice
# def roll_dice(num_dice, random_generator):
#     dice_results = []
#     for i in range(num_dice):
#         dice_roll = random_generator.randint(1, 6)  #* Assuming 6-sided dice
#         dice_results.append(dice_roll)
#     return dice_results

# #* Function to display dice visually
# def display_dice(dice_results):
#     for result in dice_results:
#         print(DICE_ART[result - 1])

# #* Function to keep selected dice
# def keep_dice(dice_results):
#     while True:
#         choice = input(messages["choose_dice"])
#         if choice.strip() == "":
#             return []
#         indices = choice.split()
#         kept_dices = []
#         try:
#             for index in indices:
#                 idx = int(index) - 1
#                 if idx < 0 or idx >= len(dice_results):
#                     raise ValueError
#                 kept_dices.append(dice_results[idx])
#             return kept_dices
#         except ValueError:
#             print(colored(messages["invalid_dice_choice"], "red", attrs=["bold"]))

# #* Function to play a round
# def play_round(round_num, random_generator):
#     print(f"\nRound {round_num + 1}")
#     kept_dices = []
#     dice_to_roll = 5

#     for roll in range(3):
#         dice_results = roll_dice(dice_to_roll, random_generator)
#         display_dice(dice_results)

#         if roll < 2:
#             kept_dices += keep_dice(dice_results)
#             dice_to_roll = 5 - len(kept_dices)
#             if dice_to_roll == 0:
#                 break
#         else:
#             kept_dices += dice_results

#     print(f"Kept dice: {kept_dices}")
#     return kept_dices

# #* Function to display the current score sheet
# def display_score_sheet(scores):
#     print("\nCurrent Score Sheet:")
#     for category, score in scores.items():
#         score_display = score if score is not None else "-"
#         print(f"{category}: {score_display}")


# #* Scoring functions for each category
# def calculate_upper_section_score(dice, number):
#     return sum(die for die in dice if die == number)

# def calculate_three_of_a_kind(dice):
#     for number in set(dice):
#         if dice.count(number) >= 3:
#             return sum(dice)
    

# def calculate_four_of_a_kind(dice):
#     for number in set(dice):
#         if dice.count(number) >= 4:
#             return sum(dice)
    

# def calculate_full_house(dice):
#     unique_numbers = set(dice)
#     if len(unique_numbers) == 2 and (dice.count(list(unique_numbers)[0]) == 2 or dice.count(list(unique_numbers)[0]) == 3):
#         return 25
    

# def calculate_small_straight(dice):
#     straights = [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}]
#     dice_set = set(dice)
#     for straight in straights:
#         if straight.issubset(dice_set):  #*? The issubset method is then used to check if the set of dice results contains the necessary elements for a small or large straight.
#             return 30
    

# def calculate_large_straight(dice):
#     straights = [{1, 2, 3, 4, 5}, {2, 3, 4, 5, 6}]
#     dice_set = set(dice)
#     for straight in straights:
#         if straight.issubset(dice_set):
#             return 40
    

# #* Update the Yahtzee scoring function to handle Yahtzee bonus
# def calculate_yahtzee(dice, scores):
#     if len(set(dice)) == 1:
#         if scores['Yahtzee'] is None:
#             return 50
#         else:
#             return 100  #* Yahtzee bonus

# def calculate_chance(dice):
#     return sum(dice)

# #* Function to update the score for a specific category
# def update_score(category, dice, scores):
#     if category == 'Ones':
#         scores['Ones'] = calculate_upper_section_score(dice, 1)
#     elif category == 'Twos':
#         scores['Twos'] = calculate_upper_section_score(dice, 2)
#     elif category == 'Threes':
#         scores['Threes'] = calculate_upper_section_score(dice, 3)
#     elif category == 'Fours':
#         scores['Fours'] = calculate_upper_section_score(dice, 4)
#     elif category == 'Fives':
#         scores['Fives'] = calculate_upper_section_score(dice, 5)
#     elif category == 'Sixes':
#         scores['Sixes'] = calculate_upper_section_score(dice, 6)
#     elif category == 'Three of a kind':
#         scores['Three of a kind'] = calculate_three_of_a_kind(dice)
#     elif category == 'Four of a kind':
#         scores['Four of a kind'] = calculate_four_of_a_kind(dice)
#     elif category == 'Full House':
#         scores['Full House'] = calculate_full_house(dice)
#     elif category == 'Small Straight':
#         scores['Small Straight'] = calculate_small_straight(dice)
#     elif category == 'Large Straight':
#         scores['Large Straight'] = calculate_large_straight(dice)
#     elif category == 'Yahtzee':
#         scores['Yahtzee'] = calculate_yahtzee(dice)
#     elif category == 'Chance':
#         scores['Chance'] = calculate_chance(dice)
#     else:
#         return messages['invalid_category']
#     return messages['score_set']