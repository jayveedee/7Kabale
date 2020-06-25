#
# Coded by: Jákup Viljam Dam
# Project: 7-Kabal
#


class GameLogic:

    # OBJECT CONSTRUCTOR AND ALL ITS VARIABLES
    def __init__(self, logic_waste_card, logic_tableau_card_piles, logic_foundation_card_piles):
        self.logicWasteCardPile = []
        self.logicTableauCardPiles = {}
        self.logicFoundationCardPiles = {}
        self.result = []
        self.previous_move = ""
        self.unknownTableau = []
        self.unknownWaste = 24
        self.unknownWasteCounter = 100
        self.loseCounter = 0
        self.allUnknownWasteFound = False
        self.reset = True
        self.update_logic_scan(logic_waste_card, logic_tableau_card_piles, logic_foundation_card_piles)

    # RESETS THE CONSTRUCTOR VARIABLES TO THEIR INITIAL STATE
    def reset_variables(self):
        self.logicWasteCardPile = []
        self.logicTableauCardPiles = {}
        self.logicFoundationCardPiles = {}
        self.result = []
        self.previous_move = ""
        self.unknownTableau = []
        self.unknownWaste = 24
        self.unknownWasteCounter = 100
        self.loseCounter = 0
        self.allUnknownWasteFound = False
        self.unknownTableau.clear()
        for i in range(7):
            counter = 0
            for j in range(i):
                counter += 1
            self.unknownTableau.append(counter)

    # ADDS THE FIRST SCANNED LISTS/VARIABLES TO THE OBJECT, THE FIRST TIME IT'S CREATED
    def insert_first_time_scan(self, wa, tb, fa):
        if wa is not None:
            self.logicWasteCardPile = wa
        if tb is not None:
            self.logicTableauCardPiles = tb
        else:
            self.logicTableauCardPiles = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
        if fa is not None:
            self.logicFoundationCardPiles = fa
        else:
            self.logicFoundationCardPiles = {0: [], 1: [], 2: [], 3: []}
        self.reset = False

    # A MAIN METHOD THAT'S USED FOR INSERTING NEWLY DETECTED CARDS INTO THE INSTANTIATED VARIABLES
    def update_logic_scan(self, logic_waste_card=None, logic_tableau_card_piles=None, logic_foundation_card_piles=None):
        # IF FIRST TIME RUNNING
        if (self.logicTableauCardPiles is None and self.logicFoundationCardPiles is None and self.logicWasteCardPile is None) or (self.reset is True):
            self.reset_variables()
            self.insert_first_time_scan(logic_waste_card, logic_tableau_card_piles, logic_foundation_card_piles)
        # ELSE ALL OTHER TIMES RUNNING
        else:
            # CHECKS IF WASTE CARD
            if logic_waste_card is not None:
                if logic_waste_card not in self.logicWasteCardPile:
                    self.unknownWaste -= 1
                    if self.unknownWaste == 0:
                        self.allUnknownWasteFound = True
                    self.logicWasteCardPile.append(logic_waste_card)
            # CHECKS IF TABLEAU LIST
            if logic_tableau_card_piles is not None:
                self.check_list_consistency(logic_tableau_card_piles, self.logicTableauCardPiles)
            # CHECKS IF FOUNDATION LIST
            if logic_foundation_card_piles is not None:
                self.check_list_consistency(logic_foundation_card_piles, self.logicFoundationCardPiles)
        # RETURNS THE UPDATED INSTANTIATED VARIABLES
        return self.logicWasteCardPile, self.logicTableauCardPiles, self.logicFoundationCardPiles

    # A MAIN METHOD THAT'S USED FOR UPDATING THE INSTANTIATED VARIABLES DEPENDING ON WHAT MOVE WAS JUST MADE
    def update_logic_move(self, move):
        # ADDS A PREVIOUS MOVE AND RESETS THE LAST MOVE
        self.previous_move = move[0]
        self.result = []
        # IF THERE IS A MOVE AND THE GAME HAS NOT FINISHED YET
        if move[0] != "NA" and move[0] != "WIN" and move[0] != "LOSE":
            # DEFINE A VARIABLE TO CHECK FOR MULTIPLE CARDS TO MOVE FROM ONE PILE TO ANOTHER
            move_from_list = False
            # DEFINE THE MOVE INTO LOCAL VARIABLES
            moved_card = move[0] + " " + move[1]
            card_pile_moved_from = int(move[2])
            card_pile_moved_to = int(move[3])
            card_placement = move[4]
            move_type = move[5]
            scan = move[6]
            # IF THERE WAS A UNKNOWN CARD IN THE CURRENT MOVE, UPDATE THE LIST OF UNKNOWN CARDS
            if scan == "YES" and move_type == "T":
                self.unknownTableau[card_pile_moved_from] -= 1
            # IF IT WAS A MOVE TO BE PLACED ON THE TABLEAU
            if card_placement == "T":
                return self.handle_update_tableau_and_moved_pile(card_pile_moved_from, card_pile_moved_to, move_from_list, moved_card)
            # IF IT WAS A MOVE TO BE PLACED ON THE FOUNDATION
            if card_placement == "F":
                return self.handle_update_foundation_and_moved_pile(card_pile_moved_from, card_pile_moved_to, moved_card)
        # THERE WAS NO MOVE, CHECK IF WE CAN ACCESS THE REVERSE WASTE PILE FUNCTION
        self.handle_update_reversed_waste_pile()
        # THERE WAS NO MOVE TO UPDATE WITH, RETURN NA TO INDICATE NOTHING WAS UPDATED
        return ["NA", "NA", "NA", "NA", "NA"]

    # A MAIN METHOD THAT HANDLES THE GAME'S ALGORITHM FOR FINDING VALID MOVES
    def calculate_move(self, reverse=False):
        if self.check_win_condition() or self.check_lose_condition():
            return self.result
        # VARIABLE THAT DEFINES IF THE FOR-LOOP SHOULD BE REVERSED OR NOT (RIGHT-LEFT OR LEFT-RIGHT)
        tableau_range = range(len(self.logicTableauCardPiles))
        if reverse:
            tableau_range = reversed(range(len(self.logicTableauCardPiles)))
        # THE FOR LOOP THAT ITERATES THROUGH THE TABLEAU PILES
        for i in tableau_range:
            current_pile = self.logicTableauCardPiles.get(i)
            if len(current_pile) > 0:
                card_number, card_type, _ = self.define_card(i, 0, "T")
                # THE NEXT FOR LOOP THAT ITERATES ALL THE NEIGHBOURS OF THE CURRENT PILE
                for j in range(len(self.logicTableauCardPiles)):
                    neighbor_pile = self.logicTableauCardPiles.get(j)
                    # IF THERE IS AN EMPTY PILE, CHECKS IF A KING CAN BE PLACED OR IF THE CURRENT CARD CAN BE PLACED ON THE FOUNDATION
                    empty_space = self.check_empty_spaces(card_number, card_type, current_pile, i, j, neighbor_pile)
                    if empty_space is "King" or empty_space is "Foundation":
                        return self.result
                    elif empty_space is False:
                        if current_pile[0] != neighbor_pile[0]:
                            next_card_number, next_card_type, _ = self.define_card(j, 0, "T")
                            # THE THIRD AND FINAL FOR LOOP THAT ITERATES THROUGH ALL SUB CARDS IN THE CURRENT PILE
                            for k in range(len(current_pile) - 1, 0, -1):
                                sub_card_number, sub_card_type, _ = self.define_card(i, k, "T")
                                if self.check_sub_pile_placement(current_pile, i, j, k, next_card_number, next_card_type, sub_card_number, sub_card_type):
                                    return self.result
                            # A PRIORITY CHECKLIST, THAT FOCUSES ON MAKING ONLY THE BEST MOVES POSSIBLE FIRST FOR THE CURRENT CARD
                            priority = self.check_priority_one(current_pile, i)
                            if priority == "NA":
                                if self.check_tableau_placement(card_number, card_type, current_pile, i, j, next_card_number, next_card_type):
                                    return self.result
                            else:
                                break
        # CHECKS IF A WASTE CARD CAN BE PLACED
        return self.check_waste_card_placement()

    # MOST OF THE IMPLEMENTED PRIORITIES
    def check_priority_one(self, current_pile, i):
        sub_current_card_number, sub_current_card_type, _ = self.define_card(i, len(current_pile) - 1, "T")
        sub_current_card_in_foundation = self.check_foundation_card_pile(sub_current_card_number, sub_current_card_type)
        # A FOR LOOP THAT ITERATES THROUGH THE WHOLE TABLEAU PILES AGAIN
        if self.how_many_unknowns_left() > 0:
            for k in range(len(self.logicTableauCardPiles)):
                sub_next_pile = self.logicTableauCardPiles.get(k)
                # IF THE TWO PILES AREN'T THE SAME AND THE NEXT PILE ISN'T EMPTY
                if len(sub_next_pile) != 0 and sub_next_pile != current_pile:
                    sub_next_card_number, sub_next_card_type, _ = self.define_card(k, len(sub_next_pile) - 1, "T")
                    sub_next_card_in_foundation = self.check_foundation_card_pile(sub_next_card_number,sub_next_card_type)
                    if self.previous_move != "NA":
                        # CHECKS IF THE TWO DIFFERENT CARDS HAVE THE SAME DIFFERING TYPE & NUMBER (WHICH MEANS THEY CAN NOT BE PLACED ON ONE ANOTHER)
                        if self.check_card_type_matches(sub_current_card_type, sub_next_card_type, 1):
                            if sub_current_card_number == sub_next_card_number:
                                # IF THERE ARE TWP CARDS OF THE SAME TYPE THAT CAN BE MOVED TO ONE PLACE, PICK THE ONE WITH MOST UNKNOWNS
                                if self.unknownTableau[k] > self.unknownTableau[i]:
                                    return "P1"
                                # IF BOTH ARE THE SAME KIND OF CARD, BUT ONE OF THEM CAN ONTO THE FOUNDATION, PLACE THAT ONE FIRST
                                if len(sub_next_pile) == 1 and sub_next_card_in_foundation != -1 and not sub_current_card_in_foundation == -1 and self.unknownTableau[k] > 0 and self.unknownTableau[i] > 0:
                                    return "P3"
                        # IF THE NEIGHBOUR CARD CAN BE PLACED ON THE FOUNDATION AND HAS UNKNOWNS UNDER IT
                        if len(sub_next_pile) == 1 and sub_next_card_in_foundation != -1 and self.unknownTableau[k] > 0:
                            return "P5"

                        # MAKES SURE THERE IS NO OTHER AVAILABLE MOVE ON THE TABLEAU WITH THE CURRENT CARD BEFORE PLACING IT ON THE FOUNDATION
                        if self.check_card_type_matches(sub_current_card_type,sub_next_card_type) and self.unknownTableau[k] != 0:
                            if sub_current_card_number - 1 == sub_next_card_number and self.check_foundation_card_pile:
                                return "P2"

                        # ONLY MOVE A CARD AWAY FROM A PLACE WITH NO UNKNOWNS IF THERE IS A KING THAT CAN BE PLACED THERE
                        if self.unknownTableau[i] == 0:
                            if ("13 s" not in self.logicWasteCardPile or "13 c" not in self.logicWasteCardPile or "13 h" not in self.logicWasteCardPile or "13 d" not in self.logicWasteCardPile) or self.check_how_many_kings_on_tableau():
                                if self.unknownTableau[k] == 0 and sub_next_card_number == 13:
                                    return "P4"
                    else:
                        break
        return "NA"

    # COUNTS HOW MANY KINGS THERE ARE ON THE TABLEAU
    def check_how_many_kings_on_tableau(self):
        king_counter = 0
        for i in range(len(self.logicTableauCardPiles)):
            current_pile = self.logicTableauCardPiles.get(i)
            if len(current_pile) != 0:
                card_number, _, _ = self.define_card(i, len(current_pile) - 1, "T")
                if card_number == 13:
                    king_counter += 1
        if king_counter == 4:
            return True
        else:
            return False

    # CHECKS IF THE CURRENT CAN BE PLACED ON THE NEIGHBOUR CARD ON THE TABLEAU
    def check_tableau_placement(self, card_number, card_type, current_pile, i, j, next_card_number, next_card_type):
        unknowns = self.check_unknown_cards(i)
        if len(current_pile) > 1:
            unknowns = -1
        if len(current_pile) > 1:
            above_card_number, _, _ = self.define_card(i, 1, "T")
            if above_card_number != next_card_number:
                if self.check_card_placement(i, card_number, card_type, j, next_card_number, next_card_type, False, unknowns, "T"):
                    return True
        else:
            if self.check_card_placement(i, card_number, card_type, j, next_card_number, next_card_type, False, unknowns, "T"):
                return True
        return False

    # CHECKS IF THE SUB CARDS CAN BE PLACED SOMEWHERE ON THE TABLEAU
    def check_sub_pile_placement(self, current_pile, i, j, k, next_number, next_type, sub_number, sub_type):
        if k == len(current_pile) - 1:
            unknowns = self.check_unknown_cards(i)
        else:
            unknowns = -1
        if len(current_pile) > 1 and k != len(current_pile) - 1:
            above_card_number, _, _ = self.define_card(i, k + 1, "T")
            if above_card_number != next_number:
                if self.check_card_placement(i, sub_number, sub_type, j, next_number, next_type, True, unknowns, "T"):
                    return True
        else:
            if sub_number != 13:
                if self.check_card_placement(i, sub_number, sub_type, j, next_number, next_type, True, unknowns, "T"):
                    return True
        return False

    # CHECKS IF THERE IS A EMPTY SPOT ON THE TABLEAU AND IF A KING CAN BE PLACED THERE OR A CARD CAN INSTEAD BE PLACED ON THE FOUNDATION
    def check_empty_spaces(self, card_number, card_type, current_pile, i, j, neighbor_pile):
        unknowns = self.unknownTableau[i]

        if len(current_pile) > 1:
            unknowns = -2
        if unknowns == 0:
            unknowns = -1

        if len(neighbor_pile) == 0:
            if self.unknownTableau[j] == 0:
                if self.check_card_placement(i, card_number, card_type, j, -1, "-1", False, unknowns, "T"):
                    return "Foundation"
                last_index = len(current_pile) - 1
                if current_pile[last_index] == "13 d" or current_pile[last_index] == "13 c" or \
                        current_pile[last_index] == "13 s" or current_pile[last_index] == "13 h":
                    king_card_number, king_card_type, _ = self.define_card(i, last_index, "T")
                    unknowns = self.unknownTableau[i]
                    if self.check_card_placement(i, king_card_number, king_card_type, j, -1, "-1", True, unknowns, "T"):
                        return "King"
            return True
        else:
            return False

    # ADDS THE NEWLY SCANNED CARDS TO THE OLD LIST
    def check_list_consistency(self, new_scanned_pile, old_scanned_pile):
        for i in range(0, len(new_scanned_pile)):
            current_new_scanned_pile = new_scanned_pile.get(i)
            current_old_scanned_pile = old_scanned_pile.get(i)
            # CHECKS IF THE PILES AREN'T THE SAME AND THE NEWLY SCANNED ONE IS NOT EMPTY
            if len(current_new_scanned_pile) != len(current_old_scanned_pile) and len(current_new_scanned_pile) != 0:
                if len(current_old_scanned_pile) == 0:
                    old_scanned_pile[i] = current_new_scanned_pile
                else:
                    # IF THE CURRENT SCANNED IS NOT CONTAINED IN THE OLD LIST ENTER
                    if current_new_scanned_pile[0] not in current_old_scanned_pile:
                        current_old_scanned_pile.append(current_new_scanned_pile[0])
                        if old_scanned_pile == self.logicTableauCardPiles:
                            # TABLEAU
                            current_old_scanned_pile.sort(reverse=False)
                        else:
                            # FOUNDATION
                            current_old_scanned_pile.sort(reverse=True)
            # IF THE CURRENT PILES ARE THE SAME ONE, BUT THEIR ELEMENTS DIFFER ENTER HERE
            elif len(current_new_scanned_pile) != 0 and len(current_old_scanned_pile) != 0:
                if current_new_scanned_pile[0] != current_old_scanned_pile[0]:
                    if current_new_scanned_pile[0] not in current_old_scanned_pile:
                        current_old_scanned_pile.append(current_new_scanned_pile[0])
                        if old_scanned_pile == self.logicTableauCardPiles:
                            # TABLEAU
                            current_old_scanned_pile.sort(reverse=False)
                        else:
                            # FOUNDATION
                            current_old_scanned_pile.sort(reverse=True)
        return old_scanned_pile

    # HANDLES THE ITERATION OF THE WASTE PILE AFTER ALL THE WASTE CARDS HAVE BEEN FOUND
    def handle_update_reversed_waste_pile(self):
        if self.allUnknownWasteFound:
            if len(self.logicWasteCardPile) - 1 == self.unknownWasteCounter:
                self.unknownWasteCounter = 0
            else:
                self.unknownWasteCounter += 1

    # HANDLES UPDATING THE TABLEAU PILES WHEN MOVING ONE PILE/CARD TO ANOTHER
    def handle_update_tableau_and_moved_pile(self, card_pile_moved_from, card_pile_moved_to, move_from_list, moved_card):
        tableau_pile_moved_to = self.logicTableauCardPiles.get(card_pile_moved_to)
        # IF IT WASN'T A WASTE CARD
        if card_pile_moved_from != -1:
            tableau_pile_moved_from = self.logicTableauCardPiles.get(card_pile_moved_from)
            # FINDS OUT HOW MANY CARDS SHOULD BE MOVED FROM THE PILE OVER TO THE NEXT PILE
            self.check_how_many_cards_to_move(move_from_list, moved_card, tableau_pile_moved_from, tableau_pile_moved_to)
        else:
            # ADDS WASTE CARD TO A TABLEAU PILE AND REMOVES IT FROM THE WASTE PILE
            waste_card = self.check_how_many_waste_found()
            tableau_pile_moved_to.append(waste_card)
            self.logicWasteCardPile.remove(waste_card)
        # SORTS THE LIST IN THE CORRECT ORDER
        tableau_pile_moved_to.sort(reverse=False)
        return tableau_pile_moved_to

    # HANDLES MOVING CARDS FROM TABLEAU OR WASTE PILE TO FOUNDATION
    def handle_update_foundation_and_moved_pile(self, card_pile_moved_from, card_pile_moved_to, moved_card):
        foundation_pile_moved_to = self.logicFoundationCardPiles.get(card_pile_moved_to)
        # IF IT WASN'T A WASTE CARD, ENTER HERE
        if card_pile_moved_from != -1:
            tableau_pile_moved_from = self.logicTableauCardPiles.get(card_pile_moved_from)
            # ADDS THE TOP CARD TO THE FOUNDATION AND REMOVES IT FROM THE TABLEAU
            if tableau_pile_moved_from[0] == moved_card:
                foundation_pile_moved_to.append(tableau_pile_moved_from[0])
                tableau_pile_moved_from.pop(0)
        else:
            # ADDS THE WASTE CARD TO THE FOUNDATION AND REMOVES IT FROM THE WASTE PILE
            waste_card = self.check_how_many_waste_found()
            foundation_pile_moved_to.append(waste_card)
            self.logicWasteCardPile.remove(waste_card)
        # SORTS THE LIST IN THE CORRECT ORDER
        foundation_pile_moved_to.sort(reverse=True)
        return foundation_pile_moved_to

    # COUNTS HOW MANY WASTE CARDS HAVE BEEN FOUND
    def check_how_many_waste_found(self):
        if self.allUnknownWasteFound:
            _, _, waste_card = self.define_card(self.unknownWasteCounter, 0, "W")
            # IF ALL WASTE CARDS HAVE BEEN FOUND, SET THE VARIABLE TO -1
            if self.unknownWasteCounter == 0:
                self.unknownWasteCounter = -1
            # IF ALL WASTE CARDS HAVE NOT BEEN FOUND, MINUS THE VARIABLE
            elif 0 < self.unknownWasteCounter < len(self.logicWasteCardPile) - 1:
                self.unknownWasteCounter -= 1
        else:
            # IF ALL WASTE CARDS HAVE BEEN FOUND, WE FOLLOW THE REVERSED_WASTE METHOD AND DO THE FOLLOWING
            _, _, waste_card = self.define_card(len(self.logicWasteCardPile) - 1, 0, "W")
        return waste_card

    # SIMPLE METHOD THAT CHECKS THE AMOUNT OF THE CURRENT CARD'S UNKNOWN CARDS
    def check_unknown_cards(self, i):
        if i != -1:
            # IF IT'S A TABLEAU PILE
            unknowns = self.unknownTableau[i]
            if unknowns == 0:
                unknowns = -1
        else:
            # IF IT'S THE WASTE PILE
            unknowns = self.unknownWaste
            if unknowns == 0:
                unknowns = -1
        return unknowns

    # CHECKS WHERE A WASTE CARD CAN BE PLACED, IF NOWHERE RETURN A "NA" MOVE
    def check_waste_card_placement(self):
        if self.logicWasteCardPile is not None:
            if self.handle_waste_card_check():
                return self.result
        if self.unknownWaste != 0:
            return ["NA", "NA", "NA", "NA", "NA", "W", "YES"]
        else:
            self.loseCounter += 1
            return ["NA", "NA", "NA", "NA", "NA", "W", "NO"]

    # FINDS OUT IF A WASTE CARD CAN BE PLACED ANYWHERE ON THE TABLEAU OR FOUNDATION
    def handle_waste_card_check(self):
        if len(self.logicWasteCardPile) != 0 and self.unknownWasteCounter != -1:
            waste_card_number, waste_card_type = self.check_if_all_waste_cards_found()
            unknowns = self.check_unknown_cards(-1)
            # ITERATES THROUGH THE TABLEAU PILES
            for i in range(len(self.logicTableauCardPiles)):

                current_pile = self.logicTableauCardPiles.get(i)
                if len(current_pile) > 0:

                    next_card_number, next_card_type, _ = self.define_card(i, 0, "T")
                    # CHECKS IF IT CAN BE PLACED ON TABLEAU OR FOUNDATION
                    if self.check_card_placement(-1, waste_card_number, waste_card_type, i, next_card_number, next_card_type, False, unknowns, "W"):
                        return True
                # CHECKS IF A KING CAN BE PLACED ON A EMPTY SPOT OR IF THERE IS NO MOVE AND PLACE IT ON THE FOUNDATION
                elif len(current_pile) == 0 and waste_card_number == 13:
                    if self.check_card_placement(-1, waste_card_number, waste_card_type, i, -1, "-1", False, unknowns, "W"):
                        return True
        return False

    # CHECKS IF ALL THE WASTE CARDS HAVE BEEN FOUND
    def check_if_all_waste_cards_found(self):
        if self.allUnknownWasteFound:
            if self.unknownWasteCounter > len(self.logicWasteCardPile) - 1:
                self.unknownWasteCounter = len(self.logicWasteCardPile) - 1
            waste_card_number, waste_card_type, _ = self.define_card(self.unknownWasteCounter, 0, "W")
        else:
            # IF ALL WASTE CARDS HAVE BEEN FOUND, WE FOLLOW THE REVERSED_WASTE METHOD APPROACH
            waste_card_number, waste_card_type, _ = self.define_card(len(self.logicWasteCardPile) - 1, 0, "W")
        return waste_card_number, waste_card_type

    # CHECKS WHERE ALL THE DIFFERENT TYPES OF CARD COULD BE PLACED IN THE GAME
    def check_card_placement(self, i, card_number, card_type, j, neighbor_card_number, neighbor_card_type, is_sub_card, unknowns=0, move_type="", priority=0):
        card_number_string, scan = self.variable_check(card_number, unknowns)

        if card_number <= 13 and priority == 0:
            # CHECKS IF THE CARD CAN BE PLACED ONTO THE FOUNDATION
            exists_in_foundation = self.check_foundation_card_pile(card_number, card_type)
            # IF IT ISN'T A SUB CARD AND IT COULD BE PLACED ON THE FOUNDATION, WE CREATE A MOVE
            if not is_sub_card:
                if exists_in_foundation > -1:
                    self.create_move(card_number_string, card_type, i, exists_in_foundation, "F", move_type, scan)
                    return True
            # IF IT'S A KING AND IT HAS UNKNOWN CARDS UNDERNEATH IT, WE CREATE A MOVE
            if neighbor_card_type == "-1" and neighbor_card_number == -1 and card_number == 13 and (
                    unknowns > 0 or move_type == "W"):
                self.create_move(card_number_string, card_type, i, j, "T", move_type, scan)
                return True
            # IF THERE IS A NEIGHBOUR AND THE CARD TYPES AND NUMBERS MATCH, WE CREATE A MOVE
            if neighbor_card_number > 0:
                if self.check_card_type_matches(card_type, neighbor_card_type, 0):
                    if neighbor_card_number - 1 == card_number:
                        self.create_move(card_number_string, card_type, i, j, "T", move_type, scan)
                        return True
        return False

    # SIMPLE METHOD THAT DEFINES THE CARD TYPES AND NUMBERS WITH USE OF THE LISTS AND THEIR INDEX LOCATIONS
    def define_card(self, i, k, pile_type):
        if pile_type == "T" or pile_type == "F":
            if pile_type == "T":
                card_pile = self.logicTableauCardPiles.get(i)[k]
            else:
                card_pile = self.logicFoundationCardPiles.get(i)[k]
        else:
            card_pile = self.logicWasteCardPile[i]
        current_card = card_pile.split()
        current_card_number = int(current_card[0])
        current_card_type = current_card[1]
        return current_card_number, current_card_type, card_pile

    # CREATES A MOVE BY APPENDING THE INFORMATION NEEDED TO THE RESULT VARIABLE AND RESETS THE LOSE COUNTER
    def create_move(self, card_number_string, card_type, i, j, move_from, move_type, scan):
        self.loseCounter = 0

        self.result.append(card_number_string)
        self.result.append(card_type)
        self.result.append(str(i))
        self.result.append(str(j))
        self.result.append(move_from)
        self.result.append(move_type)
        self.result.append(scan)

    # CHECKS IF A CARD CAN BE PLACED ON THE FOUNDATION PILE
    def check_foundation_card_pile(self, card_number, card_type):
        # ITERATES THROUGH THE 4 FOUNDATION PILES
        for i in range(4):
            if len(self.logicFoundationCardPiles.get(i)) != 0:

                foundation_card_number, foundation_card_type, _ = self.define_card(i, 0, "F")
                # CHECKS IF THE TYPES MATCH AND IF THE CURRENT CARD NUMBER IS 1 BIGGER THAN THE ONE ON THE FOUNDATION
                if foundation_card_type == card_type and foundation_card_number + 1 == card_number:
                    return i

            else:
                # IF THERE IS AN ACE AND AN EMPTY SPOT, WE ADD IT TO THIS FOUNDATION PILE
                if card_number == 1:
                    return i
        return -1

    # CHECKS WIN CONDITION BY SEEING IF ALL 52 CARDS ARE IN THE FOUNDATION PILES
    def check_win_condition(self):
        foundation_one = len(self.logicFoundationCardPiles.get(0))
        foundation_two = len(self.logicFoundationCardPiles.get(1))
        foundation_three = len(self.logicFoundationCardPiles.get(2))
        foundation_four = len(self.logicFoundationCardPiles.get(3))

        if foundation_one + foundation_two + foundation_three + foundation_four == 52:
            for i in range(7):
                self.result.append("WIN")
            return True
        return False

    # CHECKS LOSE CONDITION BY COUNTING HOW MANY TIMES THERE HAS BEEN AN "NA" MOVE COMPARED TO HOW MANY EXTRA WASTE CARDS THERE ARE LEFT
    def check_lose_condition(self):
        if self.loseCounter > len(self.logicWasteCardPile) + 1 and self.unknownWaste == 0:
            for i in range(7):
                self.result.append("LOSE")
            return True
        return False

    # AN EASY WAY TO RESET THE LOGIC AND STARTING ANEW
    def reset_logic(self, logic_waste_card, logic_tableau_card_piles, logic_foundation_card_piles):
        self.reset = True
        return self.update_logic_scan(logic_waste_card, logic_tableau_card_piles, logic_foundation_card_piles)

    # METHOD TO GET PILES TO THE COMPUTER VISION PART
    def get_piles(self):
        return self.logicTableauCardPiles, self.logicFoundationCardPiles, self.logicWasteCardPile

    # CHECKS IF THE VARIABLE IS WRITTEN AS INTENDED E.G. 1 SHOULD BE 01 AND 10 IS STILL 10
    def variable_check(self, card_number, unknowns):
        card_number_string = str(card_number)
        if card_number < 10:
            card_number_string = "0" + card_number_string
        if unknowns == -1:
            scan = "NO"
        elif unknowns == -2:
            scan = "TOPCARD"
        else:
            scan = "YES"
        return card_number_string, scan

    # DEFINES HOW MANY CARDS SHOULD BE MOVED, BY ITERATING THROUGH THE TABLEAU UNTIL FINDING THE CARD AND ADDING/REMOVING THE REST FROM THE LISTS
    def check_how_many_cards_to_move(self, move_from_list, moved_card, tableau_pile_moved_from, tableau_pile_moved_to):
        for i in range(len(tableau_pile_moved_from) - 1, -1, -1):
            if tableau_pile_moved_from[i] == moved_card:
                move_from_list = True
            if move_from_list:
                tableau_pile_moved_to.append(tableau_pile_moved_from[i])
                tableau_pile_moved_from.pop(i)

    # CHECKS IF A CARD TYPE MATCHES OR CAN BE PLACED ON A PILE DEFINED BY THE RULES
    def check_card_type_matches(self, card_type, neighbor_card_type, n=0):
        if n == 0:
            if ((card_type == "d" or card_type == "h") and (neighbor_card_type == "c" or neighbor_card_type == "s")) or \
                    ((card_type == "c" or card_type == "s") and (
                            neighbor_card_type == "d" or neighbor_card_type == "h")):
                return True
        if n == 1:
            if ((card_type == "d" or card_type == "h") and (neighbor_card_type == "d" or neighbor_card_type == "h")) or \
                    ((card_type == "c" or card_type == "s") and (
                            neighbor_card_type == "c" or neighbor_card_type == "s")):
                return True
        return False

    # SIMPLE COUNTER THAT COUNTS HOW MANY TABLEAU UNKNOWNS ARE LEFT
    def how_many_unknowns_left(self):
        unknowns = 0
        for i in range(len(self.unknownTableau)):
            unknowns += self.unknownTableau[i]
        return unknowns