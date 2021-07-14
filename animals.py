from datetime import date

class Dog:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Cat:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Goat:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Camel:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Horse:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Shark:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

class Goldfish:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

class Catfish:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

class Dolphin:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

class Whale:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

class Snake:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

class Worm:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

class Salamander:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

class Lizard:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

class Leech:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

chip = Dog("Chip", "Mut")
print(chip)
paws = Cat("Paws", "American Bobtail")
goaty = Goat("Goaty", "Wild Goat")
camele = Camel("Camele", "Dromedary")
shadowfax = Horse("Shadowfax", "Felaróf")
sharky = Shark("Sharky", "Great White")
goldy = Goldfish("Goldy", "goldfish")
catty = Catfish("Catty", "Catfish")
flipper = Dolphin("Flipper", "Stripped Dolphin")
free_willy = Whale("Free Willy", "Killer Whale")
snakey = Snake("Snakey", "Cobra")
eathworm_jim = Worm("Earthworm Gym", "Worm")
bob = Salamander("Bob", "Lizard")
lizardy = Lizard("Lizardy", "Lizard")
leechy = Leech("Leechy", "Medicinal Leech")
print(chip.species)