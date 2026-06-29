"""
Extract Characters from ``aaroth``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



aaroth_the_wizard = Character(
    name='Aaroth the Wizard',
    agility=Agility(2*D+1, {'dodge': 2*D+2, 'fighting': 2*D+2, 'melee combat': 2*D+2, 'riding': 2*D+2}),
    coordination=Coordination(2*D+1, {'sleight of hand': 3*D}),
    physique=Physique(2*D, {'lifting': 2*D+1, 'running': 2*D+1, 'stamina': 2*D+2}),
    intellect=Intellect(3*D+1, {'cultures': 3*D+2, 'healing': 3*D+2, 'navigation': 3*D+2, 'reading/writing': 3*D+2, 'scholar': 4*D, 'speaking': 3*D+2, 'trading': 3*D+2}),
    acumen=Acumen(3*D+1, {'artist': 3*D+2, 'crafting': '3D +2', 'disguise': 3*D+2, 'gambling': 3*D+2, 'hide': 3*D+2, 'investigation': 4*D, 'know-how': 3*D+2, 'search': 3*D+2, 'streetwise': 3*D+2}),
    charisma=Charisma(2*D+2, {'animal handling': 3*D, 'bluff': 3*D, 'charm': 3*D, 'command': 3*D, 'intimidation': 3*D, 'mettle': 3*D, 'persuasion': 3*D}),
    extranormal=Magic(3*D, {'alteration': 5*D, 'apportation': 3*D+2, 'conju- ration': 6*D, 'divination': 3*D}),
    strength_damage=1*D,
    move='10',
    fate_points='1',
    character_points='10',
    body=21,
    disadvantages=[
        Enemy(R2, 'hunted by members of a wizard cult'),
        Prejudice(R2, 'left a wizard cult that turned evil and he is commonly confused by people who do not know about the group as a current member')
    ],
    advantages=[
        Wealth(R3),
    ],
    special_abilities=[
        LuckGood(R1)
    ],
    equipment='small knife (damage +2); ' 
              'long staff (damage +1D+2); '
              'heavy robes (Armor Value +2); '
              'bag with various tomes; '
              'pouches with spell components and a few gold pieces; '
              'writing supplies'
)

characters = [ 
    aaroth_the_wizard, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

