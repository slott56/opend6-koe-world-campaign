"""
Extract Characters from ``ch_2_bandit_thugs.ipynb``.
Created by V2026.5.7.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



bartender = Character(
    name="Fox's tail Bartender",
    physique=Physique(3*D+2),
    agility=Agility(2*D, {'fighting': 1}),
    coordination=Coordination(3*D+2, {'sleight of hand': 1, 'throwing': 2}),
    intellect=Intellect(3*D),
    acumen=Acumen(3*D+2, {'investigation': 1,'streetwise': 2}),
    charisma=Charisma(3*D+2, {'intimidation': 3*D+1}),
    body=20,
    move=10,
    special_abilities=[
        CombatSense(1, "very aware of surroundings")
    ],
    disadvantages=[
        Quirk(2, "Greedy"),
        Quirk(2, "Terrified of Steward"),
        Disadvantage(2, "Only one leg"),
    ]
)

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
    ]
)
characters = [ 
    bartender, thug, man_at_arms, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

