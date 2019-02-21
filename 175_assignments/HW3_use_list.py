import random

suits=["D", "C", "H", "S"]
ranks=["2","3","4","5","6","7","8","9","0","A","J","Q","K"]

#### Task 1
# read file
filename = input("Please type in the game name(shuffledDeck.txt): ")
#filename = "shuffledDeck.txt" # !!!!!!!!! No usful, for test only!!!!!!!!!

try:
    f = open(filename, "r")
except:
    print("file open error.")
    exit(0)

content = f.read()
f.close()
shuffled_cards = content.strip().split('\n')

# validation
if len(shuffled_cards) != 52:
    raise Exception("card number error: the number of cards not equal 52.")
for card in shuffled_cards:
    if len(card)!=2:
        # version 1
        # print("card format error: lenght of a card not equal to 2.")
        # exit(0)

        # version2
        raise Exception("card format error: lenght of a card not equal to 2.")
    if card[1] not in suits:
        raise Exception("card format error: invalid suit.")
    if card[0] not in ranks:
        raise Exception("card format error: invalid rank.")
    if shuffled_cards.count(card) != 1:
        raise Exception("card number error: dupilicate card found.")



#### Task 2
Player1 = []
Player2 = []
romdon_int = random.randint(0,1)

# version 1
# choice = ["Player1","Player2"]
# who_take_the_card = choice[romdon_int]
# for card in shuffled_cards:
#     if who_take_the_card == "Player1":
#         Player1.append(card)
#         who_take_the_card = "Player2"
#     else:
#         Player2.append(card)
#         who_take_the_card = "Player1"

# version 2
# choice = ["1", "2"]
# who_take_the_card = choice[romdon_int]
# appending_list = Player1
# for card in shuffled_cards:
#     appending_list.append(card)
#     if who_take_the_card=="1":
#         appending_list = Player2
#         who_take_the_card = "2"
#     else:
#         appending_list = Player1
#         who_take_the_card = "1"

# version 3
for i in range(len(shuffled_cards)):
    if i % 2 == romdon_int:
        Player1.append(shuffled_cards[i].upper())
    else:
        Player2.append(shuffled_cards[i].upper())

# print(shuffled_cards)
# print(Player1)
# print(Player2)

#### Task 3
while True:
    nbWarCards = input("Enter the number of cards face-down when war(from 1 to 3): ")
    if nbWarCards in '123' and len(nbWarCards)==1:#['1','2','3']:
        break
    else:
        print("Invalid input, please enter again.")

nbWarCards = int(nbWarCards)


#### Task 4
def compareCards(card1, card2):
    rank1 = ranks.index(card1[0])
    rank2 = ranks.index(card2[0])
    if rank1 > rank2:
        return 1
    elif rank1 < rank2:
        return -1
    else:
        return 0

# print(compareCards("KS", "KC"))
# print(compareCards("KS", "2C"))
# print(compareCards("2S", "KC"))

#### Task 5
class OnTable:
    def __init__(self):
        self.__cards = []
        self.__faceUp= []

    def place(self, player, card, hidden):
        if player == 1:
            self.__cards.insert(0, card)
            self.__faceUp.insert(0, not hidden)
        else:
            self.__cards.append(card)
            self.__faceUp.append(not hidden)

    def cleanTable(self):
        out = self.__cards
        self.__cards = []
        self.__faceUp= []
        return out

    def __str__(self):
        str_exp = '['
        for i in range(len(self.__cards)):
            if i>0:
                str_exp += ', '

            if self.__faceUp[i]:
                str_exp += self.__cards[i]
            else:
                str_exp += 'XX'
        str_exp += ']'
        return str_exp

# myTable = OnTable()
# print(myTable)
# myTable.place(1, "KC", False)
# print(myTable)
# myTable.place(2, "KS", False)
# print(myTable)
# myTable.place(1, "0C", True)
# myTable.place(2, "0S", True)
# print(myTable)

#Player2 = Player2[:3] # !!!!!!!!! No usful, for test only!!!!!!!!!
#### Task 6
end_game = False
cards_on_table = OnTable()
while not end_game:
    face_up_1 = Player1.pop(0)
    cards_on_table.place(1, face_up_1, False)
    face_up_2 = Player2.pop(0)
    cards_on_table.place(2, face_up_2, False)
    print(cards_on_table)
    print("Player1:", len(Player1))
    print("Player2:", len(Player2))
    input("Press return key to continue.")
    if compareCards(face_up_1, face_up_2)==1:
        Player1.extend(cards_on_table.cleanTable())
    elif compareCards(face_up_1, face_up_2)==-1:
        Player2.extend(cards_on_table.cleanTable())
    else:
        if len(Player1) < nbWarCards:
            Player2.extend(cards_on_table.cleanTable())
            Player2.extend(Player1)
            Player1 = []
            end_game = True
        else:
            for i in range(nbWarCards):
                war_card = Player1.pop(0)
                cards_on_table.place(1, war_card, True)
            if len(Player2) < nbWarCards:
                Player1.extend(cards_on_table.cleanTable())
                Player1.extend(Player2)
                Player2 = []
                end_game = True
            else:
                for i in range(nbWarCards):
                    war_card = Player2.pop(0)
                    cards_on_table.place(2, war_card, True)

    if len(Player1)==0:
        end_game = True
        print("player 1 win")
    if len(Player2)==0:
        end_game = True
        print("player 2 win")
