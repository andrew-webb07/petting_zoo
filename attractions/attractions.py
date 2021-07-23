class PettingZoo:
    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def __str__(self):
        return f"{self.attraction_name} is where you'll find {self.description}, like "

    def add_animal(self, animal):
        self.animals.append(animal)

    @property
    def last_critter_added(self):
        return self.animals[-1]

class SnakePit:
    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    @property
    def last_critter_added(self):
        return self.animals[-1]

class Wetlands:
    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    @property
    def last_critter_added(self):
        return self.animals[-1]