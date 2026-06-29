"""
Extract Spells from ``unique_potions.ipynb``.
Created by V2025.6.27.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

With "test" argument, runs doctest, which uses the __test__ examples.

"""

from opend6_tools.magic import *



heroism = Item(
    name="Heroism",
    type="Potion",
    effect=CompositeEffect(
        "Heroism Potion",
        SpecialAbilityEffect("Endurance", 3),
        SpecialAbilityEffect("Combat Sense", 3),
    ),
    other_aspects={
        'charges': ChargesAspect(1),
    },
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
        Limitation(LimitationType.burn_out, 1, "Shelf-life of 4D6 days"),
        ArcaneKnowledgeAspect("Controller: Hildeþrymm"),
    ],
    price="D (100G)"
)

giant_strength = Item(
    name="Giant Strength",
    type="Potion",
    effect=SpecialAbilityEffect("Increase Attribute: Physique", 3),
    other_aspects={
        'charges': ChargesAspect(1),
    },
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
        Limitation(LimitationType.burn_out, 1, "Shelf-life of 4D6 days"),
        ArcaneKnowledgeAspect("Controller: Folme"),
    ],
    price="D (50G)"
)

healing = Item(
    name="Healing",
    type="Potion",
    effect=SpecialAbilityEffect("Accelerated Healing", 2),
    other_aspects={
        'charges': ChargesAspect(1),
    },
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
        Limitation(LimitationType.burn_out, 1, "Shelf-life of 4D6 days"),
        ArcaneKnowledgeAspect("Controller: Folme"),
    ],
    price="D (50G)"
)

invulnerability = Item(
    name="Invulnerability",
    type="Potion",
    effect=CompositeEffect(
        "Invulnerability",
        SpecialAbilityEffect("Hardiness", 3),
        SpecialAbilityEffect("Immunity", 3),
    ),
    other_aspects={
        'charges': ChargesAspect(1),
    },
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
        Limitation(LimitationType.burn_out, 1, "Shelf-life of 4D6 days"),
        ArcaneKnowledgeAspect("Controller: Folme"),
    ],
    price="D (50G)"
)

weakness = Item(
    name="Weakness",
    type="Potion",
    effect=DisadvantageEffect("Hindrance", 3),
    other_aspects={
        'charges': ChargesAspect(1),
    },
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
        Limitation(LimitationType.burn_out, 1, "Shelf-life of 4D6 days"),
        ArcaneKnowledgeAspect("Controller: Folme"),
    ],
    price="M (25G)"
)
items = [ 
    heroism, giant_strength, healing, invulnerability, weakness, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(items)
    app()

