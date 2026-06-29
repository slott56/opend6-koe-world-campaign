"""
Extract Characters from ``ch_5_jackal_doubleagent.ipynb``.
Created by V2026.6.6.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



double_agent_bargeman = Character(
    name='Bargeman',
    description='Double Agent in White Water',
    physique=Physique(4*D, {'stamina': 2}),
    agility=Agility(3*D+2, {'fighting': 1*D, 'melee combat': 2}),
    coordination=Coordination(3*D+2, {'seamanship': 1*D}),
    intellect=Intellect(3*D+2, {'cultures': 1, 'navigation': 1, 'reading/writing': 1, 'scholar': 1, 'speaking': 2}),
    acumen=Acumen(3*D+2, {'gambling': 1, 'hide': 1, 'know-how': 1, 'streetwise': 2}),
    charisma=Charisma(3*D+2, {'persuation': 1*D, 'charm': 1*D}),
    body=20,
    move=10,
    special_abilities=[
        SenseOfDirection(2, "doesn't get lost"),
    ],
    advantages=[
        Contacts(2, "Candler and Jackal Temple as well as Squire Neck"),
    ],
    disadvantages=[
        Quirk(2, "Loud"),
        Quirk(1, "Secret identity as double agent"),
        Enemy(2, "Squire Neck"),
        Enemy(1, "Candler"),
    ]
)
characters = [ 
    double_agent_bargeman, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

