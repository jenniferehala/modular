from parent import Pet

class Ninja(Pet):
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        print("invoking the play method")
        return self

    def feed(self):
        self.pet.eat()
        print("invoking the eat method")
        return self

    def bathe(self, sound):
        self.pet.noise(sound)
        return self


Sterling = Pet("Sterling", "russian blue", "sit", 0, 0)

Sasuke = Ninja("Sasuke", "Uchiha", "carrot", "sheba", Sterling)

# Sasuke.walk()

# Sasuke.feed()

Sasuke.bathe("I'm a talking dog")