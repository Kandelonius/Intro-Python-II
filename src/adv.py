from item import Item
from player import Player
from playerstash import Inventory
from room import Room

# Declare all the rooms

room = {
    'outside': Room(10, "Outside Cave Entrance",
                    "North of you, the cave mount beckons",
                    [Item(0, 'lucky_cat', 'outside', """This one has its left paw raised""")]),

    'foyer': Room(11, "Foyer", """Dim light filters in from the south. Dusty
passages run north and east. The door outside is now locked.""",
                  [Item(1, 'candelabra', 'foyer', """The wax has dried out and it's not useful 
    as a light source."""), Item(2, 'snow_globe', 'foyer', """There appears to be water and small white 
    flakes, but there are palm trees on a beach as well.""")]),

    'overlook': Room(12, "Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     [Item(3, 'dagger', 'overlook', """It's rather dull."""),
                      Item(4, 'broken_compass', 'overlook', """You wouldn't really need this in this 
                          place anyway."""),
                      Item(5, 'wirts_leg', 'overlook', """Hmm, where is that tome of town portal?""")]),

    'narrow': Room(13, "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                   [Item(6, 'cell_phone', 'narrow', """No reception, it looks like it wants me to enter 
    a number."""),
                    Item(7, 'teddy_bear', 'narrow', """How do I know that?""")]),

    'treasure': Room(14, "Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been mostly emptied by
earlier adventurers. The only exit is to the south.""",
                     [Item(8, 'inca_treasure', 'treasure', """This looks valuable, I hope I'm not asked to 
    destroy it."""), Item(9, "trollex", 'treasure', """a cheap knock-off""")]),

    'incinerator': Room(15, "Incinerator Room", """I believe this place has ill-purpose. 
    you see a trap-door in the ceiling.""")
}

# treasure = {
    # 1: Item('candelabra', 'foyer', """The wax has dried out and it's not useful
    # as a light source."""),
    #
    # 2: Item('snow_globe', 'foyer', """There appears to be water and small white
    # flakes, but there are palm trees on a beach as well."""),

    # 3: Item('dagger', 'overlook', """It's rather dull."""),
    #
    # 4: Item('broken_compass', 'overlook', """You wouldn't really need this in this
    # place anyway."""),
    #
    # 5: Item('wirts_leg', 'overlook', """Hmm, where is that tome of town portal?"""),

    # 6: Item('cell_phone', 'narrow', """No reception, it looks like it wants me to enter
    # a number."""),
    #
    # 7: Item('teddy_bear', 'narrow', """How do I know that?"""),

    # 8: Item('inca_treasure', 'treasure', """This looks valuable, I hope I'm not asked to
    # destroy it."""),
    #
    # 9: Item("trollex", 'treasure', """a cheap knock-off"""),
# }

# for key, goodie in treasure.items():
#     # print(key, treasure.location)
#     # Room.room_items.append(key, value)
#     for i in room:
#         # print(place, value.name)
#         # print(f"i is {room[i]}, goodie is {goodie.location}")
#         if goodie.location == str(i):
#             room[i].add_to_room(treasure)

# room_key = input("type foyer")
# if room_key not in room:
#     print("no")
#
# current_room = room[room_key]
#
# current_room.print_items()
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
player_location = darkharden.clean_name(darkharden.location)

print(f"Movement Commands are:\nn for north\nw for west\ns for south\ne for east")
print(f"Interaction Commands are:\nget (item number)\nuse (item name")
print(f"Search Command is:\nsearch room")
print(f"System Commands are:\nq to quit")

# Write a loop that:
#
while True:
    darkharden.get_room_name(darkharden.location)
    possible_items = darkharden.location.room_items
    print(len(backpack.stash))
    #
    darkharden.get_room_description(darkharden.location)
    # * Waits for user input and decides what to do.
    action = input(f"What will you do?\n").strip().lower().split()
    #
    if action[0] in cardinal_directions:
        darkharden.try_move(action[0])
    #
    if action[0] == 'get' and action[1] == 'backpack' and player_location == 'Grand Overlook':
        backpack.obtained = True
    #
    if action[0] == 'backpack':
        backpack.get_obtained()
    #
    if action[0] == 'search' and action[1] == 'room':
        darkharden.location.print_items()
    #
    if action[0] == 'get':
        # and action[1] == darkharden.location.room_items
        backpack.add_to_stash(possible_items[int(action[1])])
        darkharden.location.remove_from_room(possible_items[int(action[1])])

    #
    # If the user enters "q", quit the game.
    if action[0] == 'q':
        break
