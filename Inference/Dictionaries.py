# creating the piles
tableau_pile_1 = []
tableau_pile_2 = []
tableau_pile_3 = []
tableau_pile_4 = []
tableau_pile_5 = []
tableau_pile_6 = []
tableau_pile_7 = []
foundation_pile_1 = []
foundation_pile_2 = []
foundation_pile_3 = []
foundation_pile_4 = []
waste_pile = []

tableau_pile_1_new = []
tableau_pile_2_new = []
tableau_pile_3_new = []
tableau_pile_4_new = []
tableau_pile_5_new = []
tableau_pile_6_new = []
tableau_pile_7_new = []
foundation_pile_1_new = []
foundation_pile_2_new = []
foundation_pile_3_new = []
foundation_pile_4_new = []
waste_pile_new = []

list_of_piles = [tableau_pile_1, tableau_pile_2, tableau_pile_3, tableau_pile_4, tableau_pile_5, tableau_pile_6,
                 tableau_pile_7, foundation_pile_1, foundation_pile_2, foundation_pile_3, foundation_pile_4, waste_pile]

list_of_piles_only_containing_newly_detected_cards = [tableau_pile_1_new, tableau_pile_2_new,
                                                      tableau_pile_3_new, tableau_pile_4_new, tableau_pile_5_new, tableau_pile_6_new,
                                                      tableau_pile_7_new, foundation_pile_1_new, foundation_pile_2_new,
                                                      foundation_pile_3_new, foundation_pile_4_new, waste_pile_new]

dictionary_of_piles = {
    0: tableau_pile_1,
    1: tableau_pile_2,
    2: tableau_pile_3,
    3: tableau_pile_4,
    4: tableau_pile_5,
    5: tableau_pile_6,
    6: tableau_pile_7,
    7: foundation_pile_1,
    8: foundation_pile_2,
    9: foundation_pile_3,
    10: foundation_pile_4,
    11: waste_pile
}

dictionary_of_pile_names = {
    0: "tableau_1",
    1: "tableau_2",
    2: "tableau_3",
    3: "tableau_4",
    4: "tableau_5",
    5: "tableau_6",
    6: "tableau_7",
    7: "foundation_1",
    8: "foundation_2",
    9: "foundation_3",
    10: "foundation_4",
    11: "waste"
}

dictionaryOfIndexToName = {
    0: "8 c",
    1: "13 s",
    2: "5 c",
    3: "12 h",
    4: "7 s",
    5: "11 h",
    6: "2 c",
    7: "7 h",
    8: "1 d",
    9: "2 h",
    10: "11 c",
    11: "6 d",
    12: "4 h",
    13: "7 d",
    14: "12 c",
    15: "4 s",
    16: "8 d",
    17: "5 h",
    18: "6 c",
    19: "5 d",
    20: "7 c",
    21: "3 h",
    22: "10 h",
    23: "13 d",
    24: "6 h",
    25: "9 d",
    26: "8 s",
    27: "9 c",
    28: "3 c",
    29: "2 s",
    30: "10 s",
    31: "9 h",
    32: "4 c",
    33: "13 c",
    34: "12 d",
    35: "4 d",
    36: "5 s",
    37: "10 c",
    38: "9 s",
    39: "13 h",
    40: "12 s",
    41: "2 d",
    42: "11 d",
    43: "1 c",
    44: "3 s",
    45: "1 s",
    46: "10 d",
    47: "8 h",
    48: "6 s",
    49: "11 s",
    50: "3 d",
    51: "1 h"

}

# Keeps count of how many times a card has been seen in succession the last 5 frames.
dictionaryOfCardFrameCounter = {
    "8 c": 0,
    "13 s": 0,
    "5 c": 0,
    "12 h": 0,
    "7 s": 0,
    "11 h": 0,
    "2 c": 0,
    "7 h": 0,
    "1 d": 0,
    "2 h": 0,
    "11 c": 0,
    "6 d": 0,
    "4 h": 0,
    "7 d": 0,
    "12 c": 0,
    "4 s": 0,
    "8 d": 0,
    "5 h": 0,
    "6 c": 0,
    "5 d": 0,
    "7 c": 0,
    "3 h": 0,
    "10 h": 0,
    "13 d": 0,
    "6 h": 0,
    "9 d": 0,
    "8 s": 0,
    "9 c": 0,
    "3 c": 0,
    "2 s": 0,
    "10 s": 0,
    "9 h": 0,
    "4 c": 0,
    "13 c": 0,
    "12 d": 0,
    "4 d": 0,
    "5 s": 0,
    "10 c": 0,
    "9 s": 0,
    "13 h": 0,
    "12 s": 0,
    "2 d": 0,
    "11 d": 0,
    "1 c": 0,
    "3 s": 0,
    "1 s": 0,
    "10 d": 0,
    "8 h": 0,
    "6 s": 0,
    "11 s": 0,
    "3 d": 0,
    "1 h": 0
}

# if a card has been seen sufficient amount of times the last 5 frames, it will be marked as detected.
dictionaryOfDetectedCards = {
    "8 c": False,
    "13 s": False,
    "5 c": False,
    "12 h": False,
    "7 s": False,
    "11 h": False,
    "2 c": False,
    "7 h": False,
    "1 d": False,
    "2 h": False,
    "11 c": False,
    "6 d": False,
    "4 h": False,
    "7 d": False,
    "12 c": False,
    "4 s": False,
    "8 d": False,
    "5 h": False,
    "6 c": False,
    "5 d": False,
    "7 c": False,
    "3 h": False,
    "10 h": False,
    "13 d": False,
    "6 h": False,
    "9 d": False,
    "8 s": False,
    "9 c": False,
    "3 c": False,
    "2 s": False,
    "10 s": False,
    "9 h": False,
    "4 c": False,
    "13 c": False,
    "12 d": False,
    "4 d": False,
    "5 s": False,
    "10 c": False,
    "9 s": False,
    "13 h": False,
    "12 s": False,
    "2 d": False,
    "11 d": False,
    "1 c": False,
    "3 s": False,
    "1 s": False,
    "10 d": False,
    "8 h": False,
    "6 s": False,
    "11 s": False,
    "3 d": False,
    "1 h": False
}

dictionaryOfNewlyDiscoveredCards = {
    "8 c": False,
    "13 s": False,
    "5 c": False,
    "12 h": False,
    "7 s": False,
    "11 h": False,
    "2 c": False,
    "7 h": False,
    "1 d": False,
    "2 h": False,
    "11 c": False,
    "6 d": False,
    "4 h": False,
    "7 d": False,
    "12 c": False,
    "4 s": False,
    "8 d": False,
    "5 h": False,
    "6 c": False,
    "5 d": False,
    "7 c": False,
    "3 h": False,
    "1False h": False,
    "13 d": False,
    "6 h": False,
    "9 d": False,
    "8 s": False,
    "9 c": False,
    "3 c": False,
    "2 s": False,
    "1False s": False,
    "9 h": False,
    "4 c": False,
    "13 c": False,
    "12 d": False,
    "4 d": False,
    "5 s": False,
    "1False c": False,
    "9 s": False,
    "13 h": False,
    "12 s": False,
    "2 d": False,
    "11 d": False,
    "1 c": False,
    "3 s": False,
    "1 s": False,
    "1False d": False,
    "8 h": False,
    "6 s": False,
    "11 s": False,
    "3 d": False,
    "1 h": False
}
