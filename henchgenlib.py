# henchgenlib.py
# A henchman generator for the Adventurer Conqueror King System (ACKS)
# Library file.
# v0.5, August 1st, 2020
# This is open source code, feel free to use it for any purpose
# contact me at golan2072@gmail.com

# Import modules
import random
import stellagama
import json

# Global lists and dictionaries
warrior_template_list = ["thug", "thug", "thug", "mercenary", "mercenary", "hunter", "noble"]
commoner_template_list = ["butcher", "barrister", "folk healer", "prostitute", "beggar", "preacher", "blacksmith",
                          "lumberjack", "alchemist", "houndmaster", "fortune teller", "ditch digger",
                          "grave digger", "jester", "jeweler", "merchant", "sailor", "miller", "minstrel",
                          "scribe"]

npc_template_list = warrior_template_list + commoner_template_list+["peasant"]
pc_template_dict = {
    "anti-paladin": ["desecrator", "tormentor", "deceiver", "corruptor", "slayer", "enforcer", "doombringer",
                     "oppressor"],
    "assassin": ["cutthroat", "bounty hunter", "pirate", "bravo", "assassin-for-hire", "betrayer", "infiltrator", "cult deathbringer"],
    "barbarian": ["tribal warrior (Ivory Kingdoms)", "berserker (Jutland)", "sea rover (Jutland)",
                  "skirmisher (Skysostan)", "death dealer (Jutland)", "pit fighter (Ivory Kingdoms)",
                  "Housecarl (Jutland)", "Nomad (Skysostan"],
    "bard": ["woodland piper", "charlatan", "swashbuckler", "wandering minstrel", "historian", "beguiler", "spy", "aristocrat"],
    "bladedancer": ["warrior witch", "oracle dancer", "bringer of mercy", "bladesingress", "temple bladedancer", "veiled assassin", "consular", "warrior princess"],
    "cleric": ["hermit", "prophet", "mendicant", "proselytizer", "priest", "undead slayer", "exorcist", "crusader"],
    "craftpriest": ["outcast", "runeseer", "reliquary guardian", "documentarian", "reclaimer", "sacramentalist", "purifier", "seeker"],
    "delver": ["survivalist", "prowler", "mountaineer", "tunnel runner", "pest controller", "treasure hunter", "vermin slayer", "patroller"],
    "fury": ["foe eater", "dungeoneer", "belligerent", "warmonger", "tempest", "dirge marcher", "bloodboiler", "vengeful lord"],
    "machinist": ["scavenger", "apothecary", "mechanic", "discoverer", "engineer", "artillerist", "war machinist", "artificer"],
    "vaultguard": ["deserter", "battlerager", "sentinel", "clansdwarf", "goblin slayer", "axe bearer", "besieger", "highborn"],
    "courtier": ["dilettante", "philanthropist", "colonizer", "rake", "scion", "socialite", "intriguer", "emissary"],
    "enchanter": ["trickster", "charlatan", "occultist", "transmogrifier", "antiquarian", "siren", "militant", "patrician"],
    "ranger": ["wanderer", "trapper", "mariner", "hunter", "woodland stalker", "scout", "falconer", "mounted archer"],
    "spellsword": ["exile", "beastmaster", "dreadsword", "bladesinger", "swordmage", "flametongue", "captain", "winged knight"],
    "nightblade": ["rogue", "pursuer", "antagonist", "duelist-for-hire", "silent slayer", "arcane avenger", "deceiver", "royal enforcer"],
    "explorer": ["wanderer", "carthographer", "mariner", "pathfinder", "waylayer", "scout", "monster hunter", "outrider"],
    "fighter": ["thug", "ravager", "corsair", "guardsman", "mercenary", "gladiator", "legionary", "lancer"],
    "trickster": ["wastrel", "know-it-all", "tinker", "performer", "mummer", "jongleur", "voluptuary", "swindler"],
    "mage": ["hedge wizard", "soothsayer", "necromancer", "elementalist", "magical scholar", "eunuch sorcerer", "warmage", "court magist"],
    "mystic": ["ascetic", "yogi", "temple guard", "enlightened mind", "warrior monk", "cultist", "faith healer", "noble philosopher"],
    "wonderworker": ["ferine", "augur", "corrupted soul", "servant of fire", "astrologer", "inceptor", "wrathbringer", "messiah"],
    "paladin": ["errant", "gallant", "temple guardian", "champion", "foe hunter", "vanguard", "inquisitor", "templar"],
    "priestess": ["anchorite", "oracle", "chantress", "medician", "sacred courtesan", "missionary", "lightbringer"],
    "shaman": ["pariah", "wise man", "warchanter", "runecaster", "druid", "snake handler", "spirit raiser", "nomad shaman"],
    "thief": ["outlaw", "thief-acrobat", "buccaneer", "tomb raider", "cat burglar", "lockbreaker", "failed apprentice", "traveller"],
    "gladiator": ["runaway", "rampager", "beastfighter", "manhunter", "arena veteran", "prizefighter", "gladiator trainer", "slaver"],
    "venturer": ["bankrupt", "factotum", "merchant mariner", "merchant traveller", "antiquary", "caravaneer", "comprador", "magnate"],
    "warlock": ["pact witch", "changeling", "deranged alchemist", "defiler", "corrupt scholar", "diabolist", "destroyer", "scheming vizier"],
    "witch": ["crone (antiquarian)", "dark oracle (chthonic)", "botono (voudon)", "lorelei (sylvan)", "village witch (antiquarian)", "death mistress (chthonic)", "fetishist (voudon)", "faerie princess (sylvan)"],
    "ruinguard": ["flesheater", "hatemonger", "grimguard", "avenger", "doomwielder", "warmaster", "ruinbinder", "shadowcrown"],
    "beastmaster": ["wolfpack runner"],
    "berserker": ["bear-cult warrior"],
    "chosen": ["inheritor"],
    "spellsinger": ["sirenian"],
    "freebooter": ["spelunker (Expeditionary path)"],
    "bounder": ["kennelmaster"],
    "burglar": ["rumormonger"],
    "champion": ["warden (Ranger calling)"],
    "wizard": ["servant of fire (Fellowship path)"],
    "deathchanter": ["cryptchanter"],
    "darklord": ["warlord"],
    "warmistress": ["avenging angel"]
}
general_proficiencies = ["Alchemy", "Animal Husbandry", "Animal Training", "Art", "Bargaining", "Caving",
                         "Collegiate Wizardry",
                         "Craft", "Diplomacy", "Disguise", "Endurance", "Engineering", "Gambling", "Healing",
                         "Intimidation",
                         "Knowledge", "Labor", "Language", "Leadership", "Lip Reading", "Manual of Arms", "Mapping",
                         "Military Strategy", "Mimicry", "Naturalism", "Navigation", "Performance", "Profession",
                         "Riding", "Seafaring",
                         "Seduction", "Siege Engineering", "Signalling", "Survival", "Theology", "Tracking", "Trapping"]

