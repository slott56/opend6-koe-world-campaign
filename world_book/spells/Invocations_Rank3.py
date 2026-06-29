"""
Extract Spells from ``invocations.ipynb rank 3 invocations``.
Created by V2025.12.8.dev2 of ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

"""

from opend6_tools.magic2 import *



location_self = Miracle(
    name="Location of Self",  # R1
    skill="Divination",
    notes="The priest will know their location well enough to navigate toward another known location for the next hour.",
    effect=SpecialAbilityEffect("Enhanced Sense: Location", 2),
    duration=DurationAspect("1 hour"),
    range=RangeAspect("self"),
    speed=SpeedAspect.based_on(("range",), ""),
    casting_time=CastingTimeAspect("2 rounds"),
)

reveal_piety = Miracle(
    name="Reveal Piety",  # R2
    skill="Divination",
    notes="The priest will be understand the piety levels of another individual; this will reveal their ability to perform invocations.",
    effect=SkillEffect("understand piety", 3*D),
    duration=DurationAspect("15 min"),
    range=RangeAspect("10 m"),
    speed=SpeedAspect.based_on(("range",), ""),
    casting_time=CastingTimeAspect("1 round"),
    other_conditions=[
        GenericAspect(-1, "Only their piety")
    ],
)

reveal_wound = Miracle(
    name="Nature of Wound",  # R1
    skill="Divination",
    notes="The priest will understand the nature of an injury, including internal complications. This reveals poisons as well as broken hearts.",
    effect=SpecialAbilityEffect("Enhanced Sense: Internals", 2),
    duration=DurationAspect("10 min"),
    range=RangeAspect("touch"),
    speed=SpeedAspect.based_on(("range",), ""),
    casting_time=CastingTimeAspect("2 rounds"),
)

forgive_sins = Miracle(
    name="Forgive Sins", # R2 |
    skill="Favor",
    notes="The priest will improve the piety by 4D of everyone they touch during the invocation.",
    effect=Effect("improve piety", 12),
    duration=DurationAspect("1 day"),
    range=RangeAspect("touch"),
    speed=SpeedAspect.based_on(("range",), ""),
    casting_time=CastingTimeAspect("2 rounds"),
)

protect_temptation = Miracle(
    name="Protect from Temptation", #  R2 |
    skill="Favor",
    notes="The priest reduces temptation to stray from their religion by 3D for everyone they touch during the invocation.",
    effect=SkillEffect("increase mettle", 3*D),
    duration=DurationAspect("1 day"),
    range=RangeAspect("touch"),
    speed=SpeedAspect.based_on(("range",), ""),
    casting_time=CastingTimeAspect("2 rounds"),
)

aid_duties = Miracle(
    name="Aid in Regular Duties", #  R1 |
    skill="Favor",
    notes="The priest increases any three attributes by 1D for everyone they touch during the invocation.",
    effect=SkillEffect("increase three attributes", 3*D),
    duration=DurationAspect("1 day"),
    range=RangeAspect("touch"),
    speed=SpeedAspect.based_on(("range",), ""),
    casting_time=CastingTimeAspect("2 rounds"),
)

focus_temptation = Miracle(
    name="Focus Temptation on target", #  R2 |
    skill="Strife",
    notes="The priest can will remove any protection from temptation, reducing the mettle of the person they touch.",
    effect=SkillEffect("decrease mettle", 3*D),
    duration=DurationAspect("1 day"),
    range=RangeAspect("touch"),
    speed=SpeedAspect.based_on(("range",), ""),
    casting_time=CastingTimeAspect("2 rounds"),
)

weaken_duties = Miracle(
    name="Weaken in Regular Duties", #  R1 |
    skill="Strife",
    notes="The priest can will reduce three attributes of the person they touch.",
    effect=SkillEffect("decrease three attributes", 3*D),
    duration=DurationAspect("1 day"),
    range=RangeAspect("touch"),
    speed=SpeedAspect.based_on(("range",), ""),
    casting_time=CastingTimeAspect("2 rounds"),
)
invocations = [ 
    location_self, reveal_piety, reveal_wound, forgive_sins, protect_temptation, aid_duties, focus_temptation, weaken_duties, 
]

__test__ = {

    'location_self': '>>> -2 <= location_self.difficulty - 15 < +3\nTrue\n',

    'reveal_piety': '>>> -2 <= reveal_piety.difficulty - 15 < +3\nTrue\n',

    'reveal_wound': '>>> -2 <= reveal_wound.difficulty - 15 < +3\nTrue\n',

    'forgive_sins': '>>> -2 <= forgive_sins.difficulty - 15 < +3\nTrue\n',

    'protect_temptation': '>>> -2 <= protect_temptation.difficulty - 15 < +3\nTrue\n',

    'aid_duties': '>>> -2 <= aid_duties.difficulty - 15 < +3\nTrue\n',

    'focus_temptation': '>>> -2 <= focus_temptation.difficulty - 15 < +3\nTrue\n',

    'weaken_duties': '>>> -2 <= weaken_duties.difficulty - 15 < +3\nTrue\n',

}

if __name__ == "__main__":
    app = build_app(invocations)
    app()
