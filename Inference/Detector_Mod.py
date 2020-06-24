import os
import sys
import cv2

"""
This file is a modified version of the Detector.py from 
the following repository: https://github.com/AntonMu/TrainYourOwnYOLO
We have changed a lot to make the code fit our needs.

Modifications made by Asama Hayder (s185099)
"""

#EOW HUSK AT MARKERE HVILKE METODER DER ER VORES OG HVILKE DER ER FRA REPOEN.
#OG HUSK AT SIGE TIL FÆRGEN AT HAN OGSÅ SKAL SKRIVE SIT NAVN PÅ SIN KODE
#OG HUSK AT SKRIVE DIT NAVN PÅ SIMULATIONS-KODEN SAMMEN MED FÆRGEN!

def get_parent_dir(n=1):
    """ returns the n-th parent directory of the current
    working directory """
    current_path = os.path.dirname(os.path.abspath(__file__))
    for k in range(n):
        current_path = os.path.dirname(current_path)
    return current_path


src_path = os.path.join(get_parent_dir(1), "src")
utils_path = os.path.join(get_parent_dir(1), "Utils")

sys.path.append(src_path)
sys.path.append(utils_path)

video_stream = cv2.VideoCapture(0)

# for me, pycharm says that no module named Dictionaries and Keras_yolo3.yolo but they are detected and works fine.
# Maybe a bug?

import argparse
import Dictionaries
import GameLogic
from keras_yolo3.yolo import YOLO
from PIL import Image
import numpy as np
import copy

move_text = ""
list_of_piles = Dictionaries.list_of_piles
list_of_piles_only_containing_newly_detected_cards = Dictionaries.list_of_piles_only_containing_newly_detected_cards
dictionary_of_pile_names = Dictionaries.dictionary_of_pile_names
dictionaryOfIndexToName = Dictionaries.dictionaryOfIndexToName
dictionaryOfCardFrameCounter = Dictionaries.dictionaryOfCardFrameCounter
dictionaryOfDetectedCards = Dictionaries.dictionaryOfDetectedCards
dictionaryOfNewlyDiscoveredCards = Dictionaries.dictionaryOfNewlyDiscoveredCards
current_pile = 0

def detect_card(some_prediction):
    # we assume that if there was unknown cards, then you have just scanned it. However, we should make a smarter way
    # to detect if the unknown card has been scanned.
    # global there_are_unknown_cards
    # there_are_unknown_cards = False

    card_name = dictionaryOfIndexToName.get(some_prediction[4])
    #dictionaryOfDetectedCards[card_name] = True
    #dictionaryOfNewlyDiscoveredCards[card_name] = True
    #list_of_piles[current_pile].append(card_name)

    #if not game_has_just_started:
    #    list_of_piles_only_containing_newly_detected_cards[current_pile].append(card_name)
        # list_of_piles[current_pile].append(card_name)

    if 6 < current_pile < 11:
        foundation_piles.get(current_pile-7).append(card_name)
    elif current_pile < 7:
        tableu_piles.get(current_pile).append(card_name)
    else:
        # unknown_waste = game_logic.get_unknown_counter()
        # unknown_waste -= 1
        #TODO: this is a temporary løsning
        #game_logic.unknownWaste -= 1

        if game_logic.unknownWaste == 0:
            game_logic.allUnknownWasteFound = True #HMMMMM, dette kommer måske ikke til at virke.
        waste_pile.append(card_name)

    sortLists(tableu_piles, foundation_piles, waste_pile)

    return


def increment_card_viewed_counter(some_prediction):
    number_of_times_a_card_should_be_seen_sequentially = 15

    card_name = dictionaryOfIndexToName.get(some_prediction[4])

    # checking if already detected
    if check_if_card_already_detected(card_name):
        return

    number_of_times_viewed = dictionaryOfCardFrameCounter.get(card_name)
    number_of_times_viewed += 1
    if number_of_times_viewed >= number_of_times_a_card_should_be_seen_sequentially:
        detect_card(some_prediction)
    else:
        dictionaryOfCardFrameCounter[card_name] = number_of_times_viewed

    return


