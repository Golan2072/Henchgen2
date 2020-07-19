# henchgenlib.py
# A henchman generator for the Adventurer Conqueror King System (ACKS)
# Library file.
# v0.3, July 19th, 2020
# This is open source code, feel free to use it for any purpose
# contact me at golan2072@gmail.com

# Import modules
import random
import stellagama
import json

# Lists
warrior_template_list = ["thug", "thug", "thug", "mercenary", "mercenary", "hunter", "noble"]
commoner_template_list = ["butcher", "barrister", "folk healer", "prostitute", "beggar", "preacher", "blacksmith",
                          "lumberjack", "alchemist", "houndmaster", "fortune teller", "ditch digger",
                          "grave digger", "jester", "jeweler", "merchant", "sailor", "miller", "minstrel",
                          "scribe"]

general_proficiencies = ["Alchemy", "Animal Husbandry", "Animal Training", "Art", "Bargaining", "Caving", "Collegiate Wizardry",
         "Craft", "Diplomacy", "Disguise", "Endurance", "Engineering", "Gambling", "Healing", "Intimidation",
         "Knowledge", "Labor", "Language", "Leadership", "Lip Reading", "Manual of Arms", "Mapping",
         "Military Strategy", "Mimicry", "Naturalism", "Navigation", "Performance", "Profession", "Riding", "Seafaring",
         "Seduction", "Siege Engineering", "Signalling", "Survival", "Theology", "Tracking", "Trapping"]

classed_templates = {}


# Functions
def attribute_modifier(attribute):
    modlib = [0, -3, -3, -3, -2, -2, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3]
    return modlib[attribute]


def race_gen():
    throw = stellagama.dice(1, 100)
    if throw <= 83:
        return "human"
    elif throw in range(84, 91):
        return "elven"
    elif throw in range(91, 98):
        return "dwarven"
    elif throw == 98:
        return "thrassian"
    elif throw == 99:
        return "zaharan"
    elif throw == 100:
        sub_throw = stellagama.dice(1, 3)
        if sub_throw == 1:
            return "gnome"
        elif sub_throw == 2:
            return "halfling"
        elif sub_throw == 3:
            return "nobiran"
        else:
            return "human"
    else:
        return "human"


def ability_gen(race):
    abilities = {"strength": stellagama.dice(3, 6), "dexterity": stellagama.dice(3, 6),
                 "constitution": stellagama.dice(3, 6), "intelligence": stellagama.dice(3, 6),
                 "wisdom": stellagama.dice(3, 6), "charisma": stellagama.dice(3, 6)}
    if race == "human":
        return abilities
    elif race == "elven" and abilities["intelligence"] < 9:
        abilities["intelligence"] = 9
        return abilities
    elif race == "dwarven" and abilities["constitution"] < 9:
        abilities["constitution"] = 9
        return abilities
    elif race == "halfling" and abilities["dexterity"] < 9:
        abilities["dexterity"] = 9
        return abilities
    elif race == "thrassian":
        if abilities["strength"] < 9:
            abilities["strength"] = 9
        if abilities["dexterity"] < 9:
            abilities["dexterity"] = 9
        if abilities["constitution"] < 9:
            abilities["constitution"] = 9
        else:
            return abilities
        return abilities
    elif race == "zaharan":
        if abilities["intelligence"] < 9:
            abilities["intelligence"] = 9
        if abilities["wisdom"] < 9:
            abilities["wisdom"] = 9
        if abilities["charisma"] < 9:
            abilities["charisma"] = 9
        else:
            return abilities
        return abilities
    elif race == "gnome":
        if abilities["intelligence"] < 9:
            abilities["intelligence"] = 9
        if abilities["constitution"] < 9:
            abilities["constitution"] = 9
        else:
            return abilities
        return abilities
    elif race == "nobiran":
        if abilities["strength"] < 11:
            abilities["strength"] = 11
        if abilities["dexterity"] < 11:
            abilities["dexterity"] = 11
        if abilities["constitution"] < 11:
            abilities["constitution"] = 11
        if abilities["intelligence"] < 11:
            abilities["intelligence"] = 11
        if abilities["wisdom"] < 11:
            abilities["wisdom"] = 11
        if abilities["charisma"] < 11:
            abilities["charisma"] = 11
        else:
            return abilities
        return abilities
    else:
        return abilities


