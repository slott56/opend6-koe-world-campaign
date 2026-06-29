"""
Extract Characters from ``new_keep_swords.ipynb``.
Created by V2026.5.7.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



sword_of_the_survivor = Sword(
    name="Sword of the Survivor",
    physique=Physique(1*D),
    agility=Agility(1*D),
    intellect=Intellect(1*D),
    special_abilities=[
        CombatSense(3, "Great Attacking"),
        AttackResistance(3, "Great Blocking"),
        NaturalHandWeapon(3*D),
    ],
    disadvantages=[
        AdvantageFlaw(3, "Either Combat Sense or Attack Resistance, never both in the same round.")
    ]
)
swords = [ 
    sword_of_the_survivor, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(swords)
    app()

