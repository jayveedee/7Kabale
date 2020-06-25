import os
import sys
import cv2

"""
This file is a modified version of the Detector.py from 
the following repository: https://github.com/AntonMu/TrainYourOwnYOLO
We have changed a lot to make the code fit our needs.
We have marked all code that we haven't written between two '****'

All modifications in this file made by Asama Hayder (s185099)
"""


# ****
def get_parent_dir(n=1):
    """ returns the n-th parent directory of the current
    working directory """
    current_path = os.path.dirname(os.path.abspath(__file__))
    for i in range(n):
        current_path = os.path.dirname(current_path)
    return current_path


src_path = os.path.join(get_parent_dir(1), "src")
utils_path = os.path.join(get_parent_dir(1), "Utils")

sys.path.append(src_path)
sys.path.append(utils_path)
# ****

# We start a video_stream from the webcam
video_stream = cv2.VideoCapture(0)

# pycharm says that no module named Dictionaries and Keras_yolo3.yolo but they are detected and works fine.
import Dictionaries
import GameLogic
from keras_yolo3.yolo import YOLO
from PIL import Image
import numpy as np

dictionary_of_pile_names = Dictionaries.dictionary_of_pile_names
dictionaryOfIndexToName = Dictionaries.dictionaryOfIndexToName
dictionaryOfCardFrameCounter = Dictionaries.dictionaryOfCardFrameCounter
current_pile = 0


# This function is run when a card is detected.
def detect_card(some_prediction):
    # we get the card as an index, but we want the name.
    card_name = dictionaryOfIndexToName.get(some_prediction[4])

    # Adding the detected card to the current pile.
    if 6 < current_pile < 11:
        foundation_piles.get(current_pile-7).append(card_name)
    elif current_pile < 7:
        tableu_piles.get(current_pile).append(card_name)
    else:
        waste_pile.append(card_name)

    sort_lists(tableu_piles, foundation_piles, waste_pile)

    return


# This function increments the number of times a card has been seen sequentially. If the number reaches a specified
# amount, then we detect the card.
def increment_card_viewed_counter(some_prediction):
    number_of_times_a_card_should_be_seen_sequentially = 15

    card_name = dictionaryOfIndexToName.get(some_prediction[4])

    # checking if already detected
    if check_if_card_already_detected(card_name):
        return

    # we keep track of how many times all cards has been seen in a dictionary.
    number_of_times_viewed = dictionaryOfCardFrameCounter.get(card_name)
    number_of_times_viewed += 1
    if number_of_times_viewed >= number_of_times_a_card_should_be_seen_sequentially:
        detect_card(some_prediction)
    else:
        # updating the dictionary
        dictionaryOfCardFrameCounter[card_name] = number_of_times_viewed

    return


# This function simply checks if a card has already been detected. We need to check all the piles.
# Tableu_piles and foundation_piles are dictionaries of lists, while the waste_pile is simply a list.
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


# This functions displays all the cards in the current pile.
def display_cards_in_current_pile(some_image, font, text_size, text_thickness, border_color, border_thickness):
    cards_color = (3, 186, 252, 255)
    list_of_detected_cards = "Cards: "

    # We sort the lists differently based on if it is a tableu, foundation or waste pile.
    # This is because if there is no space left on the screen and we can't show all cards at once,
    # then we just want to show the must important cards. e.g. in foundation it is the the highest numbers.
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
                list_of_detected_cards += pile[len(pile)-i-1]
                list_of_detected_cards += ", "
        else:
            for card in pile:
                list_of_detected_cards += card
                list_of_detected_cards += ", "

    cv2.putText(some_image, list_of_detected_cards, (0, 200), font, text_size, border_color, border_thickness)
    cv2.putText(some_image, list_of_detected_cards, (0, 200), font, text_size, cards_color, text_thickness)

    return


# displays all the text on the screen.
def display_text(some_image, move):
    text_color = (255, 255, 255, 255)  # remember it is in bgr
    text_border_color = (0, 0, 0, 255)
    text_size = .75
    text_thickness = 1
    border_thickness = 3 * text_thickness
    font = cv2.FONT_HERSHEY_DUPLEX

    cv2.putText(some_image, "'ESC' to exit", (0, 30), font, text_size, text_border_color, border_thickness)
    cv2.putText(some_image, "'ESC' to exit", (0, 30), font, text_size, text_color, text_thickness)

    # depending on if you are in the middle of a move or not, then we display different info.
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

        display_cards_in_current_pile(some_image, font, text_size, text_thickness, text_border_color, border_thickness)

    display_move(move, some_image, font, text_size, text_thickness, text_border_color, border_thickness)

    return


