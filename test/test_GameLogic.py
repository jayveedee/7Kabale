from unittest import TestCase

from Inference import GameLogic

import random
import copy


def createDummyList(self, dummyVersion=0):
    dummyList = {}
    if dummyVersion >= 0:

        for i in range(0, 7):
            tempList = []

            if dummyVersion == 1:
                if i == 2:
                    cardNumber = 2
                    cardType = "d"
                    tempList.append(str(cardNumber) + " " + cardType)

            if dummyVersion == 2:
                if i != 2:
                    cardNumber = random.randint(1, 13)
                    cardType = random.choice("hdsc")
                    tempList.append(str(cardNumber) + " " + cardType)

            if dummyVersion == 3:
                if i > 3:
                    for j in range(0, i):
                        cardNumber = random.randint(1, 13)
                        cardType = random.choice("hdsc")
                        tempList.append(str(cardNumber) + " " + cardType)
                else:
                    cardNumber = random.randint(1, 13)
                    cardType = random.choice("hdsc")
                    tempList.append(str(cardNumber) + " " + cardType)

            dummyList[i] = tempList

    if dummyVersion == -1:
        for i in range(0, 4):
            tempList = []
            dummyList[i] = tempList

    return dummyList


def create_list(tb0, tb1, tb2, tb3, tb4, tb5, tb6):
    tb = {0: tb0, 1: tb1, 2: tb2, 3: tb3, 4: tb4, 5: tb5, 6: tb6}
    return tb


