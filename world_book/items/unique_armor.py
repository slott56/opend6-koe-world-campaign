"""
Extract Spells from ``unique_armor.ipynb``.
Created by V2025.6.27.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

With "test" argument, runs doctest, which uses the __test__ examples.

"""

from opend6_tools.magic import *



crown_of_Agility = Item(
    type="Crown", name="Crown of Agility",
    effect=CompositeEffect(
        "Agility",
        SpecialAbilityEffect("Fast Reactions", 1),
        AttributeEffect("Agility", 3*D),
    ),
    other_conditions=[Limitation(LimitationType.burn_out, 1, "can be lost or stolen")])

crown_of_Visions = Item(
    type="Crown", name="Crown of Visions",
    effect=CompositeEffect(
        "Battle Sense",
        SpecialAbilityEffect("Combat Sense", 1, "suprise -2"),
        SpecialAbilityEffect("Extra Sense: Opponent's Intent", 2, "+2D to predict tactics"),
    ),
    other_conditions=[Limitation(LimitationType.burn_out, 1, "can be lost or stolen")])

crown_of_Protection = Item(
    type="Crown", name="Helm of Protection",
    effect=SpecialAbilityEffect("Hardiness", 4, "+4 damage resistance"),
    other_conditions=[Limitation(LimitationType.burn_out, 1, "can be lost or stolen")])

crown_of_Strength = Item(
    type="Crown", name="Crown of Strength",
    effect=AttributeEffect("Physique", 4*D),
    other_conditions=[Limitation(LimitationType.burn_out, 1, "can be lost or stolen")])

crown_of_Immunity = Item(
    type="Crown", name="Cap of Immunity",
    effect=SpecialAbilityEffect("Immunity", 3, "+3D physique or stamina checks against poisons or diseases"),
    other_conditions=[Limitation(LimitationType.burn_out, 1, "can be lost or stolen")])

crown_of_Victory = Item(
    type="Crown", name="Crown of Victory",
    effect=DisadvantageEffect("BadLuck", 3),
    other_conditions=[Limitation(LimitationType.burn_out, 1, "can be lost or stolen")],
    notes="This is a terrible artifact to have, but it looks wonderful"
)
items = [ 
    crown_of_Agility, crown_of_Visions, crown_of_Protection, crown_of_Strength, crown_of_Immunity, crown_of_Victory, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(items)
    app()

