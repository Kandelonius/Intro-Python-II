# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __str__(self):
        return f"Name: ${self.name}, Location: {self.location}"

    def get_room_name(self, room):
        print(f"You find yourself in the {room.name}")

    def clean_name(self, room):
        return (room.name)

    def get_room_description(self, room):
        print(f"You observe {room.description}")

    def try_move(self, direction):
        attribute = direction + '_to'
        if hasattr(self.location, attribute):  # hasattr builtin checks for an attribute
            self.set_location(getattr(self.location, attribute))  # getattr builtin gets attribute
            # self.set_location(room['outside'].n_to)
        else:
            print(f"Sorry {self.name}, I'm afraid you can't do that.")

    def set_location(self, location):
        self.location = location
