"""
Extract Characters from ``jackal_internal.ipynb``.
Created by V2026.5.7.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



torturer = Character(
    name='Jackal Intelligence -- Torturer',
    physique=Physique(4*D),
    agility=Agility(4*D, {'fighting': 1}),
    coordination=Coordination(4*D,),
    intellect=Intellect(4*D, {'devices': 1*D}),
    acumen=Acumen(3*D+2, {'artist': 1*D, 'investigation': 1*D, 'know-how': 1*D}),
    charisma=Charisma(3*D+2, {'intimidation': 5*D+1}),
    body=24,
    move=10,
    special_abilities=[
        NaturalHandWeapon(2, "Brutal punch")
    ],
    disadvantages=[
        Devotion(3, "Cult of Jackal"),
        Employed(3, "Jackal Temple"),
        Quirk(3, "Brutally cruel"),
    ]
)

scrying = Character(
    name='Jackal Intelligence -- Scrying',
    physique=Physique(4*D, {'stamina': 4*D}),
    agility=Agility(4*D, {'fighting': 1*D}),
    coordination=Coordination(4*D),
    intellect=Intellect(4*D, {'navigation': 1*D, 'speaking': 1*D, 'trading': 1*D, 'traps': 1*D}),
    acumen=Acumen(3*D+2, {'disguise': 1*D, 'hide': 1*D, 'investigation': 1*D, 'search': 1*D, 'streetwise': 1*D}),
    charisma=Charisma(3*D+2, {'intimidation': 5*D+1}),
    extranormal=Magic(3*D, {'divination': 2*D}),
    body=24,
    move=10,
    special_abilities=[
    ],
    disadvantages=[
        Devotion(3, "Cult of Jackal"),
        Employed(3, "Jackal Temple"),
        Quirk(3, "Insufferable if insulted"),
    ]
)

guard = Character(
    name='Jackal Intelligence -- Guard',
    physique=Physique(4*D, {'stamina': 1}),
    agility=Agility(4*D, {'fighting': 0*D+2, 'melee combat': 2}),
    coordination=Coordination(4*D, {'charioteering': 0*D, 'lockpicking': 0*D, 'marksmanship': 0*D, 'pilotry': 0*D, 'sleight of hand': 0*D, 'throwing': 0*D}),
    intellect=Intellect(3*D+2, {'cultures': 0*D, 'devices': 0*D, 'healing': 0*D, 'navigation': 0*D, 'reading/writing': 0*D, 'scholar': 0*D, 'speaking': 0*D, 'trading': 0*D, 'traps': 0*D}),
    acumen=Acumen(3*D+2, {'artist': 0*D, 'crafting': 0*D, 'disguise': 0*D, 'gambling': 0*D, 'hide': 0*D, 'investigation': 0*D, 'know-how': 0*D, 'search': 0*D, 'streetwise': 0*D, 'survival': 0*D, 'tracking': 0*D}),
    charisma=Charisma(3*D+2, {'intimidation': 4*D}),
    body=22,
    move=10,
)
characters = [ 
    torturer, scrying, guard, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

