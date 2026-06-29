"""
Extract Characters from ``ori_swifthand``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



ori_swifthand_inn_regular = Character(
    name='Ori Swifthand, Inn Regular',
    agility=Agility(3*D, {'riding': 3*D+1}),
    coordination=Coordination(4*D, {'lockpicking': 4*D+1, 'sleight of hand': 4*D+1, 'throwing': 4*D+1}),
    physique=Physique(3*D, {}),
    intellect=Intellect(2*D+1, {'cultures': 2*D+2}),
    acumen=Acumen(2*D+2, {'hide': 4*D+1, 'streetwise': 4*D+2, 'search': 3*D}),
    charisma=Charisma(3*D, {'bluff': 3*D+2, 'charm': 3*D+1}),
    move='10',
    strength_damage=2*D,
    fate_points='0',
    character_points='1',
    body=19,
    disadvantages=[Enemy(R1, 'suspected of being a footpad and watched carefully by the mayor')],
    equipment='clothes; cloak; bag of pepper (+1 to difficulties for animals using track); '
              'lockpicking tools (+1D to lockpicking rolls; throwing dagger (damage +1D); stiletto (damage +1D); '
              'soft leather boots (+1 to stealth totals)'
)
characters = [ 
    ori_swifthand_inn_regular, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

