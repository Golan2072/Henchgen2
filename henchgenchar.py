# henchgenchar.py
# Henchman generator for the Adventurer Conqueror King System (ACKS).
# Character generator file.
# v0.7, August 4th, 2020
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
        self.inventory.sort()
        self.inventory_string = stellagama.list_stringer_comma(self.inventory)
        self.quirk = henchgenlib.quirk_gen()
    def string_output(self):
            if self.level > 1:
                output = str((
                    f"{self.name}, level {self.level} {self.sex} {self.race} {self.charclass} ({self.template}), {self.hp} HP\nSTR: {self.abilities['strength']} DEX: {self.abilities['dexterity']} CON: {self.abilities['constitution']} INT: {self.abilities['intelligence']} WIS: {self.abilities['wisdom']} CHA: {self.abilities['charisma']}\nInventory: {self.inventory_string}\nProficiencies: {self.proficiency_string}"))
            else:
                output = str((
                    f"{self.name}, level {self.level} {self.sex} {self.race} {self.charclass}, {self.hp} HP\nSTR: {self.abilities['strength']} DEX: {self.abilities['dexterity']} CON: {self.abilities['constitution']} INT: {self.abilities['intelligence']} WIS: {self.abilities['wisdom']} CHA: {self.abilities['charisma']}\nInventory: {self.inventory_string}\nProficiencies: {self.proficiency_string}"))
            if self.quirk is not None:
                output+=(f"\n{self.quirk}")
            else:
                pass
            return output
    def list_output(self):
            if self.level >1:
                output =[self.name, self.level, self.sex, self.race, self.charclass, self.template, self.hp, self.abilities['strength'], self.abilities['dexterity'], self.abilities['constitution'], self.abilities['intelligence'], self.abilities['wisdom'], self.abilities['charisma'], self.inventory_string, self.proficiency_string]
            else:
                output = [self.name, self.level, self.sex, self.race, self.charclass, self.hp,
                          self.abilities['strength'], self.abilities['dexterity'], self.abilities['constitution'],
                          self.abilities['intelligence'], self.abilities['wisdom'], self.abilities['charisma'],
                          self.inventory_string, self.proficiency_string]
            if self.quirk is not None:
                output.append(self.quirk)
            else:
                pass
            return output

# test area

for i in range(1, 101):
    character = Character(0)
    print(character.string_output())
    print("")
