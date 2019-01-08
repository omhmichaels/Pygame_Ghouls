"""
#
# S0mHmxxGh0ulz
# 
# Author: l33tH@x0rxxGh0u1
#
"""

# Character Class

class Character:

    def __init__(self, name, id, title, char_type, special_items, health_points, magik, items, stats):
        self.name = name
        self.id = id
        self.title = title
        self.char_type = char_type
        self.special_items = special_items
        self.health_points = health_points
        self.magik = magik
        self.items = items
        self.stats = stats


# Ghouls

Livy = Character("Livy", 0, "Princess", "Ghoul", ["Princess Livy's Tiara of Purity and Truth"], 100, 100, [], [])
Ivy = Character("Ivy", 0, "Queen", "Ghoul", ["Queen Ivy's Crown of Wealth and Fertility"], 100, 100, [], [])
Mivy = Character("Mivy", 0, "King", "Ghoul", ["King Mivy's Crown of Courage and Wisdom"], 100, 100, [], [])
Mickey = Character("Micky", 0, "Prince", "Ghoul", ["Prince Mickey's Crown of Strenght and Curiostity"], 100, 100, [], [])

# Mansion Staff
PollyPoltergiest = Character("Polly", 1, "Dungeon Poltergiest", "Ghoul", ["Polly Poltergiest's Poles of Perspective"], 100, 100, [], [])
GaryGardener = Character("Gary", 1, "Gardener", "Ghoul", ["Gary Gardener's Hedge Trimmers of Fate"], 100, 100, [], [])
BastianButler = Character("Bastian", 1, "Butler", "Ghoul", ["Bastian Butler's Bowls of Balance"], 100, 100, [], [])
MillyMaid = Character("Molly", 1, "Maid", "Ghoul", ["Molly Maid's Mop of Mistrust"], 100, 100, [], [])

# Villians
DamnelliaPage = Character("Damnellia Page", 1, "Queen of Dispair", "Wicked Witch", ["Damnellia Page's Book of Spirits: Present and Future"], 200, 200, [], [])

