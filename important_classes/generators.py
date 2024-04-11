import random

### NPC NAME GENERATOR ###
first_name_elements = {
    "prefixes": ["Aer", "Al", "Am", "Ar", "Bel", "Bran", "Cael", "Cor", "Dae", "El", "Faer", "Gaer", "Haer", "Ia", "Ja", "Kae", "La", "Mae", "Na", "Oa", "Pa", "Quae", "Rae", "Sae", "Tae", "Ua", "Va", "Wae", "Xae", "Yae", "Zae", "Ly", "Mer", "Niv", "Ori", "Per", "Quin", "Ri", "So", "Tha", "Ul", "Ve", "Wil", "Xy", "Yo", "Zo", "Evan", "Fio", "Gwen", "Hal", "Is", "Jo", "Kas", "Lor", "Mir", "Nys", "Ol", "Pax", "Quor", "Riv", "Ser", "Tyr", "Uri", "Val", "Wyn", "Xan", "Ys", "Zan"],
    "suffixes": ["is", "el", "an", "in", "as", "os", "us", "ent", "ard", "or", "ric", "elis", "ira", "ara", "ana", "yn", "ith", "ath", "ael", "iel", "wen", "ess", "ine", "lyn", "ith", "old", "yst", "ard", "eon", "ior", "ain", "en", "on", "van", "il", "al", "er"]
}

last_name_elements = {
    "prefixes": ["Amber", "Bright", "Cinder", "Dawn", "Ever", "Frost", "Gloom", "Hawk", "Iron", "Jade", "King", "Light", "Moon", "Night", "Oak", "Pine", "Quick", "Raven", "Storm", "Thorn", "Under", "Vale", "Whisper", "Xan", "Yellow", "Zephyr", "Ash", "Briar", "Cold", "Dark", "Ember", "Falcon", "Grim", "High", "Ice", "Jewel", "Kestrel", "Lion", "Mist", "Noble", "Oaken", "Pure", "Quartz", "Rune", "Silver", "Thunder", "Umber", "Venture", "Willow", "Xylo", "Yew", "Zenith", "Aether", "Blaze", "Crest", "Dusk", "Elder", "Flame", "Giant", "Hallow", "Ivory", "Kraken", "Leaf", "Marble", "Nether", "Orchid", "Primal", "Quarry", "River", "Stone", "Timber", "Unity", "Vex", "Wolf", "Xenon"],
    "suffixes": ["fall", "wood", "forge", "whisper", "mead", "beard", "river", "light", "heart", "wind", "shield", "walker", "shadow", "runner", "grove", "silver", "lock", "breaker", "root", "bough", "watch", "storm", "brook", "vale", "blade", "crest", "ward", "peak", "gale", "frost", "veil", "bane", "end", "might", "fist", "heart", "fire", "song", "glow", "stone", "wing", "bloom", "shade", "mist", "veil", "gale", "forge", "soul"]
}

def generate_name(elements):
    return random.choice(elements["prefixes"]) + random.choice(elements["suffixes"])

def generate_full_name(first_name_elements, last_name_elements):
    first_name = random.choice(first_name_elements["prefixes"]) + random.choice(first_name_elements["suffixes"])
    last_name = random.choice(last_name_elements["prefixes"]) + random.choice(last_name_elements["suffixes"])
    name = f"{first_name} {last_name}"
    return name

def generate_names(first_elements, last_elements, num_names):
    names = []
    for _ in range(num_names):
        first_name = generate_name(first_elements)
        last_name = generate_name(last_elements)
        names.append(f"{first_name} {last_name}")
    return names

### TAVERN NAME GENERATOR ###
TAVERN_NAME_ELEMENTS = {
    "first": [
        "Silent", "Wandering", "Sapphire", "Ruby", "Parched", "Howling", "Mystic",
        "Golden", "Whispering", "Frozen", "Crimson", "Silver", "Lonely", "Twilight",
        "Hidden", "Glimmering", "Rusty", "Last", "Fabled", "Ancient", "Drunken",
        "Sleeping", "Laughing", "Singing", "Forgotten", "Dancing", "Prancing", "Roaring",
        "Bellowing", "Smokey", "Stormy", "Cursed", "Blessed", "Eternal", "Hallowed",
        "Tarnished", "Verdant", "Obsidian", "Luminous", "Whimsical", "Desolate", "Opulent",
        "Murky", "Dusky", "Emerald", "Celestial", "Venerable", "Arid", "Gusty", "Perilous",
        "Lush", "Meandering", "Vigilant", "Tempestuous", "Zephyrous", "Starry", "Wintry",
        "Autumnal", "Serendipitous", "Vagrant", "Spectral", "Divine", "Shadowy", "Fleeting",
        "Cobalt", "Ivory", "Aqua", "Carmine", "Vivid", "Pale"
    ],
    "second": [
        "Sentinel", "Wizard", "Lagoon", "Pirate", "Hyena", "Rose", "Wyvern", "Goblet",
        "Dragon", "Owl", "Fox", "Dagger", "Sword", "Castle", "Anchor", "Skull",
        "Ship", "Wolf", "Shield", "Ghost", "Hound", "Harbor", "Star", "Moon", "King",
        "Throne", "Bear", "Eagle", "Chalice", "Jewel", "Crown", "Griffin", "Stag", "Falcon", "Raven",
        "Grove", "Meadow", "Cliff", "Stream", "Forge", "Mill", "Tower", "Portal", "Gem",
        "Orchard", "Cauldron", "Grotto", "Pike", "Lantern", "Torch", "Spire", "Ridge",
        "Valley", "Crossroad", "Cavern", "Chapel", "Shrine", "Peak", "Brook", "Hearth",
        "Glade", "Pond", "Quarry", "Spring", "Vale", "Kettle", "Mire", "Fen", "Dell", "Glen"
    ],
    "prefixes": [
        "The", "Ye Olde", "Last", "First", "Merry", "Drunken", "Quiet", "Rusty",
        "Hidden", "Lost", "Old", "Weeping", "Laughing", "Whistling", "Crooked", "Wicked",
        "Lonely", "Jolly", "Brave", "Haunted", "Wise", "Great", "Green", "Blue", "Golden",
        "Silver", "Ivory", "Black", "White", "Grey", "Red", "Mystic"
    ],
    "formats": [
        "{prefix} {first} {second}",
        "{first} {second} Tavern",
        "{first} {second} Inn",
        "{first} {second} Pub",
        "{first} {second} House",
        "{first} {second} Alehouse",
        "{first} {second} Lodge",
        "{first} {second} Saloon",
        "{first} {second} Bar",
        "{first} {second} Refuge",
        "{first} {second} Retreat",
        "{first} {second} Den"
    ]
}

def generate_building_name(elements):
    format_choice = random.choice(elements["formats"])
    name = format_choice.format(
        prefix=random.choice(elements["prefixes"]),
        first=random.choice(elements["first"]),
        second=random.choice(elements["second"])
    )
    return name