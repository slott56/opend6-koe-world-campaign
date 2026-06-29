"""
Extract Spells from ``keep_lodge_items.ipynb``.
Created by V2025.6.27.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

With "test" argument, runs doctest, which uses the __test__ examples.

"""

from opend6_tools.magic import *



shield_of_strength = Item(
    type="Shield", name="Shield of Strength",
    notes="An older-style round shield with a surprisingly shiny boss in the center; it always looks brand-new.",
    effect=SpecialAbilityEffect(SpecialAbilityType.attack_resistance, 2, "Physical and Extranormal"),
    other_conditions=[Limitation(LimitationType.burn_out, 1, "can be lost or stolen")])

fire_ring = Item(
    type="Ring", name="Ring of Fire Protection",
    effect=CompositeEffect(
        "defend from fire",
        SpecialAbilityEffect(SpecialAbilityType.attack_resistance, 2, "fire-based attacks"),
        SpecialAbilityEffect(SpecialAbilityType.environmental_resistance, 2, "heat"),
        SpecialAbilityEffect(SpecialAbilityType.atmospheric_tolerance, 2, "smoke"),
    )
)
items = [ 
    shield_of_strength, fire_ring, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(items)
    app()