def check_if_card_already_detected(card_name):
    detected = False
    for some_key, pile in tableu_piles.items():
        if card_name in pile:
            detected = True

    for some_key, pile in foundation_piles.items():
        if card_name in pile:
            detected = True

    if card_name in waste_pile:
        detected = True

    return detected


def show_detected_cards(some_image, font, text_size, text_thickness, border_color, border_thickness):
    cards_color = (3, 186, 252, 255)
    list_of_detected_cards = "Cards: "

    """for some_name in list_of_piles[current_pile]:
        list_of_detected_cards += some_name
        list_of_detected_cards += " ,"""

    # print(tableu_piles)
    # print(foundation_piles)
    # print(waste_pile)

    #TODO: Fix that foundation piles shows the waste card piles
    if 6 < current_pile < 11:
        some_range = range(6)
        pile = foundation_piles.get(current_pile-7)
    elif -1 < current_pile < 7:
        some_range = range(6)
        pile = tableu_piles.get(current_pile)
    else:
        some_range = reversed(range(6))
        pile = waste_pile

    if pile is not None:
        if len(pile) > 7:
            list_of_detected_cards += "..."
            for i in some_range:
                list_of_detected_cards += pile[len(pile)-i-1]  # we get the last/first 6 cards if there is no space for all.
                list_of_detected_cards += ", "
        else:
            for card in pile:
                list_of_detected_cards += card
                list_of_detected_cards += ", "

    cv2.putText(some_image, list_of_detected_cards, (0, 200), font, text_size, border_color, border_thickness)
    cv2.putText(some_image, list_of_detected_cards, (0, 200), font, text_size, cards_color, text_thickness)

    return


# displays various text
def show_text(some_image, move):
    text_color = (255, 255, 255, 255)  # remember it is in bgr
    text_border_color = (0, 0, 0, 255)
    text_size = .75
    text_thickness = 1
    border_thickness = 3 * text_thickness
    font = cv2.FONT_HERSHEY_DUPLEX

    cv2.putText(some_image, "'ESC' to exit", (0, 30), font, text_size, text_border_color, border_thickness)
    cv2.putText(some_image, "'ESC' to exit", (0, 30), font, text_size, text_color, text_thickness)


    """if move is not None and move[0] is not "NA" and not there_are_unknown_cards:
        cv2.putText(some_image, "'e' to confirm move", (0, 70), cv2.FONT_HERSHEY_DUPLEX, .75,
                    (209, 80, 0, 255), 2)"""

    # if move is not None and move[0] is not "NA":
    if is_confirming_move:
        cv2.putText(some_image, "'e' to confirm move", (0, 70), font, text_size, text_border_color, border_thickness)
        cv2.putText(some_image, "'e' to confirm move", (0, 70), font, text_size, text_color, text_thickness)
    else:
        cv2.putText(some_image, "'c' to clear pile", (0, 70), font, text_size, text_border_color, border_thickness)
        cv2.putText(some_image, "'c' to clear pile", (0, 70), font, text_size, text_color, text_thickness)

        cv2.putText(some_image, "'SPACE' or '0..7' to change pile", (0, 110), font, text_size, text_border_color, border_thickness)
        cv2.putText(some_image, "'SPACE' or '0..7' to change pile", (0, 110), font, text_size, text_color, text_thickness)

        cv2.putText(some_image, "'e' for done scanning", (0, 150), font, text_size, text_border_color, border_thickness)
        cv2.putText(some_image, "'e' for done scanning", (0, 150), font, text_size, text_color, text_thickness)

        pile_text = "current pile: "
        current_pile_name = dictionary_of_pile_names.get(current_pile)
        pile_text += current_pile_name
        text_width = cv2.getTextSize(pile_text, cv2.FONT_HERSHEY_DUPLEX, .75, 2)[0]
        image_width = some_image.shape[1]

        x_coordinate = image_width - text_width[0]
        cv2.putText(some_image, pile_text, (x_coordinate, 30), font, text_size, text_border_color, border_thickness)
        cv2.putText(some_image, pile_text, (x_coordinate, 30), font, text_size, text_color, text_thickness)

        show_detected_cards(some_image, font, text_size, text_thickness, text_border_color, border_thickness)

    show_move(move, some_image, font, text_size, text_thickness, text_border_color, border_thickness)

    return


