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
    0: "08 c",
    1: "13 s",
    2: "05 c",
    3: "12 h",
    4: "07 s",
    5: "11 h",
    6: "02 c",
    7: "07 h",
    8: "01 d",
    9: "02 h",
    10: "11 c",
    11: "06 d",
    12: "04 h",
    13: "07 d",
    14: "12 c",
    15: "04 s",
    16: "08 d",
    17: "05 h",
    18: "06 c",
    19: "05 d",
    20: "07 c",
    21: "03 h",
    22: "10 h",
    23: "13 d",
    24: "06 h",
    25: "09 d",
    26: "08 s",
    27: "09 c",
    28: "03 c",
    29: "02 s",
    30: "10 s",
    31: "09 h",
    32: "04 c",
    33: "13 c",
    34: "12 d",
    35: "04 d",
    36: "05 s",
    37: "10 c",
    38: "09 s",
    39: "13 h",
    40: "12 s",
    41: "02 d",
    42: "11 d",
    43: "01 c",
    44: "03 s",
    45: "01 s",
    46: "10 d",
    47: "08 h",
    48: "06 s",
    49: "11 s",
    50: "03 d",
    51: "01 h"

}

# Keeps count of how many times a card has been seen in succession the last 5 frames.
dictionaryOfCardFrameCounter = {
    "08 c": 0,
    "13 s": 0,
    "05 c": 0,
    "12 h": 0,
    "07 s": 0,
    "11 h": 0,
    "02 c": 0,
    "07 h": 0,
    "01 d": 0,
    "02 h": 0,
    "11 c": 0,
    "06 d": 0,
    "04 h": 0,
    "07 d": 0,
    "12 c": 0,
    "04 s": 0,
    "08 d": 0,
    "05 h": 0,
    "06 c": 0,
    "05 d": 0,
    "07 c": 0,
    "03 h": 0,
    "10 h": 0,
    "13 d": 0,
    "06 h": 0,
    "09 d": 0,
    "08 s": 0,
    "09 c": 0,
    "03 c": 0,
    "02 s": 0,
    "10 s": 0,
    "09 h": 0,
    "04 c": 0,
    "13 c": 0,
    "12 d": 0,
    "04 d": 0,
    "05 s": 0,
    "10 c": 0,
    "09 s": 0,
    "13 h": 0,
    "12 s": 0,
    "02 d": 0,
    "11 d": 0,
    "01 c": 0,
    "03 s": 0,
    "01 s": 0,
    "10 d": 0,
    "08 h": 0,
    "06 s": 0,
    "11 s": 0,
    "03 d": 0,
    "01 h": 0
}

# if a card has been seen sufficient amount of times the last 5 frames, it will be marked as detected.
dictionaryOfDetectedCards = {
    "08 c": False,
    "13 s": False,
    "05 c": False,
    "12 h": False,
    "07 s": False,
    "11 h": False,
    "02 c": False,
    "07 h": False,
    "01 d": False,
    "02 h": False,
    "11 c": False,
    "06 d": False,
    "04 h": False,
    "07 d": False,
    "12 c": False,
    "04 s": False,
    "08 d": False,
    "05 h": False,
    "06 c": False,
    "05 d": False,
    "07 c": False,
    "03 h": False,
    "10 h": False,
    "13 d": False,
    "06 h": False,
    "09 d": False,
    "08 s": False,
    "09 c": False,
    "03 c": False,
    "02 s": False,
    "10 s": False,
    "09 h": False,
    "04 c": False,
    "13 c": False,
    "12 d": False,
    "04 d": False,
    "05 s": False,
    "10 c": False,
    "09 s": False,
    "13 h": False,
    "12 s": False,
    "02 d": False,
    "11 d": False,
    "01 c": False,
    "03 s": False,
    "01 s": False,
    "10 d": False,
    "08 h": False,
    "06 s": False,
    "11 s": False,
    "03 d": False,
    "01 h": False
}

dictionaryOfNewlyDiscoveredCards = {
    "08 c": False,
    "13 s": False,
    "05 c": False,
    "12 h": False,
    "07 s": False,
    "11 h": False,
    "02 c": False,
    "07 h": False,
    "01 d": False,
    "02 h": False,
    "11 c": False,
    "06 d": False,
    "04 h": False,
    "07 d": False,
    "12 c": False,
    "04 s": False,
    "08 d": False,
    "05 h": False,
    "06 c": False,
    "05 d": False,
    "07 c": False,
    "03 h": False,
    "10 h": False,
    "13 d": False,
    "06 h": False,
    "09 d": False,
    "08 s": False,
    "09 c": False,
    "03 c": False,
    "02 s": False,
    "10 s": False,
    "09 h": False,
    "04 c": False,
    "13 c": False,
    "12 d": False,
    "04 d": False,
    "05 s": False,
    "10 c": False,
    "09 s": False,
    "13 h": False,
    "12 s": False,
    "02 d": False,
    "11 d": False,
    "01 c": False,
    "03 s": False,
    "01 s": False,
    "10 d": False,
    "08 h": False,
    "06 s": False,
    "11 s": False,
    "03 d": False,
    "01 h": False
}
