"""
Extract Characters from ``ch_3_grifters.ipynb``.
Created by V2026.5.7.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



grifter = Character(
    name='Grifters',
    physique=Physique(3*D, ),
    agility=Agility(3*D, {'fighting': 1*D}),
    coordination=Coordination(3*D, {'sleight of hand': 1*D, 'throwing': 1*D}),
    intellect=Intellect(3*D, {'cultures': 1*D, 'speaking': 1*D}),
    acumen=Acumen(3*D+2, {'disguise': 1*D, 'gambling': 1*D, 'streetwise': 1*D}),
    charisma=Charisma(3*D+1, {'bluff': 1*D, 'charm': 1*D, 'persuasion': 1*D}),
    body=20,
    move=10,
    disadvantages=[
        Infamy(2, "known criminal"),
        Quirk(1, "greedy"),
    ]
)
characters = [ 
    grifter, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

