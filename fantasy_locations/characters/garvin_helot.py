"""
Extract Characters from ``garvin_helot``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



garvin_helot_mayor = Character(
    name='Garvin Helot, Mayor',
    agility=Agility(2*D, {'dodge': 3*D, 'stealth': 3*D}),
    coordination=Coordination(2*D, {'lockpicking': 2*D+1}),
    physique=Physique(2*D, {}),
    intellect=Intellect(2*D, {'cultures': 2*D+1, 'reading/writing': 2*D+1, 'scholar': 3*D+2, 'speaking': 3*D+1, 'trading': 3*D+2}),
    acumen=Acumen(2*D, {'hide': 3*D, 'streetwise': 4*D}),
    charisma=Charisma(4*D, {'bluff': 4*D+1, 'charm': 4*D+1, 'persuasion': 4*D+1}),
    move='10',
    strength_damage=1*D,
    fate_points='0',
    character_points='2',
    body=16,
    advantages=[Authority(R2, 'mayor')],
    equipment='clothes; coins; keys to Government House'
)
characters = [ 
    garvin_helot_mayor, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

