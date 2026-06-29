"""
Extract Characters from ``mayan_priest``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



typical_priest = Character(
    name='Typical Priest',
    agility=Agility(3*D, {'dodge': 3*D+2, 'fighting': 3*D+1, 'melee combat': 3*D+2}),
    coordination=Coordination(2*D, {}),
    physique=Physique(3*D, {'running': 3*D+1, 'stamina': 3*D+1}),
    intellect=Intellect(2*D, {'navigation': 3*D, 'scholar': 4*D, 'search': 2*D+1}),
    acumen=Acumen(4*D, {}),
    charisma=Charisma(3*D, {'intimidation': 3*D+2, 'mettle': 4*D, 'Miracle': 1*D, 'divination': 2*D, 'strife': 1*D+1}),
    move='10',
    strength_damage=2*D,
    fate_points='1',
    character_points='4',
    body=16,
    advantages=[Authority(R2, 'priest')],
    equipment='fine clothes; feather, jade, and cloth headdress'
)
characters = [ 
    typical_priest, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

