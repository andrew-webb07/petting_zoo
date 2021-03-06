from animals import Camel, Cat, Dog, Goat, Horse, Catfish, Dolphin, Goldfish, Shark, Whale, Leech, Lizard, Salamander, Snake, Worm
from attractions import PettingZoo, SnakePit, Wetlands

roberto = Camel("Roberto", "alpaca", "midday", "grain", 111555)
chip = Dog("Chip", "Mut", "morning", "dog food", 11)
paws = Cat("Paws", "American Bobtail", "midday", "cat food", 22)
goaty = Goat("Goaty", "Wild Goat", "evening", "grass", 33)
shadowfax = Horse("Shadowfax", "Felaróf", "morning", "sugar", 44)
sharky = Shark("Sharky", "Great White", "blood", 55)
goldy = Goldfish("Goldy", "goldfish", "pellets", 66)
catty = Catfish("Catty", "Catfish", "pellets", 77)
flipper = Dolphin("Flipper", "Stripped Dolphin", "fish", 88)
free_willy = Whale("Free Willy", "Killer Whale", "big fish", 99)
snakey = Snake("Snakey", "Cobra", "toads",555)
eathworm_jim = Worm("Earthworm Gym", "Worm", "bugs", 4234)
bob = Salamander("Bob", "Lizard", "bugs", 333)
lizardy = Lizard("Lizardy", "Lizard", "bugs", 222)
leechy = Leech("Leechy", "Medicinal Leech", "blood", 12121)

# roberto.chip_num = 666


my_petting_zoo = PettingZoo("Lewis Adventure", "Come pet some animals")
my_snake_pit = SnakePit("Temple of Doom", "Don't come here...I mean why?")
my_marina = Wetlands("Seaworld", "Lots of water here")

my_petting_zoo.add_animal_pythonic(roberto)
my_petting_zoo.add_animal_pythonic(chip)
my_petting_zoo.add_animal_pythonic(paws)
my_petting_zoo.add_animal_pythonic(goaty)
my_petting_zoo.add_animal_pythonic(shadowfax)
my_petting_zoo.add_animal_pythonic(eathworm_jim)
my_snake_pit.add_animal_pythonic(snakey)
my_snake_pit.add_animal_pythonic(eathworm_jim)
my_snake_pit.add_animal_pythonic(bob)
my_snake_pit.add_animal_pythonic(lizardy)
my_snake_pit.add_animal_pythonic(leechy)
my_snake_pit.add_animal_pythonic(goaty)
my_marina.add_animal_pythonic(sharky)
my_marina.add_animal_pythonic(goldy)
my_marina.add_animal_pythonic(catty)
my_marina.add_animal_pythonic(flipper)
my_marina.add_animal_pythonic(free_willy)
my_marina.add_animal_pythonic(shadowfax)


for animal in my_petting_zoo.animals:
    print(f'You can find {animal.name} the {animal.species} in {my_petting_zoo.attraction_name}')
for animal in my_snake_pit.animals:
    print(f'You can find {animal.name} the {animal.species} in {my_snake_pit.attraction_name}')
for animal in my_marina.animals:
    print(f'You can find {animal.name} the {animal.species} in {my_marina.attraction_name}')

print(my_petting_zoo.last_critter_added)
print(my_snake_pit.last_critter_added)
print(my_marina.last_critter_added)
roberto.feed()
paws.feed()
chip.feed()