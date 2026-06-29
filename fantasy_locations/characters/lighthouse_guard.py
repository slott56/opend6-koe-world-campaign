"""
Extract Characters from ``lighthouse_guard``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



typical_lighthouse_guard = Character(
    name='Typical Lighthouse Guard',
    agility=Agility(3*D+2, {'fighting': 4*D+2, 'melee combat': 4*D+2}),
    coordination=Coordination(2*D, {}),
    physique=Physique(3*D+1, {'running': 3*D+2, 'stamina': 4*D+2}),
    charisma=Charisma(3*D, {'intimidation': 3*D+1}),
    intellect=Intellect(2*D+1, {}),
    acumen=Acumen(3*D+2, {'investigation': 4*D, 'streetwise': 4*D}),
    move='10',
    strength_damage=2*D,
    fate_points='0',
    character_points='0',
    body=15,
    equipment='chain mail armor (Armor Value +2D); halberd (damage +3D); pouch of food and water'
)
characters = [ 
    typical_lighthouse_guard, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

