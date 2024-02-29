class Item(object):
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
 
    def __str__(self):
        return "\n\n{}\n-----\n{}\nValue: {}\n".format(self.name, self.description, self.value)
#Given Items

class Money(Item):                        
    """Currency"""
    def __init__(self, amt):
        self.amt = amt
        super(Money, self).__init__(name="Money",
        description="A Paper Bill with {} stamped on the front.".format(str(self.amt)),
        value=self.amt)
        
class Weapon(Item):
    """Items that will Damage enemies"""
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super(Weapon, self).__init__(name, description, value) 
    def __str__(self):
        return "\n\n{}\n-----\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)
 
 
class Pencil(Weapon):
    def __init__(self):
        super(Pencil, self).__init__(name="Pencil",
                                     description="Only useful if sharpened",
                                     value=0,
                                     damage=1)
class Ruler(Weapon):
    def __init__(self):
        super(Ruler, self).__init__(name="Ruler",
                         description="A metal Ruler with cork backing. Can come in handy for measurements or self defense.",
                         value=10,
                         damage=20)
        
class FlashDrive(Weapon):
    def __init__(self):
        super(FlashDrive, self).__init__(name="Flash Drive",
                         description="Capable of delivering a powerful shock to your adversaries!",
                         value=100,
                         damage=20)
        
#consumables
class Consumable(object):
    def __init__(self, name, description, value,healing_value):
       
        self.name = name
        self.description = description
        self.value = value
        self.healing_value = healing_value
 
    def __str__(self):
        return "\n\n{}\n-----\n{}\nValue: {}\n".format(self.name, self.description, self.value, self.healing_value)

class Coffee(Consumable):
    def __init__(self):
       super(Coffee, self).__init__(name="Coffee",
        description="Just what you needed! 10 life points",
        value=5,healing_value = 20)

class Bagel(Consumable):
    def __init__(self):
       super(Bagel, self).__init__(name="Bagel",
        description="Multigrain goodness to start the day off right! 60 life points",
        value=10,healing_value = 60)

class Ramen(Consumable):
    def __init__(self):
       super(Ramen, self).__init__(name="Ramen",
        description="Enough sodium for the next two days! 100 life points",
        value=20,healing_value = 100)


