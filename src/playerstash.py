class Inventory:
    def __init__(self, location, obtained):
        self.location = location
        self.obtained = obtained

    def __str__(self):
        return f"Location: ${self.location}"

    def get_location(self, room):
        if self.obtained == False:
            print(f"The backpack lies in the {room.name}")
        else:
            print(f"Darkharden carries the loot")
