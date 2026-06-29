"""
Extract Characters from ``fantasy_elf.ipynb``.
Created by V2025.12.8.dev5 of ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



elf = Character(
    agility=Agility(3*D+2, {'melee combat': 3*D+2, 'stealth': 3*D+2}),
    coordination=Coordination(3*D, {'marksmanship': 4*D}),
    physique=Physique(2*D, {'running': 2*D+2}),
    intellect=Intellect(3*D, {'reading/writing': 3 * D + 1, 'scholar': 3 * D + 1,
                              'speaking': 3 * D + 1}),
    acumen=Acumen(3*D, {'artist': 3 * D + 1, 'hide': 3 * D + 2,
                         'search': 3 * D + 2, 'survival': 3 * D + 2, 'tracking': 3 * D + 2}),
    charisma=Charisma(3*D, {'animal handling': 3 * D + 2, 'charm': 3*D+2}),
    extranormal=Magic(1*D, {'alteration': 1*D+1}),
    advantages=[],
    disadvantages=[
        Devotion(2, "Nature -- feel a deep devotion and kinship with trees and plants"),
        Hindrance(2, "Arrogance -- +2 to bluff, charm and persuasion difficulties"),
        Hindrance(1, "Delicate -- -2 to damage resistance total"),
    ],
    special_abilities=[
        EnhancedSense(1, "Sight -- +2 to sight-based totals"),
        Longevity(1),
        SkillBonus(1, "Stealth -- +1 to hide, stealth, and tracking totals"),
    ],
    # :Strength Damage: 1D
    move=10,
    fate_points=0,
    character_points=2,
    # :Body Points: 17
)
characters = [ 
    elf, 
]


if __name__ == "__main__":
    app = build_app(characters)
    app()


__test__ = {
    
    "placeholder": ">>> pass\n\n"
    
}
