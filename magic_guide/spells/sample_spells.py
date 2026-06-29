"""
sample_spells from *OpenD6 Magic Guidebook*, "Alternate Magic Systems".

When run as an app, generates .RST details of each Spell.
"""

from opend6_tools.magic2 import *


spells = [
    Spell(
        name="Blink-Away",
        skill="Apportation",
        notes="",
        effect=CompositeEffect(
            "Transport",
            DistanceEffect("Move you or something", "1 kilometer"),
            MassEffect("Up to 3 people", "600 kg"),
        ),
        duration=DurationAspect(measure="instantaneous"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={},
        other_conditions=[],
    ),
    Spell(
        name="Projectile",
        skill="Conjuration",
        notes="This 6D attack requires marksmanship/firearms or apportation to hit. It takes a form of the caster’s choosing, such as a blast of fire, water, or ice.",
        effect=DamageEffect("Projectile damage", "6D"),
        duration=DurationAspect(measure="instantaneous"),
        range=RangeAspect(measure="10 m"),
        casting_time=CastingTimeAspect(measure="1 second"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={},
        other_conditions=[],
    ),
    Spell(
        name="Protective Sheath",
        skill="Conjuration",
        notes="The caster or a target within one meter of the caster is coated in an invisible sheath that absorbs up to 6D of any type of damage.",
        effect=ProtectionEffect("Protect", "6D"),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 second"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={},
        other_conditions=[],
    ),
    Spell(
        name="Improvement",
        skill="Alteration",
        notes="",
        effect=SkillEffect(
            "Add to a skill, damage, or protection", "3D", "skill modifier"
        ),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={},
        other_conditions=[],
    ),
    Spell(
        name="Search",
        skill="Divination",
        notes="",
        effect=SkillEffect("search skill", "4D", "skill modifier"),
        duration=DurationAspect(measure="1 round"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "area_effect": AreaEffectAspect("10m radius divination sphere"),
        },
        other_conditions=[],
    ),
]


__test__ = {
    "Blink-Away": ">>> spells[0].difficulty\n13",
    "Projectile": ">>> spells[1].difficulty\n14",
    "Protective Sheath": ">>> spells[2].difficulty\n14",
    "Improvement": ">>> spells[3].difficulty\n10",
    "Search": ">>> spells[4].difficulty\n17",  # Book said 16.
}



if __name__ == "__main__":
    app = build_app(spells)
    app()