def show_move(move, some_image, font, text_size, text_thickness, border_color, border_thickness):
    move_color = (0, 255, 0, 255)
    # Creating the text that will be displayed
    global move_text
    # global there_are_unknown_cards

    """elif there_are_unknown_cards:
        move_text = "Flip and Scan the unknown card"""""
    if game_has_just_started:
        move_text = "Scan first card of each pile"
    else:

        """if move is None or move[0] == "NA":
            move_text = "No move. Scan from waste/flip cards."""
        if not is_confirming_move:
            move_text = "Scan from waste/flip cards."
        elif move[0] != "NA":
            card_number = move[0]
            card_suit = move[1]
            from_pile = move[2]
            to_pile = move[3]
            pile_group = move[4]

            move_text = f"move {card_number}{card_suit} from pile {int(from_pile) + 1} to pile {int(to_pile) + 1} " \
                        f"in group {pile_group}"

    # print(move_text)

    # Calculating the coordinates and displaying the text
    border_text_size = cv2.getTextSize(move_text, font, text_size, border_thickness)[0]
    text_width = cv2.getTextSize(move_text, font, text_size, text_thickness)[0]

    x_coordinate = (some_image.shape[1] - text_width[0])/2
    y_coordinate = (some_image.shape[0] - text_width[1])
    x_b_coordinate = (some_image.shape[1] - border_text_size[0])/2
    y_b_coordinate = (some_image.shape[0] - border_text_size[1])

    x_rounded = int(round(x_coordinate))
    y_rounded = int(round(y_coordinate))
    x_b_rounded = int(round(x_b_coordinate))
    y_b_rounded = int(round(y_b_coordinate))

    cv2.putText(some_image, move_text, (x_rounded, y_rounded), font, text_size,
                border_color, border_thickness)
    cv2.putText(some_image, move_text, (x_rounded, y_rounded), font, text_size,
                move_color, text_thickness)

    return


def change_pile(some_k):
    global current_pile
    total_number_of_piles = len(dictionary_of_pile_names)
    max_pile_index = total_number_of_piles - 1

    if some_k != 32:
        switch = {
            48: 12,
            49: 1,
            50: 2,
            51: 3,
            52: 4,
            53: 5,
            54: 6,
            55: 7
        }

        current_pile = switch.get(some_k)-1
    else:
        if current_pile == max_pile_index:
            current_pile = 0
        else:
            current_pile += 1

    return


def clear_current_pile():
    if 6 < current_pile < 11:
        pile = foundation_piles[current_pile-7]
    elif current_pile < 7:
        pile = tableu_piles[current_pile]
    else:
        pile = waste_pile
        # unknown_waste_counter = game_logic.get_unknown_counter()
        # unknown_waste_counter = 24
        game_logic.unknownWaste = 24
        game_logic.allUnknownWasteFound = False

    pile.clear()

    """for card in list_of_piles[current_pile]:
        dictionaryOfDetectedCards[card] = False
        dictionaryOfNewlyDiscoveredCards[card] = False
        dictionaryOfCardFrameCounter[card] = 0

    list_of_piles_only_containing_newly_detected_cards[current_pile].clear()
    list_of_piles[current_pile].clear()"""

    return


def sortLists(some_tableu_piles, some_foundation_piles, some_waste_cards):

    for some_key, pile in some_tableu_piles.items():
        pile.sort(reverse=False)
    for some_key, pile in some_foundation_piles.items():
        pile.sort(reverse=True)

    return some_tableu_piles, some_foundation_piles, some_waste_cards


