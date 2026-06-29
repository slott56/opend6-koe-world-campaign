"""
Items from OpenD6 Fantasy Locations
"""
from textwrap import dedent
from opend6_tools.magic2 import *

dragons_kiss = Item(
    name="Dragon's Kiss",
    effect=SkillEffect(2*D, "bonus to healing skill"),
    other_conditions=[
        Limitation(DisadvantageType.burn_out, 1, note="can be lost or stolen")
    ],
    price="M (5 G)",
    notes=dedent("""\
        Rubbing this pungent concoction upon wounds hastens
        the healing process.
        The mixture must be kept dry at all times; otherwise,
        its healing properties are lost. There's enough in one
        packet for two uses.
    """)
)

# **Dragon's Kiss** (Moderate price difficulty/5 gold):
# Rubbing this pungent concoction upon wounds hastens
# the healing process (+2 bonus to two healing totals).
# The mixture must be kept dry at all times; otherwise,
# its healing properties are lost. There's enough in one
# packet for two uses.

adrik_incense = Item(
    name="Adrik Incense",
    effect=AttributeEffect(2*D, "bonus to any Intellect skill"),
    other_conditions=[
        Limitation(DisadvantageType.burn_out, 1, note="can be lost or stolen")
    ],
    price="M (4 G)",
    notes=dedent("""\
        Burning this incense while performing any Intellect
        skill adds a +2 bonus to all related totals for one round
        Each stick of incense provides one use.
    """)
)

# **Adrik Incense** (Moderate price difficulty/4 gold):
# Burning this incense while performing any Intellect
# skill adds a +2 bonus to all related totals for one round
# Each stick of incense provides one use.

dried_lion_flower_tea = Item(
    name="Dried Lion Flower Tea",
    effect=SkillEffect(2*D, "bonus to any stamina skills"),
    other_conditions=[
        Limitation(DisadvantageType.burn_out, 1, note="can be lost or stolen")
    ],
    notes=dedent("""
        Brewing this tea and consuming adds 2 to stamina
        totals for two hours. The dry tea is sold in silk packs
        with enough for a single use.
    """),
    price="M (5 G)",
)

# **Dried Lion Flower Tea** (Moderate price difficulty/ 5
# gold): Brewing this tea and consuming adds 2 to stamina
# totals for two hours. The dry tea is sold in silk packs
# with enough for a single use.


items = [
    dragons_kiss,
    adrik_incense,
    dried_lion_flower_tea,
]

__test__ = {
    "dragons_kiss": ">>> dragons_kiss.difficulty\n3",
    "adrik_incense": ">>> adrik_incense.difficulty\n3",
    "dried_lion_flower_tea": ">>> dried_lion_flower_tea.difficulty\n3",
}

if __name__ == "__main__":
    app = build_app(items)
    app()
