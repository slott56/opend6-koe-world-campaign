"""
Extract Characters from ``betha_etain``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



betha_etain_mayor = Character(
    name='Betha Etain, Mayor',
    agility=Agility(3*D, {}),
    coordination=Coordination(3*D, {'sleight of hand': 3*D+1}),
    physique=Physique(3*D, {'stamina': 3*D+2}),
    charisma=Charisma(2*D, {'bluff': 3*D, 'mettle': 4*D}),
    intellect=Intellect(3*D, {'reading/writing': 3*D+1, 'scholar': 3*D+1, 'speaking': 3*D+1, 'trading': 4*D}),
    acumen=Acumen(4*D, {'investigation': 4*D+2, 'know -how': 4*D+2, 'streetwise': 4*D+1, 'search': 4*D+1}),
    move='8',
    strength_damage=2*D,
    fate_points='1',
    character_points='5',
    body=19,
    advantages=[
        Authority(R2, 'mayor'),
        Size(R1, 'scale value of 3')],
    disadvantages=[
        Hindrance(R1, '2-meter reduction to running , swimming , and jumping Move'),
        Quirk(R1, 'officious')],
    special_abilities=[SkillBonus(R1, '+ 1 to crafting, devices, and traps totals')],
    equipment='keys to various buildings in the town; fine clothes; staff of authority (damage +1D)'
)
characters = [ 
    betha_etain_mayor, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

