"""
Extract Characters from ``fantasy_reptile_man.ipynb``.
Created by V2025.12.8.dev5 of ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



reptile_folk = Character(
    agility=Agility(3*D+2, {'fighting': 4*D+1, 'dodge': 4*D, 'melee combat': 4*D}),
    coordination=Coordination(2*D, {'throwing': 3*D}),
    physique=Physique(4*D, {'lifting': 4*D+1, 'running': 4*D+1, 'stamina': 4*D+1}),
    intellect=Intellect (3*D, {'navigation': 3 * D + 2, 'trading': 3 * D + 1}),
    acumen=Acumen (3*D+1, {'survival': 3 * D + 2,
                         'tracking': 3 * D + 2}),
    charisma=Charisma (2*D, {'intimidation': 3 * D, 'mettle': 3*D}),
    advantages=[],
    disadvantages=[
        AchillesHeel(3, 'Cold -- take 1D in damage per round in temperatures below 15 C'),
        Hindrance(2, "Arrogance -- +2 to bluff, charm, and persuasion difficulties"),
    ],
    special_abilities=[
        ExtraBodyPart(1, 'Tail'),
        NaturalArmor(1, 'Scales -- +1D to damage resistance total against physical damage'),
        NaturalHandWeapon(1, 'Claws -- +1D damage'),
    ],
    # :Strength Damage: 2D
    move=10,
    fate_points=0,
    character_points=2,
    # :Body Points: 22
)
characters = [ 
    reptile_folk, 
]


if __name__ == "__main__":
    app = build_app(characters)
    app()


__test__ = {
    
    "placeholder": ">>> pass\n\n"
    
}
