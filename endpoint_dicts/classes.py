#### CHECK ALL OF THESE FOR CORRECTNESS LATER, FLEW THREW THE BOOKS & ONLINE RESOURCES TO FIND THIS MATERIAL ####

CLASS_DICT = {
    "results": 
    [
        {
            "index": "barbarian",
            "name": "Barbarian",
            "hit_dice": "1d12",
            "starting_hp": 12,
            "main_stat": "STR",
            "proficiencies": {
                "armor": ["Light armor", "Medium armor", "Shields"],
                "weapons": ["Simple weapons", "Martial weapons"],
                "tools": [],
                "saving_throws": ["STR", "CON"],
                "skills": {2: ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"]}
            },
            "class_features": [
                {
                "name": "Rage",
                "description": "In battle, you fight with primal ferocity. On your turn, you can enter a rage as a bonus action."
                },
                {
                "name": "Unarmored Defense",
                "description": "While you are not wearing any armor, your Armor Class equals 10 + your Dexterity modifier + your Constitution modifier."
                }
            ],
            "level_progression": {
                "1": {
                "features": ["Rage", "Unarmored Defense"],
                "rages": 2,
                "rage_damage": "+2"
                },
                "2": {
                "features": ["Reckless Attack", "Danger Sense"],
                "rages": 2,
                "rage_damage": "+2"
                },
                "3": {
                "features": ["Primal Path"],
                "rages": 3,
                "rage_damage": "+2"
                },
                "4": {
                "features": ["Ability Score Improvement"],
                "rages": 3,
                "rage_damage": "+2"
                },
                "5": {
                "features": ["Extra Attack", "Fast Movement"],
                "rages": 3,
                "rage_damage": "+2"
                },
            },
            "spellcasting": {
                "is_spellcaster": False
            }
        },
        {
            "index": "bard",
            "name": "Bard",
            "hit_dice": "1d8",
            "starting_hp": 8,
            "main_stat": "WIS",
            "proficiencies": {
                "armor": ["Light armor"],
                "weapons": ["Simple weapons", "Hand crossbows", "Longswords", "Rapiers", "Shortswords"],
                "tools": ["Three musical instruments of your choice"],
                "saving_throws": ["DEX", "CHA"],
                "skills": {3: ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"]}
            },
            "class_features": [
                {
                    "name": "Spellcasting",
                    "description": "You have learned to untangle and reshape the fabric of reality in harmony with your wishes and music."
                },
                {
                    "name": "Bardic Inspiration (d6)",
                    "description": "You can inspire others through stirring words or music to do great deeds."
                }
            ],
            "level_progression": {
                "1": {
                    "features": ["Spellcasting", "Bardic Inspiration (d6)"]
                },
                "2": {
                    "features": ["Jack of All Trades", "Song of Rest (d6)"]
                },
                "3": {
                    "features": ["Bard College", "Expertise"]
                },
                "4": {
                    "features": ["Ability Score Improvement"]
                },
                "5": {
                    "features": ["Bardic Inspiration (d8)", "Font of Inspiration"]
                }
            },
            "spellcasting": {
                "is_spellcaster": True
            }
        },
        {
            "index": "cleric",
            "name": "Cleric",
            "hit_dice": "1d8",
            "starting_hp": 8,
            "main_stat": "WIS",
            "proficiencies": {
                "armor": ["Light armor", "Medium armor", "Shields"],
                "weapons": ["Simple weapons"],
                "tools": [],
                "saving_throws": ["WIS", "CHA"],
                "skills": {2: ["History", "Insight", "Medicine", "Persuasion", "Religion"]}
            },
            "class_features": [
                {
                    "name": "Spellcasting",
                    "description": "As a conduit for divine power, you can cast cleric spells."
                },
                {
                    "name": "Divine Domain",
                    "description": "Choose one domain related to your deity: Knowledge, Life, Light, Nature, Tempest, Trickery, or War."
                }
            ],
            "level_progression": {
                "1": {
                    "features": ["Spellcasting", "Divine Domain"]
                },
                "2": {
                    "features": ["Channel Divinity (1/rest)", "Divine Domain feature"]
                },
                "3": {
                    "features": []
                },
                "4": {
                    "features": ["Ability Score Improvement"]
                },
                "5": {
                    "features": ["Destroy Undead (CR 1/2)"]
                }
            },
            "spellcasting": {
                "is_spellcaster": True
            }
        },
        {
            "index": "druid",
            "name": "Druid",
            "hit_dice": "1d8",
            "starting_hp": 8,
            "main_stat": "WIS",
            "proficiencies": {
                "armor": ["Light armor (non-metal)", "Medium armor (non-metal)", "Shields (non-metal)"],
                "weapons": ["Clubs", "Daggers", "Darts", "Javelins", "Maces", "Quarterstaffs", "Scimitars", "Sickles", "Slings", "Spears"],
                "tools": ["Herbalism kit"],
                "saving_throws": ["INT", "WIS"],
                "skills": {2: ["Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"]}
            },
            "class_features": [
                {
                    "name": "Druidic",
                    "description": "You know Druidic, the secret language of druids. You can speak the language and use it to leave hidden messages."
                },
                {
                    "name": "Spellcasting",
                    "description": "Drawing on the divine essence of nature itself, you can cast spells to shape that essence to your will."
                }
            ],
            "level_progression": {
                "1": {
                    "features": ["Druidic", "Spellcasting"]
                },
                "2": {
                    "features": ["Wild Shape", "Druid Circle"]
                },
                "3": {
                    "features": []
                },
                "4": {
                    "features": ["Wild Shape Improvement", "Ability Score Improvement"]
                },
                "5": {
                    "features": []
                }
            },
            "spellcasting": {
                "is_spellcaster": True
            }
        },
        {
            "index": "fighter",
            "name": "Fighter",
            "hit_dice": "1d10",
            "starting_hp": 10,
            "main_stat": "STR",
            "proficiencies": {
                "armor": ["All armor", "Shields"],
                "weapons": ["Simple weapons", "Martial weapons"],
                "tools": [],
                "saving_throws": ["STR", "CON"],
                "skills": {2: ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"]}
            },
            "class_features": [
                {
                    "name": "Fighting Style",
                    "description": "You adopt a particular style of fighting as your specialty."
                },
                {
                    "name": "Second Wind",
                    "description": "You have a limited well of stamina that you can draw on to protect yourself from harm."
                }
            ],
            "level_progression": {
                "1": {
                    "features": ["Fighting Style", "Second Wind"]
                },
                "2": {
                    "features": ["Action Surge (one use)"]
                },
                "3": {
                    "features": ["Martial Archetype"]
                },
                "4": {
                    "features": ["Ability Score Improvement"]
                },
                "5": {
                    "features": ["Extra Attack"]
                }
            },
            "spellcasting": {
                "is_spellcaster": False
            }
        },
        {
            "index": "monk",
            "name": "Monk",
            "hit_dice": "1d8",
            "starting_hp": 8,
            "main_stat": "DEX",
            "proficiencies": {
                "armor": [],
                "weapons": ["Simple weapons", "Shortswords"],
                "tools": ["Choose one type of artisan's tools or one musical instrument"],
                "saving_throws": ["STR", "DEX"],
                "skills": {2: ["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"]}
            },
            "class_features": [
                {
                    "name": "Unarmored Defense",
                    "description": "Beginning at 1st level, while you are wearing no armor and not wielding a shield, your AC equals 10 + your Dexterity modifier + your Wisdom modifier."
                },
                {
                    "name": "Martial Arts",
                    "description": "Your practice of martial arts gives you mastery of combat styles that use unarmed strikes and monk weapons."
                }
            ],
            "level_progression": {
                "1": {
                    "features": ["Unarmored Defense", "Martial Arts"]
                },
                "2": {
                    "features": ["Ki", "Unarmored Movement"]
                },
                "3": {
                    "features": ["Monastic Tradition", "Deflect Missiles"]
                },
                "4": {
                    "features": ["Ability Score Improvement", "Slow Fall"]
                },
                "5": {
                    "features": ["Extra Attack", "Stunning Strike"]
                }
            },
            "spellcasting": {
                "is_spellcaster": False
            }
        },
        {
            "index": "paladin",
            "name": "Paladin",
            "hit_dice": "1d10",
            "starting_hp": 10,
            "main_stat": "STR",
            "proficiencies": {
                "armor": ["All armor", "Shields"],
                "weapons": ["Simple weapons", "Martial weapons"],
                "tools": [],
                "saving_throws": ["WIS", "CHA"],
                "skills": {2: ["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"]}
            },
            "class_features": [
                {
                    "name": "Divine Sense",
                    "description": "The presence of strong evil registers on your senses like a noxious odor, and powerful good rings like heavenly music in your ears."
                },
                {
                    "name": "Lay on Hands",
                    "description": "Your blessed touch can heal wounds."
                }
            ],
            "level_progression": {
                "1": {
                    "features": ["Divine Sense", "Lay on Hands"]
                },
                "2": {
                    "features": ["Fighting Style", "Divine Smite", "Spellcasting"]
                },
                "3": {
                    "features": ["Divine Health", "Sacred Oath"]
                },
                "4": {
                    "features": ["Ability Score Improvement"]
                },
                "5": {
                    "features": ["Extra Attack"]
                }
            },
            "spellcasting": {
                "is_spellcaster": True
            }
        },
        {
            "index": "ranger",
            "name": "Ranger",
            "hit_dice": "1d10",
            "starting_hp": 10,
            "main_stat": "DEX",
            "proficiencies": {
                "armor": ["Light armor", "Medium armor", "Shields"],
                "weapons": ["Simple weapons", "Martial weapons"],
                "tools": [],
                "saving_throws": ["STR", "DEX"],
                "skills": {3: ["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"]}
            },
            "class_features": [
                {
                    "name": "Favored Enemy",
                    "description": "You have significant experience studying, tracking, hunting, and even talking to a certain type of enemy."
                },
                {
                    "name": "Natural Explorer",
                    "description": "You are particularly familiar with one type of natural environment and are adept at traveling and surviving in such regions."
                }
            ],
            "level_progression": {
                "1": {
                    "features": ["Favored Enemy", "Natural Explorer"]
                },
                "2": {
                    "features": ["Fighting Style", "Spellcasting"]
                },
                "3": {
                    "features": ["Ranger Archetype", "Primeval Awareness"]
                },
                "4": {
                    "features": ["Ability Score Improvement"]
                },
                "5": {
                    "features": ["Extra Attack"]
                }
            },
            "spellcasting": {
                "is_spellcaster": True
            }
        },
        {
            "index": "rogue",
            "name": "Rogue",
            "hit_dice": "1d8",
            "starting_hp": 8,
            "main_stat": "DEX",
            "proficiencies": {
                "armor": ["Light armor"],
                "weapons": ["Simple weapons", "Hand crossbows", "Longswords", "Rapiers", "Shortswords"],
                "tools": ["Thieves' tools"],
                "saving_throws": ["DEX", "INT"],
                "skills": {4: ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"]}
            },
            "class_features": [
                {
                    "name": "Expertise",
                    "description": "Choose two of your skill proficiencies, or one of your skill proficiencies and your proficiency with thieves' tools. Your proficiency bonus is doubled for any ability check you make that uses either of the chosen proficiencies."
                },
                {
                    "name": "Sneak Attack",
                    "description": "Once per turn, you can deal an extra 1d6 damage to one creature you hit with an attack if you have advantage on the attack roll."
                }
            ],
            "level_progression": {
                "1": {
                    "features": ["Expertise", "Sneak Attack", "Thieves' Cant"]
                },
                "2": {
                    "features": ["Cunning Action"]
                },
                "3": {
                    "features": ["Roguish Archetype"]
                },
                "4": {
                    "features": ["Ability Score Improvement"]
                },
                "5": {
                    "features": ["Uncanny Dodge"]
                }
            },
            "spellcasting": {
                "is_spellcaster": False
            }
        },
        {
            "index": "sorcerer",
            "name": "Sorcerer",
            "hit_dice": "1d6",
            "starting_hp": 6,
            "main_stat": "CHA",
            "proficiencies": {
                "armor": [],
                "weapons": ["Daggers", "Darts", "Slings", "Quarterstaffs", "Light crossbows"],
                "tools": [],
                "saving_throws": ["CON", "CHA"],
                "skills": {2: ["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"]}
            },
            "class_features": [
                {
                    "name": "Spellcasting",
                    "description": "You draw on your inherent magic to cast spells."
                },
                {
                    "name": "Sorcerous Origin",
                    "description": "Choose a sorcerous origin, which describes the source of your innate magical power."
                }
            ],
            "level_progression": {
                "1": {
                    "features": ["Spellcasting", "Sorcerous Origin"]
                },
                "2": {
                    "features": ["Font of Magic"]
                },
                "3": {
                    "features": ["Metamagic"]
                },
                "4": {
                    "features": ["Ability Score Improvement"]
                },
                "5": {
                    "features": []
                }
            },
            "spellcasting": {
                "is_spellcaster": True
            }
        },
        {
            "index": "warlock",
            "name": "Warlock",
            "hit_dice": "1d8",
            "starting_hp": 8,
            "main_stat": "CHA",
            "proficiencies": {
                "armor": ["Light armor"],
                "weapons": ["Simple weapons"],
                "tools": [],
                "saving_throws": ["WIS", "CHA"],
                "skills": {2: ["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"]}
            },
            "class_features": [
                {
                    "name": "Spellcasting",
                    "description": "Your arcane research and the magic bestowed on you by your patron have given you facility with spells."
                },
                {
                    "name": "Eldritch Invocations",
                    "description": "In your study of occult lore, you have unearthed eldritch invocations, fragments of forbidden knowledge that imbue you with an abiding magical ability."
                }
            ],
            "level_progression": {
                "1": {
                    "features": ["Spellcasting", "Pact Magic", "Eldritch Invocations"]
                },
                "2": {
                    "features": ["Eldritch Invocations"]
                },
                "3": {
                    "features": ["Pact Boon"]
                },
                "4": {
                    "features": ["Ability Score Improvement"]
                },
                "5": {
                    "features": []
                }
            },
            "spellcasting": {
                "is_spellcaster": True
            }
        },
        {
            "index": "wizard",
            "name": "Wizard",
            "hit_dice": "1d6",
            "starting_hp": 6,
            "main_stat": "INT",
            "proficiencies": {
                "armor": [],
                "weapons": ["Daggers", "Darts", "Slings", "Quarterstaffs", "Light crossbows"],
                "tools": [],
                "saving_throws": ["INT", "WIS"],
                "skills": {2: ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"]}
            },
            "class_features": [
                {
                    "name": "Spellcasting",
                    "description": "You have a spellbook containing spells that show the first glimmerings of your true power."
                },
                {
                    "name": "Arcane Recovery",
                    "description": "You have learned to regain some of your magical energy by studying your spellbook."
                }
            ],
            "level_progression": {
                "1": {
                    "features": ["Spellcasting", "Arcane Recovery"]
                },
                "2": {
                    "features": ["Arcane Tradition"]
                },
                "3": {
                    "features": []
                },
                "4": {
                    "features": ["Ability Score Improvement"]
                },
                "5": {
                    "features": []
                }
            },
            "spellcasting": {
                "is_spellcaster": True
            }
        },
    ]   
}