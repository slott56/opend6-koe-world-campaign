"""
Extract Characters from ``miroko_yhukiini``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



miroko_yhukiini_warrior = Character(
    name='Miroko Yhukiini, Warrior',
    agility=Agility(2*D+2, {'dodge': 3*D+1, 'fighting': '3 D', 'melee combat': 5*D, 'riding': 4*D+2}),
    coordination=Coordination(2*D, {}),
    physique=Physique(3*D, {'running': 3*D+1, 'stamina': 4*D}),
    intellect=Intellect(2*D, {'cultures': 3*D, 'reading/writing': 3*D}),
    acumen=Acumen(2*D, {'search': 4*D+1, 'survival': 3*D+2, 'tracking': 4*D}),
    charisma=Charisma(2*D+1, {'command': 4*D, 'mettle': 3*D+1}),
    move='10',
    strength_damage=2*D,
    fate_points='0',
    character_points='3',
    body=19,
    disadvantages=[Enemy(R1, 'those who are envious of her status')],
    advantages=[Authority(R1, 'leader of an army'),
                Patron(R2, 'Kinzo Mimoto the Warlord')],
    equipment='katana (damage +2D); knife (damage +1D); armor with mempo (Armor Value +2D); steed'
)
characters = [ 
    miroko_yhukiini_warrior, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

