"""
Extract Characters from ``summer_blossom``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



summer_blossom = Character(
    name='Summer Blossom',
    agility=Agility(4*D, {'acrobatics': 5*D, 'contortion': 6*D, 'dodge': 6*D, 'fighting': 6*D, 'jumping': 5*D+1}),
    coordination=Coordination(2*D+2, {}),
    physique=Physique(2*D+1, {'running': 2*D+2, 'stamina': 3*D}),
    intellect=Intellect(2*D, {'traps': 3*D}),
    acumen=Acumen(2*D, {'tracking': 3*D}),
    charisma=Charisma(2*D, {'mettle': 2*D+1}),
    strength_damage=1*D,
    move='10',
    fate_points='0',
    character_points='4',
    body=22,
    disadvantages=[Devotion(R1, 'to improving her fighting skills'),
                   Quirk(R1, 'aloof')],
    advantages=[Contacts(R3, 'spirit of sister')],
    special_abilities=[
        Immortality(R1, 'cannot be killed so long as she avoids kissing a man, with Additional Effect (R2) of regeneration to full health after being "killed," allowing lost limbs or the like to grow back')]
)
characters = [ 
    summer_blossom, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

