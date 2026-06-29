"""
Extract Characters from ``ladira_almer``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



ladira_almer_head_priestess = Character(
    name='Ladira Almer, Head Priestess',
    agility=Agility(3*D, {'fighting': 3*D+1, 'melee combat': 4*D}),
    coordination=Coordination(2*D, {}),
    physique=Physique(2*D, {}),
    intellect=Intellect(3*D+1, {'cultures': 3*D+2, 'reading/writing': 3*D+2, 'scholar': 4*D, 'speaking': 4*D}),
    acumen=Acumen(3*D, {'search': 3*D+1}),
    charisma=Charisma(3*D, {'mettle': 4*D+2}),
    extranormal=Miracles(2*D, {'divination': 2*D+2, 'favor': 4*D, 'strife': 4*D}),
    move='10',
    strength_damage=1*D,
    fate_points='0',
    character_points='2',
    body=16,
    disadvantages=[
        Devotion(R3, 'to religion'),
        Employed(R3, "must follow sect's regulations")
    ],
    advantages=[
        Authority(R1, 'religious leader'),
        Equipment(R1, 'special holy symbol')],
    equipment='robes; holy symbol (provides +2 bonus to divination, favor and strife skill totals); quarterstaff (damage +1D+2)'
)
characters = [ 
    ladira_almer_head_priestess, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

