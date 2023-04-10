class Pet():
    def __init__(self, name, type, tricks, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.sound = sound
        self.energy = 100
        self.health = 100
        
    def sleep(self):
        self.energy += 30
        return self
    def eat(self):
        self.energy += 10
        self.health += 20
        return self
    def play(self):
        self.health += 10
    def noise(self):
        self.health += 10
        print(Self.sound)
        return self

# Bonus

class Cat(Pet):
    def __init__(self, name, type, tricks, sound):
      super().__init__(name, type, tricks, sound)

class Dog(Pet):
    def __init__(self, name, type, tricks, sound):
      super().__init__(name, type, tricks, sound)
      

toad = Pet('Kermit', 'Muppet', ['Memes', 'Acting', 'Trolling'], 'rebbit')