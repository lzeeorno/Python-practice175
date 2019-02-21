#assignment3
#Zheng Fuchen (Leon), 1465251

# step 1
import random
# import the random for shuffling the cards
suits=["D", "C", "H", "S"]
ranks=["2","3","4","5","6","7","8","9","0","A","J","Q","K"]

while True:
    filename = input("please enter the game name(shuffleddeck): ") #prompt player to input the game name
    try:
        if filename == 'shuffleddeck':
            f = open('as3_input_shuffledDeck.txt', "r")
            break
    except:
        print("filename is error,please enter again") #prompt user to enter the correct filename
        continue

content = f.read()
f.close()
shuffled_cards = content.strip().split('\n') #read the shuffledDeck.txt and get the content

#validation
if len(shuffled_cards) != 52: #avoid the txt file did not have 52 cards
    raise EXception("total cards not equal 52")
for card in shuffled_cards:
    if len(card)!= 2: #avoid the txt file did not have both suits and ranks
        print("card format error!")

    if card[1] not in suits: # cards did not have valid suits
        raise Exception("cards format error: invalid suit.")

    if card[0] not in ranks: #cards did not have valid ranks
        raise Exception("cards format error: invalid ranks.")

    if shuffled_cards.count(card) != 1: # the cards either lack a suit or lack a rank
        raise Exception ("card number error: dupilicate card ")


# step 2: distributing cards,use circular queue
#first of all, we creat a circular queue in a class
class CircularQueue:
    # Constructor, which creates a new empty queue:
    def __init__(self, capacity):
        if type(capacity) != int or capacity<=0:
            raise Exception ('Capacity Error')
        self.__items = []
        self.__capacity = capacity
        self.__count=0
        self.__head=0
        self.__tail=0

    # Adds a new item to the back of the queue, and returns nothing:
    def enqueue(self, item):
        if self.__count== self.__capacity:
            raise Exception('Error: Queue is full')
        if len(self.__items) < self.__capacity:
            self.__items.append(item)
        else:
            self.__items[self.__tail]=item
        self.__count +=1
        self.__tail=(self.__tail +1) % self.__capacity

    # Removes and returns the front-most item in the queue.
    # Returns nothing if the queue is empty.
    def dequeue(self):
        if self.__count == 0:
            raise Exception('Error: Queue is empty')
        item= self.__items[self.__head]
        self.__items[self.__head]=None
        self.__count -=1
        self.__head=(self.__head+1) % self.__capacity
        return item

    # Returns the front-most item in the queue, and DOES NOT change the queue.
    def peek(self):
        if self.__count == 0:
            raise Exception('Error: Queue is empty')
        return self.__items[self.__head]

    # Returns True if the queue is empty, and False otherwise:
    def isEmpty(self):
        return self.__count == 0

    # Returns True if the queue is full, and False otherwise:
    def isFull(self):
        return self.__count == self.__capacity

    # Returns the number of items in the queue:
    def size(self):
        return self.__count

    # Returns the capacity of the queue:
    def capacity(self):
        return self.__capacity

    # Removes all items from the queue, and sets the size to 0
    # clear() should not change the capacity
    def clear(self):
        self.__items = []
        self.__count=0
        self.__head=0
        self.__tail=0

    # Returns a string representation of the queue:
    def __str__(self):
        str_exp = "]"
        i=self.__head
        for j in range(self.__count):
            str_exp += str(self.__items[i]) + ", "
            i=(i+1) % self.__capacity
        return str_exp + "]"

    # # Returns a string representation of the object CircularQueue
    def __repr__(self):
        return str(self.__items) + " H=" + str(self.__head) + " T="+str(self.__tail) + " ("+str(self.__count)+"/"+str(self.__capacity)+")"
capicity = 52 #we should have 52 cards,so the capicity is 52
player1 = CircularQueue(capicity)
player2 = CircularQueue(capicity)
random_int = random.randint(0,1)

choice = ["player1","player2"]
first_take = choice[random_int] #randomly pick player 1 or player 2
for card in shuffled_cards:
    if first_take == "player1":
        player1.enqueue(card)
        first_take = "player2"
    else:
        player2.enqueue(card)
        first_take = "player1"