def done_scanning():
    global game_has_just_started
    global game_logic
    global list_of_piles
    global extra_move

    # print(game_logic.unknownWaste)
    #if game_logic.unknownWaste == 0:
     #   print(game_logic.unknownWasteCounter)

    #print(len(game_logic.logicWasteCardPile))

    #game_logic.allUnknownWasteFound = True

    #game_logic.handle_update_reversed_waste_pile()

    #print (game_logic.unknownWasteCounter)

    if game_has_just_started:
        game_has_just_started = False

    """  # send data to Logic
    list_of_tableu_piles, list_of_foundation_piles, waste_cards = make_separate_lists(list_of_piles)

    list_of_tableu_piles, list_of_foundation_piles, waste_cards = sortLists(list_of_tableu_piles, list_of_foundation_piles, waste_cards)

    list_of_tableu_piles, list_of_foundation_piles, new_waste_cards \
        = make_separate_lists(list_of_piles_only_containing_newly_detected_cards)

    list_of_tableu_piles, list_of_foundation_piles, new_waste_cards \
        = sortLists(list_of_tableu_piles, list_of_foundation_piles, new_waste_cards)

    if len(new_waste_cards) != 0:
        last_waste_card = new_waste_cards[len(new_waste_cards) - 1]
        game_logic.update_logic_scan(last_waste_card, list_of_tableu_piles, list_of_foundation_piles)
        print("********************************************************")
        print("Sending the following to logic:")
        print(f"Tableu_piles: {list_of_tableu_piles}")
        print(f"Foundation_piles: {list_of_foundation_piles}")
        print(f"waste_cards: {last_waste_card}")
        print(" ")
    else:
        game_logic.update_logic_scan(None, list_of_tableu_piles, list_of_foundation_piles)
        print("********************************************************")
        print("Sending the following to logic:")
        print(f"Tableu_piles: {list_of_tableu_piles}")
        print(f"Foundation_piles: {list_of_foundation_piles}")
        print(f"waste_cards: None")
        print(" ")"""


        # game_logic.update_logic_scan(new_waste_cards, list_of_tableu_piles, list_of_foundation_piles)



        # We clear the lists of newly detected cards
        #for pile in range(12):
        #    list_of_piles_only_containing_newly_detected_cards[pile].clear()

    move = game_logic.calculate_move(True)
    print(move)
    game_logic.update_logic_move(move)
    if move[0]
    """list_of_tableu_piles, list_of_foundation_piles, list_of_waste_cards = game_logic.get_piles()

    print("Getting the following piles from logic:")
    print(f"Tableu_piles: {list_of_tableu_piles}")
    print(f"Foundation_piles: {list_of_foundation_piles}")
    print(f"waste_cards: {list_of_waste_cards}")
    print(" ")

    update_card_piles(list_of_tableu_piles, list_of_foundation_piles, list_of_waste_cards)
    counter = game_logic.get_unknown_counter()
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(counter)"""

    return move


# This function checks if the move tells us to flip cards
def check_for_unknown_cards(move):
    if move is None:
        return False

    there_is_an_unknown_card = False

    if move[6] == "YES":
        there_is_an_unknown_card = True

    return there_is_an_unknown_card


def check_for_win_condition(move):
    global game_has_ended
    if move is None:
        return

    if move[0] == "WIN":
        print("You have won, closing now")
        game_has_ended = True
        return

    if move[0] == "LOSE":
        print("You have lost, closing now")
        game_has_ended = True
        return


# This function is used to separate a list into 3 smaller lists of foundation, tableau and waste piles. This is used to
# make logic and computer_vision compatible with each other.
def make_separate_lists(source_list):
    list_of_tableu_piles = {0: [],
                            1: [],
                            2: [],
                            3: [],
                            4: [],
                            5: [],
                            6: []}
    list_of_foundation_piles = {0: [],
                                1: [],
                                2: [],
                                3: []}

    for pile in range(11):
        if pile > 6:
            list_of_foundation_piles[pile - 7] = source_list[pile]
        else:
            list_of_tableu_piles[pile] = source_list[pile]

    return list_of_tableu_piles, list_of_foundation_piles, source_list[11]


def update_card_piles(tableu_piles, foundation_piles, waste_cards):
    global list_of_piles
    for pile in range(11):
        if pile > 6:
            list_of_piles[pile] = copy.deepcopy(foundation_piles[pile-7])
        else:
            list_of_piles[pile] = copy.deepcopy(tableu_piles[pile])
        list_of_piles[11] = copy.deepcopy(waste_cards)

    print("this is all the piles in this part after getting the piles from logic:")
    print(list_of_piles)
    print(" ")
    print("************************************************************************")

    return


