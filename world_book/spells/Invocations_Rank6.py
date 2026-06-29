"""
Extract Spells from ``invocations.ipynb rank 6 invocations``.
Created by V2025.12.8.dev2 of ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

"""

from opend6_tools.magic2 import *



weather = Miracle(
    name="Future Weather",  # R1
    skill="Divination",
    notes="The priest will be able to predict the weather for a spot up to 1 km away in detail.",
    effect=SpecialAbilityEffect("Enhanced Sense: Weather", 2),
    duration=DurationAspect("1 hr"),
    range=RangeAspect("1 km"),
    speed=SpeedAspect.based_on(("range",), ""),
    casting_time=CastingTimeAspect("2 rounds"),
)

manifestation = Miracle(
    name="Manifestation", #  2 * resistance (2-7) = R4-14
    skill="Favor",
    notes="The priest begs one of the temple dieties to open the veil and reveal themselves.",
    effect=CompositeEffect(
        "Veil Opening",
        Effect("Apportation to new realm (R4)", 40),
        Effect("Adjustments for experience, knowledge, and aids", 20),
    ),
    duration=DurationAspect("2 min"),
    range=RangeAspect("self"),
    speed=SpeedAspect.based_on(("range",), ""),
    casting_time=CastingTimeAspect("1 min"),
)

reanimation = Miracle(
    name="Reanimation", #  R4+ |
    skill="Favor",
    notes="The priest can reanimate someone for about an hour. The 18D can be used for all attributes to recover them (almost) fully. Skills will be lost, and the duration is only an hour.",
    effect=Effect("Temperamental Conjuration of 18D human.", 18*3),
    duration=DurationAspect("1 hr"),
    range=RangeAspect("touch"),
    speed=SpeedAspect.based_on(("range",), ""),
    casting_time=CastingTimeAspect("1 min"),
)
invocations = [ 
    weather, manifestation, reanimation, 
]

__test__ = {

    'weather': '>>> -2 <= weather.difficulty - 30 < +3\nTrue\n',

    'manifestation': '>>> -2 <= manifestation.difficulty - 30 < +3\nTrue\n',

    'reanimation': '>>> -2 <= reanimation.difficulty - 30 < +3\nTrue\n',

}

if __name__ == "__main__":
    app = build_app(invocations)
    app()

