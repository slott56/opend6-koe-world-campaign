"""
Extract Characters from ``xorn.ipynb``.
Created by V2026.6.15.dev3 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



character = Character(
    name='Xorn',
    other_notes="Quote: 'All must placate the Jackal'",
    objectives="Summon minions first, summon demons second",
    description="Black robes with Jackal glyph",
    physique=Physique(3*D+2, {'stamina': 2}),
    agility=Agility(4*D, {'fighting': 1*D+1, 'riding': 2*D, 'melee combat': 1*D}),
    coordination=Coordination(4*D, {}),
    intellect=Intellect(4*D, {'cultures': 1*D, 'reading/writing': 1*D, 'scholar': 1*D, 'speaking': 2*D}),
    acumen=Acumen(4*D, {'disguise': 1*D, 'hide': 2*D}),
    charisma=Charisma(3*D+2, {'intimidation': 4*D+2}),
    extranormal=Magic(4*D),
    body=20,
    move=10,
    advantages=[
        Authority(R3, "Head of a cult"),
        Wealth(R3),
    ],
    disadvantages=[
        Infamy(R1, "Reputation, Cruelty, known human sacrificer"),
        Prejudice(R1, "Ignorant: Common Situation, Strong Intensity, Lies about the Jackal cult constantly can't admit he's deeply into demonology.  Doesn't understand how the demons manipulate him."),
        Hindrance(R2, "Incense addict: Must have incense burning at all times"),
        Quirk(R2, "Afraid of wands"),
        Enemy(R3, "Watched by demons who manipulate his dreams"),
        Quirk(R2, "Paranoia: People are out to get him.  Mostly by concealing wands in unlikely places.  Often, his prisoners must be dismembered to check for hidden wands."),
    ],
    special_abilities=[
        CombatSense(R2),
    ],
    weapons=["A long-handled flail, carefully painted (2D+2)"],
    spells=[
        "Demon Fire 8 2D fire damage (ignore all armor)",
        "Demon Shield 14 2D protection behind wall of fire",
        "Demonic Cleansing 14 4D Boost Charisma/intimidation",
        "Demon Detection 20 R3 Enhanced Sense",
        "Demon Wings 18 R2 Flight",
        "Opening the Veil 29 R4 Apporation to new realm",
    ],
)
characters = [ 
    character, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

