"""
Extract Characters from ``library_guard``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



typical_library_guard = Character(
    name='Typical Library Guard',
    agility=Agility(3*D, {'dodge': 4*D, 'fighting': 3*D+2, 'melee combat': 4*D}),
    coordination=Coordination(2*D, {'marksmanship': 3*D}),
    physique=Physique(4*D, {'running': 4*D+1, 'Intel- lect': 2*D, 'scholar': 3*D+2}),
    acumen=Acumen(4*D, {'investigation': 4*D+1, 'search': 4*D+1, 'tracking': 4*D+2}),
    charisma=Charisma(3*D, {'intimidation': 3*D+2}),
    move='10',
    strength_damage=2*D,
    fate_points='0',
    character_points='0',
    body=17,
    equipment='hard leather armor (Armor Value +1D+1); short sword (damage +1D+2); short bow and 10 arrows (damage +1D+2)'
)
characters = [ 
    typical_library_guard, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

