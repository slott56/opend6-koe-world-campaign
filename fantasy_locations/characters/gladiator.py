"""
Extract Characters from ``gladiator``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



typical_gladiator = Character(
    name='Typical Gladiator',
    agility=Agility(4*D, {'acrobatics': 4*D+1, 'dodge': 4*D+1, 'fighting': 4*D+1, 'melee combat': 5*D}),
    coordination=Coordination(3*D, {'charioteering': 3*D+2, 'marksmanship': 3*D+1}),
    physique=Physique(4*D, {'running': 4*D+1, 'stamina': 4*D+2}),
    charisma=Charisma(2*D, {'command': 3*D, 'intimidation': 3*D, 'mettle': 3*D}),
    intellect=Intellect(2*D, {'healing': 2*D+1}),
    acumen=Acumen(3*D, {'crafting': 3*D+2, 'gambling': 3*D+2, 'know-how': 3*D+1, 'survival': 4*D}),
    move='10',
    strength_damage=2*D,
    fate_points='0',
    character_points='2',
    body=22,
    equipment='hardened leather armor (Armor Value +1D+1); small shield (Armor Value +2D); short sword (damage +1D+2)',
)
characters = [ 
    typical_gladiator, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