def class_gen(level, race, sex, abilities_dict):
    if race == "human" and level == 0:
            return random.choice(["peasant", random.choice(warrior_template_list), random.choice(warrior_template_list),
                             random.choice(commoner_template_list)])
    elif level > 0:
        if race == "human":
            if max(abilities_dict, key=abilities_dict.get) == "strength":
                return random.choice(["fighter", "fighter", "fighter", "assassin", "explorer", "anti-paladin"])
            elif max(abilities_dict, key=abilities_dict.get) == "dexterity" and "Sex" == "male":
                return random.choice(["thief", "thief", "thief", "assassin", "freebooter"])
            elif max(abilities_dict, key=abilities_dict.get) == "dexterity" and "Sex" == "female":
                return random.choice(["thief", "thief", "thief", "assassin", "freebooter", "warmistress"])
            elif max(abilities_dict, key=abilities_dict.get) == "constitution":
                return random.choice(["barbarian", "mystic", "beastmaster", "berserker"])
            elif max(abilities_dict, key=abilities_dict.get) == "intelligence":
                return random.choice(["mage", "warlock"])
            elif max(abilities_dict, key=abilities_dict.get) == "wisdom" and "sex" == "female":
                return random.choice(
                    ["cleric", "cleric", "cleric", "cleric", "bladedancer", "priestess", "shaman", "witch"])
            elif max(abilities_dict, key=abilities_dict.get) == "wisdom" and "sex" == "male":
                return random.choice(
                    ["cleric", "cleric", "cleric", "cleric", "shaman"])
            elif max(abilities_dict, key=abilities_dict.get) == "charisma":
                return random.choice(["bard", "bard", "bard", "paladin", "venturer", "chosen"])
            else:
                return "chosen"
        elif race == "dwarven":
            if max(abilities_dict, key=abilities_dict.get) == "strength":
                return random.choice(["vaultguard", "vaultguard", "vaultguard", "fury"])
            elif max(abilities_dict, key=abilities_dict.get) == "wisdom":
                return "craftpriest"
            elif max(abilities_dict, key=abilities_dict.get) == "intelligence":
                return "machinist"
            elif max(abilities_dict, key=abilities_dict.get) == "dexterity":
                return "delver"
            else:
                return "delver"
        elif race == "elven":
            if max(abilities_dict, key=abilities_dict.get) == "strength":
                return "spellsword"
            elif max(abilities_dict, key=abilities_dict.get) == "dexterity":
                return random.choice(["nightblade", "nightblade", "nightblade", "ranger"])
            elif max(abilities_dict, key=abilities_dict.get) == "charisma":
                return random.choice(["courtier", "enchanter"])
            elif max(abilities_dict, key=abilities_dict.get) == "intelligence":
                return "spellsinger"
            else:
                return "spellsword"
        elif race == "gnome":
            if max(abilities_dict, key=abilities_dict.get) == "charisma":
                return "trickster"
            else:
                return "trickster"
        elif race == "nobiran":
            if max(abilities_dict, key=abilities_dict.get) == "intelligence":
                return "wonderworker"
            elif max(abilities_dict, key=abilities_dict.get) == "charisma":
                return "champion"
            elif max(abilities_dict, key=abilities_dict.get) == "wisdom":
                return "wizard"
            else:
                return "wonderworker"
        elif race == "thrassian":
            if max(abilities_dict, key=abilities_dict.get) == "strength":
                return "gladiator"
            elif max(abilities_dict, key=abilities_dict.get) == "intelligence":
                return "deathchanter"
            else:
                return "gladiator"
        elif race == "zaharan":
            if max(abilities_dict, key=abilities_dict.get) == "strength":
                return "ruinguard"
            elif max(abilities_dict, key=abilities_dict.get) == "intelligence":
                return "sorcerer"
            elif max(abilities_dict, key=abilities_dict.get) == "charisma":
                return "darklord"
            else:
                return "ruinguard"
        elif race == "halfling":
            if max(abilities_dict, key=abilities_dict.get) == "strength":
                return "bounder"
            elif max(abilities_dict, key=abilities_dict.get) == "dexterity":
                return "burglar"
            else:
                return "burglar"
        else:
            return "fighter"
    else:
        return "fighter"


def name_gen(sex):
    name = ""
    if sex == "male":
        return stellagama.random_line("./data/malenames.txt")  # output random male name
    elif sex == "female":
        return stellagama.random_line("./data/femalenames.txt")  # output random female name
    else:
        return "Tokay"


def generate_general_proficiency_list(level, intmod):
    proflist = []
    if level == 0:
        for i in range(0, 4):
            proflist.append(random.choice(general_proficiencies))
        if intmod >= 1:
            for i in range(0, intmod):
                proflist.append(random.choice(general_proficiencies))
    else:
        if intmod >= 1:
            for i in range(0, intmod + 1):
                proflist.append(random.choice(general_proficiencies))
        else:
            proflist = [random.choice(general_proficiencies)]
    return proflist


def hp_gen(charclass, ability_dict, level):
    hp = 0
    hp_dict = {"fighter": 8, "mage": 4, "cleric": 6, "thief": 4, "assassin": 6, "bard": 6,
               "bladedancer": 6, "explorer": 6, "vaultguard": 8, "craftpriest": 6, "spellsword": 6,
               "nightblade": 6, "anti-paladin": 6, "barbarian": 8, "delver": 6, "fury": 8, "machinist": 6,
               "courtier": 6, "enchanter": 4, "ranger": 6, "trickster": 4, "mystic": 6, "wonderworker": 4,
               "paladin": 6, "priestess": 4, "shaman": 6, "gladiator": 8, "venturer": 6, "warlock": 4,
               "witch": 4, "ruinguard": 6, "beastmaster": 6, "berserker": 8, "chosen": 6, "spellsinger": 4,
               "freebooter": 4, "bounder": 6, "burglar": 4, "champion": 8, "wizard": 4, "deathchanter": 8,
               "warmistress": 6, "darklord": 4, "sorcerer": 4}
    if level == 0:
        hp = stellagama.dice(1, 6)
    elif level > 1:
        for i in range(1, level + 1):
            hp += stellagama.dice(1, hp_dict[charclass])
    else:
        hp = stellagama.dice(1, 6)
    hp += attribute_modifier(ability_dict["constitution"])
    if hp <= 0:
        hp = 1
    return hp

# Test Area