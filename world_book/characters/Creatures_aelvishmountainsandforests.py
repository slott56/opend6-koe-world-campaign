"""
Extract Characters from ``creatures.ipynb realm Ælvish, mountains and forests characters``.
Created by V2026.5.7.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



elf = Creature(
    name="Elf, Gnome, Goblin, Kobold",
    description="Inhabitants of the realm of mountains and forests",
    agility=Agility(3 * D, {'acrobatics': 2, 'dodge': 2, 'fighting': 2, "melee combat": 2, 'stealth': 2}),
    coordination=Coordination(3 * D, {"marksmanship": 2, "throwing": 1}),
    physique=Physique(3 * D,
                      {'running': 2, 'stamina': 2}),
    intellect=Intellect(3 * D, {"healing": 2, "scholar": 2, "traps": 2}),
    acumen=Acumen(3 * D, {"crafting": 2, "survival": 2}),
    charisma=Charisma(3 * D, {'command': 1, "intimidation": 2}),
    extranormal=Magic(3*D),
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
)
characters = [ 
    elf, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

