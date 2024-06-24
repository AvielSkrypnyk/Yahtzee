# data.py

#* Dice rolls will be stored in a list
dice = [0, 0, 0, 0, 0]

#* Player's scorecard (initially empty)
scorecard: dict[str, int|None] = {
    "ones": None,
    "twos": None,
    "threes": None,
    "fours": None,
    "fives": None,
    "sixes": None,
    "three_of_a_kind": None,
    "four_of_a_kind": None,
    "full_house": None,
    "small_straight": None,
    "large_straight": None,
    "yahtzee": None,
    "chance": None
}
