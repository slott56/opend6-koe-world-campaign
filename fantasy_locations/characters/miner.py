"""
Extract Characters from ``miner``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



miner = Character(
    name='Miner',
    agility=Agility(3*D+1, {'climbing': 4*D+1, 'contortion': 3*D+2, 'dodge': 3*D+2, 'melee combat pickaxe': 4*D}),
    coordination=Coordination(3*D, {'charioteering': 3*D+2}),
    physique=Physique(3*D+2, {'lifting': 5*D, 'stamina': 5*D+2, 'swimming': 4*D}),
    intellect=Intellect(2*D, {'devices': 2*D+1, 'navigation': 2*D+2}),
    acumen=Acumen(2*D, {'investigation': 3*D, 'know-how': 2*D+1, 'search': 4*D, 'tracking': 3*D}),
    charisma=Charisma(2*D, {'command': 3*D, 'mettle': 3*D+2}),
    strength_damage=3*D,
    move='10',
    fate_points='0',
    character_points='2',
    body=16,
    equipment='pickaxe (damage +2); shovel (damage +2); helmet (Armor Value +2 to head only); leather vest (Armor Value +2)'
)
characters = [ 
    miner, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

