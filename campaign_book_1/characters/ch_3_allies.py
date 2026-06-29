"""
Extract Characters from ``ch_3_allies.ipynb``.
Created by V2026.5.7.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



librarian = Character(
    name='Librarian',
    physique=Physique(3*D+2),
    agility=Agility(4*D, {'fighting': 1*D, 'melee combat': 2}),
    coordination=Coordination(4*D, {'charioteering': 0*D, 'lockpicking': 0*D, 'marksmanship': 0*D, 'pilotry': 0*D, 'sleight of hand': 0*D, 'throwing': 0*D}),
    intellect=Intellect(3*D+2, {'cultures': 0*D, 'devices': 0*D, 'healing': 0*D, 'navigation': 0*D, 'reading/writing': 0*D, 'scholar': 0*D, 'speaking': 0*D, 'trading': 0*D, 'traps': 0*D}),
    acumen=Acumen(3*D+2, {'artist': 0*D, 'crafting': 0*D, 'disguise': 0*D, 'gambling': 0*D, 'hide': 0*D, 'investigation': 0*D, 'know-how': 0*D, 'search': 0*D, 'streetwise': 0*D, 'survival': 0*D, 'tracking': 0*D}),
    charisma=Charisma(3*D+2, {'intimidation': 3*D+1}),
    extranormal=Magic(2*D),
    body=20,
    move=10,
    advantages=[
        Contacts(2, "Squire Angler"),
    ],
    disadvantages=[
        Devotion(2, "Squire Angler"),
    ],
)

library_guard = Character(
    name='Library Guards',
    physique=Physique(3*D+2),
    agility=Agility(4*D, {'fighting': 1*D, 'melee combat': 2}),
    coordination=Coordination(4*D, {'charioteering': 0*D, 'lockpicking': 0*D, 'marksmanship': 0*D, 'pilotry': 0*D, 'sleight of hand': 0*D, 'throwing': 0*D}),
    intellect=Intellect(3*D+2, {'cultures': 0*D, 'devices': 0*D, 'healing': 0*D, 'navigation': 0*D, 'reading/writing': 0*D, 'scholar': 0*D, 'speaking': 0*D, 'trading': 0*D, 'traps': 0*D}),
    acumen=Acumen(3*D+2, {'artist': 0*D, 'crafting': 0*D, 'disguise': 0*D, 'gambling': 0*D, 'hide': 0*D, 'investigation': 0*D, 'know-how': 0*D, 'search': 0*D, 'streetwise': 0*D, 'survival': 0*D, 'tracking': 0*D}),
    charisma=Charisma(3*D+2, {'intimidation': 3*D+1}),
    body=24,
    move=10,
)
characters = [ 
    librarian, library_guard, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