class TestGameLogic(TestCase):

    def test_play_game(self):
        tb = create_list(["06 h"], ["06 c"], ["13 d"], ["04 d"], ["03 h"], ["02 s"], ["08 c"])
        fd = {0: [], 1: [], 2: [], 3: []}
        wc = []

        self.gl = GameLogic.GameLogic(wc, tb, fd)

        # Move & Update
        self.calculateMove(["02", "s", "5", "4", "T", "T", "YES"], ["02 s", "03 h"])
        self.updateLists("T", "04 c", 5)

        # Move & Update
        self.calculateMove(["03", "h", "4", "5", "T", "T", "YES"], ["02 s", "03 h", "04 c"])
        self.updateLists("T", "05 s", 4)

        # Move & Update
        self.calculateMove(["04", "d", "3", "4", "T", "T", "YES"], ["04 d", "05 s"])
        self.updateLists("T", "12 s", 3)

        # Move & Update
        self.calculateMove(["12", "s", "3", "2", "T", "T", "YES"], ["12 s", "13 d"])
        self.updateLists("T", "12 c", 3)

        # Move & Update
        self.calculateMove(["05", "s", "4", "0", "T", "T", "YES"], ["04 d", "05 s", "06 h"])
        self.updateLists("T", "07 s", 4)

        # Move & Update
        self.calculateMove(["06", "h", "0", "4", "T", "T", "NO"], ["04 d", "05 s", "06 h", "07 s"])
        self.updateLists("T", "NA", 0)

        # Move & Update
        self.calculateMove(["13", "d", "2", "0", "T", "T", "YES"], ["12 s", "13 d"])
        self.updateLists("T", "03 d", 2)

        # Move & Update
        self.calculateMove(["NA", "NA", "NA", "NA", "NA", "W", "YES"], ["NA", "NA", "NA", "NA", "NA"])
        self.updateLists("T", "NA", 0)

        # Move & Update
        self.calculateMove(["NA", "NA", "NA", "NA", "NA", "W", "YES"], ["NA", "NA", "NA", "NA", "NA"])
        self.updateLists("W", "09 d", -1)

        # Move & Update
        self.calculateMove(["NA", "NA", "NA", "NA", "NA", "W", "YES"], ["NA", "NA", "NA", "NA", "NA"])
        self.updateLists("W", "08 d", -1)

        # Move & Update
        self.calculateMove(["NA", "NA", "NA", "NA", "NA", "W", "YES"], ["NA", "NA", "NA", "NA", "NA"])
        self.updateLists("W", "06 s", -1)

        # Move & Update
        self.calculateMove(["NA", "NA", "NA", "NA", "NA", "W", "YES"], ["NA", "NA", "NA", "NA", "NA"])
        self.updateLists("W", "01 d", -1)

        # Move & Update
        self.calculateMove(["01", "d", "-1", "0", "F", "W", "YES"], ["01 d"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["NA", "NA", "NA", "NA", "NA", "W", "YES"], ["NA", "NA", "NA", "NA", "NA"])
        self.updateLists("W", "01 h", -1)

        # Move & Update
        self.calculateMove(["01", "h", "-1", "1", "F", "W", "YES"], ["01 h"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["NA", "NA", "NA", "NA", "NA", "W", "YES"], ["NA", "NA", "NA", "NA", "NA"])
        self.updateLists("W", "13 c", -1)

        # Move & Update
        self.calculateMove(["NA", "NA", "NA", "NA", "NA", "W", "YES"], ["NA", "NA", "NA", "NA", "NA"])
        self.updateLists("W", "09 s", -1)

        # Move & Update
        self.calculateMove(["NA", "NA", "NA", "NA", "NA", "W", "YES"], ["NA", "NA", "NA", "NA", "NA"])
        self.updateLists("W", "10 d", -1)

        # Move & Update
        self.calculateMove(["NA", "NA", "NA", "NA", "NA", "W", "YES"], ["NA", "NA", "NA", "NA", "NA"])
        self.updateLists("W", "02 d", -1)

        # Move & Update
        self.calculateMove(["02", "d", "-1", "0", "F", "W", "YES"], ["02 d", "01 d"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["03", "d", "2", "0", "F", "T", "YES"], ["03 d", "02 d", "01 d"])
        self.updateLists("T", "12 h", 2)

        # Move & Update
        self.calculateMove(["04", "d", "4", "0", "F", "T", "NO"], ["04 d", "03 d", "02 d", "01 d"])
        self.updateLists("T", "NA", 4)

        # Move & Update
        self.calculateMove(["NA", "NA", "NA", "NA", "NA", "W", "YES"], ["NA", "NA", "NA", "NA", "NA"])
        self.updateLists("W", "11 c", -1)

        # Move & Update
        self.calculateMove(["11", "c", "-1", "2", "T", "W", "YES"], ["11 c", "12 h"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["10", "d", "-1", "2", "T", "W", "YES"], ["10 d", "11 c", "12 h"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["09", "s", "-1", "2", "T", "W", "YES"], ["09 s", "10 d", "11 c", "12 h"])
        self.updateLists("W", "11 h", -1)

        # Move & Update
        self.calculateMove(["11", "h", "-1", "0", "T", "W", "YES"], ["11 h", "12 s", "13 d"])
        self.updateLists("W", "08 s", -1)

        # Move & Update
        self.calculateMove(["NA", "NA", "NA", "NA", "NA", "W", "YES"], ["NA", "NA", "NA", "NA", "NA"])
        self.updateLists("W", "08 h", -1)

        # Move & Update
        self.calculateMove(["08", "h", "-1", "2", "T", "W", "YES"], ["08 h", "09 s", "10 d", "11 c", "12 h"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["07", "s", "4", "2", "T", "T", "YES"], ["05 s", "06 h", "07 s", "08 h", "09 s", "10 d", "11 c", "12 h"])
        self.updateLists("T", "10 c", 4)

        # Move & Update
        self.calculateMove(["10", "c", "4", "0", "T", "T", "YES"], ["10 c", "11 h", "12 s", "13 d"])
        self.updateLists("T", "05 h", 4)

        # Move & Update
        self.calculateMove(["05", "h", "4", "1", "T", "T", "NO"], ["05 h", "06 c"])
        self.updateLists("T", "NA", 4)

        # Move & Update
        self.calculateMove(["04", "c", "5", "1", "T", "T", "YES"], ["02 s", "03 h", "04 c", "05 h", "06 c"])
        self.updateLists("T", "11 s", 5)

        # Move & Update
        self.calculateMove(["NA", "NA", "NA", "NA", "NA", "W", "YES"], ["NA", "NA", "NA", "NA", "NA"])
        self.updateLists("W", "13 h", -1)

        # Move & Update
        self.calculateMove(["13", "h", "-1", "4", "T", "W", "YES"], ["13 h"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["12", "c", "3", "4", "T", "T", "YES"], ["12 c", "13 h"])
        self.updateLists("T", "11 d", 3)

        # Move & Update
        self.calculateMove(["11", "d", "3", "4", "T", "T", "NO"], ["11 d", "12 c", "13 h"])
        self.updateLists("T", "NA", 3)

        # Move & Update
        self.calculateMove(["NA", "NA", "NA", "NA", "NA", "W", "YES"], ["NA", "NA", "NA", "NA", "NA"])
        self.updateLists("W", "07 c", -1)

        # Move & Update
        self.calculateMove(["NA", "NA", "NA", "NA", "NA", "W", "YES"], ["NA", "NA", "NA", "NA", "NA"])
        self.updateLists("W", "07 c", -1)

        # Move & Update
        self.calculateMove(["NA", "NA", "NA", "NA", "NA", "W", "YES"], ["NA", "NA", "NA", "NA", "NA"])
        self.updateLists("W", "05 d", -1)

        # Move & Update
        self.calculateMove(["05", "d", "-1", "0", "F", "W", "YES"], ["05 d", "04 d", "03 d", "02 d", "01 d"])
        self.updateLists("W", "07 d", -1)

        # Move & Update
        self.calculateMove(["07", "d", "-1", "6", "T", "W", "YES"], ["07 d", "08 c"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["06", "c", "1", "6", "T", "T", "YES"], ["02 s", "03 h", "04 c", "05 h", "06 c", "07 d", "08 c"])
        self.updateLists("T", "07 h", 1)

        # Move & Update
        self.calculateMove(["NA", "NA", "NA", "NA", "NA", "W", "YES"], ["NA", "NA", "NA", "NA", "NA"])
        self.updateLists("W", "02 h", -1)

        # Move & Update
        self.calculateMove(["02", "h", "-1", "1", "F", "W", "YES"], ["02 h", "01 h"])
        self.updateLists("W", "05 c", -1)

        # Move & Update
        self.calculateMove(["NA", "NA", "NA", "NA", "NA", "W", "YES"], ["NA", "NA", "NA", "NA", "NA"])
        self.updateLists("W", "09 h", -1)

        # Move & Update
        self.calculateMove(["09", "h", "-1", "0", "T", "W", "YES"], ["09 h", "10 c", "11 h", "12 s", "13 d"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["08", "c", "6", "0", "T", "T", "YES"], ["02 s", "03 h", "04 c", "05 h", "06 c", "07 d", "08 c", "09 h", "10 c", "11 h", "12 s", "13 d"])
        self.updateLists("T", "13 s", 6)

        # Move & Update
        self.calculateMove(["12", "h", "2", "6", "T", "T", "NO"], ["05 s", "06 h", "07 s", "08 h", "09 s", "10 d", "11 c", "12 h", "13 s"])
        self.updateLists("T", "NA", 6)

        # Move & Update
        self.calculateMove(["13", "s", "6", "2", "T", "T", "YES"], ["05 s", "06 h", "07 s", "08 h", "09 s", "10 d", "11 c", "12 h", "13 s"])
        self.updateLists("T", "12 d", 6)

        # Move & Update
        self.calculateMove(["11", "s", "5", "6", "T", "T", "YES"], ["11 s", "12 d"])
        self.updateLists("T", "01 s", 5)

        # Move & Update
        self.calculateMove(["01", "s", "5", "2", "F", "T", "YES"], ["01 s"])
        self.updateLists("T", "01 c", 5)

        # Move & Update
        self.calculateMove(["02", "s", "0", "2", "F", "T", "NO"], ["02 s", "01 s"])
        self.updateLists("T", "NA", 0)

        # Move & Update
        self.calculateMove(["03", "h", "0", "1", "F", "T", "NO"], ["03 h", "02 h", "01 h"])
        self.updateLists("T", "NA", 0)

        # Move & Update
        self.calculateMove(["01", "c", "5", "3", "F", "T", "YES"], ["01 c"])
        self.updateLists("T", "10 s", 5)

        # Move & Update
        self.calculateMove(["10", "s", "5", "4", "T", "T", "NO"], ["10 s", "11 d", "12 c", "13 h"])
        self.updateLists("W", "09 c", -1)

        # Move & Update
        self.calculateMove(["NA", "NA", "NA", "NA", "NA", "W", "YES"], ["NA", "NA", "NA", "NA", "NA"])
        self.updateLists("W", "03 s", -1)

        # Move & Update
        self.calculateMove(["03", "s", "-1", "2", "F", "W", "YES"], ["03 s", "02 s", "01 s"])
        self.updateLists("W", "02 c", -1)

        # Move & Update
        self.calculateMove(["02", "c", "-1", "3", "F", "W", "YES"], ["02 c", "01 c"])
        self.updateLists("W", "04 s", -1)

        # Move & Update
        self.calculateMove(["04", "s", "-1", "2", "F", "W", "NO"], ["04 s", "03 s", "02 s", "01 s"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["05", "s", "2", "2", "F", "T", "NO"], ["05 s", "04 s", "03 s", "02 s", "01 s"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["NA", "NA", "NA", "NA", "NA", "W", "NO"], ["NA", "NA", "NA", "NA", "NA"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["09", "d", "-1", "4", "T", "W", "NO"], ["09 d", "10 s", "11 d", "12 c", "13 h"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["NA", "NA", "NA", "NA", "NA", "W", "NO"], ["NA", "NA", "NA", "NA", "NA"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["NA", "NA", "NA", "NA", "NA", "W", "NO"], ["NA", "NA", "NA", "NA", "NA"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["06", "s", "-1", "2", "F", "W", "NO"], ["06 s", "05 s", "04 s", "03 s", "02 s", "01 s"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["NA", "NA", "NA", "NA", "NA", "W", "NO"], ["NA", "NA", "NA", "NA", "NA"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["13", "c", "-1", "3", "T", "W", "NO"], ["13 c"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["12", "d", "6", "3", "T", "T", "YES"], ["11 s", "12 d", "13 c"])
        self.updateLists("T", "04 h", 6)

        # Move & Update
        self.calculateMove(["04", "h", "6", "1", "F", "T", "YES"], ["04 h", "03 h", "02 h", "01 h"])
        self.updateLists("T", "10 h", 6)

        # Move & Update
        self.calculateMove(["10", "h", "6", "3", "T", "T", "YES"], ["10 h", "11 s", "12 d", "13 c"])
        self.updateLists("T", "03 c", 6)

        # Move & Update
        self.calculateMove(["03", "c", "6", "3", "F", "T", "YES"], ["03 c", "02 c", "01 c"])
        self.updateLists("T", "06 d", 6)

        # Move & Update
        self.calculateMove(["04", "c", "0", "3", "F", "T", "NO"], ["04 c", "03 c", "02 c", "01 c"])
        self.updateLists("T", "NA", 6)

        # Move & Update
        self.calculateMove(["05", "h", "0", "1", "F", "T", "NO"], ["05 h", "04 h", "03 h", "02 h", "01 h"])
        self.updateLists("T", "NA", 0)

        # Move & Update
        self.calculateMove(["06", "h", "2", "1", "F", "T", "NO"], ["06 h", "05 h", "04 h", "03 h", "02 h", "01 h"])
        self.updateLists("T", "NA", 2)

        # Move & Update
        self.calculateMove(["07", "h", "1", "1", "F", "T", "NO"], ["07 h", "06 h", "05 h", "04 h", "03 h", "02 h", "01 h"])
        self.updateLists("T", "NA", 1)

        # Move & Update
        self.calculateMove(["07", "s", "2", "2", "F", "T", "NO"], ["07 s", "06 s", "05 s", "04 s", "03 s", "02 s", "01 s"])
        self.updateLists("T", "NA", 2)

        # Move & Update
        self.calculateMove(["08", "h", "2", "1", "F", "T", "NO"],
                           ["08 h", "07 h", "06 h", "05 h", "04 h", "03 h", "02 h", "01 h"])
        self.updateLists("T", "NA", 1)

        # Move & Update
        self.calculateMove(["06", "d", "6", "0", "F", "T", "NO"], ["06 d", "05 d", "04 d", "03 d", "02 d", "01 d"])
        self.updateLists("T", "NA", 6)

        # Move & Update
        self.calculateMove(["08", "d", "-1", "2", "T", "W", "NO"], ["08 d", "09 s", "10 d", "11 c", "12 h", "13 s"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["NA", "NA", "NA", "NA", "NA", "W", "NO"], ["NA", "NA", "NA", "NA", "NA"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["08", "s", "-1", "2", "F", "W", "NO"], ["08 s", "07 s", "06 s", "05 s", "04 s", "03 s", "02 s", "01 s"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["NA", "NA", "NA", "NA", "NA", "W", "NO"], ["NA", "NA", "NA", "NA", "NA"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["07", "c", "-1", "2", "T", "W", "NO"], ["07 c", "08 d", "09 s", "10 d", "11 c", "12 h", "13 s"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["NA", "NA", "NA", "NA", "NA", "W", "NO"], ["NA", "NA", "NA", "NA", "NA"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["05", "c", "-1", "3", "F", "W", "NO"],
                           ["05 c", "04 c", "03 c", "02 c", "01 c"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["06", "c", "0", "3", "F", "T", "NO"],
                           ["06 c", "05 c", "04 c", "03 c", "02 c", "01 c"])
        self.updateLists("T", "NA", 0)

        # Move & Update
        self.calculateMove(["07", "d", "0", "0", "F", "T", "NO"],
                           ["07 d", "06 d", "05 d", "04 d", "03 d", "02 d", "01 d"])
        self.updateLists("T", "NA", 0)

        # Move & Update
        self.calculateMove(["07", "c", "2", "3", "F", "T", "NO"],
                           ["07 c", "06 c", "05 c", "04 c", "03 c", "02 c", "01 c"])
        self.updateLists("T", "NA", 2)

        # Move & Update
        self.calculateMove(["08", "c", "0", "3", "F", "T", "NO"],
                           ["08 c", "07 c", "06 c", "05 c", "04 c", "03 c", "02 c", "01 c"])
        self.updateLists("T", "NA", 0)

        # Move & Update
        self.calculateMove(["09", "h", "0", "1", "F", "T", "NO"],
                           ["09 h", "08 h", "07 h", "06 h", "05 h", "04 h", "03 h", "02 h", "01 h"])
        self.updateLists("T", "NA", 0)

        # Move & Update
        self.calculateMove(["08", "d", "2", "0", "F", "T", "NO"],
                           ["08 d", "07 d", "06 d", "05 d", "04 d", "03 d", "02 d", "01 d"])
        self.updateLists("T", "NA", 2)

        # Move & Update
        self.calculateMove(["09", "s", "2", "2", "F", "T", "NO"],
                           ["09 s", "08 s", "07 s", "06 s", "05 s", "04 s", "03 s", "02 s", "01 s"])
        self.updateLists("T", "NA", 2)

        # Move & Update
        self.calculateMove(["10", "h", "3", "1", "F", "T", "NO"],
                           ["10 h", "09 h", "08 h", "07 h", "06 h", "05 h", "04 h", "03 h", "02 h", "01 h"])
        self.updateLists("T", "NA", 3)

        # Move & Update
        self.calculateMove(["09", "d", "4", "0", "F", "T", "NO"],
                           ["09 d", "08 d", "07 d", "06 d", "05 d", "04 d", "03 d", "02 d", "01 d"])
        self.updateLists("T", "NA", 4)

        # Move & Update
        self.calculateMove(["10", "d", "2", "0", "F", "T", "NO"],
                           ["10 d", "09 d", "08 d", "07 d", "06 d", "05 d", "04 d", "03 d", "02 d", "01 d"])
        self.updateLists("T", "NA", 2)

        # Move & Update
        self.calculateMove(["10", "s", "4", "2", "F", "T", "NO"],
                           ["10 s", "09 s", "08 s", "07 s", "06 s", "05 s", "04 s", "03 s", "02 s", "01 s"])
        self.updateLists("T", "NA", 4)

        # Move & Update
        self.calculateMove(["11", "s", "3", "2", "F", "T", "NO"],
                           ["11 s", "10 s", "09 s", "08 s", "07 s", "06 s", "05 s", "04 s", "03 s", "02 s", "01 s"])
        self.updateLists("T", "NA", 3)

        # Move & Update
        self.calculateMove(["11", "d", "4", "0", "F", "T", "NO"],
                           ["11 d", "10 d", "09 d", "08 d", "07 d", "06 d", "05 d", "04 d", "03 d", "02 d", "01 d"])
        self.updateLists("T", "NA", 4)

        # Move & Update
        self.calculateMove(["12", "d", "3", "0", "F", "T", "NO"],
                           ["12 d", "11 d", "10 d", "09 d", "08 d", "07 d", "06 d", "05 d", "04 d", "03 d", "02 d", "01 d"])
        self.updateLists("T", "NA", 3)

        # Move & Update
        self.calculateMove(["NA", "NA", "NA", "NA", "NA", "W", "NO"], ["NA", "NA", "NA", "NA", "NA"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["09", "c", "-1", "3", "F", "W", "NO"],
                           ["09 c", "08 c", "07 c", "06 c", "05 c", "04 c", "03 c", "02 c", "01 c"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["10", "c", "0", "3", "F", "T", "NO"],
                           ["10 c", "09 c", "08 c", "07 c", "06 c", "05 c", "04 c", "03 c", "02 c", "01 c"])
        self.updateLists("T", "NA", 0)

        # Move & Update
        self.calculateMove(["11", "h", "0", "1", "F", "T", "NO"],
                           ["11 h", "10 h", "09 h", "08 h", "07 h", "06 h", "05 h", "04 h", "03 h", "02 h", "01 h"])
        self.updateLists("T", "NA", 0)

        # Move & Update
        self.calculateMove(["12", "s", "0", "2", "F", "T", "NO"],
                           ["12 s", "11 s", "10 s", "09 s", "08 s", "07 s", "06 s", "05 s", "04 s", "03 s", "02 s", "01 s"])
        self.updateLists("T", "NA", 0)

        # Move & Update
        self.calculateMove(["13", "d", "0", "0", "F", "T", "NO"],
                           ["13 d", "12 d", "11 d", "10 d", "09 d", "08 d", "07 d", "06 d", "05 d", "04 d", "03 d", "02 d",
                            "01 d"])
        self.updateLists("T", "NA", 0)

        # Move & Update
        self.calculateMove(["11", "c", "2", "3", "F", "T", "NO"],
                           ["11 c", "10 c", "09 c", "08 c", "07 c", "06 c", "05 c", "04 c", "03 c", "02 c", "01 c"])
        self.updateLists("T", "NA", 2)

        # Move & Update
        self.calculateMove(["12", "h", "2", "1", "F", "T", "NO"],
                            ["12 h", "11 h", "10 h", "09 h", "08 h", "07 h", "06 h", "05 h", "04 h", "03 h", "02 h", "01 h"])
        self.updateLists("T", "NA", 2)

        # Move & Update
        self.calculateMove(["13", "s", "2", "2", "F", "T", "NO"],
                           ["13 s", "12 s", "11 s", "10 s", "09 s", "08 s", "07 s", "06 s", "05 s", "04 s", "03 s", "02 s", "01 s"])
        self.updateLists("T", "NA", 3)

        # Move & Update
        self.calculateMove(["12", "c", "4", "3", "F", "T", "NO"],
                           ["12 c", "11 c", "10 c", "09 c", "08 c", "07 c", "06 c", "05 c", "04 c", "03 c", "02 c", "01 c"])
        self.updateLists("T", "NA", 4)

        # Move & Update
        self.calculateMove(["13", "c", "3", "3", "F", "T", "NO"],
                           ["13 c", "12 c", "11 c", "10 c", "09 c", "08 c", "07 c", "06 c", "05 c", "04 c", "03 c", "02 c", "01 c"])
        self.updateLists("T", "NA", 3)

        # Move & Update
        self.calculateMove(["13", "h", "4", "1", "F", "T", "NO"],
                           ["13 h", "12 h", "11 h", "10 h", "09 h", "08 h", "07 h", "06 h", "05 h", "04 h", "03 h", "02 h", "01 h"])
        self.updateLists("T", "NA", 4)

        self.calculateMove(["WIN", "WIN", "WIN", "WIN", "WIN", "WIN", "WIN"],
                           ["NA", "NA", "NA", "NA", "NA"])

    def calculateMove(self, trueMove, trueResult):
        move = self.gl.calculate_move()
        # Calculates the move
        self.assertListEqual(move, trueMove)
        # Updates the logic with regards to the move made
        self.assertListEqual(self.gl.update_logic_move(move), trueResult)

    def updateLists(self, whereTo, card, index):
        if whereTo == "T":
            taaa = (copy.deepcopy(self.gl.logicTableauCardPiles))
            if card != "NA":
                taaa.get(index).append(card)
                if index == 0:
                    tb = create_list([card], [], [], [], [], [], [])
                if index == 1:
                    tb = create_list([], [card], [], [], [], [], [])
                if index == 2:
                    tb = create_list([], [], [card], [], [], [], [])
                if index == 3:
                    tb = create_list([], [], [], [card], [], [], [])
                if index == 4:
                    tb = create_list([], [], [], [], [card], [], [])
                if index == 5:
                    tb = create_list([], [], [], [], [], [card], [])
                if index == 6:
                    tb = create_list([], [], [], [], [], [], [card])
            else:
                tb = create_list([], [], [], [], [], [], [])
            _, taa, _ = self.gl.update_logic_scan(None, tb, None)
            self.assertDictEqual(taa, taaa)
        if whereTo == "W":
            waaa = (copy.deepcopy(self.gl.logicWasteCardPile))
            if card != "NA":
                if card not in waaa:
                    waaa.append(card)
                wa = card
            else:
                wa = None
            waa, _, _ = self.gl.update_logic_scan(wa, None, None)
            self.assertListEqual(waa, waaa)

    def test_updateR_logic(self):
        self.insertVariables(0)

        testWas, testTab, testFou = self.gl.update_logic_scan([[]], self.createDummyList(0), self.createDummyList(-1))
        self.assertListEqual(testWas, [[]])
        self.assertDictEqual(testTab, self.logicTableauCardPiles)
        self.assertDictEqual(testFou, self.logicFoundationCardPiles)

        testWas, testTab, testFou = self.gl.update_logic_scan([["1", "h"], ["2", "c"]], self.createDummyList(0),
                                                              self.createDummyList(-1))
        self.assertListEqual(testWas, [[], ["1", "h"], ["2", "c"]])
        self.assertDictEqual(testTab, self.logicTableauCardPiles)
        self.assertDictEqual(testFou, self.logicFoundationCardPiles)

    def test_check_list_consistency(self):
        self.insertVariables()
        empytyList = self.createDummyList(0)
        dummyList = self.createDummyList(1)
        testList = self.createDummyList(2)
        resultTest = testList.copy()
        resultTest[2] = ["2 d"]

        self.assertDictEqual(self.gl.check_list_consistency(dummyList, testList), resultTest)
        self.assertDictEqual(self.gl.check_list_consistency(empytyList, self.createDummyList(1)), dummyList)

    def test_reset_logic(self):
        self.insertVariables()

        testWas, testTab, testFou = self.gl.reset_logic(None, None, None)

        self.assertIsNone(testWas)
        self.assertIsNone(testTab)
        self.assertIsNone(testFou)

        testWas, testTab, testFou = self.gl.reset_logic([""], {0: ["a", "b", "c"], 1: ["a"]},
                                                        {0: ["d", "e", "c"], 1: ["c"]})

        self.assertListEqual(testWas, [""])
        self.assertDictEqual(testTab, {0: ["a", "b", "c"], 1: ["a"]})
        self.assertDictEqual(testFou, {0: ["d", "e", "c"], 1: ["c"]})

    def test_calculate_move(self):
        self.insertVariables(1)

        self.gl.calculate_move()

        self.assertListEqual(self.gl.calculate_move(), ["5", "h", "2", "0", "T", "T", "YES"])
        self.gl.update_logic_move(self.gl.calculate_move())
        self.assertListEqual(self.gl.calculate_move(), ["1", "s", "4", "0", "F", "T", "YES"])
        self.gl.update_logic_move(self.gl.calculate_move())
        self.assertListEqual(self.gl.calculate_move(), ["13", "s", "5", "2", "T", "T", "YES"])
        self.gl.update_logic_move(self.gl.calculate_move())
        self.assertListEqual(self.gl.calculate_move(), ["3", "h", "6", "2", "F", "T", "YES"])
        self.gl.update_logic_move(self.gl.calculate_move())
        self.assertListEqual(self.gl.calculate_move(), ["1", "d", "-1", "1", "F", "W", "YES"])
        self.gl.update_logic_move(self.gl.calculate_move())
        self.gl.logicTableauCardPiles.get(5).clear()
        self.gl.logicTableauCardPiles.get(5).append("4 h")
        self.assertListEqual(self.gl.calculate_move(), ["4", "h", "5", "2", "F", "T", "YES"])
        self.gl.update_logic_move(self.gl.calculate_move())
        self.gl.logicWasteCardPile = [["12", "d"]]
        self.assertListEqual(self.gl.calculate_move(), ["12", "d", "-1", "2", "T", "W", "YES"])
        self.gl.update_logic_move(self.gl.calculate_move())
        self.gl.logicFoundationCardPiles.clear()
        self.gl.logicFoundationCardPiles = {0: [], 1: [], 2: ["2 c"], 3: []}
        self.assertListEqual(self.gl.calculate_move(), ["11", "s", "1", "2", "T", "T", "YES"])
        self.gl.update_logic_move(self.gl.calculate_move())
        # SHOULD BE ERROR, PLS FIX
        self.assertListEqual(self.gl.calculate_move(), ["12", "d", "2", "3", "T", "T", "NO"])

    def test_updateM_logic(self):
        self.insertVariables()

        self.assertListEqual(self.gl.update_logic_move(["05", "h", "2", "0", "T", "T", "NO"]),
                             ["04 s", "05 h", "06 c", "07 d", "08 s"])
        self.assertListEqual(self.gl.update_logic_move(self.gl.calculate_move()), ["01 s"])
        self.assertListEqual(self.gl.update_logic_move(self.gl.calculate_move()), ["13 s"])
        self.gl.logicTableauCardPiles.get(5).clear()
        self.gl.logicTableauCardPiles.get(5).append("04 h")
        self.assertListEqual(self.gl.update_logic_move(self.gl.calculate_move()), ["03 h", "02 h", "01 h"])
        self.assertListEqual(self.gl.update_logic_move(self.gl.calculate_move()), ["04 h", "03 h", "02 h", "01 h"])
        self.assertListEqual(self.gl.update_logic_move(self.gl.calculate_move()), ["01 d"])
        self.gl.logicWasteCardPile.append(["12", "d"])
        self.assertListEqual(self.gl.update_logic_move(["12", "d", "-1", "3", "T", "W", "YES"]), ["12 d", "13 c"])
        self.gl.logicWasteCardPile.append(["11", "c"])
        self.assertListEqual(self.gl.update_logic_move(self.gl.calculate_move()), ["11 s", "12 d", "13 c"])
        self.gl.logicTableauCardPiles.get(2).append("12 h")
        self.assertListEqual(self.gl.update_logic_move(["12", "h", "2", "4", "T", "T", "NO"]), ["12 h", "13 s"])
        self.assertListEqual(self.gl.update_logic_move(self.gl.calculate_move()), ["11 c", "12 h", "13 s"])
        self.assertListEqual(self.gl.update_logic_move(self.gl.calculate_move()), ["NA", "NA", "NA", "NA", "NA"])

    def test_check_card_placement(self):
        self.insertVariables()

        self.assertTrue(self.gl.check_card_placement(-1, 5, "d", 0, 6, "c", False))
        self.assertTrue(self.gl.check_card_placement(-1, 13, "c", 3, -1, "-1", False))
        self.assertTrue(self.gl.check_card_placement(6, 3, "h", 2, -1, "-1", False))
        self.assertFalse(self.gl.check_card_placement(6, 4, "h", 1, -1, "-1", False))
        self.assertFalse(self.gl.check_card_placement(3, 11, "s", 5, 10, "s", False))
        self.assertTrue(self.gl.check_card_placement(3, 11, "s", 5, 12, "d", False))
        self.assertFalse(self.gl.check_card_placement(2, 7, "d", 1, 8, "d", False))
        self.assertFalse(self.gl.check_card_placement(2, 7, "d", 1, 7, "d", False))

    def test_check_foundation_card_pile(self):
        self.insertVariables(0)

        self.assertEqual(self.gl.check_foundation_card_pile(3, "h"), 2)
        self.assertEqual(self.gl.check_foundation_card_pile(1, "s"), 0)
        self.assertEqual(self.gl.check_foundation_card_pile(6, "s"), -1)
        self.assertEqual(self.gl.check_foundation_card_pile(3, "c"), -1)

    def insertVariables(self, testNumber=0):
        self.logicWasteCard = []
        self.logicWasteCard.append("01 d")

        list0 = []
        list00 = []
        list000 = []
        list0000 = []

        if testNumber == 0:
            list000.append("02 h")
            list000.append("01 h")

        list1 = []
        list11 = []
        list111 = []
        list1111 = []
        list11111 = []
        list111111 = []
        list1111111 = []

        if testNumber == 0:
            list1.append("06 c")
            list1.append("07 d")
            list1.append("08 s")
            list11.append("11 s")
            list111.append("04 s")
            list111.append("05 h")
            list1111.append("13 c")
            list11111.append("01 s")
            list111111.append("13 s")
            list111111.append("12 unknown")
            list1111111.append("03 h")
        if testNumber == 1:
            list1.append("06 c")
            list11.append("11 s")
            list111.append("04 s")
            list1111.append("13 c")
            list11111.append("01 s")
            list111111.append("13 s")
            list1111111.append("03 h")

        if testNumber == 2:
            list1.append("13 h")
            list111.append("13 s")

        self.logicTableauCardPiles = {0: list1, 1: list11, 2: list111, 3: list1111, 4: list11111, 5: list111111,
                                      6: list1111111}
        self.logicFoundationCardPiles = {0: list0, 1: list00, 2: list000, 3: list0000}

        self.gl = GameLogic.GameLogic(self.logicWasteCard, self.logicTableauCardPiles, self.logicFoundationCardPiles)
