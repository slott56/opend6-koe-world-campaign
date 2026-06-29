"""
Extract Characters from ``namo``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



namo_high_priest = Character(
    name='Namo, high priest',
    agility=Agility(4*D, {'fighting': 4*D+1, 'melee combat': 4*D+2, 'climbing': 4*D+1, 'stealth': 4*D+1}),
    coordination=Coordination(3*D, {'marksmanship': 4*D, 'throwing': 3*D+1}),
    physique=Physique(3*D, {'running': 4*D+2, 'stamina': 4*D+1, 'swimming': 4*D}),
    intellect=Intellect(3*D, {'trading': 4*D}),
    acumen=Acumen(2*D, {'hide': 3*D+1, 'investigation': 3*D, 'search': 3*D+2}),
    charisma=Charisma(2*D, {'intimidation': 3*D+2, 'mettle': 3*D, 'persuasion': 3*D}),
    extranormal=Miracles(1*D, {'divination': 2*D+1, 'favor': 1*D+2}),
    strength_damage=2*D,
    move='10',
    fate_points='1',
    character_points='5',
    body=24,
    disadvantages=[
        Prejudice(R1, 'those not from Gadara represent potential threats (+4 to the difficulty to all interactions with non-natives)')
    ],
    advantages=[
        Authority(R3, 'high priest and ruler of Gadara')
    ],
    special_abilities=[],
    equipment='holy symbol; tribal leader staff (damage +1D+2)'
)
characters = [ 
    namo_high_priest, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

