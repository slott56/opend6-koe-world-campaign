"""
Extract Characters from ``kasen``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



kasen = Character(
    name='Kasen',
    agility=Agility(3*D, {'dodge': 3*D+2, 'stealth': 4*D}),
    coordination=Coordination(3*D, {}),
    physique=Physique(2*D, {'running': 2*D+1}),
    intellect=Intellect(3*D+1, {'reading/writing': 3*D+2, 'scholar': 4*D+1, 'speaking': 3*D+2, 'trading': 5*D}),
    acumen=Acumen(3*D, {'hide': 4*D, 'search': '3D +1', 'survival': 3*D+2, 'tracking': 3*D+1}),
    charisma=Charisma(3*D+2, {'charm': 4*D, 'persuasion': 4*D}),
    strength_damage=1*D,
    move='10',
    fate_points='1',
    character_points='5',
    body=21,
    disadvantages=[
        Devotion(R2, 'spends much time searching for new plants and herbs, and pays little attention to local events'),
        Employed(R3, 'driven to work until he can earn enough money to quit the business')
    ],
    special_abilities=[
        UncannyAptitude(R1, 'has a natural sense about plants - can select herbs and mix them into incense and potions that have astounding properties')
    ],
    advantages=[
        Contacts(R2, 'has many contacts from various lands who supply him with rare plants and herbs')
    ],
    equipment='fine clothes; keys; pouch bulging with coins '
)
characters = [ 
    kasen, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

