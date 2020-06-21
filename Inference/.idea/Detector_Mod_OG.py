import os
import sys
import cv2

"""
This file is a modified version of the Detector.py from 
the following repository: https://github.com/AntonMu/TrainYourOwnYOLO
We have changed a lot to make the code fit our needs. 
"""


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
    dictionaryOfDetectedCards[card_name] = True
    dictionaryOfNewlyDiscoveredCards[card_name] = True
    list_of_piles[current_pile].append(card_name)

    if not game_has_just_started:
        list_of_piles_only_containing_newly_detected_cards[current_pile].append(card_name)
        # list_of_piles[current_pile].append(card_name)

    return


def increment_card_viewed_counter(some_prediction):
    card_name = dictionaryOfIndexToName.get(some_prediction[4])

    # checking if already detected
    if dictionaryOfDetectedCards.get(card_name):
        return

    number_of_times_viewed = dictionaryOfCardFrameCounter.get(card_name)
    number_of_times_viewed += 1
    if number_of_times_viewed >= 10:
        detect_card(some_prediction)
    else:
        dictionaryOfCardFrameCounter[card_name] = number_of_times_viewed

    return


def show_detected_cards(some_image):
    list_of_detected_cards = "Cards: "

    for some_name in list_of_piles[current_pile]:
        list_of_detected_cards += some_name
        list_of_detected_cards += " ,"
    cv2.putText(some_image, list_of_detected_cards, (0, 200), cv2.FONT_HERSHEY_DUPLEX, .75, (209, 80, 0, 255), 2)

    return


# displays various text
def show_text(some_image, move):
    cv2.putText(some_image, "'ESC' to exit", (0, 30), cv2.FONT_HERSHEY_DUPLEX, .75, (209, 80, 0, 255), 2)

    """if move is not None and move[0] is not "NA" and not there_are_unknown_cards:
        cv2.putText(some_image, "'e' to confirm move", (0, 70), cv2.FONT_HERSHEY_DUPLEX, .75,
                    (209, 80, 0, 255), 2)"""

    if move is not None and move[0] is not "NA":
        cv2.putText(some_image, "'e' to confirm move", (0, 70), cv2.FONT_HERSHEY_DUPLEX, .75,
                    (209, 80, 0, 255), 2)
    else:
        cv2.putText(some_image, "'c' to clear current pile", (0, 70), cv2.FONT_HERSHEY_DUPLEX, .75,
                    (209, 80, 0, 255), 2)
        cv2.putText(some_image, "'SPACE' for next pile", (0, 110), cv2.FONT_HERSHEY_DUPLEX, .75, (209, 80, 0, 255), 2)
        cv2.putText(some_image, "'e' for done scanning", (0, 150), cv2.FONT_HERSHEY_DUPLEX, .75, (209, 80, 0, 255), 2)
        current_pile_text = "current pile: "
        current_pile_name = dictionary_of_pile_names.get(current_pile)
        current_pile_text += current_pile_name
        text_size = cv2.getTextSize(current_pile_text, cv2.FONT_HERSHEY_DUPLEX, .75, 2)[0]
        image_width = some_image.shape[1]

        x_coordinate = image_width - text_size[0]
        cv2.putText(some_image, current_pile_text, (x_coordinate, 30),
                    cv2.FONT_HERSHEY_DUPLEX, .75, (209, 80, 0, 255), 2)

        show_detected_cards(some_image)
    show_move(move, some_image)

    return


def show_move(move, some_image):
    # Creating the text that will be displayed
    global move_text
    # global there_are_unknown_cards

    """elif there_are_unknown_cards:
        move_text = "Flip and Scan the unknown card"""""
    if game_has_just_started:
        move_text = "Scan first card of each pile"
    else:
        if move is None or move[0] == "NA":
            move_text = "No Valid move. Take a card from the waste pile."
        else:
            card_number = move[0]
            card_suit = move[1]
            from_pile = move[2]
            to_pile = move[3]
            pile_group = move[4]

            move_text = f"move {card_number}{card_suit} from pile {int(from_pile) + 1} to pile {int(to_pile) + 1} " \
                        f"in group {pile_group}"

    # print(move_text)

    # Calculating the coordinates and displaying the text
    text_size = cv2.getTextSize(move_text, cv2.FONT_HERSHEY_DUPLEX, .75, 2)[0]
    x_coordinate = (some_image.shape[1] - text_size[0])/2
    y_coordinate = (some_image.shape[0] - text_size[1])

    x_coordinate_rounded = int(round(x_coordinate))
    y_coordinate_rounded = int(round(y_coordinate))
    cv2.putText(some_image, move_text, (x_coordinate_rounded, y_coordinate_rounded), cv2.FONT_HERSHEY_DUPLEX, .75,
                (0, 255, 0, 255), 2)

    return


