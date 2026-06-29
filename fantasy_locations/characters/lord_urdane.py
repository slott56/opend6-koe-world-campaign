"""
Extract Characters from ``lord_urdane``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



lord_urdane = Character(
    name='Lord Urdane',
    agility=Agility(2*D+2, {'dodge': 3*D, 'fighting': 3*D, 'melee combat': 3*D, 'riding': 3*D+2}),
    coordination=Coordination(2*D, {'charioteering': 2*D+1, 'lockpicking': 2*D+2, 'marksmanship': 4*D}),
    physique=Physique(2*D+1, {'lifting': 2*D+2, 'running': 2*D+2}),
    intellect=Intellect(4*D, {'cultures': 4*D, 'navigation': 4*D, 'reading/writing': 4*D, 'scholar': 4*D, 'speaking': 4*D, 'trading': 4*D}),
    acumen=Acumen(3*D, {'crafting': 3*D+1, 'disguise': 3*D+1, 'gambling': 3*D+2, 'investigation': 4*D, 'search': 3*D+1, 'streetwise': 4*D}),
    charisma=Charisma(3*D, {'animal handling': 4*D, 'bluff': 5*D, 'command': 4*D, 'intimidation': 4*D, 'mettle': 4*D, 'persuasion': 5*D}),
    strength_damage=1*D,
    move='10',
    fate_points='1',
    character_points='5',
    body=22,
    disadvantages=[
        Enemy(R2, 'neighboring kingdoms'),
        Devotion(R3, 'to acquiring land and power')],
    advantages=[
        Authority(R3, 'ruler'),
        Wealth(R4)],
    special_abilities=[],
    equipment='ornate staff of office (damage +1D+2); short sword (damage +1D+2); fine garments with a heavy brocade vest (Armor Value +1); pouch of coins and jewels'
)

characters = [ 
    lord_urdane, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

