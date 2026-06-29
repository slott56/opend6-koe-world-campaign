"""
Extract from Rank5 Workbook.ipynb.

When run as app with "detail" argument, generates .RST-formatted details of all the Spells.

When run as app with "debug" argument, writes debugging details for selected spells.
"""
from opend6_tools.magic2 import *


dirt_to_mud = Spell(
        name="Dirt to Mud",
        skill="Elemental Alteration",
        notes="The water must be located nearby; the mud starts to revert after 5 minutes, escape is difficult requiring patience and sometimes the help of a shovel or pry-bar",
        effect=DisadvantageEffect("Hindrance", 4, "mired in mud"),
        duration=DurationAspect(measure="5 min"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Earth and Water Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
            "area_of_effect": AreaEffectAspect("10m radius circle"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Hælan Coordination")
        ],
    )

reanimation_r4 = Spell(
    name = "Reanimate liche",
    skill = "Temperamental Conjuration",
    notes="Reanimates one normal human for 1 day",
    effect=Effect("Temperamental Conjuration of 1x25D human", 30),
    duration=DurationAspect(measure="1 day"),
    range=RangeAspect(measure="10 m"),
    casting_time=CastingTimeAspect(measure="5 s"),
    speed=SpeedAspect.based_on(("range",), ""),
    other_aspects={
        "concentration": ConcentrationAspect(measure="5 s"),
        "components": ComponentsAspect("a resonating artifact to help the balance", "very rare"),
        "incantation": IncantationsAspect("Conjuration Chant", "litany"),
    },
    other_conditions=[
        GenericAspect(difficulty=0, description="Controller: None"),
        GenericAspect(difficulty=3, description="All four elements present in the environment: fire, flowing water, wind, and loose earth."),
    ],
)
spells = [ 
    dirt_to_mud, reanimation_r4, 
]

__test__ = {
    "Dirt to Mud": ">>> spells[0].difficulty\n24",
    "Reanimate liche": ">>> spells[1].difficulty\n24",
}

if __name__ == "__main__":
    app = build_app(spells)
    app()

