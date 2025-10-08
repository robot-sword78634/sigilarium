import random

# Lovecraftian-style syllables
syllables_start = [
    "Az", "Yog", "Cth", "Shub", "Ny", "Thul", "Dho", "Rly", "Itha", "Hast", "Zan", "Gha", "Xal", "Kla"
]

syllables_middle = [
    "th", "og", "ul", "ar", "ee", "aa", "oo", "ix", "en", "ath", "esh", "ok", "um", "i"
]

syllables_end = [
    "hu", "oth", "ai", "on", "ka", "is", "oth", "az", "eth", "ax", "u", "il", "ag", "ek"
]

def generate_lovecraftian_name():
    # Decide on number of syllables (2-4)
    syllable_count = random.randint(2, 4)

    name = ""
    for i in range(syllable_count):
        if i == 0:
            name += random.choice(syllables_start)
        elif i == syllable_count - 1:
            name += random.choice(syllables_end)
        else:
            name += random.choice(syllables_middle)

    # Optionally add apostrophes for extra eldritch effect
    if random.random() < 0.5:
        pos = random.randint(1, len(name)-2)
        name = name[:pos] + "'" + name[pos:]

    return name

# Generate multiple names
for _ in range(10):
    print(generate_lovecraftian_name())

