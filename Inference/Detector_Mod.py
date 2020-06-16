import os
import sys
import cv2

"""
This file is a modified version of the Detector.py from 
the following repository: https://github.com/AntonMu/TrainYourOwnYOLO
We have changed a lot to make the code fit our needs. 
"""


def get_parent_dir(n=1):
    """ returns the n-th parent dicrectory of the current
    working directory """
    current_path = os.path.dirname(os.path.abspath(__file__))
    for k in range(n):
        current_path = os.path.dirname(current_path)
    return current_path


src_path = os.path.join(get_parent_dir(1), "src")
utils_path = os.path.join(get_parent_dir(1), "Utils")

sys.path.append(src_path)
sys.path.append(utils_path)

cap = cv2.VideoCapture(0)

# for me, pycharm says that no module named Dictionaries and Keras_yolo3.yolo but they are detected and works fine.
# Maybe a bug?

import argparse
import Dictionaries
import GameLogic
from keras_yolo3.yolo import YOLO
from PIL import Image
import numpy as np

list_of_piles = Dictionaries.list_of_piles
dictionary_of_piles = Dictionaries.dictionary_of_piles
dictionary_of_pile_names = Dictionaries.dictionary_of_pile_names
dictionaryOfIndexToName = Dictionaries.dictionaryOfIndexToName
dictionaryOfCardFrameCounter = Dictionaries.dictionaryOfCardFrameCounter
dictionaryOfDetectedCards = Dictionaries.dictionaryOfDetectedCards

current_pile = 0


def detect_card(some_prediction):
    card_name = dictionaryOfIndexToName.get(some_prediction[4])
    dictionaryOfDetectedCards[card_name] = True
    if current_pile == 11:
        split_string_array = card_name.split()
        dictionary_of_piles[current_pile].append(split_string_array)
    else:
        dictionary_of_piles[current_pile].append(card_name)
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

    for some_name in dictionary_of_piles[current_pile]:
        list_of_detected_cards += some_name
        list_of_detected_cards += " ,"
    cv2.putText(some_image, list_of_detected_cards, (0, 200), cv2.FONT_HERSHEY_DUPLEX, .75, (209, 80, 0, 255), 2)

    return


# displays various text
def show_text(some_image):
    cv2.putText(opencv_image, "'ESC' to exit", (0, 30), cv2.FONT_HERSHEY_DUPLEX, .75, (209, 80, 0, 255), 2)
    cv2.putText(opencv_image, "'c' to clear current pile", (0, 70), cv2.FONT_HERSHEY_DUPLEX, .75,
                (209, 80, 0, 255), 2)
    cv2.putText(opencv_image, "'SPACE' for next pile", (0, 110), cv2.FONT_HERSHEY_DUPLEX, .75, (209, 80, 0, 255), 2)
    cv2.putText(opencv_image, "'e' for done scanning", (0, 150), cv2.FONT_HERSHEY_DUPLEX, .75, (209, 80, 0, 255), 2)

    current_pile_text = "current pile: "
    current_pile_name = dictionary_of_pile_names.get(current_pile)
    current_pile_text += current_pile_name
    text_size = cv2.getTextSize(current_pile_text, cv2.FONT_HERSHEY_DUPLEX, .75, 2)[0]
    image_width = some_image.shape[1]

    x_coordinate = image_width - text_size[0]
    cv2.putText(opencv_image, current_pile_text, (x_coordinate, 30),
                cv2.FONT_HERSHEY_DUPLEX, .75, (209, 80, 0, 255), 2)
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
    for card in dictionary_of_piles[current_pile]:
        dictionaryOfDetectedCards[card] = False
        dictionaryOfCardFrameCounter[card] = 0

    dictionary_of_piles[current_pile].clear()

    return


def done_scanning():
    # send data to Logic
    list_of_tableu_piles = {0: [],
                            1: [],
                            2: [],
                            3: [],
                            4: [],
                            5: [],
                            6: []}
    list_of_foundation_piles = {7: [],
                                8: [],
                                9: [],
                                10: []}
    for pile in range(11):
        if pile > 6:
            list_of_foundation_piles[pile] = list_of_piles[pile]
        else:
            list_of_tableu_piles[pile] = list_of_piles[pile]
    game_logic = GameLogic.GameLogic(list_of_piles[11], list_of_tableu_piles, list_of_foundation_piles)

    moves = game_logic.calculate_move()
    for move in moves:
        print(move)

    return


os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

# Set up folder names for default values

model_folder = os.path.join(get_parent_dir(1), "Model_Weights")

model_weights = os.path.join(model_folder, "trained_weights_final.h5")
model_classes = os.path.join(model_folder, "data_classes.txt")

anchors_path = os.path.join(src_path, "keras_yolo3", "model_data", "yolo_anchors.txt")

FLAGS = None

if __name__ == "__main__":
    # Delete all default flags
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    """
    Command line options
    """

    parser.add_argument(
        "--yolo_model",
        type=str,
        dest="model_path",
        default=model_weights,
        help="Path to pre-trained weight files. Default is " + model_weights,
    )

    parser.add_argument(
        "--anchors",
        type=str,
        dest="anchors_path",
        default=anchors_path,
        help="Path to YOLO anchors. Default is " + anchors_path,
    )

    parser.add_argument(
        "--classes",
        type=str,
        dest="classes_path",
        default=model_classes,
        help="Path to YOLO class specifications. Default is " + model_classes,
    )

    parser.add_argument(
        "--gpu_num", type=int, default=1, help="Number of GPU to use. Default is 1"
    )

    parser.add_argument(
        "--confidence",
        type=float,
        dest="score",
        default=0.25,
        help="Threshold for YOLO object confidence score to show predictions. Default is 0.25.",
    )

    FLAGS = parser.parse_args()

    # define YOLO detector
    yolo = YOLO(
        **{
            "model_path": FLAGS.model_path,
            "anchors_path": FLAGS.anchors_path,
            "classes_path": FLAGS.classes_path,
            "score": FLAGS.score,
            "gpu_num": FLAGS.gpu_num,
            "model_image_size": (416, 416),
        }
    )

    # labels to draw on images
    class_file = open(FLAGS.classes_path, "r")
    input_labels = [line.rstrip("\n") for line in class_file.readlines()]
    print("Found {} input labels: {} ...".format(len(input_labels), input_labels))

    while True:
        ret, img = cap.read()
        im_pil = Image.fromarray(img)
        predictions, image = yolo.detect_image(im_pil)
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
                """while True:
                    print(key)
                    print(prediction[4])
                    k = cv2.waitKey(30) & 0xff
                    if k == 27:
                        break"""
                if key == prediction_name:
                    found_card = True
                    continue
            if not found_card:
                dictionaryOfCardFrameCounter[key] = 0

        opencv_image = np.asarray(image)
        show_text(opencv_image)
        show_detected_cards(opencv_image)
        cv2.imshow('img', opencv_image)
        k = cv2.waitKey(30) & 0xff
        if k == 27:  # When 'ESC" is pressed, we exit.
            break
        if k == 99:  # When 'c' is pressed we clear current pile
            clear_current_pile()
        if k == 32:  # When 'SPACE' is pressed we change pile
            change_pile()
        if k == 101:  # When 'e' is pressed, we stop scanning
            done_scanning()
            break

    cv2.destroyAllWindows()
    cap.release()
    yolo.close_session()
