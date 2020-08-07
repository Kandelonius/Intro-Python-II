class Item:
    def __init__(self, name, location, description):
        self.name = name
        self.location = location
        self.description = description
        self.clue = ''

    def get_location(self, room):
        return room.name