classed_templates = {}

# Load data files
with open('npc_templates.json') as json_file:
    npc_templates = json.load(json_file)
with open('pc_templates.json') as json_file:
    pc_templates = json.load(json_file)


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


def ability_modifiers(ability_dict):
    ability_mod_dict = {"str": attribute_modifier(ability_dict["strength"]),
                        "dex": attribute_modifier(ability_dict["dexterity"]),
                        "con": attribute_modifier(ability_dict["constitution"]),
                        "int": attribute_modifier(ability_dict["intelligence"]),
                        "wis": attribute_modifier(ability_dict["wisdom"]),
                        "cha": attribute_modifier(ability_dict["charisma"])}
    return ability_mod_dict


def class_gen(level, race, sex, abilities_dict):
    if race == "human" and level == 0:
        return random.choice(["peasant", random.choice(warrior_template_list), random.choice(warrior_template_list),
                              random.choice(commoner_template_list)])
    elif level > 0:
        if race == "human":
            if max(abilities_dict, key=abilities_dict.get) == "strength":
                return random.choice(["fighter", "fighter", "fighter", "assassin", "explorer", "anti-paladin"])
            elif max(abilities_dict, key=abilities_dict.get) == "dexterity" and sex == "male":
                return random.choice(["thief", "thief", "thief", "assassin", "freebooter"])
            elif max(abilities_dict, key=abilities_dict.get) == "dexterity" and sex == "female":
                return random.choice(["thief", "thief", "thief", "assassin", "freebooter", "warmistress"])
            elif max(abilities_dict, key=abilities_dict.get) == "constitution":
                return random.choice(["barbarian", "mystic", "beastmaster", "berserker"])
            elif max(abilities_dict, key=abilities_dict.get) == "intelligence":
                return random.choice(["mage", "warlock"])
            elif max(abilities_dict, key=abilities_dict.get) == "wisdom" and sex == "female":
                return random.choice(
                    ["cleric", "cleric", "cleric", "cleric", "bladedancer", "priestess", "shaman", "witch"])
            elif max(abilities_dict, key=abilities_dict.get) == "wisdom" and sex == "male":
                return random.choice(
                    ["cleric", "cleric", "cleric", "cleric", "shaman"])
            elif max(abilities_dict, key=abilities_dict.get) == "charisma":
                return random.choice(["bard", "bard", "bard", "paladin", "paladin", "venturer", "venturer", "venturer", "chosen"])
            else:
                return "fighter"
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
            return "peasant"
    else:
        return "peasant"


