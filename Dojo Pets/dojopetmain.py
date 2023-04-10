from ninja import *
from pet import *

b_ninja = Ninja('Christian', 'Ramirez', 'toad', ['cookies', 'brownies', 'cake'], ['Steaks', 'Chicken', 'Sausage'])
b_ninja.feed()
b_ninja.walk()
b_ninja.bathe()

print(b_ninja.pet.name)

#Bonus

kitten = Cat('Cleo', 'Leopard', ['Flips', 'Juggles', 'Bites'], 'Purrr')
kitten.noise()

snoop = Dog('Snoop', 'beagle', ['Jokes', 'Talks', 'charming'], 'Woof woof')
snoop.noise()