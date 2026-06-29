"""
Extract Characters from ``balam_mis``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



balam_mis_king = Character(
    name='Balam Mis, King',
    agility=Agility(3*D, {'fighting': 3*D+2, 'melee combat': 4*D}),
    coordination=Coordination(3*D, {'throwing': 3*D+1}),
    physique=Physique(3*D, {'running': 4*D+2, 'stamina': 3*D+1}),
    charisma=Charisma(3*D, {'animal handling': 3*D+2, 'intimidation': 4*D+1}),
    intellect=Intellect(2*D, {'navigation': 2*D+1, 'traps': 2*D+2}),
    acumen=Acumen(3*D, {'search': 3*D+1, 'Miracle': 1*D, 'divination': 1*D+2}),
    move='10',
    strength_damage=2*D,
    fate_points='1',
    character_points='5',
    body=27,
    disadvantages=[Enemy(R1, "another ruler doesn't like him")],
    advantages=[Authority(R3, 'ruler')],
    equipment='fine clothes; feathered robe (Armor Value +1); feather and cloth headdress'
)
characters = [ 
    balam_mis_king, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

