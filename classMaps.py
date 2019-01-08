"""
#
# S0mHmxxGh0ulz
# 
# Author: l33tH@x0rxxGh0u1
#
"""


class Maps:

    # Maps
    maps = ["Dungeon of Desire", "Garden of Heathens", "Mansion", "King's Chambers", "Queen's Quarters"]
    
    # Map Variable's

    

    # Enemies
    garden_enemies = ["Terrifying Tulips", "Lovely Liliac's", "Lusterous Lilies", "Serious Sunflower", "Rectifying Rose"]
    dungeon_enemies = ["Tasty Taco's", "Heavenly Confections", "Fantastic Feast", "Beautiful Beautrice", "Handsome Henry"]
    mansion_enemies = []



    # Bosses
    bosses = []

    def __init__(self, name, enemies, boss, id):
        self.name = name
        self.enemies = enemies
        self.boss = boss
        self.id = id

## Maps

garden = Maps(maps[1], garden_enemies, None, 10)
# Garden Enememies will be flower apparations. Ghouls love gardens and flowers

dungeon = Maps(maps[0], dungeon_enemies, None, 10)
# Dungeon consists of human desire apparations as enemies

masion = Maps(maps[2], mansion_enemies, None, 10)
# Mansion consists of 

kings_chambers = Maps(maps[3], kingsChambers_enemies, None, 10)
# Kings Chambers

queens_chambers = Maps(maps[4], mansion_enemies, None, 10)
# Queens Chambers



