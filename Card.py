class Card:

    def __init__(self, health, attack):
        self.health = health
        self.attack = attack

    def get_attack(self):
        return self.attack

    def get_health(self):
        return self.health

    def set_attack(self, attack):
        self.attack = attack

    def set_health(self, health):
        self.health = health

