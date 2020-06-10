from unittest import TestCase

from src import GameLogic


class TestGameLogic(TestCase):

    def insertVariables(self):
        self.logicWasteCard = []
        self.logicWasteCard.append("1")
        self.logicWasteCard.append("r")

        list0 = []
        list00 = []
        list000 = []
        list0000 = []

        list000.append("2 h")
        list000.append("1 h")

        list1 = []
        list11 = []
        list111 = []
        list1111 = []
        list11111 = []
        list111111 = []
        list1111111 = []

        list1.append("6 k")
        list1.append("7 r")
        list1.append("8 s")
        list11.append("11 s")
        list111.append("4 s")
        list111.append("5 h")
        list1111.append("13 k")
        list11111.append("1 s")
        list111111.append("13 s")
        list111111.append("12 unknown")
        list1111111.append("3 h")

        self.logicTableauCardPiles = {0: list1, 1: list11, 2: list111, 3: list1111, 4: list11111, 5: list111111,
                                      6: list1111111}
        self.logicFoundationCardPiles = {0: list0, 1: list00, 2: list000, 3: list0000}

        self.gl = GameLogic.GameLogic(self.logicWasteCard, self.logicTableauCardPiles, self.logicFoundationCardPiles)

    def test_updateR_logic(self):
        self.fail()

    def test_check_list_consistency(self):
        self.fail()

    def test_reset_logic(self):
        self.insertVariables()

        testWas, testTab, testFou = self.gl.resetLogic(None, None, None)

        self.assertIsNone(testWas)
        self.assertIsNone(testTab)
        self.assertIsNone(testFou)

        testWas, testTab, testFou = self.gl.resetLogic([""], {0: ["a", "b", "c"], 1: ["a"]}, {0: ["d", "e", "c"], 1: ["k"]})

        self.assertListEqual(testWas, [""])
        self.assertDictEqual(testTab, {0: ["a", "b", "c"], 1: ["a"]})
        self.assertDictEqual(testFou, {0: ["d", "e", "c"], 1: ["k"]})

    def test_calculate_move(self):
        self.insertVariables()

        self.assertListEqual(self.gl.calculateMove(), ["5", "h", "2", "0", "T"])
        self.gl.updateLogicM(self.gl.calculateMove())
        self.assertListEqual(self.gl.calculateMove(), ["1", "s", "4", "0", "F"])
        self.gl.updateLogicM(self.gl.calculateMove())
        self.assertListEqual(self.gl.calculateMove(), ["13", "s", "5", "2", "T"])
        self.gl.updateLogicM(self.gl.calculateMove())
        self.assertListEqual(self.gl.calculateMove(), ["3", "h", "6", "2", "F"])
        self.gl.updateLogicM(self.gl.calculateMove())
        self.assertListEqual(self.gl.calculateMove(), ["1", "r", "-1", "1", "F"])
        self.gl.updateLogicM(self.gl.calculateMove())
        self.gl.logicTableauCardPiles.get(5).clear()
        self.gl.logicTableauCardPiles.get(5).append("4 h")
        self.assertListEqual(self.gl.calculateMove(), ["4", "h", "5", "2", "F"])
        self.gl.updateLogicM(self.gl.calculateMove())
        self.gl.logicWasteCard = ["12", "r"]
        self.assertListEqual(self.gl.calculateMove(), ["12", "r", "-1", "2", "T"])

    def test_updateM_logic(self):
        self.insertVariables()

        self.assertListEqual(self.gl.updateLogicM(["5", "h", "2", "0", "T"]), ["4 s", "5 h", "6 k", "7 r", "8 s"])
        self.assertListEqual(self.gl.updateLogicM(self.gl.calculateMove()), ["1 s"])
        self.assertListEqual(self.gl.updateLogicM(self.gl.calculateMove()), ["13 s"])
        self.gl.logicTableauCardPiles.get(5).clear()
        self.gl.logicTableauCardPiles.get(5).append("4 h")
        self.assertListEqual(self.gl.updateLogicM(self.gl.calculateMove()), ["3 h", "2 h", "1 h"])
        self.assertListEqual(self.gl.updateLogicM(self.gl.calculateMove()), ["4 h", "3 h", "2 h", "1 h"])
        self.assertListEqual(self.gl.updateLogicM(self.gl.calculateMove()), ["1 r"])
        self.gl.logicWasteCard = ["12", "r"]
        self.assertListEqual(self.gl.updateLogicM(["12", "r", "-1", "3", "T"]), ["12 r", "13 k"])
        self.gl.logicWasteCard = ["11", "k"]
        self.assertListEqual(self.gl.updateLogicM(self.gl.calculateMove()), ["11 s", "12 r", "13 k"])
        self.gl.logicTableauCardPiles.get(2).append("12 h")
        self.assertListEqual(self.gl.updateLogicM(["12", "h", "2", "4", "T"]), ["12 h", "13 s"])
        self.assertListEqual(self.gl.updateLogicM(self.gl.calculateMove()), ["11 k", "12 h", "13 s"])
        self.assertListEqual(self.gl.updateLogicM(self.gl.calculateMove()), ["NA", "NA", "NA", "NA", "NA"])

    def test_check_card_placement(self):
        self.insertVariables()

        self.assertTrue(self.gl.checkCardPlacement(-1, 5, "r", 0, 6, "k", False))
        self.assertTrue(self.gl.checkCardPlacement(-1, 13, "k", 3, -1, "-1", False))
        self.assertTrue(self.gl.checkCardPlacement(6, 3, "h", 2, -1, "-1", False))
        self.assertFalse(self.gl.checkCardPlacement(6, 4, "h", 1, -1, "-1", False))
        self.assertFalse(self.gl.checkCardPlacement(3, 11, "s", 5, 10, "s", False))
        self.assertTrue(self.gl.checkCardPlacement(3, 11, "s", 5, 12, "r", False))
        self.assertFalse(self.gl.checkCardPlacement(2, 7, "r", 1, 8, "r", False))
        self.assertFalse(self.gl.checkCardPlacement(2, 7, "r", 1, 7, "r", False))

    def test_check_foundation_card_pile(self):
        self.insertVariables()

        self.assertEqual(self.gl.checkFoundationCardPile(3, "h"), 2)
        self.assertEqual(self.gl.checkFoundationCardPile(1, "s"), 0)
        self.assertEqual(self.gl.checkFoundationCardPile(6, "s"), -1)
        self.assertEqual(self.gl.checkFoundationCardPile(3, "k"), -1)
