#Blackjack how does it work? You might wonder if you have never played. The dealer gives you two random cards and himself two one face up and another faced down.
import random

class Player:
    def __repr__(self):
        return "This is the Casino object for their players information for later use, but mostly BlackJack."

    def __init__(self, name, age, money=0):
        self.name = name
        self.age = age
        self.money = float(money)

    
    def Bet(self, Bet):
        self.money -= Bet

    def Player_Won(self, Amount):
        self.money += Amount * 2
    


Card_lists = []
def Counter(card):
    value = 0
    fail_list = []
    for j in card:
        try:
            value += int(j)
        except:
            fail_list.append(j)
            continue
    for i in fail_list:
        if i == "Ace":
            value += 11
        if i == "King" or i == "Queen" or i == "Jack":
            value += 10
    return value

    
def Manage(Card_lists):
    if len(Card_lists) == 0:
        global Card_list
        Card_list = Shuffle(Card_lists)
    
    return Card_list


def Shuffle(Card_lists):
    Card_list = ["Ace","2","3","4","5","6","7","8","9","10", "Jack", "Queen", "King"]
    for i in range(4):
        Card_lists += Card_list
    return Card_lists


def Card(Card):
    Card_lists = Manage(Card)
    remove = len(Card_lists) - 1
    num = random.randint(0, remove)
    Card = Card_lists[num]
    Card_lists.pop(remove)
    return Card

def SplitFunc(List1, List2):
    return Counter(List1), Counter(List2)
    



j = ""
for i in range(50):
    j += "-" 


print(j + "\nWelcome to BlackJack Terminal")
print(j)

print("Username: ")
name = input()
print("Age: ")
age = int(input())
print("Money: ")
money = input()

User = Player(name, age, money)
if User.age < 18:
    print("Your too young...")
    Age_To_Young = True
else:
    Age_To_Young = False

Player_Plays = False
if Age_To_Young == False:
    
    print("Would you like to play: ")
    Player_play = input().upper()

    if Player_play == "Y" or Player_play == "YES":
        Player_Plays = True


