"""
Extract Characters from ``fantasy_dwarf.ipynb``.
Created by V2025.12.8.dev5 of ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



dwarf = Character(
    agility=Agility(3*D, {'fighting': 3*D+2, 'melee combat': 4*D}),
    coordination=Coordination(2*D),
    physique=Physique(3*D+2, {'lifting': 4*D, 'running': 4*D, 'stamina': 4*D}),
    intellect=Intellect (2*D, {'devices': 3 * D, 'trading': 2 * D + 1,
                              'traps': 2 * D + 2}),
    acumen=Acumen (3*D, {'artist': 3 * D + 2, 'crafting': 4 * D,
                         'gambling': 3 * D + 1}),
    charisma=Charisma (2*D+1, {'intimidation': 2 * D + 2}),
    advantages=[
        Size(1, "Small -- scale value of 3"),
    ],
    disadvantages=[
        Hindrance(2, "Gruffness -- +2 to bluff, charm and persuasion difficulties"),
        Hindrance(1, "Shorter Stride -- 2-meter reduction to running, swimming, and jumping Move"),
    ],
    special_abilities=[
        Hardiness(2, "+2 to damage resistance totals"),
        Longevity(1),
        InfravisionUltravision(1, "Ultravision -- +2 to sight-based totals while in dim or dark conditions"),
    ],
    # :Strength Damage: 2D
    move=8,
    fate_points=0,
    character_points=2,
    # :Body Points: 19
)
characters = [ 
    dwarf, 
]


if __name__ == "__main__":
    app = build_app(characters)
    app()


__test__ = {
    
    "placeholder": ">>> pass\n\n"
    
}
