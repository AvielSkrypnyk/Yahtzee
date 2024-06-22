DICE_ART = [
    """
     _______ 
    |       |
    |   •   |
    |       |
     ￣￣￣￣     
    """,
    """
     _______ 
    | •     |
    |       |
    |     • |
     ￣￣￣￣
    """,
    """
     _______
    | •     |
    |   •   |
    |     • |
     ￣￣￣￣
    """,
    """
     _______
    | •   • |
    |       |
    | •   • |
     ￣￣￣￣
    """,
    """
     _______
    | •   • |
    |   •   |
    | •   • |
     ￣￣￣￣
    """,
    """
     _______
    | •   • |
    | •   • |
    | •   • |
     ￣￣￣￣
    """
]

messages = {
    "invalid_input": "Invalid input. Please try again.",
    "invalid_category": "Invalid category. Please choose a valid category.",
    "score_set": "Score successfully set.",
    "total_score": "Your total score is: {}",
    "roll_again": "Would you like to roll again? (yes/no): ",
    "choose_dice": "Choose which dice to keep (e.g., 1 3 5 for keeping the first, third, and fifth dice): ",
    "invalid_dice_choice": "Invalid dice choice. Please enter valid dice positions.",
    "game_over": "Game over! Thank you for playing Yahtzee.",
    "enter_score": "Enter the score for category '{}': ",
    "bonus_earned": "Congratulations! You've earned the bonus of 35 points.",
    "no_bonus": "You did not earn the bonus."
}

START = """
### Instructions for Yahtzee (English)

1. **Objective:** Achieve the highest score by making various dice combinations.
2. **Materials:** 5 dice, a score sheet, and a pen.
3. **Gameplay:**
    - Each game consists of 13 rounds.
    - In each round, you may roll the dice up to three times.
    - After each roll, choose which dice to keep and which to roll again.
4. **Scoring:**
    - Record your score in one of the 13 categories on the score sheet.
    - The upper section includes numbers 1 through 6. Score points equal to the sum of the dice showing that number.
    - The lower section includes combinations like Three of a Kind, Four of a Kind, Full House, Small Straight, Large Straight, Yahtzee, and Chance.
5. **Yahtzee:** Five of the same dice (50 points).
6. **Bonus:** If you score 63 points or more in the upper section, you receive a bonus of 35 points.
7. **End of the Game:** After 13 rounds, tally all the scores. The player with the highest total score wins.
"""

scores = {
    'Ones': None,
    'Twos': None,
    'Threes': None,
    'Fours': None,
    'Fives': None,
    'Sixes': None,
    'Three of a kind': None,
    'Four of a kind': None,
    'Full House': None,
    'Small Straight': None,
    'Large Straight': None,
    'Yahtzee': None,
    'Chance': None
}


#! Some ideas for the data part of the game

# Constants for dice and scores
# DICE_ART = [
#     """
#      _______ 
#     |       |
#     |   •   |
#     |       |
#      ￣￣￣￣     
#     """,
#     """
#      _______ 
#     | •     |
#     |       |
#     |     • |
#      ￣￣￣￣
#     """,
#     """
#      _______
#     | •     |
#     |   •   |
#     |     • |
#      ￣￣￣￣
#     """,
#     """
#      _______
#     | •   • |
#     |       |
#     | •   • |
#      ￣￣￣￣
#     """,
#     """
#      _______
#     | •   • |
#     |   •   |
#     | •   • |
#      ￣￣￣￣
#     """,
#     """
#      _______
#     | •   • |
#     | •   • |
#     | •   • |
#      ￣￣￣￣
#     """
# ]

# messages = {
#     "invalid_input": "Invalid input. Please try again.",
#     "invalid_category": "Invalid category. Please choose a valid category.",
#     "score_set": "Score successfully set.",
#     "total_score": "Your total score is: {}",
#     "roll_again": "Would you like to roll again? (yes/no): ",
#     "choose_dice": "Choose which dice to keep (e.g., 1 3 5 for keeping the first, third, and fifth dice), (Or you can alos choose not to keep dice): ",
#     "invalid_dice_choice": "Invalid dice choice. Please enter valid dice positions.",
#     "game_over": "Game over! Thank you for playing Yahtzee.",
#     "enter_score": "Enter the score for category '{}': ",
#     "bonus_earned": "Congratulations! You've earned the bonus of 35 points.",
#     "no_bonus": "You did not earn the bonus."
# }

# START = """
# ### Instructions for Yahtzee (English)

# 1. **Objective:** Achieve the highest score by making various dice combinations.
# 2. **Materials:** 5 dice, a score sheet, and a pen.
# 3. **Gameplay:**
#     - Each game consists of 13 rounds.
#     - In each round, you may roll the dice up to three times.
#     - After each roll, choose which dice to keep and which to roll again.
# 4. **Scoring:**
#     - Record your score in one of the 13 categories on the score sheet.
#     - The upper section includes numbers 1 through 6. Score points equal to the sum of the dice showing that number.
#     - The lower section includes combinations like Three of a Kind, Four of a Kind, Full House, Small Straight, Large Straight, Yahtzee, and Chance.
# 5. **Yahtzee:** Five of the same dice (50 points).
# 6. **Bonus:** If you score 63 points or more in the upper section, you receive a bonus of 35 points.
# 7. **End of the Game:** After 13 rounds, tally all the scores. The player with the highest total score wins.
# """

# scores = {
#     'Ones': None,
#     'Twos': None,
#     'Threes': None,
#     'Fours': None,
#     'Fives': None,
#     'Sixes': None,
#     'Three of a kind': None,
#     'Four of a kind': None,
#     'Full House': None,
#     'Small Straight': None,
#     'Large Straight': None,
#     'Yahtzee': None,
#     'Chance': None
# }

# dice_to_roll = 5
# total_kept_dices = []
