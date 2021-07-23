from walking import Camel, Cat, Dog, Goat, Horse
from swimming import Catfish, Dolphin, Goldfish, Shark, Whale
from slithering import Leech, Lizard, Salamander, Snake, Worm
from attractions import PettingZoo, SnakePit, Wetlands

roberto = Camel("Roberto", "alpaca", "midday", "grain")
chip = Dog("Chip", "Mut", "morning", "dog food")
paws = Cat("Paws", "American Bobtail", "midday", "cat food")
goaty = Goat("Goaty", "Wild Goat", "evening", "grass")
shadowfax = Horse("Shadowfax", "Felaróf", "morning", "sugar")
sharky = Shark("Sharky", "Great White", "blood")
goldy = Goldfish("Goldy", "goldfish", "pellets")
catty = Catfish("Catty", "Catfish", "pellets")
flipper = Dolphin("Flipper", "Stripped Dolphin", "fish")
free_willy = Whale("Free Willy", "Killer Whale", "big fish")
snakey = Snake("Snakey", "Cobra", "toads")
eathworm_jim = Worm("Earthworm Gym", "Worm", "bugs")
bob = Salamander("Bob", "Lizard", "bugs")
lizardy = Lizard("Lizardy", "Lizard", "bugs")
leechy = Leech("Leechy", "Medicinal Leech", "blood")

my_petting_zoo = PettingZoo("Lewis Adventure", "Come pet some animals")
my_snake_pit = SnakePit("Temple of Doom", "Don't come here...I mean why?")
my_marina = Wetlands("Seaworld", "Lots of water here")

my_petting_zoo.add_animal(roberto)
my_petting_zoo.add_animal(chip)
my_petting_zoo.add_animal(paws)
my_petting_zoo.add_animal(goaty)
my_petting_zoo.add_animal(shadowfax)
my_snake_pit.add_animal(snakey)
my_snake_pit.add_animal(eathworm_jim)
my_snake_pit.add_animal(bob)
my_snake_pit.add_animal(lizardy)
my_snake_pit.add_animal(leechy)
my_marina.add_animal(sharky)
my_marina.add_animal(goldy)
my_marina.add_animal(catty)
my_marina.add_animal(flipper)
my_marina.add_animal(free_willy)


for animal in my_petting_zoo.animals:
    print(f'You can find {animal.name} the {animal.species} in {my_petting_zoo.attraction_name}')
for animal in my_snake_pit.animals:
    print(f'You can find {animal.name} the {animal.species} in {my_snake_pit.attraction_name}')
for animal in my_marina.animals:
    print(f'You can find {animal.name} the {animal.species} in {my_marina.attraction_name}')