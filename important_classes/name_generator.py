import random

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

# Incase I want to do a large generation later and add it to a dict, not sure
# if that would be a good or bad idea, might make it easier than running this everytime?
def generate_names(first_elements, last_elements, num_names):
    names = []
    for _ in range(num_names):
        first_name = generate_name(first_elements)
        last_name = generate_name(last_elements)
        names.append(f"{first_name} {last_name}")
    return names
