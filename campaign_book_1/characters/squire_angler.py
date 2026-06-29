"""
Extract Characters from ``squire_angler.ipynb``.
Created by V2026.5.7.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



squire_angler = Character(
    name='Squire Angler, Spymaster in Eagles',
    description='Captain of the Guard in Eagles.  An old friend of one of the characters.  Worried about the increase in tensions between Eagles and White Water.  Worried about highwaymen along the road.  Worried about the high price of corn.',
    other_notes="Quote: 'What can you do?'",
    physique=Physique(3*D+2),
    agility=Agility(4*D, {'fighting': 1*D+1, 'riding': 1*D, 'melee combat': 2}),
    coordination=Coordination(4*D, {'sleight of hand': 2}),
    intellect=Intellect(4*D, {'cultures': 1*D, 'speaking': 1*D, 'traps': 2}),
    acumen=Acumen(3*D+2, {'artist': 2}),
    charisma=Charisma(4*D, {'intimidation': 6*D}),
    body=24,
    move=10.0,
    advantages=[
        Patron(R1, "Sir Warrant"),
        Authority(R1, "aristocracy"),
    ],
    disadvantages=[
        Infamy(R1, "Worrier"),
        Quirk(R1, "Worrier"),
        Quirk(R1, "Womanizer"),
        Quirk(R1, "Clothes horse"),
        Prejudice(R1, "Terrified of ælvish creatures like goblins"),
        Employed(R2, "Spymaster for Sir Warrant"),
    ],
)
characters = [ 
    squire_angler, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

