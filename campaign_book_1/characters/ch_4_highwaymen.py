"""
Extract Characters from ``ch_4_highwaymen.ipynb``.
Created by V2026.5.7.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



highwaymen = Character(
    name='Bandit Army Highwaymen',
    physique=Physique(3*D+2),
    agility=Agility(3*D+1, {'fighting': 2, 'melee combat': 2}),
    coordination=Coordination(3*D, {'marksmanship': 1}),
    intellect=Intellect(3*D, {'traps': 1}),
    acumen=Acumen(3*D, {'survival': 1, 'tracking': 1}),
    charisma=Charisma(2*D),
    body=22,
    move=10,
    disadvantages=[
        Infamy(2, "Known outlaws"),
        Quirk(2, "greedy"),
    ]
)
characters = [ 
    highwaymen, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

