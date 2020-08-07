class Inventory:
    def __init__(self, obtained):
        self.obtained = obtained
        self.stash = []

    # def __str__(self):
    #     return f"Location: ${self.location}"

    # def get_location(self, location):
    #     if self.obtained == False:
    #         print(f"The backpack lies in the {location.name}")
    #     else:
    #         print(f"{location.name} carries the loot")

    def get_obtained(self):
        if self.obtained:
            print("obtained")
        else:
            print("not obtained")

    def add_to_stash(self, treasure):
        self.stash.append(treasure)
        print(f"added {treasure.name}")

    def set_obtained(self, obtained):
        self.obtained = obtained
