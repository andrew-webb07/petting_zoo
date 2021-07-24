from datetime import date
from animals import Animal
from movements import Walking

class Dog(Animal, Walking):
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")} while chasing a ball')

    def __str__(self):
        return f"{self.name} is a {self.species}"