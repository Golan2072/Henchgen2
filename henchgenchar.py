# henchgenchar.py
# Henchman generator for the Adventurer Conqueror King System (ACKS).
# Character generator file.
# v0.5, August 1st, 2020
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
        self.ability_mods = henchgenlib.ability_modifiers(self.abilities)
        self.name = henchgenlib.name_gen(self.sex)
        self.charclass = henchgenlib.class_gen(self.level, self.race, self.sex, self.abilities)
        if level > 0:
            self.template = henchgenlib.template_gen(self.charclass)
        else:
            pass
        self.hp = henchgenlib.hp_gen(self.charclass, self.abilities, self.level)
        self.inventory = []
        self.gold = 10 * stellagama.dice(3, 6)
        self.proficiencies = henchgenlib.prof_gen(self.level, self.charclass, self.ability_mods["int"])
        self.inventory = henchgenlib.inventory_gen(self.level, self.charclass)
        self.trinket=henchgenlib.trinket_gen()
        if self.trinket is not None:
            self.inventory.append(self.trinket)
        else:
            pass
        self.proficiency_string = stellagama.list_stringer_comma(self.proficiencies)
        self.inventory_string = stellagama.list_stringer_comma(self.inventory)
        self.quirk = henchgenlib.quirk_gen()


# test area

for i in range(1, 101):
    character = Character(0)
    if character.level >1:
        print(f"{character.name}, level {character.level} {character.sex} {character.race} {character.charclass} ({character.template}), {character.hp} HP")
    else:
        print(
            f"{character.name}, level {character.level} {character.sex} {character.race} {character.charclass}, {character.hp} HP")
    print(
        f"STR: {character.abilities['strength']} DEX: {character.abilities['dexterity']} CON: {character.abilities['constitution']} INT: {character.abilities['intelligence']} WIS: {character.abilities['wisdom']} CHA: {character.abilities['charisma']}")
    print("Inventory:", character.inventory_string)
    print("Proficiencies:", character.proficiency_string)
    if character.quirk is not None:
        print(character.quirk)
    else:
        pass
    print("")
