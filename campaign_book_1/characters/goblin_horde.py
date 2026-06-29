"""
Extract Characters from ``goblin_horde.ipynb``.
Created by V2026.6.15.dev3 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



great_leader = Creature(
    name="Goblin Great Leader",
    agility=Agility(3 * D + 2, {'acrobatics': 2, 'dodge': 2, 'fighting': 4, "melee combat": 4, 'stealth': 1}),
    coordination=Coordination(3 * D + 1, {"throwing": 1}),
    physique=Physique(4 * D,
                      {'running': 2, 'stamina': 3}),
    intellect=Intellect(3 * D, {"healing": 3}),
    acumen=Acumen(3 * D, {"crafting": 2, "survival": 3}),
    charisma=Charisma(3 * D, {'command': 3, "intimidation": 3}),
    disadvantages=[
        CulturalUnfamiliarity(2, "Lost in human company"),
    ],
    advantages=[
        Equipment(2, "Weapon or survival gear unknown to humans"),
    ],
    special_abilities=[
        CombatSense(2, "Surprise reduced by 4"),
    ],
    realm="Ælvish, mountains and forests",
    armor=["bone and hide armor +1D", "buckler +2",],
    weapons=["sword +1D+2"],
)

officer = Creature(
    name="Goblin Officer",
    agility=Agility(3 * D + 2, {'acrobatics': 2, 'dodge': 2, 'fighting': 2, "melee combat": 4, 'stealth': 2}),
    coordination=Coordination(3 * D, {"throwing": 1}),
    physique=Physique(3 * D + 1,
                      {'running': 2, 'stamina': 2}),
    intellect=Intellect(3 * D, {"healing": 2}),
    acumen=Acumen(3 * D, {"crafting": 2, "survival": 2}),
    charisma=Charisma(2 * D, {'command': 2, "intimidation": 2}),
    disadvantages=[
        CulturalUnfamiliarity(2, "Lost in human company"),
    ],
    advantages=[
        Equipment(2, "Weapon or survival gear unknown to humans"),
    ],
    special_abilities=[
        CombatSense(2, "Surprise reduced by 4"),
    ],
    realm="Ælvish, mountains and forests",
    armor=["bone and hide armor +1D", "buckler +1",],
    weapons=["sword +1D"],
)

forager = Creature(
    name="Goblin Forager",
    agility=Agility(3 * D, {'acrobatics': 2, 'dodge': 1, 'fighting': 2, "melee combat": 2, 'stealth': 1}),
    coordination=Coordination(3 * D, {"throwing": 1}),
    physique=Physique(3 * D,
                      {'running': 2, 'stamina': 2}),
    intellect=Intellect(3 * D, {"healing": 1}),
    acumen=Acumen(2 * D, {"tracking": 1*D, "survival": 2}),
    charisma=Charisma(2 * D, {'command': 1, "intimidation": 2}),
    disadvantages=[
        CulturalUnfamiliarity(2, "Lost in human company"),
    ],
    advantages=[
        Equipment(2, "Weapon or survival gear unknown to humans"),
    ],
    special_abilities=[
        CombatSense(2, "Surprise reduced by 4"),
    ],
    realm="Ælvish, mountains and forests",
    armor=["bone and hide armor +1D"],
    weapons=["hammer +1D"],
)
characters = [ 
    great_leader, officer, forager, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

