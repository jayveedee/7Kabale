class GameLogic:

    def __init__(self, logic_waste_card, logic_tableau_card_piles, logic_foundation_card_piles):
        self.logicWasteCard = []
        self.logicTableauCardPiles = {}
        self.logicFoundationCardPiles = {}
        self.unknownWaste = 0
        self.unknownTableau = []
        self.reset = True
        self.result = []
        self.updateLogicR(logic_waste_card, logic_tableau_card_piles, logic_foundation_card_piles)

    def updateLogicR(self, logic_waste_card=None, logic_tableau_card_piles=None, logic_foundation_card_piles=None):

        # IF THE LISTS DO NOT EXIST OR IF THE RESET METHOD HAS BEEN CALLED, THE BELOW FUNCTION WILL RESET/INITIALIZE
        # THE OBJECT INSTANCE VARIABLES
        if (
                self.logicTableauCardPiles is None and self.logicFoundationCardPiles is None and self.logicWasteCard is None) or (
                self.reset is True):
            self.logicWasteCard = logic_waste_card
            self.logicTableauCardPiles = logic_tableau_card_piles
            self.logicFoundationCardPiles = logic_foundation_card_piles
            self.unknownWaste = 24
            for i in range(7):
                counter = 0
                for j in range(i):
                    counter += 1
                self.unknownTableau.append(counter)
            self.reset = False

        # IF THE LISTS EXIST, WE UPDATE THE LISTS WITH THE NEW INFORMATION WITHOUT ERASING ANYTHING
        else:

            # UPDATING THE WASTE CARD
            if logic_waste_card is not None and len(logic_waste_card) != 0:
                if len(logic_waste_card) < len(self.logicWasteCard):
                    self.logicWasteCard.pop(len(self.logicWasteCard) - 1)
                elif len(logic_waste_card) > len(self.logicWasteCard):
                    for i in range(len(logic_waste_card)):
                        self.logicWasteCard.append(logic_waste_card[i])
                else:
                    self.logicWasteCard = logic_waste_card

            # UPDATING THE TABLEAU LIST WITH THE NEW CARDS
            if logic_tableau_card_piles is not None:
                self.checkListConsistency(logic_tableau_card_piles, self.logicTableauCardPiles)

            # UPDATING THE FOUNDATION LIST WITH THE NEW CARDS
            if logic_foundation_card_piles is not None:
                self.checkListConsistency(logic_foundation_card_piles, self.logicFoundationCardPiles)

        return self.logicWasteCard, self.logicTableauCardPiles, self.logicFoundationCardPiles

    def checkListConsistency(self, list_one, list_two):
        for i in range(0, len(list_one)):

            if len(list_one.get(i)) != len(list_two.get(i)):
                if len(list_one.get(i)) != 0:
                    if len(list_two.get(i)) == 0:
                        list_two[i] = list_one.get(i)
                    else:
                        list_two.get(i).append(list_one.get(i)[0])
                        if list_two == self.logicTableauCardPiles:
                            list_two.get(i).sort(reverse=False)
                        else:
                            list_two.get(i).sort(reverse=True)
            elif len(list_one.get(i)) != 0 and len(list_two.get(i)) != 0:
                if list_one.get(i)[0] != list_two.get(i)[0]:
                    list_two.get(i).append(list_one.get(i)[0])
                    if list_two == self.logicTableauCardPiles:
                        list_two.get(i).sort(reverse=False)
                    else:
                        list_two.get(i).sort(reverse=True)

        return list_two

    def resetLogic(self, logic_waste_card, logic_tableau_card_piles, logic_foundation_card_piles):

        # RESET METHOD TO RESTART THE GAME
        self.reset = True
        return self.updateLogicR(logic_waste_card, logic_tableau_card_piles, logic_foundation_card_piles)

    def updateLogicM(self, move):

        # UPDATE LOGIC GLOBAL VARIABLES
        self.result = []

        # IF THERE WAS NO MOVE SPECIFIED, NOTHING CHANGES
        if move != ["NA", "NA", "NA", "NA", "NA"]:

            # DEFINE THE CARD BEING MOVED AND WHERE TO
            move_from_list = False
            moved_card = move[0] + " " + move[1]
            card_pile_moved_from = int(move[2])
            card_pile_moved_to = int(move[3])
            card_placement = move[4]
            move_type = move[5]
            scan = move[6]

            # UPDATE THE CARD PILE UNKNOWNS UNDER THE CARD BEING MOVED. THIS MEANS THE CARD SHOULD'VE BEEN SCANNED BY
            # NOW
            if scan == "YES":
                if move_type == "W":
                    self.unknownWaste -= 1
                else:
                    self.unknownTableau[card_pile_moved_from] -= 1

            # IF THE CARD SHOULD BE PLACED ON THE TABLEAU, WE ENTER THIS PART
            if card_placement == "T":

                # CHECKS WHETHER THE CARD IS A WASTE CARD OR NOT
                if card_pile_moved_from != -1:

                    # ITERATES THROUGH THE TABLEAU PILE TO SEE IF THERE IS A CARD BENEATH THE CARD BEING MOVED
                    for i in range(len(self.logicTableauCardPiles.get(card_pile_moved_from)) - 1, -1, -1):
                        if self.logicTableauCardPiles.get(card_pile_moved_from)[i] == moved_card:
                            move_from_list = True

                        # IF WE'VE FOUND THE CARD, THE STATEMENT BELOW WILL BECOME TRUE AND WE ADD THE CURRENT CARD AND
                        # THE ONES BELOW IT TO THE OTHER PILE, AFTERWARDS THE CARDS WILL BE DELETED FROM THE MOVED FROM
                        # PILE
                        if move_from_list:
                            self.logicTableauCardPiles.get(card_pile_moved_to).append \
                                (self.logicTableauCardPiles.get(card_pile_moved_from)[i])
                            self.logicTableauCardPiles.get(card_pile_moved_from).pop(i)

                # IF IT'S A WASTE CARD, WE USE THE WASTE CARD STRING ARRAY
                else:
                    waste_card_array = self.logicWasteCard[len(self.logicWasteCard) - 1]
                    self.logicTableauCardPiles.get(card_pile_moved_to).append \
                        (waste_card_array[0] + " " + waste_card_array[1])
                    self.logicWasteCard.remove(waste_card_array)

                # SORTS THE PILE SO THAT THE SMALLEST NUMBER IS THE FIRST INDEX
                self.logicTableauCardPiles.get(card_pile_moved_to).sort(reverse=False)
                return self.logicTableauCardPiles.get(card_pile_moved_to)

            # IF THE CARD SHOULD BE PLACED ON THE FOUNDATION, WE ENTER HERE
            if card_placement == "F":

                # CHECKS WHETHER THE CARD IS A WASTE CARD OR NOT
                if card_pile_moved_from != -1:

                    # TAKES THE CARD FROM THE TABLEAU AND MOVES IT ONTO THE FOUNDATION, DELETING THE CARD FROM THE
                    # PREVIOUS PILE IN THE PROCESS
                    if self.logicTableauCardPiles.get(card_pile_moved_from)[0] == moved_card:
                        self.logicFoundationCardPiles.get(card_pile_moved_to).append \
                            (self.logicTableauCardPiles.get(card_pile_moved_from)[0])
                        self.logicTableauCardPiles.get(card_pile_moved_from).pop(0)

                # IF IT'S A WASTE CARD, WE USE THE WASTE CARD STRING ARRAY
                else:
                    waste_card_array = self.logicWasteCard[len(self.logicWasteCard) - 1]
                    self.logicFoundationCardPiles.get(card_pile_moved_to).append \
                        (waste_card_array[0] + " " + waste_card_array[1])
                    self.logicWasteCard.remove(waste_card_array)

                # SORTS THE PILE SO THAT THE BIGGEST NUMBER IS THE FIRST INDEX
                self.logicFoundationCardPiles.get(card_pile_moved_to).sort(reverse=True)
                return self.logicFoundationCardPiles.get(card_pile_moved_to)

        return ["NA", "NA", "NA", "NA", "NA"]

    def calculateMove(self):

        # FOR LOOP THAT ITERATES THROUGH EVERY PILE OF CARDS IN THE TABLEAU SECTION
        for i in range(len(self.logicTableauCardPiles)):

            # CHECK IF CURRENT PILE IS NOT EMPTY
            if len(self.logicTableauCardPiles.get(i)) > 0:

                # DEFINE WHAT CARD NUMBER & TYPE THE CURRENT CARD IS
                current_tableau_card_pile = self.logicTableauCardPiles.get(i)[0]
                current_card_array = current_tableau_card_pile.split()
                current_card_number = int(current_card_array[0])
                current_card_type = current_card_array[1]

                # FOR LOOP THAT ITERATES THROUGH EVERY NEIGHBOUR AND COMPARES IT TO THE CURRENT CARD
                for j in range(len(self.logicTableauCardPiles)):

                    # CHECKS EMPTY SPACES ON FOUNDATION & TABLEAU, RETURNS A RESULT ARRAY IF A KING CAN BE PLACED ON ONE
                    # OF THEM
                    if len(self.logicTableauCardPiles.get(j)) == 0:
                        if len(self.logicTableauCardPiles.get(i)) > 1 or self.unknownTableau[i] > 0:
                            if self.checkCardPlacement(i, current_card_number, current_card_type, j, -1, "-1", False, self.unknownTableau[i], "T"):
                                return self.result
                            else:
                                for k in range(len(self.logicTableauCardPiles.get(i)) - 1, 0, -1):

                                    # DEFINE CURRENT SUB CARD IN THE CURRENT PILE
                                    tableau_card_pile = self.logicTableauCardPiles.get(i)[k]
                                    tableau_card_pile_array = tableau_card_pile.split()
                                    tableau_card_pile_card_number = int(tableau_card_pile_array[0])
                                    tableau_card_pile_card_type = tableau_card_pile_array[1]

                                    if self.checkCardPlacement(i, tableau_card_pile_card_number, tableau_card_pile_card_type, j, -1, "-1", False, self.unknownTableau[i], "T"):
                                        return self.result

                    # IF WE DO NOT HAVE A KING, WE CHECK THE OTHER OPTIONS FOR ALL OTHER CARDS
                    else:
                        if self.logicTableauCardPiles.get(i)[0] != self.logicTableauCardPiles.get(j)[0]:

                            # CHECKS IF THERE ARE OTHER UNKNOWN CARDS UNDER THE CURRENT CARD
                            unknowns = self.unknownTableau[i]
                            if len(self.logicTableauCardPiles.get(i)) > 1:
                                unknowns = 0

                            # DEFINE WHAT CARD NUMBER & TYPE THE NEIGHBOR CARD IS
                            next_tableau_card_pile = self.logicTableauCardPiles.get(j)[0]
                            next_card_array = next_tableau_card_pile.split()
                            next_card_number = int(next_card_array[0])
                            next_card_type = next_card_array[1]

                            if self.logicTableauCardPiles.get(i)[0] is not None:
                                for k in range(len(self.logicTableauCardPiles.get(i)) - 1, 0, -1):

                                    # DEFINE CURRENT SUB CARD IN THE CURRENT PILE
                                    tableau_card_pile = self.logicTableauCardPiles.get(i)[k]
                                    tableau_card_pile_array = tableau_card_pile.split()
                                    tableau_card_pile_card_number = int(tableau_card_pile_array[0])
                                    tableau_card_pile_card_type = tableau_card_pile_array[1]

                                    # CHECK IF THERE ARE UNKNOWNS BENEATH PILE IF WE'RE MOVING THE WHOLE PILE
                                    if k == len(self.logicTableauCardPiles.get(i)) - 1:
                                        unknowns = self.unknownTableau[i]
                                    else:
                                        unknowns = 0

                                    # CHECKS WHETHER A SUB CARD IN A PILE CAN BE MOVED TO ANOTHER PILE SOMEWHERE ELSE
                                    # ON THE TABLEAU

                                    if self.checkCardPlacement(i, tableau_card_pile_card_number, tableau_card_pile_card_type, j, next_card_number, next_card_type, True, unknowns, "T"):
                                        return self.result

                            # PREVENTS THE LOGIC MAKING USELESS MOVES SUCH AS MOVING A CARD BETWEEN TWO PILES WITHOUT
                            # CHANGING ANYTHING, INSTEAD FOCUS ON THE NEXT CARD THAT COULD MAKE A DIFFERENCE IN THE GAME
                            if len(self.logicTableauCardPiles.get(i)) > 1:

                                # DEFINE THE CURRENT SUB CARD AND ITS NEIGHBOR CARD
                                curr_sub_pile = self.logicTableauCardPiles.get(i)[0]
                                curr_sub_pile_array = curr_sub_pile.split()
                                neigh_sub_pile = self.logicTableauCardPiles.get(j)[0]
                                neigh_sub_pile_array = neigh_sub_pile.split()

                                if int(curr_sub_pile_array[0]) + 1 != int(neigh_sub_pile_array[0]):
                                    if self.checkCardPlacement(i, current_card_number, current_card_type, j, next_card_number, next_card_type, False, self.unknownTableau[i], "T"):
                                        return self.result

                            # CHECKS IF A CARD ON TOP OF THE PILE CAN BE PLACED ANYWHERE IN THE FOUNDATION OR
                            # NEIGHBOR TABLEAU PILE
                            elif self.checkCardPlacement(i, current_card_number, current_card_type, j, next_card_number, next_card_type, False, unknowns, "T"):
                                return self.result

        # CHECKS IF THERE EXISTS A WASTE CARD
        if self.logicWasteCard is not None:
            if len(self.logicWasteCard) != 0:

                # DEFINE WASTE CARD NUMBER AND TYPE
                waste_card_array = self.logicWasteCard[len(self.logicWasteCard) - 1]
                waste_card_number = int(waste_card_array[0])
                waste_card_type = waste_card_array[1]

                # ITERATE THROUGH CARD PILES TO SEE IF WASTE CARD CAN BE PLACED SOMEWHERE
                for i in range(len(self.logicTableauCardPiles)):

                    if len(self.logicTableauCardPiles.get(i)) > 0:

                        # DEFINE NEIGHBOR CARDS
                        next_tableau_card_pile = self.logicTableauCardPiles.get(i)[0]
                        next_card_array = next_tableau_card_pile.split()
                        next_card_number = int(next_card_array[0])
                        next_card_type = next_card_array[1]

                        # CHECKS IF WASTE CARD CAN BE PLACED ON CURRENT PILE IN THE LIST
                        if self.checkCardPlacement(-1, waste_card_number, waste_card_type, i, next_card_number,
                                                   next_card_type,
                                                   False, self.unknownWaste, "W"):
                            return self.result

        return ["NA", "NA", "NA", "NA", "NA"]

    def checkCardPlacement(self, i, card_number, card_type, j, neighbor_card_number, neighbor_card_type, is_sub_card,
                           unknowns=0, move_type=""):

        # IF UNKNOWNS IS ZERO, THAT MEANS THERE ARE NO OTHER CARDS BENEATH THE CURRENT CARD
        if unknowns == 0:
            scan = "NO"
        else:
            scan = "YES"

        if card_number <= 13:

            # CHECKS IF CURRENT CARD IS A SUB CARD OR NOT
            if not is_sub_card or (card_number == 13 and unknowns != 0):

                # ITERATES THROUGH FOUNDATION PILES TO SEE IF CURRENT CARD CAN BE PLACED THERE
                exists_in_foundation = self.checkFoundationCardPile(card_number, card_type)

                # IF IT CAN BE PLACED IN THE FOUNDATION, THE VALUE WILL BE BETWEEN 0-3
                if exists_in_foundation > -1:
                    self.result.append(str(card_number))
                    self.result.append(card_type)
                    self.result.append(str(i))
                    self.result.append(str(exists_in_foundation))
                    self.result.append("F")
                    self.result.append(move_type)
                    self.result.append(scan)
                    return True

                # THE -1 SPECIFIES IF THE LAST PILE WAS EMPTY AND IT ALSO CHECKS IF TRE CURRENT CARD IS A KING. IF IT
                # IS, THEN WE CAN PLACE A KING THERE
                elif neighbor_card_type == "-1" and neighbor_card_number == -1 and card_number == 13:
                    self.result.append(str(card_number))
                    self.result.append(card_type)
                    self.result.append(str(i))
                    self.result.append(str(j))
                    self.result.append("T")
                    self.result.append(move_type)
                    self.result.append(scan)
                    return True

            # IF THERE WAS A NEIGHBOUR, THE VALUE WILL BE BIGGER THAN 0 AND THEREFORE WE WILL CHECK IF THE CURRENT
            # CARD CAN BE PLACED ON TOP OF A NEIGHBOUR CARD
            if neighbor_card_number > 0:

                # CHECKS IF THE TYPES OF BOTH CARDS MATCH TOGETHER r+h<->k+s k+s<->r+h
                if ((card_type == "d" or card_type == "h") and (
                        neighbor_card_type == "c" or neighbor_card_type == "s")) or \
                        ((card_type == "c" or card_type == "s") and (
                                neighbor_card_type == "d" or neighbor_card_type == "h")):

                    # CHECKS IF THE NUMBER OF THE NEIGHBOUR CARD IS 1 HIGHER THAN THE CURRENT CARD. IF IT IS,
                    # WE CAN THEN PLACE THE CURRENT CARD ON THE NEIGHBOUR CARD
                    if neighbor_card_number - 1 == card_number:
                        self.result.append(str(card_number))
                        self.result.append(card_type)
                        self.result.append(str(i))
                        self.result.append(str(j))
                        self.result.append("T")
                        self.result.append(move_type)
                        self.result.append(scan)
                        return True
        return False

    def checkFoundationCardPile(self, card_number, card_type):

        # ITERATES THROUGH THE FOUNDATION PILES
        for i in range(4):
            if len(self.logicFoundationCardPiles.get(i)) != 0:

                # DEFINES THE CURRENT FOUNDATION CARD
                foundation_card_pile = self.logicFoundationCardPiles.get(i)[0]
                foundation_array = foundation_card_pile.split()
                foundation_card_number = int(foundation_array[0])
                foundation_card_type = foundation_array[1]

                # IF CARD OF FOUNDATION AND THE CURRENT CARD TYPE MATCHES AND CURRENT CARD NUMBER IS 1 BIGGER THAN
                # FOUNDATION, THEN WE CAN PLACE IT ON THIS FOUNDATION PILE
                if foundation_card_type == card_type and foundation_card_number + 1 == card_number:
                    return i

            else:

                # IF THE CARD IS AN ACE, PLACE THE CARD ON THIS FOUNDATION PILE
                if card_number == 1:
                    return i

        # IF THE CARD CANNOT BE PLACED ON THE FOUNDATION PILES, RETURN -1
        return -1
