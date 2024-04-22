import random

class Character:
    def __init__(self, name, class_type):
        self.name = name
        self.class_type = class_type
        self.health = 25
        self.initiative = 0
        self.defense = 0
        self.attack = 0
        self.weapon = None
        self.generate_attributes()

    def generate_attributes(self):
        if self.class_type == 'Warrior':
            self.strength = random.randint(1, 10) + 10
            self.agility = random.randint(1, 6) + random.randint(1, 6) + 8
            self.dexterity = random.randint(1, 6) * 3
        elif self.class_type == 'Thief':
            self.strength = random.randint(1, 6) * 3
            self.agility = random.randint(1, 10) + 10
            self.dexterity = random.randint(1, 6) + random.randint(1, 6) + 8
        elif self.class_type == 'Cleric':
            self.strength = random.randint(1, 6) + random.randint(1, 6) + 8
            self.agility = random.randint(1, 6) * 3
            self.dexterity = random.randint(1, 10) + 10

    def choose_weapon(self, weapon):
        self.weapon = weapon
        self.initiative = max(0, self.agility - 10) + weapon.speed
        self.defense = max(0, self.dexterity - 10) + weapon.defense
        self.attack = max(0, self.strength - 10) + weapon.attack

    def __str__(self):
        return f"{self.name} the {self.class_type} (HP: {self.health}, STR: {self.strength}, AGI: {self.agility}, DEX: {self.dexterity})"

class Weapon:
    def __init__(self, name, damage, speed, defense, attack):
        self.name = name
        self.damage = damage
        self.speed = speed
        self.defense = defense
        self.attack = attack

def roll_dice(expression):
    amount, sides = map(int, expression.split('d'))
    return sum(random.randint(1, sides) for _ in range(amount))

def create_character():
    name = input("Enter your character's name: ")
    class_type = input("Choose a class (Warrior, Thief, Cleric): ")
    character = Character(name, class_type)
    print(character)
    return character

def assign_weapon(character):
    weapons = {
        'Sword': Weapon("Sword", "1d6+3", 6, 8, 6),
        'Dagger': Weapon("Dagger", "1d6", 10, 3, 10),
        'Staff': Weapon("Staff", "1d4", 8, 10, 8),
        'Greatsword': Weapon("Greatsword", "2d6", 1, 1, 4),
        'Mace': Weapon("Mace", "2d4+2", 4, 5, 4)
    }

    print("Available weapons:")
    for weapon in weapons.values():
        print(f"{weapon.name} - Damage: {weapon.damage}, Speed: {weapon.speed}, Defense: {weapon.defense}, Attack: {weapon.attack}")

    weapon_choice = input("Choose your weapon: ")
    character.choose_weapon(weapons[weapon_choice])
    print(f"{character.name} now wields a {character.weapon.name}.")

# Example usage
player1 = create_character()
assign_weapon(player1)
