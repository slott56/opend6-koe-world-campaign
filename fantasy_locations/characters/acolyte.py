"""
Extract Characters from ``acolyte``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



typical_acolyte = Character(
    name='Typical Acolyte',
    agility=Agility(2*D, {'melee combat': 3*D}),
    coordination=Coordination(2*D, {}),
    physique=Physique(3*D, {}),
    intellect=Intellect(3*D, {'cultures': '3D +1', 'reading/writing': 3*D+1, 'speaking': 3*D+1}),
    acumen=Acumen(3*D, {'investigation': 3*D+2}),
    charisma=Charisma(3*D, {'mettle': 3*D+1}),
    extranormal=Miracles(1*D, {'divination': 2*D, 'favor': 2*D+1, 'strife': 2*D+2}),
    move='10',
    strength_damage=2*D,
    fate_points='0',
    character_points='2',
    body=11,
    disadvantages=[
        Devotion(R1, 'to religion'),
        Employed(R1, "must follow sect's regulations")],
    equipment='robes; holy symbol; quarterstaff (damage +1D+2)'
)
characters = [ 
    typical_acolyte, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

