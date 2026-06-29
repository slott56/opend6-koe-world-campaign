"""
Extract Characters from ``thufer``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



thufer_the_pious = Character(
    name='Thufer the Pious',
    agility=Agility(2*D+2, {'dodge': 3*D+1, 'fighting': 3*D, 'melee combat': 4*D+1, 'riding': 4*D+2}),
    coordination=Coordination(2*D, {'marksmanship': 3*D}),
    physique=Physique(3*D, {'running': 3*D+1, 'stamina': 4*D}),
    intellect=Intellect(2*D, {'cultures': 3*D, 'reading/writing': 3*D}),
    acumen=Acumen(2*D, {'search': 4*D+1, 'survival': 3*D+2, 'tracking': 4*D}),
    charisma=Charisma(2*D, {'command': 4*D, 'mettle': 3*D+1}),
    move='10',
    strength_damage=2*D,
    fate_points='1',
    character_points='3',
    body=19,
    disadvantages=[Devotion(R3, 'to chivalrous code')],
    advantages=[Authority(R1, 'leader of an army'), Patron(R1, 'King Thuslund')],
    equipment='broadsword (damage +2D); knife (damage +1D); plate armor with helmet (Armor Value +2D); steed'
)
characters = [ 
    thufer_the_pious, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

