class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

kevin = {"first_name": "Kevin", "last_name": "Lee", "treats": "chews", "pet_food": "purina", "pet": "dogs"}

Ninja_kevin = Ninja(kevin["first_name"], kevin["last_name"], kevin["pet"], kevin["pet_food"], kevin["treats"])
print(Ninja_kevin.first_name)

def walk(self): 
    self.pet.play()
    return self
def feed(self):
    self.pet.eat()
    return self
def bathe(self):
    self.pet.noise()
    return self