"""
Extract Characters from ``phylo_duran``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



phylo_duran = Character(
    name='Phylo Duran',
    agility=Agility(3*D, {'climbing': 3*D+2}),
    coordination=Coordination(2*D, {}),
    physique=Physique(2*D, {'lifting': 2*D+2, 'stamina': 3*D}),
    intellect=Intellect(4*D, {'cultures': 5*D, 'reading/writing': 6*D+2, 'scholar': 6*D, 'speaking': 4*D+1}),
    acumen=Acumen(4*D, {'investigation': 5*D, 'search': 4*D+2}),
    charisma=Charisma(3*D, {'bluff': 3*D+1, 'intimidation': 3*D+2, 'mettle': 4*D, 'persuasion': 3*D+1}),
    strength_damage=1*D,
    move='10',
    fate_points='1',
    character_points='6',
    body=21,
    disadvantages=[
        Employed(R2, "dedication to the library and Inachon's Point prevents venturing from the town"),
        Hindrance(R1, '+ 1 to charm , persuasion , and speaking difficulties'),
        Quirk(R2, 'loathes ignorance and anyone less knowledgeable than he (which is most everyone)')],
    advantages=[
        Patron(R3, "the ruling council of Inachon's Point pays for the funds the library, its employees, and new acquisitions")],
    equipment='mismatched clothes; keys; cloth bookmarks'
)
characters = [ 
    phylo_duran, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

