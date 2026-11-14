class Pet:
    def __init__(self, name, pet_type):
        self.name = name
        self.pet_type = pet_type

        self.energy = 80
        self.hunger = 30
        self.happiness = 70
        self.mood = ("Normal", "🙂")

    def feed(self):
        self.hunger = max(0, self.hunger - 10)
        self.happiness = min(100, self.happiness + 5)

    def play(self):
        self.happiness = min(100, self.happiness + 10)
        self.hunger = self.hunger + 10
        self.energy = self.energy - 10

    def sleep(self):
        self.energy = min(100, self.energy + 30)
        self.hunger = min(100, self.hunger + 10)

    def is_alive(self):
        if self.energy < 0:
            return False
        if self.hunger > 100:
            return False
        return True

    def get_mood(self):
        self.update_mood()
        return self.mood

    def update_mood(self):
        # negative
        positive = True
        if self.hunger >= 50:
            self.mood = ("Very Hungry", "😠")
            positive = False
        if self.energy <= 50:
            self.mood = ("Very Tired", "🫩")
            positive = False
        if self.happiness <= 50:
            self.mood = ("Sad and lonely", "🥺")
            positive = False

        # positive
        if positive:
            if self.happiness >= 80:
                self.mood = ("Super Happy!", "😍")
            else:
                self.mood = ("Normal", "🙂")

        return self.mood

    def pass_time(self):
        self.hunger += 5
        self.energy -= 3
        self.happiness -= 2
        self.update_mood()