def change_pile():
    global current_pile
    total_number_of_piles = len(dictionary_of_pile_names)
    max_pile_index = total_number_of_piles - 1
    if current_pile == max_pile_index:
        current_pile = 0
    else:
        current_pile += 1
    return


def clear_current_pile():
    for card in list_of_piles[current_pile]:
        dictionaryOfDetectedCards[card] = False
        dictionaryOfNewlyDiscoveredCards[card] = False
        dictionaryOfCardFrameCounter[card] = 0

    list_of_piles_only_containing_newly_detected_cards[current_pile].clear()
    list_of_piles[current_pile].clear()

    return

def sortLists(some_tableu_piles, some_foundation_piles, some_waste_cards):

    for some_key, pile in some_tableu_piles.items():
        pile.sort(reverse=False)
    for some_key, pile in some_foundation_piles.items():
        pile.sort(reverse=True)

    return some_tableu_piles, some_foundation_piles, some_waste_cards

def done_scanning():
    print("I am running!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    global game_has_just_started
    global game_logic
    global list_of_piles

    # send data to Logic
    list_of_tableu_piles, list_of_foundation_piles, waste_cards = make_separate_lists(list_of_piles)

    list_of_tableu_piles, list_of_foundation_piles, waste_cards = sortLists(list_of_tableu_piles, list_of_foundation_piles, waste_cards)

    if game_has_just_started:
        game_has_just_started = False
        print("********************************************************")
        print("Sending the following to logic:")
        print(f"Tableu_piles: {list_of_tableu_piles}")
        print(f"Foundation_piles: {list_of_foundation_piles}")
        print(f"waste_cards: {waste_cards}")
        print(" ")
        game_logic = GameLogic.GameLogic(waste_cards, list_of_tableu_piles, list_of_foundation_piles)
    else:
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
            print(" ")


        # game_logic.update_logic_scan(new_waste_cards, list_of_tableu_piles, list_of_foundation_piles)



        # We clear the lists of newly detected cards
        for pile in range(12):
            list_of_piles_only_containing_newly_detected_cards[pile].clear()

    move = game_logic.calculate_move()
    game_logic.update_logic_move(move)
    list_of_tableu_piles, list_of_foundation_piles, list_of_waste_cards = game_logic.get_piles()

    print("Getting the following piles from logic:")
    print(f"Tableu_piles: {list_of_tableu_piles}")
    print(f"Foundation_piles: {list_of_foundation_piles}")
    print(f"waste_cards: {list_of_waste_cards}")
    print(" ")

    update_card_piles(list_of_tableu_piles, list_of_foundation_piles, list_of_waste_cards)
    counter = game_logic.get_unknown_counter()
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(counter)

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
    if move is None:
        return

    if move[0] == "WIN":
        global game_has_ended
        print("You have won, closing now")
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
# there_are_unknown_cards = False

while not game_has_ended:
    # print(list_of_piles)
    ret, img = video_stream.read()
    final_image = img
    if not is_confirming_move:
        im_pil = Image.fromarray(img)
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

    k = cv2.waitKey(30) & 0xff
    if k == 27:  # When 'ESC' is pressed, we exit.
        break
    if k == 99 and not is_confirming_move:  # When 'c' is pressed we clear current pile
        clear_current_pile()
    if k == 32 and not is_confirming_move:  # When 'SPACE' is pressed we change pile
        change_pile()
    if k == 101:  # When 'e' is pressed, we stop scanning or confirm move
        """if not is_confirming_move:
            if not there_are_unknown_cards:
                some_move = done_scanning()
                if some_move[0] != "NA":
                    is_confirming_move = True
        else:
            if check_for_unknown_cards(some_move):
                is_confirming_move = False
                some_move = None
                there_are_unknown_cards = True
            else:
                some_move = done_scanning()
                if some_move[0] == "NA":
                    is_confirming_move = False"""

        if not is_confirming_move:
            some_move = done_scanning()
            if some_move[0] != "NA":
                is_confirming_move = True
        else:
            some_move = done_scanning()
            if some_move[0] == "NA":
                is_confirming_move = False

    check_for_win_condition(some_move)
    show_text(final_image, some_move)
    cv2.imshow('img', final_image)

cv2.destroyAllWindows()
video_stream.release()
yolo.close_session()
