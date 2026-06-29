"""
Extract Spells from ``fantasy_holy_items.ipynb``.
Created by V2025.6.27.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

With "test" argument, runs doctest, which uses the __test__ examples.

"""

from opend6_tools.magic import *



warding_symbol = Item(
    name = "Warding Holy Symbol",
    notes = "Shaped from metal or wood in a sacred representation, this item helps the user turn away undead creatures",
    effect = SpecialAbilityEffect(SpecialAbilityType.skill_bonus, 1, "+3 to intimidation totals",
        modifications=[
            Limitation(LimitationType.ability_loss, 1, "only works on undead beings"),
            Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
        ]
    ),
    type="Symbol",
    price="VD (20 G)"
)

blessed_water = Item(
    name="Blessed Water or Herbs",
    notes="Sprinkled on the opponent, this causes harm only to those with evil in their hearts (Natural Magick (R10): Harm to Evil)",
    effect=DamageEffect(5*D, "physical damage"),
    range=RangeAspect("10m"),
    duration=DurationAspect("2.5sec"),
    casting_time=CastingTimeAspect("1.5sec"),
    other_aspects={
        "components": ComponentsAspect("blessed water or herbs", "rare"),
    },
    other_conditions=[
        GenericAspect(-2, "Against Evil Only"),
        Limitation(LimitationType.burn_out, 2, "one-time use")
    ],
    type="Weapon",
    price="VD (50 G)"
)
items = [ 
    warding_symbol, blessed_water, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(items)
    app()

