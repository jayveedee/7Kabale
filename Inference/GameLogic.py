class GameLogic:

    def __init__(self, logicWasteCard, logicTableauCardPiles, logicFoundationCardPiles):
        self.logicWasteCard = [[]]
        self.logicTableauCardPiles = {}
        self.logicFoundationCardPiles = {}
        self.reset = True
        self.result = []
        self.updateLogicR(logicWasteCard, logicTableauCardPiles, logicFoundationCardPiles)

    def updateLogicR(self, logicWasteCard, logicTableauCardPiles, logicFoundationCardPiles):

        # IF THE LISTS DO NOT EXIST OR IF THE RESET METHOD HAS BEEN CALLED, THE BELOW FUNCTION WILL RESET/INITIALIZE
        # THE OBJECT INSTANCE VARIABLES
        if (
                self.logicTableauCardPiles is None and self.logicFoundationCardPiles is None and self.logicWasteCard is None) or (
                self.reset is True):
            self.logicWasteCard = logicWasteCard
            self.logicTableauCardPiles = logicTableauCardPiles
            self.logicFoundationCardPiles = logicFoundationCardPiles
            self.reset = False

        # IF THE LISTS EXIST, WE UPDATE THE LISTS WITH THE NEW INFORMATION WITHOUT ERASING ANYTHING
        else:

            # UPDATING THE WASTE CARD
            if logicWasteCard is not None and len(logicWasteCard) != 0:
                if len(logicWasteCard) < len(self.logicWasteCard):
                    self.logicWasteCard.pop(len(self.logicWasteCard) - 1)
                elif len(logicWasteCard) > len(self.logicWasteCard):
                    for i in range(len(logicWasteCard)):
                        self.logicWasteCard.append(logicWasteCard[i])
                else:
                    self.logicWasteCard = logicWasteCard

            # UPDATING THE TABLEAU LIST WITH THE NEW CARDS
            self.checkListConsistency(logicTableauCardPiles, self.logicTableauCardPiles)

            # UPDATING THE FOUNDATION LIST WITH THE NEW CARDS
            self.checkListConsistency(logicFoundationCardPiles, self.logicFoundationCardPiles)

        return self.logicWasteCard, self.logicTableauCardPiles, self.logicFoundationCardPiles

    def checkListConsistency(self, listOne, listTwo):
        for i in range(0, len(listOne)):

            if len(listOne.get(i)) != len(listTwo.get(i)):
                if len(listOne.get(i)) != 0:
                    if len(listTwo.get(i)) == 0:
                        listTwo[i] = listOne.get(i)
                    else:
                        listTwo.get(i).append(listOne.get(i)[0])
                        listTwo.get(i).sort(reverse=False)
            elif len(listOne.get(i)) != 0 and len(listTwo.get(i)) != 0:
                if listOne.get(i)[0] != listTwo.get(i)[0]:
                    listTwo.get(i).append(listOne.get(i)[0])
                    listTwo.get(i).sort(reverse=False)

        return listTwo

    def resetLogic(self, logicWasteCard, logicTableauCardPiles, logicFoundationCardPiles):

        # RESET METHOD TO RESTART THE GAME
        self.reset = True
        return self.updateLogicR(logicWasteCard, logicTableauCardPiles, logicFoundationCardPiles)

    def updateLogicM(self, move):

        # UPDATE LOGIC GLOBAL VARIABLES
        self.result = []

        # IF THERE WAS NO MOVE SPECIFIED, NOTHING CHANGES
        if move != ["NA", "NA", "NA", "NA", "NA"]:

            # DEFINE THE CARD BEING MOVED AND WHERE TO
            moveFromList = False
            movedCard = move[0] + " " + move[1]
            cardPileMovedFrom = int(move[2])
            cardPileMovedTo = int(move[3])
            cardPlacement = move[4]

            # IF THE CARD SHOULD BE PLACED ON THE TABLEAU, WE ENTER THIS PART
            if cardPlacement == "T":

                # CHECKS WHETHER THE CARD IS A WASTE CARD OR NOT
                if cardPileMovedFrom != -1:

                    # ITERATES THROUGH THE TABLEAU PILE TO SEE IF THERE IS A CARD BENEATH THE CARD BEING MOVED
                    for i in range(len(self.logicTableauCardPiles.get(cardPileMovedFrom)) - 1, -1, -1):
                        if self.logicTableauCardPiles.get(cardPileMovedFrom)[i] == movedCard:
                            moveFromList = True

                        # IF WE'VE FOUND THE CARD, THE STATEMENT BELOW WILL BECOME TRUE AND WE ADD THE CURRENT CARD AND
                        # THE ONES BELOW IT TO THE OTHER PILE, AFTERWARDS THE CARDS WILL BE DELETED FROM THE MOVED FROM
                        # PILE
                        if moveFromList:
                            self.logicTableauCardPiles.get(cardPileMovedTo).append \
                                (self.logicTableauCardPiles.get(cardPileMovedFrom)[i])
                            self.logicTableauCardPiles.get(cardPileMovedFrom).pop(i)

                # IF IT'S A WASTE CARD, WE USE THE WASTE CARD STRING ARRAY
                else:
                    wasteCardArray = self.logicWasteCard[len(self.logicWasteCard) - 1]
                    self.logicTableauCardPiles.get(cardPileMovedTo).append \
                        (wasteCardArray[0] + " " + wasteCardArray[1])
                    self.logicWasteCard.remove(wasteCardArray)

                # SORTS THE PILE SO THAT THE SMALLEST NUMBER IS THE FIRST INDEX
                self.logicTableauCardPiles.get(cardPileMovedTo).sort(reverse=False)
                return self.logicTableauCardPiles.get(cardPileMovedTo)

            # IF THE CARD SHOULD BE PLACED ON THE FOUNDATION, WE ENTER HERE
            if cardPlacement == "F":

                # CHECKS WHETHER THE CARD IS A WASTE CARD OR NOT
                if cardPileMovedFrom != -1:

                    # TAKES THE CARD FROM THE TABLEAU AND MOVES IT ONTO THE FOUNDATION, DELETING THE CARD FROM THE
                    # PREVIOUS PILE IN THE PROCESS
                    if self.logicTableauCardPiles.get(cardPileMovedFrom)[0] == movedCard:
                        self.logicFoundationCardPiles.get(cardPileMovedTo).append \
                            (self.logicTableauCardPiles.get(cardPileMovedFrom)[0])
                        self.logicTableauCardPiles.get(cardPileMovedFrom).pop(0)

                # IF IT'S A WASTE CARD, WE USE THE WASTE CARD STRING ARRAY
                else:
                    wasteCardArray = self.logicWasteCard[len(self.logicWasteCard) - 1]
                    self.logicFoundationCardPiles.get(cardPileMovedTo).append \
                        (wasteCardArray[0] + " " + wasteCardArray[1])
                    self.logicWasteCard.remove(wasteCardArray)

                # SORTS THE PILE SO THAT THE BIGGEST NUMBER IS THE FIRST INDEX
                self.logicFoundationCardPiles.get(cardPileMovedTo).sort(reverse=True)
                return self.logicFoundationCardPiles.get(cardPileMovedTo)

        return ["NA", "NA", "NA", "NA", "NA"]

    def calculateMove(self):

        # FOR LOOP THAT ITERATES THROUGH EVERY PILE OF CARDS IN THE TABLEAU SECTION
        for i in range(len(self.logicTableauCardPiles)):

            # CHECK IF CURRENT PILE IS EMPTY
            if len(self.logicTableauCardPiles.get(i)) > 0:

                # DEFINE WHAT CARD NUMBER & TYPE THE CURRENT CARD IS
                currentTableauCardPile = self.logicTableauCardPiles.get(i)[0]
                currentCardArray = currentTableauCardPile.split()
                currentCardNumber = int(currentCardArray[0])
                currentCardType = currentCardArray[1]

                # FOR LOOP THAT ITERATES THROUGH EVERY NEIGHBOUR AND COMPARES IT TO THE CURRENT CARD
                for j in range(len(self.logicTableauCardPiles)):

                    # CHECKS EMPTY SPACES ON FOUNDATION & TABLEAU, RETURNS A STRING IF A KING CAN BE PLACED ON ONE OF
                    # THEM
                    if len(self.logicTableauCardPiles.get(j)) == 0:
                        if len(self.logicTableauCardPiles.get(i)) > 1:
                            if self.checkCardPlacement(i, currentCardNumber, currentCardType, j, -1, "-1", False):
                                return self.result

                    else:
                        if self.logicTableauCardPiles.get(i)[0] != self.logicTableauCardPiles.get(j)[0]:

                            # DEFINE WHAT CARD NUMBER & TYPE THE NEIGHBOR CARD IS
                            nextTableauCardPile = self.logicTableauCardPiles.get(j)[0]
                            nextCardArray = nextTableauCardPile.split()
                            nextCardNumber = int(nextCardArray[0])
                            nextCardType = nextCardArray[1]

                            if self.logicTableauCardPiles.get(i)[0] is not None:
                                for k in range(len(self.logicTableauCardPiles.get(i)) - 1, 0, -1):

                                    # DEFINE CURRENT CARD IN THE CURRENT PILE
                                    tableauCardPile = self.logicTableauCardPiles.get(i)[k]
                                    tableauCardPileArray = tableauCardPile.split()
                                    tableauCardPileCardNumber = int(tableauCardPileArray[0])
                                    tableauCardPileCardType = tableauCardPileArray[1]

                                    # CHECKS WHETHER A SUBCARD IN A PILE CAN BE MOVED TO ANOTHER PILE SOMEWHERE ELSE
                                    # ON THE TABLEAU

                                    if self.checkCardPlacement(i, tableauCardPileCardNumber, tableauCardPileCardType, j,
                                                               nextCardNumber, nextCardType, True):
                                        return self.result

                            # PREVENTS THE LOGIC MAKING USELESS MOVES SUCH AS MOVING A CARD BETWEEN TWO PILES WITHOUT
                            # CHANGING ANYTHING, INSTEAD FOCUS ON THE NEXT CARD THAT COULD MAKE A DIFFERENCE IN THE GAME
                            if len(self.logicTableauCardPiles.get(i)) > 1 and len(
                                    self.logicTableauCardPiles.get(j)) > 1:
                                currSubPile = self.logicTableauCardPiles.get(i)[0]
                                currSubPileArray = currSubPile.split()
                                neigSubPile = self.logicTableauCardPiles.get(j)[0]
                                neigSubPileArray = neigSubPile.split()
                                if int(currSubPileArray[0]) + 1 != int(neigSubPileArray[0]):
                                    if self.checkCardPlacement(i, currentCardNumber, currentCardType, j, nextCardNumber,
                                                               nextCardType, False):
                                        return self.result

                            # CHECKS IF A CARD ON TOP OF THE PILE CAN BE PLACED ANYWHERE IN THE FOUNDATION OR
                            # NEIGHBOR TABLEAU PILE
                            elif self.checkCardPlacement(i, currentCardNumber, currentCardType, j, nextCardNumber,
                                                         nextCardType, False):
                                return self.result

        # CHECKS IF THERE EXISTS A WASTE CARD
        if self.logicWasteCard is not None:
            if len(self.logicWasteCard) != 0:

                # DEFINE WASTE CARD NUMBER AND TYPE
                wasteCardTableauPile = self.logicWasteCard[len(self.logicWasteCard) - 1]
                wasteCardArray = wasteCardTableauPile.split()
                wasteCardNumber = int(wasteCardArray[0])
                wasteCardType = wasteCardArray[1]

                # ITERATE THROUGH CARD PILES TO SEE IF WASTE CARD CAN BE PLACED SOMEWHERE
                for i in range(len(self.logicTableauCardPiles)):

                    if len(self.logicTableauCardPiles.get(i)) > 0:

                        # DEFINE NEIGHBOR CARDS
                        nextTableauCardPile = self.logicTableauCardPiles.get(i)[0]
                        nextCardArray = nextTableauCardPile.split()
                        nextCardNumber = int(nextCardArray[0])
                        nextCardType = nextCardArray[1]

                        # CHECKS IF WASTE CARD CAN BE PLACED ON CURRENT PILE IN THE LIST
                        if self.checkCardPlacement(-1, wasteCardNumber, wasteCardType, i, nextCardNumber, nextCardType,
                                                   False):
                            return self.result

        return ["NA", "NA", "NA", "NA", "NA"]

    def checkCardPlacement(self, i, cardNumber, cardType, j, neighborCardNumber, neighborCardType, isSubCard):

        if cardNumber <= 13:

            # CHECKS IF CURRENT CARD IS A SUBCARD OR NOT
            if not isSubCard:

                # ITERATES THROUGH FOUNDATION PILES TO SEE IF CURRENT CARD CAN BE PLACED THERE
                existsInFoundation = self.checkFoundationCardPile(cardNumber, cardType)

                # IF IT CAN BE PLACED IN THE FOUNDATION, THE VALUE WILL BE BETWEEN 0-3
                if existsInFoundation > -1:
                    self.result.append(str(cardNumber))
                    self.result.append(cardType)
                    self.result.append(str(i))
                    self.result.append(str(existsInFoundation))
                    self.result.append("F")
                    return True

                # THE -1 SPECIFIES IF THE LAST PILE WAS EMPTY AND IT ALSO CHECKS IF TRE CURRENT CARD IS A KING. IF IT
                # IS, THEN WE CAN PLACE A KING THERE
                elif neighborCardType == "-1" and neighborCardNumber == -1 and cardNumber == 13:
                    self.result.append(str(cardNumber))
                    self.result.append(cardType)
                    self.result.append(str(i))
                    self.result.append(str(j))
                    self.result.append("T")
                    return True

            # IF THERE WAS A NEIGHBOUR, THE VALUE WILL BE BIGGER THAN 0 AND THEREFORE WE WILL CHECK IF THE CURRENT
            # CARD CAN BE PLACED ON TOP OF A NEIGHBOUR CARD
            if neighborCardNumber > 0:

                # CHECKS IF THE TYPES OF BOTH CARDS MATCH TOGETHER r+h<->k+s k+s<->r+h
                if ((cardType == "d" or cardType == "h") and (neighborCardType == "c" or neighborCardType == "s")) or \
                        ((cardType == "c" or cardType == "s") and (neighborCardType == "d" or neighborCardType == "h")):

                    # CHECKS IF THE NUMBER OF THE NEIGHBOUR CARD IS 1 HIGHER THAN THE CURRENT CARD. IF IT IS,
                    # WE CAN THEN PLACE THE CURRENT CARD ON THE NEIGHBOUR CARD
                    if neighborCardNumber - 1 == cardNumber:
                        self.result.append(str(cardNumber))
                        self.result.append(cardType)
                        self.result.append(str(i))
                        self.result.append(str(j))
                        self.result.append("T")
                        return True
        return False

    def checkFoundationCardPile(self, cardNumber, cardType):

        # ITERATES THROUGH THE FOUNDATION PILES
        for i in range(4):
            if len(self.logicFoundationCardPiles.get(i)) != 0:

                # DEFINES THE CURRENT FOUNDATION CARD
                foundationCardPile = self.logicFoundationCardPiles.get(i)[0]
                foundationArray = foundationCardPile.split()
                foundationCardNumber = int(foundationArray[0])
                foundationCardType = foundationArray[1]

                # IF CARD OF FOUNDATION AND THE CURRENT CARD TYPE MATCHES AND CURRENT CARD NUMBER IS 1 BIGGER THAN
                # FOUNDATION, THEN WE CAN PLACE IT ON THIS FOUNDATION PILE
                if foundationCardType == cardType and foundationCardNumber + 1 == cardNumber:
                    return i

            else:

                # IF THE CARD IS AN ACE, PLACE THE CARD ON THIS FOUNDATION PILE
                if cardNumber == 1:
                    return i

        # IF THE CARD CANNOT BE PLACED ON THE FOUNDATION PILES, RETURN -1
        return -1

    def get_piles(self):
        return self.logicTableauCardPiles, self.logicFoundationCardPiles, self.logicWasteCard
