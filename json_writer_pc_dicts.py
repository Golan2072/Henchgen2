import json

pc_templates = {"desecrator": {"proficiencies": ['Dungeon Bashing', "Knowledge (occult)"],
                               "weapon": "befouled scourge, rusted ball and chain", "armor": "none",
                               "items": "gnawed wooden holy symbol"},
                "tormentor": {"proficiencies": ['Combat Trickery (incapacitate)', "Profession (Torturer)"],
                              "weapon": "jagged battle axe", "armor": "black hide armor",
                              "items": "blackened wavy dagger (unholy symbol)"},
                "deceiver": {"proficiencies": ['Ambushing', "Diplomacy"],
                             "weapon": "3 concealed daggers", "armor": "fine leather armor",
                             "items": "unholy symbol of the Horned Rat"},
                "corruptor": {"proficiencies": ['Mystic Aura', "Seduction"],
                              "weapon": "slender scimitar , copper-barbed scourge", "armor": "black leather armor",
                              "items": "unholy symbol of the Medusa"},
                "Slayer": {"proficiencies": ['Berserkergang', "Endurance"],
                           "weapon": "barbed morning star and serrated two-handed sword", "armor": "banded plate armor",
                           "items": "unholy symbol of the Black Gauntlet"},
                "Enforcer": {"proficiencies": ['Alertness', "Intimidation"],
                             "weapon": "black-shafted spear, blackened sword",
                             "armor": "black steel shield, black lamellar armor",
                             "items": "unholy symbol of the Draconic Eye"},
                "Doombringer": {"proficiencies": ['Kin-Slaying', "Theology"],
                                "weapon": "wickedly-curved sickle, barbed flail",
                                "armor": "black banded plate armor, black steel shield",
                                "items": "unholy symbol of the Black Circle"},
                "oppressor": {"proficiencies": ['Command', "Riding"],
                              "weapon": "black-shafted spear, polished sword",
                              "armor": "black steel shield, black lamellar armor",
                              "items": "unholy symbol of the Worm"},
                "tribal warrior (Ivory Kingdoms)": {"proficiencies": ['Beast Friendship', "Tracking", "Running"],
                                                    "weapon": "bola, 5 feathered darts, spear, club",
                                                    "armor": "cowhide shield, wildebeest hide armor",
                                                    "items": "loincloth"},
                "berserker (Jutland)": {"proficiencies": ['Berserkergang', "Intimidation", "Climbing"],
                                        "weapon": "long bearded axe",
                                        "armor": "chainmail",
                                        "items": "rough spun wool tunic"},
                "sea rover (Jutland)": {"proficiencies": ['Swashbuckling', "Seafaring", "Climbing"],
                                        "weapon": "shortbow, iron-tipped spear, bearded axe",
                                        "armor": "kite shield, leather armor",
                                        "items": "wineskin with strong ale"},
                "skirmisher (Skysostan)": {"proficiencies": ['Skirmishing', "Endurance", "Precise Shooting"],
                                        "weapon": "composite bow, pair of scimitars",
                                        "armor": "leather scale armor",
                                        "items": "wool tunic"},
                "death dealer (Jutland)": {"proficiencies": ['Ambushing', "Survival", "Climbing"],
                                           "weapon": "two-handed iron sword, francisca",
                                           "armor": "chainmail",
                                           "items": "silver arm-bands (25gp value"},
                "pit fighter (Ivory Kingdoms)": {"proficiencies": ['Combat Reflexes', "Gambling", "Running"],
                                           "weapon": "spear, weighted net, hand axe",
                                           "armor": "gladiatoral armor",
                                           "items": "49gp in arena earnings"},
                "housecarl (Jutland)": {"proficiencies": ['Fighting Style (weapon and shield)', "Military Strategy", "Climbing"],
                                                 "weapon": "shortbow, iron spear, iron sword",
                                                 "armor": "kite shield, chainmail",
                                                 "items": "silver arm-bands (25gp value), silver amulet (25gp value)"},
                "nomad (Skysostan": {
                    "proficiencies": ['Weapon Focus (bow/crossbow)', "Riding", "Precise Shooting"],
                    "weapon": "composite bow, scimitar",
                    "armor": "leather scale armor",
                    "items": "light riding horse"},
                "woodland piper": {
                    "proficiencies": ['Beast Friendship', "Naturalism", "Performance (instruments)"],
                    "weapon": "2 javelins",
                    "armor": "hide armor",
                    "items": "pan pipes"},
                "charlatan": {
                    "proficiencies": ['Prestidigitation', "Alchemy", "Performance (oration)"],
                    "weapon": "quarterstaff",
                    "armor": "leather armor under mage's cassock",
                    "items": "4 pints of rare wine in potion vials"},
                "swashbuckler": {
                    "proficiencies": ['Swashbuckler', "Seafaring", "Performance (singing)"],
                    "weapon": "shortbow, scimitar, 2 well-balanced daggers",
                    "armor": "leather armor",
                    "items": "grappling hook"},
                "wandering minstrel": {
                    "proficiencies": ['Magical Music', "Diplomacy", "Performance (instruments)"],
                    "weapon": "crossbow, shortsword, dagger",
                    "armor": "well-maintained leather armor",
                    "items": "parchment journal half-filled with entries"},
                "historian": {
                    "proficiencies": ['Magical Engineering', "Knowledge (history)", "Performance (epic poetry)"],
                    "weapon": "crossbow, shortsword, dagger",
                    "armor": "well-maintained leather armor",
                    "items": "parchment journal half-filled with entries"},
                "beguiler": {
                    "proficiencies": ['Mystic Aura', "Seduction", "Performance (singing)"],
                    "weapon": "crossbow, sword",
                    "armor": "polished leather armor",
                    "items": "bright silk sash"},
                "spy": {
                    "proficiencies": ['Eavesdropping', "Lip Reading", "Performance (acting)"],
                    "weapon": "crossbow, short sword, dagger",
                    "armor": "unmarked leather armor",
                    "items": "disguise kit"},
                "aristocrat": {
                    "proficiencies": ['Command', "Leadership", "Performance (oration)"],
                    "weapon": "crossbow, matching sword and dagger with lacquered hilts",
                    "armor": "exquisitely stitched leather armor",
                    "items": "medium riding horse"}}


with open('pc_templates.json', 'w') as fileHandle:
    json.dump(pc_templates, fileHandle)
