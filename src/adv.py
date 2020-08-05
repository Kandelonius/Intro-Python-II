from room import Room
from player import Player
import argparse
import sys

# Construct and parse parameters
ap = argparse.ArgumentParser()

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}
# for n in room:
#     print(room[n])


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
darkharden = Player("Darkharden", room['outside'])
# print(darkharden)

# Write a loop that:
#
print(f"Movement Commands are:\nn for north\nw for west\ns for south\ne for east")
print(f"Interaction Commands are:\nget (item name)\nuse (item name")
print(f"System Commands are:\nq to quit")
while True:
# * Prints the current room name
    darkharden.get_room_name(darkharden.location)
# * Prints the current description (the textwrap module might be useful here).
    darkharden.get_room_description(darkharden.location)
# * Waits for user input and decides what to do.
    action = input(f"What will you do? ")
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
    if action == 'q':
        break