#step 3: asking user for data
while True:
    nbWarCards = input(" enter the number of cards face down in the war from 1 to 3: ") #prompt user to play game
    if nbWarCards in ['1','2','3'] and len(nbWarCards)==1:
        break
    else:
        print("invalid input, the number out of range, please enter again. ")

nbWarCards = int(nbWarCards)

# step 4: comparing cards
def compareCards(card1,card2): #comparing the rank of the card between player1 and player2
    rank1 = ranks.index(card1[0])
    rank2 = ranks.index(card2[0])
    if rank1 > rank2:
        return 1
    elif rank1< rank2:
        return -1
    else:
        return 0

#step 5: class ontable
#creat a class to show the cards in the screen and place them in a suitable position
class OnTable:
    def __init__(self):
        self.__cards = []
        self.__faceUp = []

    def place(self, player, card, hidden):
        if player == 1:
            self.__cards.insert(0,card)
            self.__faceUp.insert(0, not hidden)
        else:
            self.__cards.append(card)
            self.__faceUp.append(not hidden)

    def cleanTable(self):
        out = self.__cards
        self.__cards = []
        self.__faceUp = []

        return out


    def __str__(self):
        str_exp = '['
        for i in range(len(self.__cards)):
            if i >0:
                str_exp +=', '
            if self.__faceUp[i]:
                str_exp += self.__cards[i]
            else:
                str_exp += 'XX'
        str_exp +=']'
        return str_exp


# step 6: the game

end_game = False
cards_on_table = OnTable()
while not end_game:
    face_up_1 = player1.dequeue() #dequeue one card from circular queue 1 and put it on the table
    cards_on_table.place(1, face_up_1, False)
    face_up_2 = player2.dequeue() # dequeue one card from circular queue 2 and  put it on the table
    cards_on_table.place(2, face_up_2, False)
    print(cards_on_table) #shows the two cards which are on the table
    print("Player1: ", player1.size()) #shows how many cards did the player1 and player2 own right now
    print("Player2: ", player2.size())
    x = input("press enter to continue or quit to end the game") # prompt player continue the game 
    if x.lower() == 'quit':
        end_game = True

    if compareCards(face_up_1, face_up_2) == 1: #compareCards method return 1 means player1 win
        for cards in cards_on_table.cleanTable(): #player1 collect all the cards on the table right now
            player1.enqueue(cards)

    elif compareCards(face_up_1, face_up_2) == -1: #compareCards method return -1 means player2 win
        for cards in cards_on_table.cleanTable(): #player2 collect all the cards on the table right now
            player2.enqueue(cards)
    else:
        if int(player1.size()) < nbWarCards: #if player did not have enough cards for war, then player2 win
            for cards in cards_on_table.cleanTable(): #player2 collect all the cards on tables
                player2.enqueue(cards)
            for cards in player1:#player2 collect all rest cards of player1, b/c player2 win the whole game
                player2.enqueue(cards)
            player1.clear() #player1 become empty queue
            end_game = True #end the game
        else:
            for i in range (nbWarCards): #player1 has enough cards for war
                war_card = player1.dequeue()
                cards_on_table.place(1, war_card, True) #put the cars which from player1 on table to do the war
            if player2.size()< nbWarCards: #player2 did not have enough cards for war, player1 win the whole game
                for cards in cards_on_table.cleanTable():
                    player1.enqueue(cards)# player1 collect all the cards ontable right now
                for cards in player2:
                    player1.enqueue(player2)# player1 get all rest cards from player2, b/c player1 win the whole game
                player2.clear() #player2 become a empty queue
                end_game = True #end the game
            else: #both player1 and player2 have enough cards for war
                for i in range (nbWarCards):
                    war_card = player2.dequeue() #put the cards which from player2 ontable and do the war
                    cards_on_table.place(2, war_card, True)
    # show the final result
    if player1.size()==0:
        end_game = True
        print("player 1 win")
    if player2.size()==0:
        end_game = True
        print("player 2 win")
