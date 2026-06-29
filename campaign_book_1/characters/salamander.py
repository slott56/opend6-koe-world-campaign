"""
Extract Characters from ``salamander.ipynb``.
Created by V2026.6.6.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



salamander = Creature(
    name='Salamander',
    description='A big lizard, 10-14 ft. tall capable of walking upright and using weapons.  Weapons are crystals that can withstand the heat of its lair.',
    physique=Physique(4*D+2),
    agility=Agility(4*D+1, {'fighting': 1*D+1, 'stealth': 1*D, 'melee combat': 1*D}),
    coordination=Coordination(4*D+1),
    intellect=Intellect(3*D+2, {'cultures': 1*D, 'navigation': 1*D, 'reading/writing': 1*D, 'scholar': 1*D, 'speaking': 2*D}),
    acumen=Acumen(3*D+2, {'artist': 1*D, 'crafting': 1*D, 'survival': 1*D}),
    charisma=Charisma(3*D+2, {'intimidation': 1*D+1, 'persuasion': 2}),
    body=40,
    move=10,
    natural_abilities=[
        NaturalArmor(4, "thick skin"),
        Blur(2, "Flash to blind temporarily, improving attack and defense"),
        NaturalRangedWeapon(6*D, "fire breath"),
        Size(5, "800Kg mass, 8x typical human, scale 15"),
        Hypermovement(6, "12m Leap, 4x typical human"),
    ],
    disadvantages=[
        AchillesHeel(3, "Double damage from water-based attacks"),
        AchillesHeel(3, "Requires heat source"),
        Infamy(2, "Monsterous"),
    ]
)

hordling = Creature(
    name='Hordling',
    description='Dim-witted, pathetic creatures with wings and stingers in their tails.',
    physique=Physique(4*D, {'stamina': 4*D+1}),
    agility=Agility(3*D+2, {'fighting': 1*D}),
    coordination=Coordination(3*D+2, {'flight': 2}),
    intellect=Intellect(3*D+1),
    acumen=Acumen(3*D+1),
    charisma=Charisma(3*D, {'intimidation': 3*D+1}),
    body=18,
    move=10,
    natural_abilities=[
        NaturalHandWeapon(1*D, "Stinger on tail"),
        LifeDrain(1, "After attack +1D stun-only increase to body"),
    ],
    disadvantages=[
        AchillesHeel(2, "silver or magic"),
        AchillesHeel(1, "pentagrams"),
        Quirk(3, "obeys true name"),
        Quirk(2, "malicious"),
        Quirk(2, "fears holy symbols"),
        Quirk(2, "goes berserk when insulted"),
        Infamy(1, "a demon"),
        AchillesHeel(2, "holy ground, reduces PHY 1D each phase"),
        AchillesHeel(2, "holy water, stun-only 1D each phase")
    ]
)
characters = [ 
    salamander, hordling, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

