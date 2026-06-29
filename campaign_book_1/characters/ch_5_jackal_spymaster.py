"""
Extract Characters from ``ch_5_jackal_spymaster.ipynb``.
Created by V2026.6.6.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



spymaster_candler = Character(
    name='Candler',
    description='Jackal Spy Master -- City of White Water',
    physique=Physique(3*D+2),
    agility=Agility(3*D, {'fighting': 0*D+2, 'melee combat': 2}),
    coordination=Coordination(2*D+2),
    intellect=Intellect(2*D+2, {'cultures': 1, 'reading/writing': 1, 'scholar': 1, 'speaking': 1, 'trading': 1, 'traps': 1}),
    acumen=Acumen(3*D, {'crafting': 1, 'disguise': 1, 'gambling': 1, 'hide': 1, 'streetwise': 1}),
    charisma=Charisma(3*D, {'intimidation': 2*D}),
    extranormal=Miracles(2*D),
    body=20,
    move=10,
    special_abilities=[
        UncannyAptitude(2, "Hardiness, +2 damage resistance")
    ],
    advantages=[
        Contacts(1, "Bargeman and Jackal Temple"),
    ],
    disadvantages=[
        Quirk(2, "Always glancing around nervously"),
        Employed(2, "Temple of the Jackal"),
        Quirk(2, "Voyeur"),
        Quirk(1, "Secret identity as spymaster")
    ]
)
characters = [ 
    spymaster_candler, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

