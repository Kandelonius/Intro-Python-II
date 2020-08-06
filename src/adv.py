from item import Item
from player import Player
from playerstash import Inventory
from room import Room

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east. The door outside is now locked."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been mostly emptied by
earlier adventurers. The only exit is to the south."""),

    'incinerator': Room("Incinerator Room", """I believe this place has ill-purpose. 
    you see a trap-door in the ceiling.""")
}
# for n in room:
#     print(room[n])

item = {
    'candelabra': Item("candelabra", 'overlook', """The wax has dried out and it's not useful 
    as a light source."""),

    'snow_globe': Item("snow globe", 'foyer', """There appears to be water and small white 
    flakes, but there are palm trees on a beach as well."""),

    'dagger': Item("dagger", 'overlook', """It's rather dull."""),

    'broken_compas': Item("broken compass", 'narrow', """You wouldn't really need this in this 
    place anyway."""),

    'wirts_leg': Item("Wirt's leg", 'overlook', """Hmm, where is that tome of town portal?"""),

    'cell_phone': Item("cell phone", 'narrow', """No reception, it looks like it wants me to enter 
    a number."""),

    'teddy_bear': Item("Sir Stuffs-a-lot", 'foyer', """How do I know that?"""),

    'time_piece': Item("Trollex", 'treasure', """a cheap knock-off"""),

    'lucky_cat': Item("lucky neko", 'foyer', """This one has its left paw raised"""),

    'gold_coin': Item("Inca Gold", 'treasure', """This looks valuable, I hope I'm not asked to 
    destroy it."""),
}

# room['outside'].m_to = playerstash['backpack']
# room['foyer'].m_to = playerstash['backpack']
# room['overlook'].m_to = playerstash['backpack']
# room['narrow'].m_to = playerstash['backpack']
# room['treasure'].m_to = playerstash['backpack']

# Link rooms together

room['outside'].n_to = room['foyer']  # has attribute .n_to
# room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['incinerator'].u_to = room['outside']
room['incinerator'].u_to = room['outside']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
darkharden = Player("Darkharden", room['outside'])
backpack = Inventory(False)
cardinal_directions = ['n', 'w', 's', 'e']
# print(darkharden)

print(f"Movement Commands are:\nn for north\nw for west\ns for south\ne for east")
print(f"Interaction Commands are:\nget (item name)\nuse (item name")
print(f"System Commands are:\nq to quit")

# Write a loop that:
#
while True:
    # * Prints the current room name
    darkharden.get_room_name(darkharden.location)
    # * Prints the current description (the textwrap module might be useful here).
    darkharden.get_room_description(darkharden.location)
    # * Waits for user input and decides what to do.
    action = input(f"What will you do?\n").strip().lower().split()
    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    if action[0] in cardinal_directions:
        darkharden.try_move(action[0])
    #
    # allow player to obtain backpack
    if action[0] == 'get' and action[1] == 'backpack' and darkharden.clean_name(darkharden.location) == 'Grand Overlook':
        backpack.obtained = True
        # backpack.set_location('Darkharden')
        # backpack.set_obtained(True)
        # darkharden.get_location(backpack.location)

    if action[0] == 'backpack':
        print(darkharden.location)
        backpack.get_obtained()
        # backpack.get_location(backpack.location)
    #
    # If the user enters "q", quit the game.
    if action[0] == 'q':
        break
