"""
Extract Characters from ``ch_3_bandit_thugs.ipynb``.
Created by V2026.5.7.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



stable_boss = Character(
    name='Boss at Oaks Stable',
    physique=Physique(3*D+2,),
    agility=Agility(3*D+2, {'melee combat': 0*D+2}),
    coordination=Coordination(3*D+2, {'sleight of hand': 2}),
    intellect=Intellect(3*D+2, {'speaking': 2, 'traps': 2}),
    acumen=Acumen(3*D+2, {'hide': 2, 'streetwise': 2}),
    charisma=Charisma(3*D+2, {'persuasion': 3*D+1}),
    body=20,
    move=10,
    disadvantages=[
        Enemy(1, "Secretly working for Jackal Temple"),
        Employed(1, "by Jackal Temple"),
        Quirk(2, "Rabid follower of the Jackal")
    ],
)

stable_hands = Character(
    name='Stable Hands at The Oaks',
    physique=Physique(3*D+2),
    agility=Agility(4*D, {'melee combat': 1*D}),
    coordination=Coordination(4*D, {'sleight of hand': 1}),
    intellect=Intellect(3*D+2),
    acumen=Acumen(3*D+2, {'hide': 1, 'streetwise': 1}),
    charisma=Charisma(3*D, {'intimidation': 3*D+1}),
    body=24,
    move=10,
)
characters = [ 
    stable_boss, stable_hands, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

