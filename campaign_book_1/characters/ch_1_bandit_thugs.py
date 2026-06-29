"""
Extract Characters from ``ch_1_bandit_thugs.ipynb``.
Created by V2026.6.15.dev3 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



thug = Character(
    name='Hired Thug Leader',
    physique=Physique(3*D, {'stamina': 1*D}),
    agility=Agility(3*D, {'fighting': 1*D, 'melee combat': 2}),
    coordination=Coordination(3*D),
    intellect=Intellect(3*D, {'healing': 2}),
    acumen=Acumen(3*D, {'hide': 1*D, 'streetwise': 2, 'tracking': 1*D}),
    charisma=Charisma(3*D, {'intimidation': 2*D+2}),
    body=20,
    move=10,
    fate_points=0,
    disadvantages=[
        Devotion(2, "Cult of the Jackal"),
        Employed(2, "Cult of the Jackal"),
        Quirk(2, "Exercise Nut"),
    ],
    weapons=[
        "Short bow 1D+2 10/100/250 (6 arrows)",
        "hatchet 1D+1"
        ],
    armor=[
        "padded leather armor +1D",
    ]
)

man_at_arms = Character(
    name='Bandit Army -- Guard, Thug, etc.',
    physique=Physique(3*D,),
    agility=Agility(3*D, {'fighting': 1*D, 'melee combat': 2}),
    coordination=Coordination(3*D),
    intellect=Intellect(3*D),
    acumen=Acumen(3*D),
    charisma=Charisma(2*D),
    body=24,
    move=10,
    fate_points=0,
    special_abilities=[
        NaturalHandWeapon(3, "Brutal punch")
    ],
    disadvantages=[
        Devotion(3, "Cult of Jackal"),
        Employed(3, "Jackal Temple"),
        Quirk(2, "Hopes to becomes an agent"),
    ],
    weapons=["Short bow 1D+2 10/100/250 (6 arrows)",
        "hatchet 1D+1"],
    armor=[
        "padded leather armor +1D",
    ]
)
characters = [ 
    thug, man_at_arms, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

