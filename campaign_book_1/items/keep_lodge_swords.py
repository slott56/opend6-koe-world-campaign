"""
Extract Characters from ``keep_lodge_swords.ipynb``.
Created by V2026.3.11.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



sword_of_piercing = Sword(
    name="Sword of Piercing",
    physique=Physique(1*D),
    intellect=Intellect(1*D),
    charisma=Charisma(1*D),
    special_abilities=[
        NaturalHandWeapon(2*D),
        ArmorDefeatingAttack(1, "negates 1D of armor"),
    ]
)
swords = [ 
    sword_of_piercing, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(swords)
    app()

