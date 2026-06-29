"""
Extract Spells from ``invocations.ipynb rank 2 invocations``.
Created by V2025.12.8.dev2 of ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

"""

from opend6_tools.magic2 import *



reveal_secrets = Miracle(
    name="Reveal Secrets",  # R1
    skill="Divination",
    notes="The priest will be understand a closely-held secret from another individual during a brief psionic interrogation. The process isn't obvious to most people. A weak result roll below 3 for link or effect allows a mettle roll to understand the query.",
    effect=SkillEffect("limited psychic communication", 2*D),
    duration=DurationAspect("2.5 min"),
    range=RangeAspect("10 m"),
    speed=SpeedAspect.based_on(("range",), ""),
    casting_time=CastingTimeAspect("2 rounds"),
)

protect_magic = Miracle(
    name="Protect from Magic", #  R1 |
    skill="Favor",
    notes="The priest reduce the effect of magic by 4D for everyone they touch during the invocation.",
    effect=ProtectionEffect("Reduce effect (after a link)", "4D"),
    duration=DurationAspect("10 min"),
    range=RangeAspect("touch"),
    speed=SpeedAspect.based_on(("range",), ""),
    casting_time=CastingTimeAspect("2 rounds"),
)

protect_danger = Miracle(
    name="Protect from Danger", #  R3 |
    skill="Favor",
    notes="The priest increases Acumen by 3D, permitting everyone they touch during the invocation to avoid danger.",
    effect=AttributeEffect("increase Acumen", 3*D),
    duration=DurationAspect("1 hr"),
    range=RangeAspect("touch"),
    speed=SpeedAspect.based_on(("range",), ""),
    casting_time=CastingTimeAspect("2 rounds"),
)

aid_combat = Miracle(
    name="Aid in Combat", #  R1 |
    skill="Favor",
    notes="The priest increases fighting skill of everyone they touch during the invocation.",
    effect=SkillEffect("increase fighting skill", 3*D),
    duration=DurationAspect("1 hr"),
    range=RangeAspect("touch"),
    speed=SpeedAspect.based_on(("range",), ""),
    casting_time=CastingTimeAspect("2 rounds"),
)

aid_magic = Miracle(
    name="Aid in Magic", #  R4 |
    skill="Favor",
    notes="The priest increases a Extranormal skill of everyone they touch during the invocation.",
    effect=SkillEffect("increase Extranormal attribute", 2*D+2),
    duration=DurationAspect("30 min"),
    range=RangeAspect("touch"),
    speed=SpeedAspect.based_on(("range",), ""),
    casting_time=CastingTimeAspect("1 rounds"),
)

focus_magic = Miracle(
    name="Focus Magic on target", #  R1 |
    skill="Strife",
    notes="The priest can will remove any protection from magic, making the person they touch a target.",
    effect=ProtectionEffect("Increase effect (after a link)", "4D"),
    duration=DurationAspect("10 min"),
    range=RangeAspect("touch"),
    speed=SpeedAspect.based_on(("range",), ""),
    casting_time=CastingTimeAspect("2 rounds"),
)

focus_danger = Miracle(
    name="Expose Danger to target", #  R3 |
    skill="Strife",
    notes="The priest can will remove any protection from danger, reducing the Acumen of the person they touch.",
    effect=AttributeEffect("decrease Acumen", 3*D),
    duration=DurationAspect("1 hr"),
    range=RangeAspect("touch"),
    speed=SpeedAspect.based_on(("range",), ""),
    casting_time=CastingTimeAspect("2 rounds"),
)

weaken_combat = Miracle(
    name="Weaken in Combat", #  R1 |
    skill="Strife",
    notes="The priest can will remove any combat aid, reducing the fighting skill of the person they touch.",
    effect=SkillEffect("decrease fighting skill", 3*D),
    duration=DurationAspect("1 hr"),
    range=RangeAspect("touch"),
    speed=SpeedAspect.based_on(("range",), ""),
    casting_time=CastingTimeAspect("1 rounds"),
)

weaken_magic = Miracle(
    name="Weaken in Magic", #  R4 |
    skill="Strife",
    notes="The priest can will remove any magic or extranormal aid, reducing the magic skill of the person they touch.",
    effect=SkillEffect("increase Extranormal attribute", 2*D+2),
    duration=DurationAspect("30 min"),
    range=RangeAspect("touch"),
    speed=SpeedAspect.based_on(("range",), ""),
    casting_time=CastingTimeAspect("1 rounds"),
)
invocations = [ 
    reveal_secrets, protect_magic, protect_danger, aid_combat, aid_magic, focus_magic, focus_danger, weaken_combat, weaken_magic, 
]

__test__ = {

    'reveal_secrets': '>>> -2 <= reveal_secrets.difficulty - 10 < +3\nTrue\n',

    'protect_magic': '>>> -2 <= protect_magic.difficulty - 10 < +3\nTrue\n',

    'protect_danger': '>>> -2 <= protect_danger.difficulty - 10 < +3\nTrue\n',

    'aid_combat': '>>> -2 <= aid_combat.difficulty - 10 < +3\nTrue\n',

    'aid_magic': '>>> -2 <= aid_magic.difficulty - 10 < +3\nTrue\n',

    'focus_magic': '>>> -2 <= focus_magic.difficulty - 10 < +3\nTrue\n',

    'focus_danger': '>>> -2 <= focus_danger.difficulty - 10 < +3\nTrue\n',

    'weaken_combat': '>>> -2 <= weaken_combat.difficulty - 10 < +3\nTrue\n',

    'weaken_magic': '>>> -2 <= weaken_magic.difficulty - 10 < +3\nTrue\n',

}

if __name__ == "__main__":
    app = build_app(invocations)
    app()