def template_gen(charclass):
    return random.choice(pc_template_dict[charclass])


def name_gen(sex):
    name = ""
    if sex == "male":
        return stellagama.random_line("./data/malenames.txt")  # output random male name
    elif sex == "female":
        return stellagama.random_line("./data/femalenames.txt")  # output random female name
    else:
        return "Tokay"


def prof_gen(level, charclass, intmod):
    proflist = []
    if level == 0:
        proflist += npc_templates[charclass]["proficiencies"]
        for i in range(0, 2):
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
    final_profs=[]
    for proficiency in proflist:
        if proficiency in ["Alchemy", "Animal Husbandry", "Animal Training", "Art", "Bargaining", "Craft", "Engineering", "Healing", "Performance", "Language", "Profession", "Riding", "Siege Engineering", "Weapon Focus"]:
            if proficiency in final_profs:
                final_profs.remove(proficiency)
                final_profs.append(proficiency + " 2")
            elif proficiency + " 2" in final_profs:
                final_profs.remove(proficiency + " 2")
                final_profs.append(proficiency + " 3")
            elif proficiency + " 3" in final_profs:
                final_profs.remove(proficiency + " 3")
                final_profs.append(proficiency + " 4")
            else:
                final_profs.append(random.choice(general_proficiencies))
        else:
            if proficiency in final_profs:
                final_profs.append(random.choice(general_proficiencies))
                if proficiency in final_profs:
                    final_profs.append(random.choice(general_proficiencies))
                else:
                    final_profs.append(proficiency)
            else:
                final_profs.append(proficiency)
    return final_profs


def inventory_gen(level, charclass):
    inventory = []
    if level == 0:
        armor = random.choice(npc_templates[charclass]["armor"])
        if armor is not None:
            inventory.append(armor)
        else:
            pass
        weapon = random.choice(npc_templates[charclass]["weapons"])
        if weapon is not None:
            inventory.append(weapon)
        else:
            pass
        items = random.choice(npc_templates[charclass]["items"])
        if items is not None:
            inventory.append(items)
        else:
            pass
    else:
        inventory = []
    return inventory


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


def trinket_gen():
    if stellagama.dice(1, 6) >= 5:
        return stellagama.random_line("./data/trinkets.txt")
    else:
        pass


def quirk_gen():
    if stellagama.dice(1, 6) >= 5:
        return stellagama.random_line("./data/quirks.txt")
    else:
        pass

# Test Area