# def update_piles

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

# Set up folder names for default values

model_folder = os.path.join(get_parent_dir(1), "Model_Weights")

model_weights = os.path.join(model_folder, "trained_weights_final.h5")
model_classes = os.path.join(model_folder, "data_classes.txt")

anchors_path = os.path.join(src_path, "keras_yolo3", "model_data", "yolo_anchors.txt")

# define YOLO detector
yolo = YOLO(
    **{
        "model_path": model_weights,
        "anchors_path": anchors_path,
        "classes_path": model_classes,
        "score": 0.25,
        "gpu_num": 1,
        "model_image_size": (416, 416),
    }
)

# labels to draw on images
class_file = open(model_classes, "r")
input_labels = [line.rstrip("\n") for line in class_file.readlines()]
print("Found {} input labels: {} ...".format(len(input_labels), input_labels))

game_has_ended = False
game_has_just_started = True
some_move = None
is_confirming_move = False  # the confirming_move-state is when the player is doing the move physically.
game_logic = None
tableu_piles = {}
foundation_piles = {}
waste_pile = []
game_logic = GameLogic.GameLogic(None, None, None)
extra_move = 0
# there_are_unknown_cards = False

while not game_has_ended:
    if some_move is not None:
        if some_move[0] == "NA":
            is_confirming_move = False

    # print(list_of_piles)

    # Getting the piles from the logic.
    tableu_piles, foundation_piles, waste_pile = game_logic.get_piles()

    # Getting a frame from camera.
    ret, img = video_stream.read()
    final_image = img

    if not is_confirming_move:
        # converting image to make it work with the detection
        im_pil = Image.fromarray(img)

        # making the detection
        predictions, image = yolo.detect_image(im_pil, False)

        # sort the predictions based on ymin
        predictions.sort(key=lambda x: x[1], reverse=False)

        desired_min_confidence_level = 0.25
        list_of_certain_detections = []

        # removing all non certain predictions
        for prediction in predictions:
            if prediction[5] >= desired_min_confidence_level:
                list_of_certain_detections.append(prediction)

        # removing duplicates
        list_of_detected_names = []
        list_of_detections_without_duplicates = []
        for prediction in list_of_certain_detections:
            name = dictionaryOfIndexToName.get(prediction[4])
            if name not in list_of_detected_names:
                list_of_detected_names.append(name)
                list_of_detections_without_duplicates.append(prediction)

        # incrementing the count of each card seen in succession from frame to frame
        for prediction in list_of_detections_without_duplicates:
            increment_card_viewed_counter(prediction)

        # resetting the count for all the cards that has not been detected this frame
        for key, value in dictionaryOfCardFrameCounter.items():
            found_card = False
            for prediction in list_of_detections_without_duplicates:
                prediction_name = dictionaryOfIndexToName.get(prediction[4])
                if key == prediction_name:
                    found_card = True
                    continue
            if not found_card:
                dictionaryOfCardFrameCounter[key] = 0

        opencv_image = np.asarray(image)
        final_image = opencv_image

    k = cv2.waitKey(1) & 0xff
    if k == 27:  # When 'ESC' is pressed, we exit.
        break
    if k == 99 and not is_confirming_move:  # When 'c' is pressed we clear current pile
        clear_current_pile()
    if (k == 32 or (47 < k < 56)) and not is_confirming_move:  # When 'SPACE' or '0..7' is pressed we change pile
        change_pile(k)
    if k == 101:  # When 'e' is pressed, we stop scanning or confirm move
        print("Just pressed e")
        if not is_confirming_move:
            some_move = done_scanning()
            if some_move[0] != "NA":
                is_confirming_move = True
        else:
            if some_move[6] == "YES" and some_move[5] != "W": #TODO: FIX WHEN IT IS THE WASTE CARD
                # TODO: EOW PRINT EN 6'SER YO
                is_confirming_move = False
            else:
                some_move = done_scanning()


    check_for_win_condition(some_move)
    show_text(final_image, some_move)
    cv2.imshow('img', final_image)


cv2.destroyAllWindows()
video_stream.release()
yolo.close_session()
