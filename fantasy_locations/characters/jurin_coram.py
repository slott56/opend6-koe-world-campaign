"""
Extract Characters from ``jurin_coram``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



jurin_coram_inn_keeper = Character(
    name='Jurin Coram, Inn Keeper',
    agility=Agility(2*D, {'riding': 2*D+2}),
    coordination=Coordination(2*D, {}),
    physique=Physique(2*D, {'stamina': 3*D+1}),
    intellect=Intellect(2*D, {'cultures': 2*D+1, 'trading': 4*D}),
    acumen=Acumen(2*D, {'streetwise': 3*D+2, 'search': 4*D}),
    charisma=Charisma(3*D, {'bluff': 4*D, 'charm': 3*D+1, 'persuasion': 3*D+1}),
    move='10',
    strength_damage=1*D,
    fate_points='0',
    character_points='2',
    body=16,
    equipment='clothes; pipe; small knife (damage +2)'
)
characters = [ 
    jurin_coram_inn_keeper, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

