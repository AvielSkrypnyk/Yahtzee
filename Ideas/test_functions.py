# functions.py

import random
from test_data import dice, scorecard

def roll_dice():
    """Rolls five dice and updates the dice list."""
    for i in range(5):
        dice[i] = random.randint(1, 6)

def reroll_dice(keep):
    """Rerolls the dice that the player does not want to keep.
    
    Args:
        keep (list): A list of booleans indicating which dice to keep.
    """
    for i in range(5):
        if not keep[i]:
            dice[i] = random.randint(1, 6)

def print_dice():
    """Prints the current dice."""
    print("Dice:", dice)

def print_scorecard():
    """Prints the current scorecard."""
    for category, score in scorecard.items():
        print(f"{category}: {score}")

def calculate_score(category):
    """Calculates the score for a given category.
    
    Args:
        category (str): The category to calculate the score for.
    
    Returns:
        int: The calculated score.
    """
    if category == "ones":
        return dice.count(1) * 1
    elif category == "twos":
        return dice.count(2) * 2
    elif category == "threes":
        return dice.count(3) * 3
    elif category == "fours":
        return dice.count(4) * 4
    elif category == "fives":
        return dice.count(5) * 5
    elif category == "sixes":
        return dice.count(6) * 6
    elif category == "three_of_a_kind":
        if any(dice.count(x) >= 3 for x in set(dice)):
            return sum(dice)
    elif category == "four_of_a_kind":
        if any(dice.count(x) >= 4 for x in set(dice)):
            return sum(dice)
    elif category == "full_house":
        unique_dice = set(dice)
        if len(unique_dice) == 2 and any(dice.count(x) == 3 for x in unique_dice):
            return 25
    elif category == "small_straight":
        straights = [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}]
        if any(straight.issubset(dice) for straight in straights):
            return 30
    elif category == "large_straight":
        if set(dice) in [{1, 2, 3, 4, 5}, {2, 3, 4, 5, 6}]:
            return 40
    elif category == "yahtzee":
        if len(set(dice)) == 1:
            return 50
    elif category == "chance":
        return sum(dice)
    return 0

def update_scorecard(category, score):
    """Updates the scorecard with the score for the given category.
    
    Args:
        category (str): The category to update.
        score (int): The score to set.
    """
    if scorecard[category] is None:
        scorecard[category] = score
    else:
        print("Category already filled!")
