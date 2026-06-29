"""
Extract Characters from ``unique_sword_relics.ipynb``.
Created by V2026.3.11.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



stormhammer = Sword(
    name="Stormhammer",
    race='sword',
    description='An old, well-made, but heavy bronze sword, decorated with runes in an unknown language',
    intellect=Intellect(3 * D, {"speaking": 1 * D}),
    agility=Agility(2 * D),
    acumen=Acumen(2*D),
    charisma=Charisma(2*D, {"persuasion": 2*D}),
    coordination=Coordination(0*D),
    physique=Physique(3*D, {"lifting": 2*D}),
    extranormal=Magic(3*D, {"divination": 1}),
    disadvantages=[
        Hindrance(R3, "A sword; immobile without a wielder"),
    ],
    special_abilities=[
        SpecialAbility(R5, "Lighting Strike Enchantment")
    ],
    natural_abilities=[
        NaturalHandWeapon(2*D+2, "damage")
    ],
    move=0,
    funds=0*D,
    body=2*D,
    personality='Stormhammer is one of a pair of ancient swords, passed down from a forgotten empire. It seeks the other sword, forcing whomever carries it on paths too dark and lonely to imagine.'
)

foeseeker = Sword(
    name="Foeseeker",
    race='sword',
    description='An old, well-made, but heavy bronze sword, decorated with runes in an unknown language',
    intellect=Intellect(3 * D, {"speaking": 1 * D}),
    agility=Agility(2 * D),
    acumen=Acumen(2*D),
    charisma=Charisma(2*D, {"persuasion": 2*D}),
    coordination=Coordination(0*D),
    physique=Physique(3*D, {"lifting": 2*D}),
    extranormal=Magic(3*D, {"divination": 1}),
    disadvantages=[
        Hindrance(R3, "A sword; immobile without a wielder"),
    ],
    special_abilities=[
        SpecialAbility(3, "Search for enemies")
    ],
    natural_abilities=[
        NaturalHandWeapon(2*D+2, "damage")
    ],
    move=0,
    funds=0*D,
    body=2*D,
    personality='Foeseeker is one of a pair of ancient swords, passed down from a forgotten empire. It seeks the other sword, forcing whomever carries it on paths too dark and lonely to imagine.'
)
swords = [ 
    stormhammer, foeseeker, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(swords)
    app()

