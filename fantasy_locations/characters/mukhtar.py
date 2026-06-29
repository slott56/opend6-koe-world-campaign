"""
Extract Characters from ``mukhtar``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



mukhtar_nomad_leader = Character(
    name='Mukhtar, Nomad Leader',
    agility=Agility(4*D, {'fighting': 4*D+1, 'melee combat': 5*D, 'riding': 4*D+2}),
    coordination=Coordination(3*D, {'marksmanship': 3*D+2}),
    physique=Physique(4*D, {'stamina': 5*D}),
    intellect=Intellect(2*D, {'cultures': 2*D+2, 'navigation': 4*D, 'trading': 3*D, 'traps': 2*D+2}),
    acumen=Acumen(3*D, {'gambling': 3*D+2, 'search': 3*D+1}),
    charisma=Charisma(2*D, {'animal handling': '3D +1', 'intimidation': 4*D+1}),
    move='10',
    strength_damage=2*D,
    fate_points='1',
    character_points='0',
    body=32,
    disadvantages=[
        Enemy(R1, 'a member of the Dahae tribe desires to become its new leader'),
        Enemy(R2, 'rules of cities that the Dahae have raided')],
    advantages=[
        Contacts(R1, 'local spies in many of the cities raided by the Dahae'),
        Authority(R2, 'possesses total rule and dedication of the band of nomads')],
    equipment='horse; camel; quilted silk robe (Armor Value +2); two-handed sword (damage +3D+1); water skin; food pouch; pouch of coins'
)
characters = [ 
    mukhtar_nomad_leader, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

