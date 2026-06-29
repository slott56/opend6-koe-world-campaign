"""
Generic People from OpenD6 Fantasy Rulebook.
Used to populate "Adventure Tips" chapter.
"""
from textwrap import dedent
from opend6_tools.character import *

healer = Character(
    occupation="Healer",
    race="Human",
    agility=Agility(2*D),
    coordination=Coordination(
        2 * D,
      {"sleight of hand": 2*D+1}),
    physique=Physique(
        2 * D, {"stamina": 2*D+1}),
    intellect=Intellect(
        3 * D,
        {
            "healing": 4*D,
            "reading/writing": 2*D+1,
            "scholar": 2*D+2,
        },
    ),
    acumen=Acumen(
        3 * D + 1,
        {
            "investigation": 2*D+1,
        },
    ),
    charisma=Charisma(2 * D),
    move=10,
    fate_points=0,
    character_points=2,
    body=10,
    equipment="large healer's kit (+1 bonus to 6 to 12 healing attempts)",
)

henchman = Character(
    occupation="Henchman",
    race="Human",
    agility=Agility(
        2*D,
        {"fighting": 4*D, "melee combat": 3*D, "stealth": 3*D}),
    coordination=Coordination(
        2 * D,
      {"lockpicking": 3*D, "marksmanship": 4*D}),
    physique=Physique(
        3 * D, {"running": 3*D+2}),
    intellect=Intellect(
        2 * D,
    ),
    acumen=Acumen(
        2 * D,
        {"hide": 3*D, "streetwise": 3*D, "tracking": 3*D},
    ),
    charisma=Charisma(2 * D),
    move=10,
    fate_points=0,
    character_points=2,
    body=13,
    weapons=["dagger (damage +1D)"],
    armor=["soft leather armor (Armor Value +2)"],
    equipment=["lockpicking tools (+1D to lockpicking rolls)"],
)

merchant = Character(
    occupation="Merchant",
    race="Human",
    agility=Agility(
        2*D,
        {"riding": 2*D+1}),
    coordination=Coordination(
        2 * D,
      {"sleight of hand": 2*D+2}),
    physique=Physique(
        2 * D, {"running": 2*D+1}),
    intellect=Intellect(
        2 * D, {"cultures": 3*D, "reading/writing": 2*D+2, "scholar": 3*D, "speaking": 3*D, "trading": 3*D}
    ),
    acumen=Acumen(
        2 * D,
        {"streetwise": 2*D+1,},
    ),
    charisma=Charisma(3 * D, {"bluff": 3*D+2, "charm": 4*D, "persuasion": 3*D}),
    move=10,
    fate_points=0,
    character_points=2,
    body=11,
    weapons=["small knife (damage +2)"],
    armor=["heavy garments (Armor Value +1)"],
    equipment=[
        "coins of various realms",
        "trinkets or wares to sell",
        "pouches",
    ],
)

ranger = Character(
    occupation="Ranger",
    race="Human",
    agility=Agility(
        3 * D,
        {"dodge": 3*D+1, "fighting": 3*D+1, "melee combat": 3*D+1, "stealth": 3*D+2}
    ),
    coordination=Coordination(
        2 * D),
    physique=Physique(
        2 * D, {"running": 3 * D + 1, "lifting": 3*D+2}),
    intellect=Intellect(
        2 * D),
    acumen=Acumen(
        2 * D,
        {"hide": 2*D+2, "investigation": 2*D+1, "search": 2*D+1, "survival": 2*D+2, "tracking": 2*D+2}
    ),
    charisma=Charisma(2 * D, {"intimidation": 2 * D + 1, "mettle": 2 * D + 2,}
    ),
    move=10,
    fate_points=0,
    character_points=2,
    body=14,
    weapons=["short sword (damage +1D+2)", "knife (damage +1D)"],
    armor=["soft leather armor (Armor Value+2)"],
    equipment="mottled green-grey cloak (+1 to hide attempts among trees)",
)

ruffian = Character(
    occupation="Ruffian",
    race="Human",
    agility=Agility(
        2 * D,
        {"fighting": 3 * D, "melee combat": 3 * D ,
         "stealth": 2 * D + 1}
    ),
    coordination=Coordination(
        2 * D, {"lockpicking": 3*D}),
    physique=Physique(
        3 * D),
    intellect=Intellect(
        2 * D, {"traps": 3*D}),
    acumen=Acumen(
        2 * D,
        {"gambling": 2*D+2, "hide": 2 * D + 2, "streetwise": 3 * D}
    ),
    charisma=Charisma(1 * D, {"intimidation": 3*D}),
    move=10,
    fate_points=0,
    character_points=2,
    body=12,
    weapons=["dagger (damage +1D)"],
    equipment="burlap bag",
)

soldier = Character(
    occupation = "Soldier",
    race = "Human",
    agility = Agility(
        2 * D,
        {"dodge": 3 * D, "fighting": 3 * D, "melee combat": 3 * D}
    ),
    coordination = Coordination(
        2 * D),
    physique = Physique(
        3 * D, {"lifting": 3*D+1, "running": 3 * D + 1}),
    intellect = Intellect(
        2 * D),
    acumen = Acumen(
        2 * D,
        {"search": 2 * D + 1, "streetwise": 2*D+1,
         "survival": 2 * D + 2}
    ),
    charisma = Charisma(2 * D, {"intimidation": 2 * D + 2, "mettle": 2 * D + 1, }
                        ),
    move = 10,
    fate_points = 0,
    character_points = 2,
    body = 15,
    weapons=["short sword (damage +1D+2)", "knife (damage +1D)"],
    armor=["padded leather armor (Armor Value +1D)", "helmet"],
)

all_characters = {
    'Healer': healer,
    'Henchman': henchman,
    'Merchant': merchant,
    'Ranger': ranger,
    'Ruffian': ruffian,
    'Soldier': soldier,
}

if __name__ == "__main__":
    app = build_app(all_characters)
    app()

__test__ = {
    "pass": ">>> pass\n"
}
