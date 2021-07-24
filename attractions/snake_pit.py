from attractions import Attraction

class SnakePit(Attraction):
    def __init__(self, name, description):
        super().__init__(name, description)

    def add_animal(self, animal):
        self.animals.append(animal)

    @property
    def last_critter_added(self):
        return self.animals[-1]