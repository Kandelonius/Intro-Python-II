# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, room_name, room_description):
        self.room_name = room_name
        self.room_description = room_description

    def __str__(self) -> str:
        return 'Room(room_name =' + self.room_name + ', room_description =' + self.room_description + ')'

    # def get_room_name(self):
    #     print(f"Location is {self.room_name}")
    #
    # def room_description(self):
    #     return f"Description: ${self.room_description}"