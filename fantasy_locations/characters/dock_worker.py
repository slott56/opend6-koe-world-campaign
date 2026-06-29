"""
Extract Characters from ``dock_worker``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



typical_dock_worker = Character(
    name='Typical Dock Worker',
    agility=Agility(3*D, {'fighting': 4*D, 'melee combat': 4*D}),
    coordination=Coordination(2*D, {'pilotry': 3*D+1}),
    physique=Physique(4*D, {'lifting': 5*D, 'running': 4*D+1, 'stamina': 5*D}),
    intellect=Intellect(3*D, {}),
    acumen=Acumen(3*D, {'gambling': 3*D+1, 'hide': 4*D, 'streetwise': 4*D}),
    charisma=Charisma(3*D, {'bluff': 3*D+2}),
    strength_damage=3*D,
    fate_points='0',
    character_points='0',
    body=12,
    equipment='clothes; small knife (damage +2); heavy garments (Armor Value +1)',
)
characters = [ 
    typical_dock_worker, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

