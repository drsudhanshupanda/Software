import game
import world
import enemies

class Player(object):
    def __init__(self):
        self.backpack = [game.Pencil(),
                         game.Ruler(),
                         game.Coffee()]
        self.x = 2
        self.y = 3
        self.lifepoints =100
        self.Money = 100
        self.victory = False

    def is_alive(self):
        return self.lifepoints > 0
        
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def move_forward(self):
        self.move(dx=0,dy=-1)
        
    def move_backward(self):
        self.move(dx=0,dy=1)
        
    def move_right(self):
        self.move(dx=1,dy=0)
        
    def move_left(self):
        self.move(dx=-1,dy=0)

    def print_pack(self):
        print ("***Backpack Contents***")
        best_weapon = self.most_powerful_weapon()
        for item in self.backpack:
            print(item)
        print ("\nYour best weapon is your {}\n" .format(best_weapon.name))
        print ("Money: {}".format(self.Money))
            
    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.backpack:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass
        return best_weapon

    def attack(self):
        best_weapon = self.most_powerful_weapon()
        room = world.tile_at(self.x,self.y)
        enemy = room.enemy
        print("\nYou use the {} against {}!".format(best_weapon.name, enemy.name))
        enemy.lifepoints -= best_weapon.damage
        if not enemy.is_alive():
            print("\nYou Killed the {}!" .format(enemy.name))
        else:
            print ("\n{}'s Life Points are {}." .format(enemy.name, enemy.lifepoints))

    def heal(self):
        consumables = [item for item in self.backpack if isinstance( item,game.Consumable)]
        if not consumables:
            print ("\nYou don't have any items to heal you!")
            return

        for i, item in enumerate(consumables,1):
            print("Choose an item to restore Life Points: ")
            print("{}. {}".format(i,item))
            valid = False
            while not valid:
                choice = raw_input("")
                try:
                    to_eat = consumables[int(choice) -1]
                    self.lifepoints = min(100, self.lifepoints + to_eat.healing_value)
                    self.backpack.remove(to_eat)
                    print("Current Life Points {}".format(self.lifepoints))
                    valid = True
                except (ValueError, IndexError):
                    print("Invalid choice, try again.")

    def trade(self):
        room = world.tile_at(self.x, self.y)
        room.check_if_trade(self)
                    
            
        
