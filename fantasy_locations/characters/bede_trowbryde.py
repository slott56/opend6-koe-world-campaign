"""
Extract Characters from ``bede_trowbryde``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



bede_trowbryde_mayor = Character(
    name='Bede Trowbryde, Mayor',
    agility=Agility(2*D, {'riding': 2*D+1}),
    coordination=Coordination(2*D, {'sleight of hand': 2*D+2}),
    physique=Physique(2*D, {'running': 2*D+1}),
    intellect=Intellect(2*D, {'cultures': 3*D, 'reading/writing': 2*D+2, 'scholar': 3*D, 'speaking': 3*D, 'trading': 4*D}),
    acumen=Acumen(2*D, {'hide': 2*D+1, 'streetwise': 4*D, 'search': 3*D}),
    charisma=Charisma(3*D, {'bluff': 3*D+2, 'charm': 4*D, 'persuasion': 3*D+1}),
    move='10',
    strength_damage=1*D,
    fate_points='0',
    character_points='1',
    body=16,
    advantages=[Authority(R2, 'mayor')],
    equipment='fine clothes; cloak; hat; pouch with coins'
)
characters = [ 
    bede_trowbryde_mayor, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

