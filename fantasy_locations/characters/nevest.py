"""
Extract Characters from ``nevest``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



nevest_guard = Character(
    name='Nevest, Guard',
    agility=Agility(4*D, {'melee combat': 5*D}),
    coordination=Coordination(3*D, {}),
    physique=Physique(4*D, {'stamina': 4*D+2}),
    intellect=Intellect(2*D, {}),
    acumen=Acumen(3*D, {'streetwise': 3*D+2, 'search': 3*D+1}),
    charisma=Charisma(2*D, {'intimidation': 2*D+1}),
    move='10',
    strength_damage=2*D,
    fate_points='0',
    character_points='0',
    body=17,
    equipment='ring mail armor (Armor Value +1D+1); long sword (damage +2D+2)'
)
characters = [ 
    nevest_guard, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

