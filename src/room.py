# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return 'Room(x =' + self.x + ', y =' + self.y + ')'