# This function displays the current move, or displays what to do if there is no move.
def display_move(move, some_image, font, text_size, text_thickness, border_color, border_thickness):
    global move_text
    move_color = (0, 255, 0, 255)

    # Creating the text that will be displayed
    if game_has_just_started:
        move_text = "Scan first card of each pile"
    else:
        if not is_confirming_move:
            move_text = "Scan from waste/flip cards."
        elif move[0] != "NA" and move[0] != "WIN":
            card_number = move[0]
            card_suit = move[1]
            from_pile = move[2]
            to_pile = move[3]
            pile_group = move[4]

            move_text = f"move {card_number}{card_suit} from pile {int(from_pile) + 1} to pile {int(to_pile) + 1} " \
                        f"in group {pile_group}"

    # Calculating the coordinates and displaying the text
    text_width = cv2.getTextSize(move_text, font, text_size, text_thickness)[0]

    x_coordinate = (some_image.shape[1] - text_width[0])/2
    y_coordinate = (some_image.shape[0] - text_width[1])

    x_rounded = int(round(x_coordinate))
    y_rounded = int(round(y_coordinate))

    cv2.putText(some_image, move_text, (x_rounded, y_rounded), font, text_size,
                border_color, border_thickness)
    cv2.putText(some_image, move_text, (x_rounded, y_rounded), font, text_size,
                move_color, text_thickness)

    return


# This function cahnges the current pile. It takes some_k which is a key-press.
def change_pile(some_k):
    global current_pile
    total_number_of_piles = len(dictionary_of_pile_names)
    max_pile_index = total_number_of_piles - 1

    # If the key isn't SPACE we want to change to the exact pile
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
        # else we simply increment the current pile number.
        if current_pile == max_pile_index:
            current_pile = 0
        else:
            current_pile += 1

    return


# This function clears the current pile.
def clear_current_pile():
    if 6 < current_pile < 11:
        pile = foundation_piles[current_pile-7]
    elif current_pile < 7:
        pile = tableu_piles[current_pile]
    else:
        pile = waste_pile

    pile.clear()

    return


# This function is used to sort the lists so it makes sense to what type of pile it is. e.g. if it is a foundation pile, then we want the numbers decreasing etc.
def sort_lists(some_tableu_piles, some_foundation_piles, some_waste_cards):

    for some_key, pile in some_tableu_piles.items():
        pile.sort(reverse=False)
    for some_key, pile in some_foundation_piles.items():
        pile.sort(reverse=True)

    return some_tableu_piles, some_foundation_piles, some_waste_cards


# This function is used when you are done scanning and want to check for a move.
def get_move():
    global game_has_just_started
    global game_logic
    global extra_move

    # It is no longer the first move in the game
    if game_has_just_started:
        game_has_just_started = False

    # calculating the move
    move = game_logic.calculate_move(True)
    print(move)

    # updating the cards inside the logic by using the move from logic.
    game_logic.update_logic_move(move)

    # This code is used to fix a bug, where we need to get move twice.
    if move[0] == "NA" and extra_move == 0:
        move = game_logic.calculate_move(True)
        game_logic.update_logic_move(move)
        extra_move += 1
    elif extra_move > 0 and move[0] != "NA" and move[0] != "LOSE" and move[0] != "WIN":
        extra_move = 0

    return move


# This function checks if the game has finished.
def check_for_win_condition(move):
    global game_has_ended
    if move is None:
        return

    if move[0] == "WIN":
        print("*************** You have won, closing now ***************")
        game_has_ended = True
        return


# ****
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
# ****

game_has_ended = False
game_has_just_started = True  # Used to display different info at the start of the game
some_move = None
is_confirming_move = False  # the confirming_move-state is when the player is doing the move physically.
game_logic = None
tableu_piles = {}
foundation_piles = {}
waste_pile = []
game_logic = GameLogic.GameLogic(None, None, None)
extra_move = 0  # Used to fix a bug where we need to press 'e' twice.
move_text = ""

# This is the big game loop. It continues until the game has ended.
while not game_has_ended:
    # We check if we had a move from last frame.
    if some_move is not None:
        if some_move[0] == "NA":
            is_confirming_move = False

    # Getting the piles from the logic.
    tableu_piles, foundation_piles, waste_pile = game_logic.get_piles()

    # Getting a frame from camera.
    ret, img = video_stream.read()
    final_image = img

    # This is where the detection happens. We only want to detect cards if we are not in the middle of a move.
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

        # We convert the image back to open_cv form.
        opencv_image = np.asarray(image)
        final_image = opencv_image

    # we wait 1 millisecond every frame for a potential keypress.
    k = cv2.waitKey(1) & 0xff
    if k == 27:  # When 'ESC' is pressed, we exit.
        break
    if k == 99 and not is_confirming_move:  # When 'c' is pressed we clear current pile
        clear_current_pile()
    if (k == 32 or (47 < k < 56)) and not is_confirming_move:  # When 'SPACE' or '0..7' is pressed we change pile
        change_pile(k)
    if k == 101:  # When 'e' is pressed, we stop scanning or confirm move
        if not is_confirming_move:
            # if we are not in the middle of a move, we request a move.
            some_move = get_move()
            # then we check if the received move is valid.
            if some_move[0] != "NA":
                is_confirming_move = True
        else:
            # here we check if there are unknown cards that we need to flip. In that case, we do not request another move.
            if some_move[6] == "YES" and some_move[5] != "W":
                is_confirming_move = False
            else:
                some_move = get_move()

    # Check if the game has ended
    check_for_win_condition(some_move)
    # Drawing text on image
    display_text(final_image, some_move)
    # Showing image
    cv2.imshow('img', final_image)

# Closing the application.
cv2.destroyAllWindows()
video_stream.release()
yolo.close_session()
