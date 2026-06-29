"""
Extract Characters from ``fane``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



fane = Character(
    name='Fane',
    agility=Agility(3*D, {'dodge': 3*D+1, 'fighting': 3*D+1, 'melee combat': 3*D+1, 'stealth': 4*D}),
    coordination=Coordination(4*D, {'lockpicking': 4*D+2, 'sleight of hand': 5*D, 'throwing': 4*D+1}),
    physique=Physique(2*D, {'lifting': 2*D+1, 'stam- ina': 2*D+2}),
    intellect=Intellect(3*D, {'reading/writing': 3*D+1, 'speaking': 3*D+1}),
    acumen=Acumen(3*D, {'hide': 4*D+2, 'search': 3*D+2, 'streetwise': 3*D+1, 'tracking': 4*D}),
    charisma=Charisma(3*D, {'bluff': 3*D+2, 'charm': 3*D+1, 'intimidation': 4*D, 'mettle': 4*D+2}),
    strength_damage=1*D,
    move='10',
    fate_points='1',
    character_points='2',
    body=21,
    disadvantages=[
        Enemy(R1, 'detested by other guilds attempting to move into the city'),
        Enemy(R2, 'harassed by local authorities')],
    advantages=[
        Authority(R2, "respected leader of the local thieves' guild")],
    special_abilities=[],
    equipment='lockpicking tools; long sword (damage +2D+2); soft leather vest (worn beneath a jerkin Armor Value +2); dagger (damage +1D)'
)
characters = [ 
    fane, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

