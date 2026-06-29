"""
Extract Characters from ``tiu_mali``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



tiu_mali = Character(
    name='Tiu Mali',
    agility=Agility(4*D, {'contortion': 4*D+1, 'climbing': 4*D+2, 'stealth': 4*D+1}),
    coordination=Coordination(2*D, {'pilotry crystal ship': 2*D+2}),
    physique=Physique(2*D, {'stamina': 3*D, 'swimming': 4*D}),
    charisma=Charisma(2*D, {'bluff': 3*D+1, 'charm': 3*D+2, 'mettle': 3*D}),
    intellect=Intellect(4*D, {'cultures': 5*D, 'reading/writing': 4*D+2, 'scholar': 5*D, 'speaking': 4*D+2, 'trading': 4*D+1}),
    acumen=Acumen(4*D, {'hide': 4*D+1, 'investigation': 5*D}),
    strength_damage=1*D,
    move='12',
    fate_points='1',
    character_points='3',
    body=21,
    disadvantages=[
        CulturalUnfamiliarity(R2, 'the surface world is a strange place, even documents cannot fully describe it (+1D to the difficulty of streetwise rolls)'),
        LanguageProblems(R2, 'the surface tongue is very different -- speaks with an unusual accent (+6 to the difficulty of all communication skills)')],
    advantages=[Wealth(R3)],
    special_abilities=[Hypermovement(R1)],
    equipment='clothes; maps; pouch full of pearls'
)
characters = [ 
    tiu_mali, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

