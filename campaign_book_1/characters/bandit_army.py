"""
Extract Characters from ``bandit_army.ipynb``.
Created by V2026.5.7.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



general = Character(
    name='Bandit Army General (Knight)',
    description="First Officer in Xorn's Bandit Army.  Ambitious, professional soldier.  Health and fitness buff: goes running and stretching and stuff.",
    other_notes="""Quote: "I've never let this stop me before." """,
    physique=Physique(4*D, {'stamina': 1*D}),
    agility=Agility(4*D, {'fighting': 1*D, "riding": 1*D, "melee combat": 1*D}),
    coordination=Coordination(4*D),
    intellect=Intellect(3*D+2, {'speaking': 1*D, 'healing': 1*D}),
    acumen=Acumen(3*D+2, {'survival': 1*D, 'tracking': 1*D, 'investigation': 1*D, 'gambling': 1*D}),
    charisma=Charisma(3*D+2, {'intimidation': 4*D+2}),
    body=26,
    move=10.0,
    disadvantages=[
        Devotion(2, "Cult of the Jackal"),
        Employed(2, "Cult of the Jackal"),
        Quirk(2, "Exercie Nut"),
    ]
)

colonel = Character(
    name='Bandit Army Colonel (Squire)',
    description="Wild-man from the hills, tamed and leading other crazies in Xorn's army.  Chews tobacco, spits, scratches and acts like a country bumpkin.",
    other_notes="Quote: 'Well, hells bells!'",
    physique=Physique(4*D, {'stamina': 1*D+1}),
    agility=Agility(4*D, {'fighting': 1*D, "melee combat": 2}),
    coordination=Coordination(4*D),
    intellect=Intellect(3*D+2),
    acumen=Acumen(3*D+2, {'gambling': 1*D, 'hide': 1*D, 'survival': 1*D, 'tracking': 1*D}),
    charisma=Charisma(3*D+2, {'intimidation': 4*D+2}),
    body=28,
    move=10,
    disadvantages=[
        Devotion(2, "Cult of the Jackal"),
        Employed(2, "Cult of the Jackal"),
        Hindrance(3, "Thinks he's invincible"),
        Quirk(2, "Ruthless political climber"),
    ]
)

high_mage = Character(
    name='Bandit Army High Mage',
    description='Magician with a craving for large-unit combat.',
    other_notes="Quote: 'This will teach you humility'",
    physique=Physique(4*D, {'stamina': 1*D+1}),
    agility=Agility(4*D, {'fighting': 0*D+2, 'melee combat': 0*D+2}),
    coordination=Coordination(4*D),
    intellect=Intellect(3*D+2, {'reading/writing': 1*D}),
    acumen=Acumen(3*D+2, {'gambling': 1*D, 'know-how': 1*D,}),
    charisma=Charisma(3*D+2, {'intimidation': 4*D+2}),
    extranormal=Magic(3*D),
    body=20,
    move=10.0,
    disadvantages=[
        Devotion(2, "Cult of the Jackal"),
        Employed(2, "Cult of the Jackal"),
        Quirk(2, "Loves the idea of a fight, not the fighting"),
    ]
)

mage = Character(
    name='Bandit Army Mage',
    description='',
    physique=Physique(3*D+2),
    agility=Agility(4*D, {'fighting': 0*D+2}),
    coordination=Coordination(4*D, {'charioteering': 0*D, 'lockpicking': 0*D, 'marksmanship': 0*D, 'pilotry': 0*D, 'sleight of hand': 0*D, 'throwing': 0*D}),
    intellect=Intellect(3*D+2, {'cultures': 0*D, 'devices': 0*D, 'healing': 0*D, 'navigation': 0*D, 'reading/writing': 0*D, 'scholar': 0*D, 'speaking': 0*D, 'trading': 0*D, 'traps': 0*D}),
    acumen=Acumen(3*D+2, {'artist': 0*D, 'crafting': 0*D, 'disguise': 0*D, 'gambling': 0*D, 'hide': 0*D, 'investigation': 0*D, 'know-how': 0*D, 'search': 0*D, 'streetwise': 0*D, 'survival': 0*D, 'tracking': 0*D}),
    charisma=Charisma(3*D+2, {'intimidation': 4*D}),
    extranormal=Magic(2*D),
    body=20,
    move=10.0,
    disadvantages=[
        Devotion(2, "Cult of the Jackal"),
        Employed(2, "Cult of the Jackal"),
        Quirk(2, "Back-stabbing little shitweasel"),
    ]
)

man_at_arms = Character(
    name='Bandit Army -- Guard, Thug, etc.',
    physique=Physique(3*D,),
    agility=Agility(4*D, {'fighting': 2, 'melee combat': 2}),
    coordination=Coordination(3*D),
    intellect=Intellect(3*D),
    acumen=Acumen(3*D),
    charisma=Charisma(2*D),
    body=24,
    move=10.0,
    special_abilities=[
        NaturalHandWeapon(1*D, "Brutal punch")
    ],
    disadvantages=[
        Devotion(3, "Cult of Jackal"),
        Employed(3, "Jackal Temple"),
        Quirk(2, "Hopes to becomes an agent"),
    ]
)
characters = [ 
    general, colonel, high_mage, mage, man_at_arms, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

