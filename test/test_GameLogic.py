from unittest import TestCase

from Inference import GameLogic

import random
import copy


def insertVariables(self, testNumber=0):
    self.logicWasteCard = [[]]
    self.logicWasteCard[0] = ["1", "d"]

    list0 = []
    list00 = []
    list000 = []
    list0000 = []

    if testNumber == 0:
        list000.append("2 h")
        list000.append("1 h")

    list1 = []
    list11 = []
    list111 = []
    list1111 = []
    list11111 = []
    list111111 = []
    list1111111 = []

    if testNumber == 0:
        list1.append("6 c")
        list1.append("7 d")
        list1.append("8 s")
        list11.append("11 s")
        list111.append("4 s")
        list111.append("5 h")
        list1111.append("13 c")
        list11111.append("1 s")
        list111111.append("13 s")
        list111111.append("12 unknown")
        list1111111.append("3 h")
    else:
        list1.append("6 c")
        list11.append("11 s")
        list111.append("4 s")
        list1111.append("13 c")
        list11111.append("1 s")
        list111111.append("13 s")
        list1111111.append("3 h")

    self.logicTableauCardPiles = {0: list1, 1: list11, 2: list111, 3: list1111, 4: list11111, 5: list111111,
                                  6: list1111111}
    self.logicFoundationCardPiles = {0: list0, 1: list00, 2: list000, 3: list0000}

    self.gl = GameLogic.GameLogic(self.logicWasteCard, self.logicTableauCardPiles, self.logicFoundationCardPiles)


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


def combine_list(tbfalist, card, index):
    if card != "":
        tbfalist.get(index).append(card)
    return tbfalist

