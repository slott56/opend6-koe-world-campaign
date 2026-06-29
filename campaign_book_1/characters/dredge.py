"""
Extract Characters from ``dredge.ipynb``.
Created by V2026.5.7.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



dredge = Character(
    name='Groom Dredge, lackey to Squire Neck',
    description='Lackey to captain of guard in White Water. Only use clubs and maces, boss afraid of swords.',
    other_notes="Quote: 'Of course, sir.'",
    physique=Physique(3*D+2),
    agility=Agility(4*D, {'fighting': 0*D+2, 'riding': 2, 'melee combat': 2}),
    coordination=Coordination(4*D, {'lockpicking': 1*D}),
    intellect=Intellect(3*D+2, {'cultures': 1, 'traps': 1}),
    acumen=Acumen(3*D+2, {'hide': 1*D, 'search': 2, 'streetwise': 2}),
    charisma=Charisma(3*D+2, {'intimidation': 3*D+1}),
    body=24,
    move=10.0,
        advantages=[
        Patron(R1, "Squire Neck"),
    ],
    disadvantages=[
        Employed(R2, "Squire Neck"),
        Quirk(R2, "Inflated self-image, thinks he's irreplaceable"),
    ],
)
characters = [ 
    dredge, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

