"""
Extract Characters from ``eagles_swords.ipynb``.
Created by V2026.5.7.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



ice_knife = Sword(
    name="Ice Knife",
    description="If it persuades the wielder, there will be a killing rampage over friend and foe alike",
    physique=Physique(1*D),
    agility=Agility(1*D),
    intellect=Intellect(1*D),
    charisma=Charisma(2*D, {"persuasion": 1}),
    special_abilities=[
        NaturalHandWeapon(2*D+1, "+1D damage to creatures vulnerable to cold")
    ],
    disadvantages=[
        AdvantageFlaw(3, "wants to rampage and kill everything.")
    ]
)

goblin_death = Sword(
    name="Goblin Death",
    description="If it detects goblins but doesn't get to kill them, it sulks and refuses to detect any for a few hours",
    physique=Physique(1*D),
    agility=Agility(1*D),
    intellect=Intellect(1*D),
    charisma=Charisma(2*D),
    special_abilities=[
        NaturalHandWeapon(2*D+1),
        ArmorDefeatingAttack(2, "Reduces armor by -2"),
        ExtraSense(2, "Detects goblins and other creatures from the same realm")
    ],
    disadvantages=[
        AdvantageFlaw(3, "insists on killing the goblins it detects.")
    ]
)
swords = [ 
    ice_knife, goblin_death, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(swords)
    app()

