"""
Extract Spells from ``old_keep_items.ipynb``.
Created by V2025.6.27.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

With "test" argument, runs doctest, which uses the __test__ examples.

"""

from opend6_tools.magic import *



wand_of_submission = Item(
    type="Wand", name="Wand of Submission",
    effect=AttributeEffect("boost wielder's intimidation/charisma", 5*D, "forces them to submit"),
    other_aspects={'charges': ChargesAspect(5)},
    other_conditions=[Limitation(LimitationType.burn_out, 1, "can be lost or stolen")]
)

wand_of_intention = Item(
    type="Wand", name="Wand of Intention",
    effect=CompositeEffect(
        "Understanding an enemy",
        AttributeEffect("boost wielder's acumen", 3 * D, "divine their intentions"),
        SpecialAbilityEffect(SpecialAbilityType.possession_limited, 3, "limited"),
    ),
    other_aspects={'charges': ChargesAspect(5)},
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen")]
)

knife_of_slaughter = Item(
    type="Weapon", name="Knife of Slaughter",
    notes="The knife is awkwardly large, not really built for human hands",
    effect = DamageEffect(2*D, "ignores magical armor"),
    other_conditions=[Limitation(LimitationType.burn_out, 1, "can be lost or stolen")]
)
items = [ 
    wand_of_submission, wand_of_intention, knife_of_slaughter, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(items)
    app()