#Game Loop ---------------------------------------------------------------------------------------------------------------
while Player_Plays:
    Player_Bust = False
    Player_Has_Won = False
    print("User Wallet: {}".format(User.money) + "\nBet:")
    if User.money <= 0:
        print("You have run out of money...")
        break
    try:
        Bet = float(input())
        if Bet > User.money:
            print("Invalid amount, try again...\n")
            continue
        User.Bet(Bet)
    except:
        print("Please, try again the transaction didn't go through.")
        Bet = float(input())
        User.Bet(Bet)

    dealer_Card1 = Card(Card_lists)
    dealer_Card2 = Card(Card_lists)
    
    print(j + "\nDealer: " + dealer_Card1 + ", ***\n"+ j + "\n")
    Dealer = [dealer_Card1, dealer_Card2]

    Player_card1 = Card(Card_lists)
    Player_card2 = Card(Card_lists)
    print(User.name + ": " + Player_card1 + ", " + Player_card2)
    The_Player = [Player_card1, Player_card2]
    Insurance = False
    if dealer_Card1 == "Ace":
        
        print("Would you like insurance? Y? N?")
        Insurance = input().upper()
        
        if Insurance == "Y" or Insurance == "YES":
            if User.money <= 0:
                print("You have run out of money...")
                Insurance = False
                pass
            Insurance = True
            User.Bet(Bet)
        else:
            Insurance = False
    if Counter(Dealer) == 21:
        print(Dealer)
        if Insurance == True:
            User.Player_Won(Bet)
        continue

    if Counter(The_Player) == 21:
        Player_Has_Won = True
        User.Player_Won(Bet)
        continue
    if Insurance == True:
        print("Dealer didn't have 21...")

    Play = True
    hits = 0
    spliting = False
    while Play:
        if spliting == True:
            break
        double_down = False
        if hits == 0:
            print("Options: Hit, Pass, Double, Split...")
        else:
            print("Options: Hit, Pass...")

        inp = input().upper()
        
        if inp == "HIT":
            New_Card = Card(Card_lists)
            The_Player.append(New_Card)
            print(j +"\n"+ str(New_Card)+ " --- New Count: " + str(Counter(The_Player)) +"\n"+ j)
            hits += 1
        elif inp == "PASS":
            break

        elif inp == "DOUBLE" and hits == 0 and User.money > Bet:
            User.Bet(Bet)
            double_down = True
            New_Card = Card(Card_lists)
            print(j +"\n"+ str(New_Card)+"\n"+ j)
            The_Player.append(New_Card)
            if Counter(The_Player) > 21:
                Count = 0
                for k in The_Player:
                    if k == "Ace":
                        The_Player[Count] = "1"
                        print(Counter(The_Player))
                    Count += 1 
            break 

        elif inp == "SPLIT" and hits == 0 and User.money >= Bet:
                User.Bet(Bet)
                spliting = True
                The_Player2 = [The_Player[1]]
                The_Player.pop(1)
                Pass1 = True
                Pass2 = False
                Lot = 0
                skip = False
                while spliting:
                    if Pass1 == False and Pass2 == False:
                        break
                    if Counter(The_Player) > 21 and skip != True:
                        Count = 0
                        skip = False
                        for k in The_Player:
                            if k == "Ace":
                                skip = True
                                The_Player[Count] = "1"
                                print(Counter(The_Player))
                                continue
                            Count += 1
                        
                        
                    elif Counter(The_Player) == 21:
                        Pass1 = False
                    elif Counter(The_Player2) == 21:
                        Pass2 = False
                    if Counter(The_Player2) > 21:
                        Pass2 = False
                    elif Counter(The_Player) > 21:
                        Pass1 = False
                        Pass2 = True
                    print("First Hand:",The_Player, "Second Hand:", The_Player2)
                    print("Options: Hit, Pass...")
                    inp = input().upper()
                    if inp == "HIT":
                        New_Card = Card(Card_lists)
                        if Pass1 == True:
                            The_Player.append(New_Card)
                        elif Pass2 == True:
                            The_Player2.append(New_Card)

                    elif inp == "PASS":
                        Lot += 1
                        if Pass1 == False:
                            Lot = 2
                        if Lot == 1:
                            Pass1 = False
                            Pass2 = True
                        elif Lot == 2:
                            Pass2 = False
                
        if Counter(The_Player) > 21:
            Count = 0
            skip = False
            for k in The_Player:
                if k == "Ace":
                    skip = True
                    The_Player[Count] = "1"
                    print(Counter(The_Player))
                    continue
                Count += 1
            if skip == True:
                continue
            Player_Bust = True
            break
        elif Counter(The_Player) == 21:
            break
        

    if Player_Bust == True:
        continue
    elif Player_Has_Won:
        User.Player_Won(Bet)
        if double_down == True:
            User.Player_Won(Bet)
        continue

    print(j + "\nDealer's Hand: " + dealer_Card1 + ", " + dealer_Card2 + "\n" + j)
    while True:
        
        if Counter(The_Player) < Counter(Dealer):
            Count = 0
            skip = False
            for k in Dealer:
                if k == "Ace":
                    skip = True
                    Dealer[Count] = "1"
                    print(Counter(Dealer))
                    continue
                Count += 1
            if skip == True:
                continue
            break
        elif Counter(Dealer) < 17:
            New_Dealer_Card = Card(Card_lists)
            Dealer.append(New_Dealer_Card)
            print("Dealer hit:", New_Dealer_Card, "--- New count:", Counter(Dealer), "\n", j)
        elif Counter(Dealer) > 21:
            Count = 0
            skip = False
            for k in Dealer:
                if k == "Ace":
                    skip = True
                    Dealer[Count] = "1"
                    print(Counter(Dealer))
                    continue
                Count += 1
            if skip == True:
                continue
            break
        else:
            break
    if spliting == True:
        if Counter(Dealer) < Counter(The_Player2) and Counter(The_Player2) < 22:
            User.Player_Won(Bet)

    if Counter(The_Player) == Counter(Dealer):
        User.Player_Won(Bet / 2)
        continue
    elif Counter(The_Player) > Counter(Dealer) and Counter(The_Player) < 22:
        User.Player_Won(Bet)
        if double_down == True:
            User.Player_Won(Bet)
        continue

    elif Counter(The_Player) < Counter(Dealer):
        if Counter(Dealer) > 21:
            User.Player_Won(Bet)
            print("\nPlayer Won!")
            if double_down == True:
                User.Player_Won(Bet)
        else:
            print("\nPlayer Lost")
            continue