class TestGameLogic(TestCase):

    def test_play_game(self):
        tb = create_list(["6 h"], ["6 c"], ["13 d"], ["4 d"], ["3 h"], ["2 s"], ["8 c"])
        fd = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
        wc = [[]]

        gl = GameLogic.GameLogic(wc, tb, fd)

        move = gl.calculateMove()
        self.assertListEqual(move, ["2", "s", "5", "4", "T", "T", "YES"])
        self.assertListEqual(gl.updateLogicM(move), ["2 s", "3 h"])
        taaa = combine_list(copy.deepcopy(gl.logicTableauCardPiles), "4 c", 5)
        tb = create_list([], [], [], [], [], ["4 c"], [])
        _, taa, _ = gl.updateLogicR(None, tb, None)
        self.assertDictEqual(taa, taaa)

        move = gl.calculateMove()
        self.assertListEqual(move, ["3", "h", "4", "5", "T", "T", "YES"])
        self.assertListEqual(gl.updateLogicM(move), ["2 s", "3 h", "4 c"])
        taaa = combine_list(copy.deepcopy(gl.logicTableauCardPiles), "5 s", 4)
        tb = create_list([], [], [], [], ["5 s"], [], [])
        _, taa, _ = gl.updateLogicR(None, tb, None)
        self.assertDictEqual(taa, taaa)

        move = gl.calculateMove()
        self.assertListEqual(move, ["4", "d", "3", "4", "T", "T", "YES"])
        self.assertListEqual(gl.updateLogicM(move), ["4 d", "5 s"])
        taaa = combine_list(copy.deepcopy(gl.logicTableauCardPiles), "12 s", 3)
        tb = create_list([], [], [], ["12 s"], [], [], [])
        _, taa, _ = gl.updateLogicR(None, tb, None)
        self.assertDictEqual(taa, taaa)

        move = gl.calculateMove()
        self.assertListEqual(move, ["12", "s", "3", "2", "T", "T", "YES"])
        self.assertListEqual(gl.updateLogicM(move), ["12 s", "13 d"])
        taaa = combine_list(copy.deepcopy(gl.logicTableauCardPiles), "12 k", 3)
        tb = create_list([], [], [], ["12 k"], [], [], [])
        _, taa, _ = gl.updateLogicR(None, tb, None)
        self.assertDictEqual(taa, taaa)

        move = gl.calculateMove()
        self.assertListEqual(move, ["5", "s", "4", "0", "T", "T", "YES"])
        self.assertListEqual(gl.updateLogicM(move), ["4 d", "5 s", "6 h"])
        taaa = combine_list(copy.deepcopy(gl.logicTableauCardPiles), "7 s", 4)
        tb = create_list([], [], [], [], ["7 s"], [], [])
        _, taa, _ = gl.updateLogicR(None, tb, None)
        self.assertDictEqual(taa, taaa)

        move = gl.calculateMove()
        self.assertListEqual(move, ["6", "h", "0", "4", "T", "T", "NO"])
        self.assertListEqual(gl.updateLogicM(move), ["4 d", "5 s", "6 h", "7 s"])
        taaa = combine_list(copy.deepcopy(gl.logicTableauCardPiles), "", 0)
        tb = create_list([], [], [], [], [], [], [])
        _, taa, _ = gl.updateLogicR(None, tb, None)
        self.assertDictEqual(taa, taaa)

        move = gl.calculateMove()
        self.assertListEqual(move, ["13", "d", "2", "0", "T", "T", "YES"])
        self.assertListEqual(gl.updateLogicM(move), ["12 s", "13 d"])
        taaa = combine_list(copy.deepcopy(gl.logicTableauCardPiles), "3 d", 2)
        tb = create_list([], [], ["3 d"], [], [], [], [])
        _, taa, _ = gl.updateLogicR(None, tb, None)
        self.assertDictEqual(taa, taaa)

        move = gl.calculateMove()
        self.assertListEqual(move, ["NA", "NA", "NA", "NA", "NA"])


    def test_updateR_logic(self):
        self.insertVariables(0)

        testWas, testTab, testFou = self.gl.updateLogicR([[]], self.createDummyList(0), self.createDummyList(-1))
        self.assertListEqual(testWas, [[]])
        self.assertDictEqual(testTab, self.logicTableauCardPiles)
        self.assertDictEqual(testFou, self.logicFoundationCardPiles)

        testWas, testTab, testFou = self.gl.updateLogicR([["1", "h"], ["2", "c"]], self.createDummyList(0),
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

        self.assertDictEqual(self.gl.checkListConsistency(dummyList, testList), resultTest)
        self.assertDictEqual(self.gl.checkListConsistency(empytyList, self.createDummyList(1)), dummyList)

    def test_reset_logic(self):
        self.insertVariables()

        testWas, testTab, testFou = self.gl.resetLogic(None, None, None)

        self.assertIsNone(testWas)
        self.assertIsNone(testTab)
        self.assertIsNone(testFou)

        testWas, testTab, testFou = self.gl.resetLogic([""], {0: ["a", "b", "c"], 1: ["a"]},
                                                       {0: ["d", "e", "c"], 1: ["c"]})

        self.assertListEqual(testWas, [""])
        self.assertDictEqual(testTab, {0: ["a", "b", "c"], 1: ["a"]})
        self.assertDictEqual(testFou, {0: ["d", "e", "c"], 1: ["c"]})

    def test_calculate_move(self):
        self.insertVariables(0)

        self.assertListEqual(self.gl.calculateMove(), ["5", "h", "2", "0", "T", "T", "YES"])
        self.gl.updateLogicM(self.gl.calculateMove())
        self.assertListEqual(self.gl.calculateMove(), ["1", "s", "4", "0", "F", "T", "YES"])
        self.gl.updateLogicM(self.gl.calculateMove())
        self.assertListEqual(self.gl.calculateMove(), ["13", "s", "5", "2", "T", "T", "YES"])
        self.gl.updateLogicM(self.gl.calculateMove())
        self.assertListEqual(self.gl.calculateMove(), ["3", "h", "6", "2", "F", "T", "YES"])
        self.gl.updateLogicM(self.gl.calculateMove())
        self.assertListEqual(self.gl.calculateMove(), ["1", "d", "-1", "1", "F", "W", "YES"])
        self.gl.updateLogicM(self.gl.calculateMove())
        self.gl.logicTableauCardPiles.get(5).clear()
        self.gl.logicTableauCardPiles.get(5).append("4 h")
        self.assertListEqual(self.gl.calculateMove(), ["4", "h", "5", "2", "F", "T", "YES"])
        self.gl.updateLogicM(self.gl.calculateMove())
        self.gl.logicWasteCard = [["12", "d"]]
        self.assertListEqual(self.gl.calculateMove(), ["12", "d", "-1", "2", "T", "W", "YES"])
        self.gl.updateLogicM(self.gl.calculateMove())
        self.gl.logicFoundationCardPiles.clear()
        self.gl.logicFoundationCardPiles = {0: [], 1: [], 2: ["2 c"], 3: []}
        self.assertListEqual(self.gl.calculateMove(), ["11", "s", "1", "2", "T", "T", "YES"])
        self.gl.updateLogicM(self.gl.calculateMove())
        # SHOULD BE ERROR, PLS FIX
        self.assertListEqual(self.gl.calculateMove(), ["12", "d", "2", "3", "T", "T", "NO"])

    def test_updateM_logic(self):
        self.insertVariables()

        self.assertListEqual(self.gl.updateLogicM(["5", "h", "2", "0", "T", "T", "NO"]),
                             ["4 s", "5 h", "6 c", "7 d", "8 s"])
        self.assertListEqual(self.gl.updateLogicM(self.gl.calculateMove()), ["1 s"])
        self.assertListEqual(self.gl.updateLogicM(self.gl.calculateMove()), ["13 s"])
        self.gl.logicTableauCardPiles.get(5).clear()
        self.gl.logicTableauCardPiles.get(5).append("4 h")
        self.assertListEqual(self.gl.updateLogicM(self.gl.calculateMove()), ["3 h", "2 h", "1 h"])
        self.assertListEqual(self.gl.updateLogicM(self.gl.calculateMove()), ["4 h", "3 h", "2 h", "1 h"])
        self.assertListEqual(self.gl.updateLogicM(self.gl.calculateMove()), ["1 d"])
        self.gl.logicWasteCard.append(["12", "d"])
        self.assertListEqual(self.gl.updateLogicM(["12", "d", "-1", "3", "T", "W", "YES"]), ["12 d", "13 c"])
        self.gl.logicWasteCard.append(["11", "c"])
        self.assertListEqual(self.gl.updateLogicM(self.gl.calculateMove()), ["11 s", "12 d", "13 c"])
        self.gl.logicTableauCardPiles.get(2).append("12 h")
        self.assertListEqual(self.gl.updateLogicM(["12", "h", "2", "4", "T", "T", "NO"]), ["12 h", "13 s"])
        self.assertListEqual(self.gl.updateLogicM(self.gl.calculateMove()), ["11 c", "12 h", "13 s"])
        self.assertListEqual(self.gl.updateLogicM(self.gl.calculateMove()), ["NA", "NA", "NA", "NA", "NA"])

    def test_check_card_placement(self):
        self.insertVariables()

        self.assertTrue(self.gl.checkCardPlacement(-1, 5, "d", 0, 6, "c", False))
        self.assertTrue(self.gl.checkCardPlacement(-1, 13, "c", 3, -1, "-1", False))
        self.assertTrue(self.gl.checkCardPlacement(6, 3, "h", 2, -1, "-1", False))
        self.assertFalse(self.gl.checkCardPlacement(6, 4, "h", 1, -1, "-1", False))
        self.assertFalse(self.gl.checkCardPlacement(3, 11, "s", 5, 10, "s", False))
        self.assertTrue(self.gl.checkCardPlacement(3, 11, "s", 5, 12, "d", False))
        self.assertFalse(self.gl.checkCardPlacement(2, 7, "d", 1, 8, "d", False))
        self.assertFalse(self.gl.checkCardPlacement(2, 7, "d", 1, 7, "d", False))

    def test_check_foundation_card_pile(self):
        self.insertVariables(0)

        self.assertEqual(self.gl.checkFoundationCardPile(3, "h"), 2)
        self.assertEqual(self.gl.checkFoundationCardPile(1, "s"), 0)
        self.assertEqual(self.gl.checkFoundationCardPile(6, "s"), -1)
        self.assertEqual(self.gl.checkFoundationCardPile(3, "c"), -1)
