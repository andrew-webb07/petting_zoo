from datetime import date

class Camel:
    def __init__(self, name, species, shift, food, chip_num):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food
        self.__chip_num = chip_num

    @property
    def chip_num(self):
        return self.__chip_num

    @chip_num.setter
    def chip_num(self, new_chip_num):
        pass

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"