"""
Item from OpenD6 Fantasy Locations
"""
from textwrap import dedent
from opend6_tools.magic2 import *

sun_mirror = Item(
    name="Mirror of the Highest Sun",
    effect=SpecialAbilityEffect(SpecialAbilityType.uncanny_aptitude, 4),
    other_aspects={
        "disdvantage": Limitation(DisadvantageType.burn_out, 1)
    },
    notes=dedent("""\
        These holy items are highly polished metal, made more
        reflective than any conventional means by the abbey's secret
        process. Although it does not seem to have any miraculous
        abilities of its own, it can augment other effects that rely on
        light or the sun. Thus vampires find light reflected by this
        mirror even more unbearable, illusions using it as a component
        are more effective, and so on
    """),
    price="VD (100 G)"
)

# These holy items are highly polished metal, made more
# reflective than any conventional means by the abbey's secret
# process. Although it does not seem to have any miraculous
# abilities of its own, it can augment other effects that rely on
# light or the sun. Thus vampires find light reflected by this
# mirror even more unbearable, illusions using it as a component
# are more effective, and so on
#
# **Mirror of the Highest Sun**:
# effect: (Uncanny Aptitude (R4),
# +4 to all totals utilizing or requiring sunlight; Burn-out (R1),
# can be lost or stolen). Price: VD (100 G).


items = [
    sun_mirror,
]


__test__ = {
    "sun_mirror": ">>> sun_mirror.difficulty\n18",
}

if __name__ == "__main__":
    app = build_app(items)
    app()
