class Item:
    def __init__(self, id, name, location, description):
        self.id = id
        self.name = name
        self.location = location
        self.description = description
        self.clue = ''

    def get_location(self, room):
        return room.name

    def __str__(self):
        return f"{self.name}, {self.description}"
