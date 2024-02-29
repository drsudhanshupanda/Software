import game   
from player import Player
import world
import collections

                
def get_player_command():
    """the player input"""
    return raw_input('Action: ').lower().strip()




### Main Script
#print("++++++++++++++++++++++++++++++++++")
#print("|      DEATHSCHOOL!!!!           |")
#print("|           By: Cori Sparks      |")
#print("++++++++++++++++++++++++++++++++++\n\n\n")
#print("You walk up the stairs on the first day of school.\n Something doesn't feel right......\n The parking lot was full, but building is eerily silent.\n")
#player = Player()

#while True:
##    room = world.tile_at(player.x, player.y)
##    print(room.intro_text())
##    room.modify_player(player)
##    action_input = get_player_command()
##    if action_input == 'w':
##        player.move_forward()
##    elif action_input == 's':
##        player.move_backward()
##    elif action_input == 'a':
##        player.move_left()
##    elif action_input == 'd':
##        player.move_right()
##    elif action_input == 'b':
##        player.print_pack()
##    elif action_input == 'f':
##        player.attack()
##    elif action_input == 'h':
##        player.heal()
##    elif action_input == 'q':
##        break
##    else:
##        print("Invalid!")
##




    
 
def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))

def get_available_actions(room,player):
    actions = collections.OrderedDict()
    print ("Choose an action: ")
    if player.backpack:
        action_adder(actions, 'b', player.print_pack, "Print Backpack")
    if isinstance (room, world.TraderTile):
        action_adder(actions, 't', player.trade, "Trade") 
    if isinstance (room, world.EnemyTile) and room.enemy.is_alive():
        action_adder(actions, 'f', player.attack, "Fight!")
    else:
        if world.tile_at(room.x, room.y - 1):
            action_adder(actions, 'w', player.move_forward, "Go Forward!")
        if world.tile_at(room.x, room.y + 1):
            action_adder(actions, 's', player.move_backward, "Go Backward!")
        if world.tile_at(room.x + 1, room.y):
            action_adder(actions, 'd', player.move_right, "Go Right!")
        if world.tile_at(room.x - 1, room.y):
            action_adder(actions, 'a', player.move_left, "Go Left!")
    if player.lifepoints < 100:
        action_adder(actions, 'h', player.heal, "Heal")
        
    return actions

             



def choose_action(room, player):
    action = None

    while not action:
        available_actions = get_available_actions(room, player)

        action_input = raw_input("Action: ").lower().strip()
        action = available_actions.get(action_input)
        if action:
            action()

        else:
            print("Invalid action!")


def play():
    print("++++++++++++++++++++++++++++++++++")
    print("|      DEATHSCHOOL!!!!           |")
    print("|           By: Cori Sparks      |")
    print("++++++++++++++++++++++++++++++++++\n\n\n")
    print("You walk up the stairs on the first day of school.\n Something doesn't feel right......\n The parking lot was full, but building is eerily silent.\n")
    player = Player()
    while True:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        room.modify_player(player)
        choose_action(room, player)
    if player.is_alive() and not player.victory:
        choose_action(room,player)
    elif not player.is_alive():
        print("Failure...")
        


play()






           
