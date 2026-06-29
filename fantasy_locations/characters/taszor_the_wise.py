"""
Extract Characters from ``taszor_the_wise``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



taszor_the_wise = Character(
    name='Taszor the Wise',
    agility=Agility(2*D+1, {'fighting': 3*D+2, 'melee combat': 4*D}),
    coordination=Coordination(2*D, {}),
    physique=Physique(3*D+2, {'lifting': 4*D, 'running': 4*D, 'stamina': 4*D}),
    intellect=Intellect(3*D, {'devices': 4*D, 'trading': 3*D+1, 'traps': 4*D}),
    acumen=Acumen(3*D, {'artist': 4*D, 'crafting': 5*D, 'gambling': 3*D+1}),
    charisma=Charisma(2*D+1, {'intimidation': 3*D+2}),
    extranormal=Magic(3*D, {'alteration': 4*D+1, 'apportation': 4*D, 'conjuration': 4*D+2, 'divination': 4*D}),
    move='8',
    strength_damage=2*D,
    fate_points='0',
    character_points='3',
    body=21,
    disadvantages=[
        Hindrance(R2, '+2 to bluff, charm, and persuasion difficulties'),
        Hindrance(R1, '2-meter reduction to running, swimming, and jumping Move')],
    advantages=[Size(R1, 'scale value of 3')],
    special_abilities=[
        Hardiness(R2, '+2 to damage resistance totals'),
        Longevity(R1),
        InfravisionUltravision(R1, '+2 to sight-based totals while in dim or dark conditions')],
    equipment='leather garments (Armor Value +2); writing materials; pouch of spell components'
)
characters = [ 
    taszor_the_wise, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

