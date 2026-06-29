"""
Extract Characters from ``old_keep_creatures.ipynb``.
Created by V2026.5.7.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



poisonous_cavesnake = Creature(
    name="Watersnake",
    description="A human-size -- 2m long -- snake, starkly white, with bulbs instead of eyes, and a long tongue",
    agility=Agility(2 * D),
    coordination=Coordination(2 * D),
    physique=Physique(1 * D,
                      {'stamina': 1 * D, 'swimming': 3*D}),
    intellect=Intellect(1 * D),
    acumen=Acumen(3 * D, {"search": D, "survival": D}),
    charisma=Charisma(1 * D, {'intimidation': 2 * D}),
    advantages=[
    ],
    disadvantages=[
        AchillesHeel(3, "Vulnerability to Fire, takes double damage"),
    ],
    special_abilities=[
        EnhancedSense(3, "Hearing; +1D for all search"),
        NaturalHandWeapon(3, "Sleep venom in fangs: 3D stun-only damage"),
    ],
    natural_abilities=[
        NaturalAbility("Swimming"),
    ],
    realm="dark cold and mist",
)
characters = [ 
    poisonous_cavesnake, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

