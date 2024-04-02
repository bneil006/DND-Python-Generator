#### CHECK ALL OF THESE FOR CORRECTNESS LATER, FLEW THREW THE BOOKS & ONLINE RESOURCES TO FIND THIS MATERIAL ####

RACE_DICT = {
    "results": 
    [
        {
            "index": "dragonborn",
            "name": "Dragonborn",
            "ability_score_increases": {"CHA": 1, "STR": 2},
            "age": "Reach adulthood by 15 and live to around 80.",
            "alignment": "Tend towards their draconic ancestry. Chromatic dragon ancestry may lean towards evil, while metallic may lean towards good.",
            "size": "Medium",
            "speed": 30,
            "languages": ["Common", "Draconic"],
            "vision": "Normal",
            "skill_proficiencies": [],
            "tool_proficiencies": [],
            "weapon_proficiencies": [],
            "armor_proficiencies": [],
            "special_abilities": [
                {
                    "name": "Breath Weapon",
                    "description": "You can use your action to exhale destructive energy. Your draconic ancestry determines the size, shape, and damage type of the exhalation."
                },
                {
                    "name": "Damage Resistance",
                    "description": "You have resistance to the damage type associated with your draconic ancestry."
                }
            ],
            "physical_description": "Dragonborn look very much like dragons standing erect in humanoid form, though they lack wings or a tail.",
            "traits": {
                "Draconic Ancestry": "You choose one type of dragon as your ancestor. The type determines your breath weapon and damage resistance."
            },
            "subraces": [],
            "other": [],
        },
        {
            "index": "dwarf",
            "name": "Dwarf",
            "ability_score_increases": {"CON": 2},
            "age": "Mature at the same rate as humans, but are considered young until they reach 50. Live about 350 years.",
            "alignment": "Most dwarves are lawful, with a strong sense of fair play and a belief that everyone deserves to share in the benefits of a just order.",
            "size": "Medium",
            "speed": 25,
            "languages": ["Common", "Dwarvish"],
            "vision": "Darkvision (60 feet)",
            "skill_proficiencies": [],
            "tool_proficiencies": ["Smiths tools", "Brewers supplies","Masons tools"],
            "weapon_proficiencies": ["Battleaxe", "Handaxe", "Light hammer", "Warhammer"],
            "armor_proficiencies": [],
            "special_abilities": [],
            "physical_description": "Dwarves are solid and enduring like the mountains they love, weathering the passage of centuries with stoic endurance and little change.",
            "traits": {
                
            },
            "subraces": 
            [
                {
                    "index": "hill-dwarf",
                    "name": "Hill Dwarf",
                    "ability_score_increases": {"WIS": 1},
                    "skill_proficiencies": [],
                    "traits": {
                        "Dwarven Toughness": "Your hit point maximum increases by 1, and it increases by 1 every time you gain a level."
                    }
                },
                {
                    "index": "mountain-dwarf",
                    "name": "Mountain Dwarf",
                    "ability_score_increases": {"STR": 2},
                    "skill_proficiencies": ["Light armor", "Medium armor"],
                    "traits": {
                        "Dwarven Armor Training": "You have proficiency with light and medium armor."
                    }
                }
            ],
            "other": [],
        },
        {
        "index": "elf",
        "name": "Elf",
        "ability_score_increases": {"DEX": 2},
        "age": "Typically claim adulthood and an adult name around the age of 100 and can live to be 750 years old.",
        "alignment": "Elves love freedom, variety, and self-expression, so they lean strongly towards the gentler aspects of chaos. They value and protect others' freedom as well as their own, and they are more often good than not.",
        "size": "Medium",
        "speed": 30,
        "languages": ["Common", "Elvish"],
        "vision": "Darkvision (60 feet)",
        "skill_proficiencies": [],
        "tool_proficiencies": [],
        "weapon_proficiencies": [],
        "armor_proficiencies": [],
        "special_abilities": [
            {
                "name": "Fey Ancestry",
                "description": "You have advantage on saving throws against being charmed, and magic can't put you to sleep."
            },
            {
                "name": "Trance",
                "description": "Elves don't need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day. The Common word for such meditation is 'trance.'"
            },
            {
                "name": "Keen Senses",
                "description": "You have proficiency in the Perception skill."
            }
        ],
        "physical_description": "Elves are of human height, but they are slender, with pointed ears and no facial hair. They have a grace that makes them seem almost to dance as they walk.",
        "traits": {},
        "subraces": 
        [
            {
                "index": "high-elf",
                "name": "High Elf",
                "ability_score_increases": {"INT": 1},
                "skill_proficiencies": [],
                "traits": {
                    "Elf Weapon Training": "You have proficiency with the longsword, shortsword, shortbow, and longbow.",
                    "Cantrip": "You know one cantrip of your choice from the wizard spell list. Intelligence is your spellcasting ability for it.",
                    "Extra Language": "You can speak, read, and write one extra language of your choice."
                }
            },
            {
                "index": "wood-elf",
                "name": "Wood Elf",
                "ability_score_increases": {"WIS": 1},
                "skill_proficiencies": [],
                "traits": {
                    "Elf Weapon Training": "You have proficiency with the longsword, shortsword, shortbow, and longbow.",
                    "Fleet of Foot": "Your base walking speed increases to 35 feet.",
                    "Mask of the Wild": "You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena."
                }
            },
            {
                "index": "dark-elf",
                "name": "Dark Elf",
                "ability_score_increases": {"CHA": 1},
                "skill_proficiencies": [],
                "traits": {
                    "Superior Darkvision": "Your darkvision has a radius of 120 feet.",
                    "Sunlight Sensitivity": "You have disadvantage on attack rolls and Wisdom (Perception) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight.",
                    "Drow Magic": "You know the dancing lights cantrip. When you reach 3rd level, you can cast the faerie fire spell once per day. When you reach 5th level, you can also cast the darkness spell once per day. Charisma is your spellcasting ability for these spells.",
                    "Drow Weapon Training": "You have proficiency with rapiers, shortswords, and hand crossbows."
                }
            }
        ],
        "other": [],
        },
        {
        "index": "gnome",
        "name": "Gnome",
        "ability_score_increases": {"INT": 2},
        "age": "Gnomes mature at the same rate humans do, and most are expected to settle down into an adult life by around age 40. They can live 350 to almost 500 years.",
        "alignment": "Gnomes are most often good. Those who tend towards law are sages, engineers, researchers, scholars, investigators, or inventors. Those who tend towards chaos are minstrels, tricksters, wanderers, or fanciful jewelers. Gnomes are good-hearted, and even the tricksters among them are more playful than vicious.",
        "size": "Small",
        "speed": 25,
        "languages": ["Common", "Gnomish"],
        "vision": "Darkvision (60 feet)",
        "skill_proficiencies": [],
        "tool_proficiencies": [],
        "weapon_proficiencies": [],
        "armor_proficiencies": [],
        "special_abilities": [
            {
                "name": "Gnome Cunning",
                "description": "You have advantage on all Intelligence, Wisdom, and Charisma saving throws against magic."
            }
        ],
        "physical_description": "Gnomes are diminutive, fairy-like folk, with their whimsical expressions and bright eyes. They often have the appearance of elderly humans from a young age, yet their faces invariably carry a mischievous smile.",
        "traits": {},
        "subraces": 
        [
            {
                "index": "rock-gnome",
                "name": "Rock Gnome",
                "ability_score_increases": {"CON": 1},
                "skill_proficiencies": [],
                "traits": {
                    "Artificer's Lore": "Whenever you make an Intelligence (History) check related to magic items, alchemical objects, or technological devices, you can add twice your proficiency bonus, instead of any proficiency bonus you normally apply.",
                    "Tinker": "You have proficiency with artisan's tools (tinker's tools). Using those tools, you can spend 1 hour and 10 gp worth of materials to construct a Tiny clockwork device (AC 5, 1 hp). The device ceases to function after 24 hours (unless you spend 1 hour repairing it to keep the device functioning), or when you use your action to dismantle it."
                }
            },
            {
                "index": "forest-gnome",
                "name": "Forest Gnome",
                "ability_score_increases": {"DEX": 1},
                "skill_proficiencies": [],
                "traits": {
                    "Natural Illusionist": "You know the minor illusion cantrip. Intelligence is your spellcasting ability for it.",
                    "Speak with Small Beasts": "Through sounds and gestures, you can communicate simple ideas with Small or smaller beasts. Forest Gnomes love animals and often keep squirrels, badgers, rabbits, moles, woodpeckers, and other creatures as beloved pets."
                }
            }
        ],
        "other": [],
        },
        {
        "index": "half-elf",
        "name": "Half Elf",
        "ability_score_increases": {"CHA": 2},
        "age": "Half-Elves mature at the same rate humans do and reach adulthood around the age of 20. They live much longer than humans, however, often exceeding 180 years.",
        "alignment": "Half-Elves share the chaotic bent of their elven heritage. They value both personal freedom and creative expression, demonstrating neither love of leaders nor desire for followers. They chafe at rules, resent others’ demands, and sometimes prove unreliable, or at least unpredictable.",
        "size": "Medium",
        "speed": 30,
        "languages": ["Common", "Elvish", "One extra language of your choice"],
        "vision": "Darkvision (60 feet)",
        "skill_proficiencies": ["Two skills of your choice"],
        "tool_proficiencies": [],
        "weapon_proficiencies": [],
        "armor_proficiencies": [],
        "special_abilities": [
            {
                "name": "Fey Ancestry",
                "description": "You have advantage on saving throws against being charmed, and magic can't put you to sleep."
            },
            {
                "name": "Skill Versatility",
                "description": "You gain proficiency in two skills of your choice."
            }
        ],
        "physical_description": "Half-Elves stand taller than humans but shorter than elves. They inherit a mix of physical features from their human and elven parents, and their ears are pointed, though less dramatically so than an elf's. They have the same range of complexions as humans and elves, making them as diverse as either race.",
        "traits": {},
        "subraces": [],
        "other": ["Two other ability scores of your choice: +1"],
        },
        {
        "index": "half-orc",
        "name": "Half-Orc",
        "ability_score_increases": {"STR": 2, "CON": 1},
        "age": "Half-Orcs mature a little faster than humans, reaching adulthood around age 14. They age noticeably faster and rarely live longer than 75 years.",
        "alignment": "Half-Orcs inherit a tendency toward chaos from their orc parents and are not strongly inclined toward good. Half-Orcs raised among orcs and willing to live out their lives among them are usually evil.",
        "size": "Medium",
        "speed": 30,
        "languages": ["Common", "Orc"],
        "vision": "Darkvision (60 feet)",
        "skill_proficiencies": [],
        "tool_proficiencies": [],
        "weapon_proficiencies": [],
        "armor_proficiencies": [],
        "special_abilities": [
            {
                "name": "Relentless Endurance",
                "description": "When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You cant use this feature again until you finish a long rest."
            },
            {
                "name": "Savage Attacks",
                "description": "When you score a critical hit with a melee weapon attack, you can roll one of the weapon's damage dice one additional time and add it to the extra damage of the critical hit."
            },
        ],
        "physical_description": "Half-Orcs are somewhat larger and bulkier than humans, and they range from 5 to well over 6 feet tall. Their skin tones range from gray to pale green, and their faces feature the distinctive orcish tusk-like canines. Their eyes are usually dark, showing the fierce determination of their lineage.",
        "traits": {},
        "subraces": [],
        "other": [],
        },
        {
        "index": "halfling",
        "name": "Halfling",
        "ability_score_increases": {"DEX": 2},
        "age": "Halflings reach adulthood at the age of 20 and generally live into the middle of their second century.",
        "alignment": "Halflings tend towards lawful good. With their inherent kindness and a tendency not to make waves, they get along well with others. They are loyal to their family and friends, and most halflings see the value in a harmonious and orderly life.",
        "size": "Small",
        "speed": 25,
        "languages": ["Common", "Halfling"],
        "vision": "Normal",
        "skill_proficiencies": [],
        "tool_proficiencies": [],
        "weapon_proficiencies": [],
        "armor_proficiencies": [],
        "special_abilities": [
            {
                "name": "Lucky",
                "description": "When you roll a 1 on the d20 for an attack roll, ability check, or saving throw, you can reroll the die and must use the new roll."
            },
            {
                "name": "Brave",
                "description": "You have advantage on saving throws against being frightened."
            },
            {
                "name": "Halfling Nimbleness",
                "description": "You can move through the space of any creature that is of a size larger than yours."
            }
        ],
        "physical_description": "Halflings average about 3 feet tall and weigh about 40 pounds. Their size makes them agile and capable of moving quietly and stealthily. They have curly hair, bright eyes, and wear simple, comfortable, and practical clothes.",
        "traits": {},
        "subraces": 
        [
            {
                "index": "lightfoot-halfling",
                "name": "Lightfoot Halfling",
                "ability_score_increases": {"CHA": 1},
                "skill_proficiencies": [],
                "traits": {
                    "Naturally Stealthy": "You can attempt to hide even when you are obscured only by a creature that is at least one size larger than you."
                }
            },
            {
                "index": "stout_halfling",
                "name": "Stout Halfling",
                "ability_score_increases": {"CON": 1},
                "skill_proficiencies": [],
                "traits": {
                    "Stout Resilience": "You have advantage on saving throws against poison, and you have resistance against poison damage."
                }
            }
        ],
        "other": [],
        },
        {
        "index": "human",
        "name": "Human",
        "ability_score_increases": {"STR": 1, "DEX": 1, "CON": 1, "INT": 1, "WIS": 1, "CHA": 1},
        "age": "Humans reach adulthood in their late teens and live less than a century.",
        "alignment": "Humans tend towards no particular alignment. The best and the worst are found among them.",
        "size": "Medium",
        "speed": 30,
        "languages": ["Common", "One extra language of your choice"],
        "vision": "Normal",
        "skill_proficiencies": [],
        "tool_proficiencies": [],
        "weapon_proficiencies": [],
        "armor_proficiencies": [],
        "special_abilities": [],
        "physical_description": "Humans vary widely in height and build, from barely 5 feet to well over 6 feet tall. Skin tones range from dark to light and everything in between. Their hair and eye colors are similarly varied.",
        "traits": {},
        "subraces": [],
        "other": [],
        },
        {
        "index": "tiefling",
        "name": "Tiefling",
        "ability_score_increases": {"CHA": 2, "INT": 1},
        "age": "Tieflings mature at the same rate as humans but live a few years longer.",
        "alignment": "Tieflings might not have an innate tendency towards evil, but many of them end up there. Evil or not, an independent nature inclines many tieflings toward a chaotic alignment.",
        "size": "Medium",
        "speed": 30,
        "languages": ["Common", "Infernal"],
        "vision": "Darkvision (60 feet)",
        "skill_proficiencies": [],
        "tool_proficiencies": [],
        "weapon_proficiencies": [],
        "armor_proficiencies": [],
        "special_abilities": [
            {
                "name": "Hellish Resistance",
                "description": "You have resistance to fire damage."
            },
            {
                "name": "Infernal Legacy",
                "description": "You know the thaumaturgy cantrip. At 3rd level, you can cast the hellish rebuke spell as a 2nd-level spell once with this trait and regain the ability to do so when you finish a long rest. At 5th level, you can cast the darkness spell once with this trait and regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for these spells."
            }
        ],
        "physical_description": "Tieflings have large horns that take any of a variety of shapes, from straight points to elaborate curves mimicking those of a ram. Their skin tones cover the full range of human coloration, but also include various shades of red. Their eyes are solid colors—black, red, white, silver, or gold—with no visible sclera or pupil. Their tails are thick and long, and their canine teeth are sharply pointed.",
        "traits": {},
        "subraces": [],
        "other": [],
        },
    ]
}