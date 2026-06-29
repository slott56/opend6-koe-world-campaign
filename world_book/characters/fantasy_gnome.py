"""
Extract Characters from ``fantasy_gnome.ipynb``.
Created by V2025.12.8.dev5 of ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



gnome = Character(
    agility=Agility(3*D, {'fighting': 3*D+1}),
    coordination=Coordination(2*D, {'lockpicking': 2*D+2}),
    physique=Physique(3*D, {'lifting': 3*D+1}),
    intellect=Intellect (3*D, {'devices': 4 * D, 'speaking': 3*D+1, 'trading': 3 * D + 1, 'traps': 3 * D + 2}),
    acumen=Acumen (3*D, {'artist': 3 * D + 2, 'crafting': 4 * D,
                         'know-how': 3 * D + 1}),
    charisma=Charisma (2*D+2, {'persuasion': 3 * D}),
    extranormal=Magic(D, {"alteration": D+1}),
    advantages=[
        Size(1, "Small -- scale value of 3"),
    ],
    disadvantages=[
        Hindrance(1, "Shorter Stride -- 2-meter reduction to running, swimming, and jumping Move"),
    ],
    special_abilities=[
        SkillBonus(1, "Mechanical Aptitude -- +1 to crafting, devices, and traps totals"),
    ],
    # :Strength Damage: 2D
    move=8,
    fate_points=0,
    character_points=2,
    # :Body Points: 18
)
characters = [ 
    gnome, 
]


if __name__ == "__main__":
    app = build_app(characters)
    app()


__test__ = {
    
    "placeholder": ">>> pass\n\n"
    
}
