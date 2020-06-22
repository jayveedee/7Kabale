from unittest import TestCase

from Inference import GameLogic

import random
import copy


class TestGameLogic(TestCase):

    # TC00 - Test Case (Spil et spil færdigt)
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
        self.calculateMove(["07", "s", "4", "2", "T", "T", "YES"],
                           ["05 s", "06 h", "07 s", "08 h", "09 s", "10 d", "11 c", "12 h"])
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
        self.calculateMove(["06", "c", "1", "6", "T", "T", "YES"],
                           ["02 s", "03 h", "04 c", "05 h", "06 c", "07 d", "08 c"])
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
        self.calculateMove(["08", "c", "6", "0", "T", "T", "YES"],
                           ["02 s", "03 h", "04 c", "05 h", "06 c", "07 d", "08 c", "09 h", "10 c", "11 h", "12 s",
                            "13 d"])
        self.updateLists("T", "13 s", 6)

        # Move & Update
        self.calculateMove(["12", "h", "2", "6", "T", "T", "NO"],
                           ["05 s", "06 h", "07 s", "08 h", "09 s", "10 d", "11 c", "12 h", "13 s"])
        self.updateLists("T", "NA", 6)

        # Move & Update
        self.calculateMove(["13", "s", "6", "2", "T", "T", "YES"],
                           ["05 s", "06 h", "07 s", "08 h", "09 s", "10 d", "11 c", "12 h", "13 s"])
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
        self.calculateMove(["07", "h", "1", "1", "F", "T", "NO"],
                           ["07 h", "06 h", "05 h", "04 h", "03 h", "02 h", "01 h"])
        self.updateLists("T", "NA", 1)

        # Move & Update
        self.calculateMove(["07", "s", "2", "2", "F", "T", "NO"],
                           ["07 s", "06 s", "05 s", "04 s", "03 s", "02 s", "01 s"])
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
        self.calculateMove(["08", "s", "-1", "2", "F", "W", "NO"],
                           ["08 s", "07 s", "06 s", "05 s", "04 s", "03 s", "02 s", "01 s"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["NA", "NA", "NA", "NA", "NA", "W", "NO"], ["NA", "NA", "NA", "NA", "NA"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["07", "c", "-1", "2", "T", "W", "NO"],
                           ["07 c", "08 d", "09 s", "10 d", "11 c", "12 h", "13 s"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["NA", "NA", "NA", "NA", "NA", "W", "NO"], ["NA", "NA", "NA", "NA", "NA"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["05", "c", "-1", "3", "F", "W", "NO"],
                           ["05 c", "04 c", "03 c", "02 c", "01 c"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["06", "c", "0", "3", "F", "T", "TOPCARD"],
                           ["06 c", "05 c", "04 c", "03 c", "02 c", "01 c"])
        self.updateLists("T", "NA", 0)

        # Move & Update
        self.calculateMove(["07", "d", "0", "0", "F", "T", "TOPCARD"],
                           ["07 d", "06 d", "05 d", "04 d", "03 d", "02 d", "01 d"])
        self.updateLists("T", "NA", 0)

        # Move & Update
        self.calculateMove(["07", "c", "2", "3", "F", "T", "TOPCARD"],
                           ["07 c", "06 c", "05 c", "04 c", "03 c", "02 c", "01 c"])
        self.updateLists("T", "NA", 2)

        # Move & Update
        self.calculateMove(["08", "c", "0", "3", "F", "T", "TOPCARD"],
                           ["08 c", "07 c", "06 c", "05 c", "04 c", "03 c", "02 c", "01 c"])
        self.updateLists("T", "NA", 0)

        # Move & Update
        self.calculateMove(["09", "h", "0", "1", "F", "T", "TOPCARD"],
                           ["09 h", "08 h", "07 h", "06 h", "05 h", "04 h", "03 h", "02 h", "01 h"])
        self.updateLists("T", "NA", 0)

        # Move & Update
        self.calculateMove(["08", "d", "2", "0", "F", "T", "NO"],
                           ["08 d", "07 d", "06 d", "05 d", "04 d", "03 d", "02 d", "01 d"])
        self.updateLists("T", "NA", 2)

        # Move & Update
        self.calculateMove(["09", "s", "2", "2", "F", "T", "TOPCARD"],
                           ["09 s", "08 s", "07 s", "06 s", "05 s", "04 s", "03 s", "02 s", "01 s"])
        self.updateLists("T", "NA", 2)

        # Move & Update
        self.calculateMove(["10", "h", "3", "1", "F", "T", "NO"],
                           ["10 h", "09 h", "08 h", "07 h", "06 h", "05 h", "04 h", "03 h", "02 h", "01 h"])
        self.updateLists("T", "NA", 3)

        # Move & Update
        self.calculateMove(["09", "d", "4", "0", "F", "T", "TOPCARD"],
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
                           ["12 d", "11 d", "10 d", "09 d", "08 d", "07 d", "06 d", "05 d", "04 d", "03 d", "02 d",
                            "01 d"])
        self.updateLists("T", "NA", 3)

        # Move & Update
        self.calculateMove(["NA", "NA", "NA", "NA", "NA", "W", "NO"], ["NA", "NA", "NA", "NA", "NA"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["09", "c", "-1", "3", "F", "W", "NO"],
                           ["09 c", "08 c", "07 c", "06 c", "05 c", "04 c", "03 c", "02 c", "01 c"])
        self.updateLists("W", "NA", -1)

        # Move & Update
        self.calculateMove(["10", "c", "0", "3", "F", "T", "TOPCARD"],
                           ["10 c", "09 c", "08 c", "07 c", "06 c", "05 c", "04 c", "03 c", "02 c", "01 c"])
        self.updateLists("T", "NA", 0)

        # Move & Update
        self.calculateMove(["11", "h", "0", "1", "F", "T", "TOPCARD"],
                           ["11 h", "10 h", "09 h", "08 h", "07 h", "06 h", "05 h", "04 h", "03 h", "02 h", "01 h"])
        self.updateLists("T", "NA", 0)

        # Move & Update
        self.calculateMove(["12", "s", "0", "2", "F", "T", "TOPCARD"],
                           ["12 s", "11 s", "10 s", "09 s", "08 s", "07 s", "06 s", "05 s", "04 s", "03 s", "02 s",
                            "01 s"])
        self.updateLists("T", "NA", 0)

        # Move & Update
        self.calculateMove(["13", "d", "0", "0", "F", "T", "NO"],
                           ["13 d", "12 d", "11 d", "10 d", "09 d", "08 d", "07 d", "06 d", "05 d", "04 d", "03 d",
                            "02 d",
                            "01 d"])
        self.updateLists("T", "NA", 0)

        # Move & Update
        self.calculateMove(["11", "c", "2", "3", "F", "T", "TOPCARD"],
                           ["11 c", "10 c", "09 c", "08 c", "07 c", "06 c", "05 c", "04 c", "03 c", "02 c", "01 c"])
        self.updateLists("T", "NA", 2)

        # Move & Update
        self.calculateMove(["12", "h", "2", "1", "F", "T", "TOPCARD"],
                           ["12 h", "11 h", "10 h", "09 h", "08 h", "07 h", "06 h", "05 h", "04 h", "03 h", "02 h",
                            "01 h"])
        self.updateLists("T", "NA", 2)

        # Move & Update
        self.calculateMove(["13", "s", "2", "2", "F", "T", "NO"],
                           ["13 s", "12 s", "11 s", "10 s", "09 s", "08 s", "07 s", "06 s", "05 s", "04 s", "03 s",
                            "02 s", "01 s"])
        self.updateLists("T", "NA", 3)

        # Move & Update
        self.calculateMove(["12", "c", "4", "3", "F", "T", "TOPCARD"],
                           ["12 c", "11 c", "10 c", "09 c", "08 c", "07 c", "06 c", "05 c", "04 c", "03 c", "02 c",
                            "01 c"])
        self.updateLists("T", "NA", 4)

        # Move & Update
        self.calculateMove(["13", "c", "3", "3", "F", "T", "NO"],
                           ["13 c", "12 c", "11 c", "10 c", "09 c", "08 c", "07 c", "06 c", "05 c", "04 c", "03 c",
                            "02 c", "01 c"])
        self.updateLists("T", "NA", 3)

        # Move & Update
        self.calculateMove(["13", "h", "4", "1", "F", "T", "NO"],
                           ["13 h", "12 h", "11 h", "10 h", "09 h", "08 h", "07 h", "06 h", "05 h", "04 h", "03 h",
                            "02 h", "01 h"])
        self.updateLists("T", "NA", 4)

        self.calculateMove(["WIN", "WIN", "WIN", "WIN", "WIN", "WIN", "WIN"],
                           ["NA", "NA", "NA", "NA", "NA"])

    def test_play_game_two(self):
        gl = create_empty_object()
        waste_card_pile_actual = []
        tableau_actual = create_list(["12 d"], ["03 d"], ["01 d"], ["11 c"], ["05 d"], ["10 d"], ["09 c"])
        foundation_actual = create_list([], [], [], [])
        gl.reset_logic(waste_card_pile_actual, tableau_actual, foundation_actual)

        list_of_moves = [["01", "d", "2", "0", "F", "T", "YES"],
                         ["01", "c", "2", "1", "F", "T", "YES"],
                         ["11", "c", "3", "0", "T", "T", "YES"],
                         ["05", "d", "4", "3", "T", "T", "YES"],
                         ["08", "h", "4", "6", "T", "T", "YES"],
                         ["10", "d", "5", "0", "T", "T", "YES"],
                         ["09", "c", "6", "0", "T", "T", "YES"],
                         ["02", "h", "2", "6", "T", "T", "NO"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "YES"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "YES"],
                         ["02", "c", "-1", "1", "F", "W", "YES"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "YES"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "YES"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "YES"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "YES"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "YES"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "YES"],
                         ["04", "c", "-1", "3", "T", "W", "YES"],
                         ["03", "d", "1", "3", "T", "T", "YES"],
                         ["12", "d", "0", "1", "T", "T", "NO"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "YES"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "YES"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "YES"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "YES"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "YES"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "YES"],
                         ["07", "c", "-1", "1", "T", "W", "YES"],
                         ["06", "d", "4", "1", "T", "T", "YES"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "YES"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "YES"],
                         ["06", "h", "-1", "4", "T", "W", "YES"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "YES"],
                         ["11", "d", "-1", "5", "T", "W", "YES"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "YES"],
                         ["01", "s", "-1", "2", "F", "W", "YES"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "YES"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "YES"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "YES"],
                         ["05", "c", "-1", "1", "T", "W", "YES"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "YES"],
                         ["02", "s", "-1", "2", "F", "W", "YES"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "YES"],
                         ["02", "d", "-1", "0", "F", "W", "YES"],
                         ["03", "d", "3", "0", "F", "T", "TOPCARD"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "YES"],
                         ["01", "h", "-1", "3", "F", "W", "YES"],
                         ["02", "h", "6", "3", "F", "T", "TOPCARD"],
                         ["03", "c", "6", "1", "F", "T", "YES"],
                         ["04", "c", "3", "1", "F", "T", "TOPCARD"],
                         ["05", "c", "1", "1", "F", "T", "TOPCARD"],
                         ["03", "s", "6", "2", "F", "T", "YES"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "YES"],
                         ["06", "c", "-1", "1", "F", "W", "NO"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "NO"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "NO"],
                         ["10", "c", "-1", "5", "T", "W", "NO"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "NO"],
                         ["04", "d", "-1", "0", "F", "W", "NO"],
                         ["05", "d", "3", "0", "F", "T", "TOPCARD"],
                         ["06", "d", "1", "0", "F", "T", "TOPCARD"],
                         ["07", "c", "1", "1", "F", "T", "TOPCARD"],
                         ["07", "s", "4", "1", "T", "T", "YES"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "NO"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "NO"],
                         ["03", "h", "-1", "3", "F", "W", "NO"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "NO"],
                         ["07", "d", "-1", "0", "F", "W", "NO"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "NO"],
                         ["05", "h", "-1", "3", "T", "W", "NO"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "NO"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "NO"],
                         ["08", "c", "-1", "1", "F", "W", "NO"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "NO"],
                         ["09", "h", "-1", "5", "T", "W", "NO"],
                         ["08", "s", "6", "5", "T", "T", "YES"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "NO"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "NO"],
                         ["04", "h", "-1", "3", "F", "W", "NO"],
                         ["05", "h", "3", "3", "F", "T", "TOPCARD"],
                         ["06", "h", "1", "3", "F", "T", "TOPCARD"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "NO"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "NO"],
                         ["08", "d", "-1", "0", "F", "W", "NO"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "NO"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "NO"],
                         ["NA", "NA", "NA", "NA", "NA", "W", "NO"],
                         ["LOSE", "LOSE", "LOSE", "LOSE", "LOSE", "LOSE", "LOSE"],
                         ]
        list_of_updates = [create_list([],[],["01 c"],[],[],[],[]),
                           create_list([],[],["02 h"],[],[],[],[]),
                           create_list([],[],[],["06 s"],[],[],[]),
                           create_list([],[],[],[],["08 h"],[],[]),
                           create_list([],[],[],[],["06 d"],[],[]),
                           create_list([],[],[],[],[],["12 c"],[]),
                           create_list([],[],[],[],[],[],["03 c"]),
                           create_list([],[],[],[],[],[],[]),
                           "08 d", "02 c", None, "10 c", "04 d", "09 s", "03 h", "07 d", "04 c", None,
                           create_list([], ["13 c"], [], [], [], [], []),
                           create_list([], [], [], [], [], [], []),
                           "05 h", "10 h", "08 c", "09 h", "12 c", "07 c", None,
                           create_list([], [], [], [], ["07 s"], [], []), None,
                           "06 h", None, "11 d", None, "01 s", None, "04 h", "11 s", "05 c", None, "02 s",
                           None, "02 d", None, None, "01 h", None, None,
                           create_list([], [], [], [], [], [], ["03 s"]), None, None,
                           create_list([], [], [], [], [], [], ["08 s"]),
                           "06 c", None, None, None, None, None, None, None, None, None,
                           create_list([], [], [], [], ["13 s"], [], []), None, None, None, None, None,
                           None, None, None, None, None, None, None,
                           create_list([], [], [], [], [], [], ["10 s"]), None,
                           None, None, None, None, None, None, None, None, None, None, None
                           ]
        for i in range(len(list_of_moves)):
            self.assertListEqual(gl.calculate_move(), list_of_moves[i])
            gl.update_logic_move(gl.calculate_move())
            if list_of_moves[i][5] == "T" and list_of_moves[i][0] != "NA":
                gl.update_logic_scan(None, list_of_updates[i], None)
            else:
                gl.update_logic_scan(list_of_updates[i], None, None)

    # TC01 - Test Case (Opdater via scan)
    def test_update_logic_scan(self):
        gl = create_empty_object()
        waste_card_pile_actual = []
        waste_card_unknown_actual = 24
        tableau_actual = create_list([], [], [], [], [], [], [])
        foundation_actual = create_list([], [], [], [])

        max_range = 100000
        card_count = 0
        card_type = 0
        for i in range(1, max_range):
            card_count += 1
            if card_count == 14: card_count = 1; card_type += 1
            if card_type == 4: card_type = 0
            if card_count > 9:
                waste_card_actual = str(card_count)
            else:
                waste_card_actual = str(0) + str(card_count)
            if card_type == 0: waste_card_actual += " h"
            if card_type == 1: waste_card_actual += " s"
            if card_type == 2: waste_card_actual += " c"
            if card_type == 3: waste_card_actual += " d"
            gl.update_logic_scan(waste_card_actual, None, None)
            if waste_card_actual not in waste_card_pile_actual:
                waste_card_pile_actual.append(waste_card_actual)
                waste_card_unknown_actual -= 1
            self.assertListEqual(gl.logicWasteCardPile, waste_card_pile_actual)
            self.assertEqual(gl.unknownWaste, waste_card_unknown_actual)
            self.assertEqual(len(gl.logicWasteCardPile), len(waste_card_pile_actual))
        for i in range(1, max_range):
            rand_index = random.randrange(7)
            tableau_expected = create_list([], [], [], [], [], [], [])
            card_count += 1
            if card_count == 14: card_count = 1; card_type += 1
            if card_type == 4: card_type = 0
            if card_count > 9:
                tableau_card_actual = str(card_count)
            else:
                tableau_card_actual = str(0) + str(card_count)
            if card_type == 0: tableau_card_actual += " h"
            if card_type == 1: tableau_card_actual += " s"
            if card_type == 2: tableau_card_actual += " c"
            if card_type == 3: tableau_card_actual += " d"
            tableau_expected.get(rand_index).append(tableau_card_actual)
            gl.update_logic_scan(None, tableau_expected, None)
            if tableau_card_actual not in tableau_actual.get(rand_index):
                tableau_actual.get(rand_index).append(tableau_card_actual)
            tableau_actual.get(rand_index).sort(reverse=False)
            self.assertDictEqual(gl.logicTableauCardPiles, tableau_actual)
            self.assertEqual(len(gl.logicTableauCardPiles.get(rand_index)), len(tableau_actual.get(rand_index)))
        for i in range(1, max_range):
            rand_index = random.randrange(4)
            foundation_expected = create_list([], [], [], [])
            card_count += 1
            if card_count == 14: card_count = 1; card_type += 1
            if card_type == 4: card_type = 0
            if card_count > 9:
                foundation_card_actual = str(card_count)
            else:
                foundation_card_actual = str(0) + str(card_count)
            if card_type == 0: foundation_card_actual += " h"
            if card_type == 1: foundation_card_actual += " s"
            if card_type == 2: foundation_card_actual += " c"
            if card_type == 3: foundation_card_actual += " d"
            foundation_expected.get(rand_index).append(foundation_card_actual)
            gl.update_logic_scan(None, None, foundation_expected)
            if foundation_card_actual not in foundation_actual.get(rand_index):
                foundation_actual.get(rand_index).append(foundation_card_actual)
            foundation_actual.get(rand_index).sort(reverse=True)
            self.assertDictEqual(gl.logicFoundationCardPiles, foundation_actual)
            self.assertEqual(len(gl.logicFoundationCardPiles.get(rand_index)), len(foundation_actual.get(rand_index)))
        return

    # TC02 - Test Case (Opdater via træk)
    def test_update_logic_move(self):
        gl = create_empty_object()
        waste_card_pile_actual = ["11 c", "02 s", "01 h"]
        tableau_actual = create_list(["01 s"], ["13 c"], ["12 h"], ["07 d"], ["08 s"], ["06 c"], ["09 h"])
        foundation_actual = create_list([], [], [], [])

        gl.reset_logic(waste_card_pile_actual, tableau_actual, foundation_actual)

        for i in range(7):
            self.assertEqual(gl.unknownTableau[i], i)

        self.assertListEqual(gl.update_logic_move(gl.calculate_move()), ["01 s"])
        self.assertListEqual(gl.update_logic_move(gl.calculate_move()), ["13 c"])
        self.assertListEqual(gl.update_logic_move(gl.calculate_move()), ["12 h", "13 c"])
        self.assertListEqual(gl.update_logic_move(gl.calculate_move()), ["07 d", "08 s"])
        self.assertListEqual(gl.update_logic_move(gl.calculate_move()), ["07 d", "08 s", "09 h"])
        self.assertListEqual(gl.update_logic_move(gl.calculate_move()), ["06 c", "07 d", "08 s", "09 h"])
        self.assertListEqual(gl.update_logic_move(gl.calculate_move()), ["01 h"])
        self.assertListEqual(gl.update_logic_move(gl.calculate_move()), ["02 s", "01 s"])
        self.assertListEqual(gl.update_logic_move(gl.calculate_move()), ["11 c", "12 h", "13 c"])
        self.assertListEqual(gl.update_logic_move(gl.calculate_move()), ["NA", "NA", "NA", "NA", "NA"])

        self.assertEqual(gl.unknownTableau[0], 0)
        self.assertEqual(gl.unknownTableau[1], 0)
        self.assertEqual(gl.unknownTableau[2], 1)
        self.assertEqual(gl.unknownTableau[3], 2)
        self.assertEqual(gl.unknownTableau[4], 3)
        self.assertEqual(gl.unknownTableau[5], 4)
        self.assertEqual(gl.unknownTableau[6], 6)

        waste_card_pile_actual = ["05 d", "13 c", "06 s"]
        tableau_actual = create_list(["03 s"], ["05 h"], ["10 s"], ["07 c"], ["07 h"], ["06 c"], ["09 h"])
        foundation_actual = create_list([], [], [], [])

        gl.reset_logic(waste_card_pile_actual, tableau_actual, foundation_actual)

        for i in range(7):
            self.assertEqual(gl.unknownTableau[i], i)

        self.assertListEqual(gl.update_logic_move(gl.calculate_move()), ["05 h", "06 c"])
        self.assertListEqual(gl.update_logic_move(gl.calculate_move()), ["05 h", "06 c", "07 h"])
        self.assertListEqual(gl.update_logic_move(gl.calculate_move()), ["09 h", "10 s"])
        self.assertListEqual(gl.update_logic_move(gl.calculate_move()), ["NA", "NA", "NA", "NA", "NA"])

        self.assertEqual(gl.unknownTableau[0], 0)
        self.assertEqual(gl.unknownTableau[1], 0)
        self.assertEqual(gl.unknownTableau[2], 2)
        self.assertEqual(gl.unknownTableau[3], 3)
        self.assertEqual(gl.unknownTableau[4], 4)
        self.assertEqual(gl.unknownTableau[5], 4)
        self.assertEqual(gl.unknownTableau[6], 5)

    # TC03 - Test Case (Kalkuler et træk)
    def test_calculate_move(self):
        gl = create_empty_object()
        waste_card_pile_actual = ["08 s", "12 c", "03 c", "03 d", "09 d"]
        waste_card_unknown_actual = 24
        tableau_actual = create_list(["04 s"], ["05 h", "06 c"], ["01 d"], ["02 d"], ["10 c"], ["11 h"], ["13 h"])
        foundation_actual = create_list(["02 c", "01 c"], [], [], [])

        gl.reset_logic(waste_card_pile_actual, tableau_actual, foundation_actual)

        list_of_actual_moves = [["04", "s", "0", "1", "T", "T", "NO"], ["01", "d", "2", "1", "F", "T", "YES"],
                                ["02", "d", "3", "1", "F", "T", "YES"], ["10", "c", "4", "5", "T", "T", "YES"],
                                ["13", "h", "6", "0", "T", "T", "YES"], ["09", "d", "-1", "5", "T", "W", "YES"],
                                ["03", "d", "-1", "1", "F", "W", "YES"], ["03", "c", "-1", "0", "F", "W", "YES"],
                                ["12", "c", "-1", "0", "T", "W", "YES"], ["11", "h", "5", "0", "T", "T", "YES"],
                                ["08", "s", "-1", "0", "T", "W", "YES"], ["NA", "NA", "NA", "NA", "NA", "W", "YES"]]
        for i in range(len(list_of_actual_moves)):
            self.assertListEqual(gl.calculate_move(), list_of_actual_moves[i])
            gl.update_logic_move(gl.calculate_move())

    # Test prioriteter
    def test_priorities(self):
        gl = create_empty_object()
        waste_card_pile_actual = []
        tableau_actual = create_list(["06 c"], ["06 s"], ["07 d"], [], [], [], [])
        foundation_actual = create_list([], [], [], [])
        gl.reset_logic(waste_card_pile_actual, tableau_actual, foundation_actual)

        self.assertListEqual(gl.calculate_move(), ["06", "s", "1", "2", "T", "T", "YES"])

        gl = create_empty_object()
        waste_card_pile_actual = []
        tableau_actual = create_list([], ["06 s"], ["07 d"], ["06 c"], [], [], [])
        foundation_actual = create_list([], [], [], [])
        gl.reset_logic(waste_card_pile_actual, tableau_actual, foundation_actual)

        self.assertListEqual(gl.calculate_move(), ["06", "s", "1", "2", "T", "T", "YES"])

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


def create_list(li0, li1, li2, li3, li4=None, li5=None, li6=None):
    if li4 is not None:
        dict_lists = {0: li0, 1: li1, 2: li2, 3: li3, 4: li4, 5: li5, 6: li6}
    else:
        dict_lists = {0: li0, 1: li1, 2: li2, 3: li3}
    return dict_lists


def create_empty_object():
    list0 = [];
    list00 = [];
    list000 = [];
    list0000 = []
    foundation_piles = {0: list0, 1: list00, 2: list000, 3: list0000}
    list1 = [];
    list11 = [];
    list111 = [];
    list1111 = [];
    list11111 = [];
    list111111 = [];
    list1111111 = []
    tableau_piles = {0: list1, 1: list11, 2: list111, 3: list1111, 4: list11111, 5: list111111, 6: list1111111}
    return GameLogic.GameLogic(None, tableau_piles, foundation_piles)
