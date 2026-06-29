"""
Extract Characters from ``guild_member``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



typical_guild_member = Character(
    name='Typical guild member',
    agility=Agility(3*D, {'fighting': 3*D+1, 'melee': 3*D+1}),
    coordination=Coordination(4*D, {'lockpicking': 4*D+1, 'sleight of hand': 5*D}),
    physique=Physique(3*D, {}),
    intellect=Intellect(2*D, {}),
    acumen=Acumen(3*D, {'hide': 3*D+1, 'streetwise': 4*D, 'search': 3*D+2}),
    charisma=Charisma(3*D, {'bluff': 3*D+1, 'charm': 3*D+1}),
    move='10',
    strength_damage=1*D,
    fate_points='0',
    character_points='1',
    body=14,
    equipment='clothes; cloak; basic lockpicking tools; dagger (damage +1D)'
)
characters = [ 
    typical_guild_member, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

