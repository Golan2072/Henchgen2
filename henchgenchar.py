# henchgenchar.py
# Henchman generator for the Adventurer Conqueror King System (ACKS).
# Character generator file.
# v0.3, July 19th, 2020
# This is open source code, feel free to use it for any purpose.
# Contact the author at golan2072@gmail.com.

# import modules
import random
import string
import os
import platform
import stellagama
import henchgenlib


# set classes

class Character:
    def __init__(self, level):
        self.level = level
        self.sex = random.choice(["male", "female"])
        self.race = henchgenlib.race_gen()
        self.abilities = henchgenlib.ability_gen(self.race)
        self.name = henchgenlib.name_gen(self.sex)
        self.charclass = henchgenlib.class_gen(self.level, self.race, self.sex, self.abilities)
        self.hp = henchgenlib.hp_gen(self.charclass, self.abilities, self.level)
        self.gold = 10 * stellagama.dice(3, 6)
        self.trinket = stellagama.random_line("./data/trinkets.txt")  # generates trinket
        self.quirk = stellagama.random_line("./data/quirks.txt")  # generates quirk


# test area

for i in range(1, 21):
    character = Character(stellagama.dice(1, 4)-1)
    print(f"{character.name}, level {character.level} {character.sex} {character.race} {character.charclass}, {character.hp} HP")
    print(f"STR: {character.abilities['strength']} DEX: {character.abilities['dexterity']} CON: {character.abilities['constitution']} INT: {character.abilities['intelligence']} WIS: {character.abilities['wisdom']} CHA: {character.abilities['charisma']}")
    print("proficiencies:")
    print(character.quirk)
    print(character.trinket)
    print("")