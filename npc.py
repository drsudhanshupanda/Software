import game

class Npc(object):
    def __init__(self):
        raise NotImplementedError("Do not create raw NPC objects.")

    def __str__(self):
        return self.name

class Trader(Npc):
    def __init__(self):
        self.name = "Shop Keeper"
        self.Money = 10000
        self.backpack = [game.Bagel(),
                         game.Ramen(),
                         game.Coffee(),
                         game.FlashDrive()]
        
    def trade(self, buyer, seller):
        for i in item in enumerate(seller.backpack,1):
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
                
    def swap( self, seller, buyer, item):
        if game.value > buyer.gold:
            print("You don't have enough money for that!")
            return
        seller.backpack.remove(item)
        buyer.backpack.append(item)
        seller.gold = seller.gold + item.value
        print ("Thank You come again!")

    def check_if_trade(self, player,buyer):
        while True:
            print ("Would you like to Buy(B), Sell(S), or Exit(X)?")
            user_input = raw_input().lower.strip
            if user_input == 'q':
                return
            elif user_input == 'b':
                print ("Here is what you can buy: ")
                self.trade(buyer=self.player, seller=self.Trader)
            elif user_input == 's':
                print ("Here is what you can sell: ")
                self.trade(buyer=self.Trader, seller=self.player)
            else:
                           print ("Invalid Choice!")
                       
                       
                       
                   
            
    
    
                
    
