"""
Extract Characters from ``creatures.ipynb realm bright towers and cities characters``.
Created by V2026.5.7.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



æsir = Character(
    name="Æs",
    description="Tall and pretty, these beings have powerful magic skills and often have wonderful equipment.",
    acumen=Acumen(4*D),
    charisma=Charisma(4*D, {"charm": 2*D, "intimidation": 3*D, "mettle": 3*D}),
    intellect=Intellect(4*D, {"speaking": 2*D}),
    agility=Agility(4*D, {"combat": 2*D, "fighting": 2*D, "melee combat": 2*D}),
    coordination=Coordination(4*D, {"throwing": 2*D}),
    physique=Physique(4*D, {"lifting": 2*D, "running": 2*D}),
    extranormal=Magic(4*D),
    advantages=[Fame(3, "widely-known and recognized"),],
    special_abilities=[
        Longevity(3, "Lives thousands of years"),
        NaturalArmor(2, "Very tough"),
        NaturalHandWeapon(2, "Throws a powerful punch"),
    ],
    realm="bright towers and cities",
)
characters = [ 
    æsir, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

