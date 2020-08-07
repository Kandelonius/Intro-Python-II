# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, room_id, room_name, room_description, room_items=[]):
        self.id = room_id
        self.name = room_name
        self.description = room_description
        self.room_items = room_items

    def add_to_room(self, treasure):
        self.room_items.append(treasure)
        print(f"added {treasure.name}")

    def remove_from_room(self, treasure):
        self.room_items.remove(treasure)
        print(f"removed {treasure.name}")

    # def __str__(self) -> str:
    #     return 'Room(room_name =' + self.room_name + ', room_description =' + self.room_description + ')'

    def get_room_name(self):
        print(f"Location is {self.name}")

    #
    def print_items(self):
        for name, i in enumerate(self.room_items):
            print(f"{name}: {i}")
        print()
