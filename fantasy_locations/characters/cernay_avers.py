"""
Extract Characters from ``cernay_avers``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



cernay_avers_cleric = Character(
    name='Cernay Avers, Cleric',
    agility=Agility(2*D+1, {'melee combat': 4*D+1}),
    coordination=Coordination(2*D, {'throwing': 2*D+2}),
    physique=Physique(2*D, {}),
    intellect=Intellect(3*D, {'cultures': 4*D, 'reading/writing': 3*D+1, 'scholar': 3*D+1, 'speaking': 3*D+1}),
    acumen=Acumen(3*D, {'search': 3*D+1}),
    charisma=Charisma(3*D, {'mettle': 4*D}),
    extranormal=Miracles(2*D, {'divination': 3*D, 'favor': 2*D+1, 'strife': 2*D+2}),
    move='10',
    strength_damage=1*D,
    fate_points='0',
    character_points='2',
    body=16,
    disadvantages=[
        Devotion(R3, 'to religion'),
        Employed(R2, "must follow sect's regulations")],
    equipment='robes; coins; pouches containing holy symbols; mace (damage +1D+1)',
)
characters = [ 
    cernay_avers_cleric, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

