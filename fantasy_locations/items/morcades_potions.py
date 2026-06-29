"""
Items from OpenD6 Fantasy Locations
"""
from textwrap import dedent
from opend6_tools.magic2 import *

charm = Item(
    name="Charm",
    effect=SkillEffect(4 * D, "bonus to charm skill"),
    other_conditions=[
        Limitation(DisadvantageType.burn_out, 1, note="can be lost or stolen"),
        OtherAlterant(-2, "acrid taste and a strong odor: Easy mettle or stamina to detect")
    ],
    price="M (5 G)",
    notes=dedent("""\
        This potion improves the attractiveness of a
        person for one day ( +4D to charm skill), but it requires that
        the user to ingest the liquid. Since the clear fluid has an
        acrid taste and a strong odor, imbibing it's a challenge (Easy
        mettle or stamina attempt). Mixing it with a substance that
        covers the flavor and smell reduces the difficulty.
    """)
)

# **Charm**: This potion improves the attractiveness of a
# person for one day ( +4D to charm skill), but it requires that
# the user to ingest the liquid. Since the clear fluid has an
# acrid taste and a strong odor, imbibing it's a challenge (Easy
# mettle or stamina attempt). Mixing it with a substance that
# covers the flavor and smell reduces the difficulty.

wretchedness = Item(
    name="Water of Wretchedness",
    effect=DisadvantageEffect(DisadvantageType.bad_luck, 3),
    other_conditions=[
        Limitation(DisadvantageType.burn_out, 1, note="can be lost or stolen"),
        OtherAlterant(-2, "offensive odor: Easy mettle or stamina to detect")
    ],
    price="M (5 G)",
    notes=dedent("""\
        A thick, syrupy substance that possesses an offensive
        odor. Once this potion has been consumed, the target
        suffers Bad Luck (R3). If the potion is mixed with another
        liquid or poured over food, the effect is reduced to Bad •
        Luck (R2), as the potency is decreased. Coaxing or fooling a victim into consuming the liquid is at a +S to the
        interaction attempt.
    """)
)

# **Water of Wretchedness**: The Water of Wretchedness
# is a thick, syrupy substance that possesses an offensive
# odor. Once this potion has been consumed, the target
# suffers Bad Luck (R3). If the potion is mixed with another
# liquid or poured over food, the effect is reduced to Bad •
# Luck (R2), as the potency is decreased. Coaxing or fooling a victim into consuming the liquid is at a +S to the
# interaction attempt.


items = [
    charm,
    wretchedness,
]

__test__ = {
    "charm": ">>> charm.difficulty\n7",
    "wretchedness": ">>> wretchedness.difficulty\n5",
}

if __name__ == "__main__":
    app = build_app(items)
    app()
