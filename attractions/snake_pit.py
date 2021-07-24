from attractions import Attraction
from movements import Slithering

class SnakePit(Attraction):
    def __init__(self, name, description):
        super().__init__(name, description)

    def add_animal_pythonic(self, animal):
        try:
            if animal.slither_speed > -1:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")
        except AttributeError as ex:
            print(f'{animal} doesn\'t like to be with snakes, so please do not put it in the {self.attraction_name} attraction.')

    @property
    def last_critter_added(self):
        return self.animals[-1]