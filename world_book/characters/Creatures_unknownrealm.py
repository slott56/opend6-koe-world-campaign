"""
Extract Characters from ``creatures.ipynb realm unknown realm characters``.
Created by V2026.5.7.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



metal_man = Creature(
    name="Metal Man",
    description="Inhabitants of the unknown realm",
    agility=Agility(2 * D, {'fighting': 2, "melee combat": 2}),
    coordination=Coordination(2 * D),
    physique=Physique(4 * D,
                      {'lifting': 2*D, 'stamina': 2*D}),
    intellect=Intellect(2 * D),
    acumen=Acumen(2 * D),
    charisma=Charisma(1 * D, {"intimidation": 2*D}),
    disadvantages=[
        CulturalUnfamiliarity(2, "Lost in human company"),
        AchillesHeel(3, "Vulnerability to water and acid, takes double damage"),
    ],
    advantages=[
        Equipment(2, "Weapon or survival gear unknown to humans"),
    ],
    special_abilities=[
    ],
    realm="unknown realm",
)
characters = [ 
    metal_man, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

