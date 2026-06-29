"""
Extract Characters from ``kinzo_mimoto``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



kinzo_mimoto_warlord = Character(
    name='Kinzo Mimoto, Warlord',
    agility=Agility(2*D, {'dodge': 3*D, 'melee combat': 4*D+2, 'riding': 4*D}),
    coordination=Coordination(2*D+1, {}),
    physique=Physique(2*D+2, {}),
    intellect=Intellect(3*D, {'cultures': 4*D+1, 'reading/writing': 5*D, 'scholar': 3*D+1, 'speaking': 4*D}),
    acumen=Acumen(2*D, {}),
    charisma=Charisma(3*D, {'charm': 4*D, 'command': 5*D+1, 'intimidation': 3*D+2, 'mettle': 3*D+1}),
    move='10',
    strength_damage=1*D,
    fate_points='1',
    character_points='5',
    body=23,
    disadvantages=[Enemy(R2, 'neighboring warlords')],
    advantages=[Authority(R2, 'over lands and people'),
                Contacts(R2, 'has made treaties with other warlords'),
                Wealth(R4)],
    equipment='katana (damage +2D); knife (damage +1D); exceptional armor with mempo (Armor Value +2D+2); steed'
)
characters = [ 
    kinzo_mimoto_warlord, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

