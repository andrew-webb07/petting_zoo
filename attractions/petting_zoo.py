from attractions import Attraction

class PettingZoo(Attraction):
    def __init__(self, name, description):
        super().__init__(name, description)

    def __str__(self):
        return f"{self.attraction_name} is where you'll find {self.description}, like "

    def add_animal(self, animal):
        self.animals.append(animal)

    @property
    def last_critter_added(self):
        return self.animals[-1]