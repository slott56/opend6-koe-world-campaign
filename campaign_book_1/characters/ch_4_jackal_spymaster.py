"""
Extract Characters from ``ch_4_jackal_spymaster.ipynb``.
Created by V2026.6.6.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



spymaster_steward = Character(
    name='Steward',
    description='Jackal Spy Master in City of Eagles',
    physique=Physique(3*D+2),
    agility=Agility(3*D+1, {'melee combat': 1*D}),
    coordination=Coordination(2*D+2, {'sleight of hand': 2}),
    intellect=Intellect(3*D, {'cultures': 1, 'reading/writing': 1, 'speaking': 1, 'traps': 2}),
    acumen=Acumen(3*D+1, {'disguise': 1, 'gambling': 1, 'hide': 1*D, 'investigation': 1, 'search': 1, 'streetwise': 1}),
    charisma=Charisma(3*D+2, {'persuasion': 1*D}),
    extranormal=Miracles(2*D),
    body=24,
    move=10,
    special_abilities=[
        UncannyAptitude(1, "Eidetic memory")
    ],
    advantages=[
        Contacts(1, "Barkeep, Stable Boss"),
    ],
    disadvantages=[
        Quirk(2, "Ruthless use of power"),
        Employed(2, "Temple of the Jackal"),
        Quirk(2, "Voyeur"),
        Quirk(1, "Secret identity as spymaster")
    ]
)
characters = [ 
    spymaster_steward, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

