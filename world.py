import random
import enemies
import player
import npc

###Title Words
def tile_exists(x, y):
    return _world.get((x, y))

def tile_at(x,y):
    """ Locates the map tile at a coordinate"""
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None    
            
class MapTile(object):
    def __init__(self, x, y):
        self.x = 2
        self.y = 3

    def intro_text(self):
        raise NotImplementedError("Create a subclass instread!")

    def modify_player(self, player):
        pass 
    

    
class StartTile(MapTile):
    def intro_text(self):
        print("You are standing in the building's threshhold.\n There are 4 hallways in front of you.")
           

class BoringTile (MapTile):
    def intro_text(self):
        print ("This part of the school is especially borring...")

class VictoryTile(MapTile):
    def modify_player(self, player):
        player.victory = True
        
    def intro_text(self):
        print("You saved the school and all your classmates!!\n Now can you pass your test next week?\n")

class EnemyTile(MapTile):
    def __init__(self, x,y):
        r = random.random()
        if r < 0.50:
            self.enemy = enemies.Guilt()
            self.alive_text = "\nYou skipped class AGAIN!?\nPrepare to be eaten by GUILT!!"
            self.dead_text = "\nYou decide to go to class anyway.\nBetter late than never:)" 
        elif r < 0.80:
            self.enemy = enemies.ResearchPaper()
            self.alive_text = "\nA Rabid Research paper stands before you!!\nDid you cite your sources!?\nPrepare to be expelled for plagarism!!"
            self.dead_text = "\nThe Research Paper rips down the middle and falls at your feet" 
        elif r < 0.95:
            self.enemy = enemies.Homework()
            self.alive_text = "\nAn ornary Homework Assignment is blocking your way.\nYou thought Homework was supposed to be done at home...\nHomework follows you EVERYWHERE!!"
            self.dead_text = "\nYou know the answers and showed that homework who's boss" 
        else:
            self.enemy = enemies.Procrastination()
            self.alive_text = "\nIts the embodiement of PROCRASTINATION!!!\nYou can defeat your homework and a research paper... \nbut can you defeat your own bad habits?"
            self.dead_text = "\nLucky for you, you do your best work under pressure."
            
        super(EnemyTile, self).__init__(x,y)

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.lifepoints = player.lifepoints - self.enemy.damage
            print ("\nEnemy does {} damage. You Have {} Life Points remaining.".format(self.enemy.damage,player.lifepoints))

    def intro_text(self):
        if self.enemy.is_alive():
            return self.alive_text if self.enemy.is_alive() else self.dead_text
    
     
class TraderTile(MapTile):
    def __init__(self, x, y):
        self.trader = npc.Trader()
        super(TraderTile,self).__init__(x,y)

    def intro_text(self):
        return ("The Student Center Shop keeper smiles at you cheerfully,\n she doesn't seem to know whats going on in the rest of the school")

    def check_if_trade(self, player):
        while True:
            print ("Would you like to Buy(B), Sell(S), or Exit(X)?")
            user_input = raw_input().lower().strip()
            if user_input == 'x':
                return
            elif user_input == 'b':
                print ("Here is what you can buy: ")
                self.trade(buyer=player, seller=self.trader)
            elif user_input == 's':
                print ("Here is what you can sell: ")
                self.trade(buyer=self.trader, seller=player)
            else:
                print ("Invalid Choice!")
    
    def swap( self, seller, buyer, item):
        if item.value > buyer.Money:
            print("You don't have enough money for that!")
            return
        seller.backpack.remove(item)
        buyer.backpack.append(item)
        seller.Money = seller.Money + item.value
        print ("Thank You come again!")
                                  
    def trade(self, buyer, seller):
        for i, item in enumerate(seller.backpack,1):
            print("{}. {} - {} Money" .format(i,item.name, item.value))
        while True:
            user_input = raw_input ("Choose an Item or press X to exit: ").lower().strip()
            if user_input == 'x':
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.backpack[choice-1]
                    self.swap(seller, buyer, to_swap)
                except ValueError:
                    print("Invalid choice!")

  
class FindGoldTile(MapTile):
    def __init__(self,x,y):
        self.Money = random.randint(1,50)
        self.Money_claimed = False
        super(FindGoldTile,self).__init__(x,y)

    def modify_player(self, player):
        if not self.Money_claimed:
            self.Money_claimed = True
            player.Money = player.Money + self.Money
            print("+{} Money added." .format(self.Money))
            
    def intro_text(self):
        if self.Money_claimed:
            return """
            Another hallway.
            """
        else:
            return """
            Some one dropped some money here, Lucky you!
            """

world_map = [[EnemyTile(0,0),EnemyTile(0,1),VictoryTile(0,2),EnemyTile(0,3),EnemyTile(0,4)],
    [EnemyTile(1,0),BoringTile(1,1),BoringTile(1,2),BoringTile(1,3),EnemyTile(1,4)],
    [EnemyTile(2,0),FindGoldTile(1,2),EnemyTile(2,2),BoringTile(2,3),TraderTile(2,4)],
    [TraderTile(3,0),BoringTile(3,1),StartTile(3,2),FindGoldTile(3,3),EnemyTile(3,4)],
    [FindGoldTile(4,0),BoringTile(4,1),EnemyTile(4,2),BoringTile(4,3),FindGoldTile(4,4)]]

world_dsl = """
|ET|ET|VT|ET|ET|
|ET|  |  |  |ET|
|ET|FG|ET|  |TT|
|TT|  |ST|FG|ET|
|FG|  |ET|  |FG|
"""

def is_dsl_valid(dsl):
    if dsl.count("|ST|" != 1:
                 return False
    if dsl.count("|VT|") == 0:
                 return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
                 if count != pipe_counts[0]:
                     return False
    return True

tile_type_dict = {"VT": VictoryTile,
                  "EN":EnemyTile,
                  "ST":StartTile,
                  "FG":FindGoldTile,
                  "
                 
                 

