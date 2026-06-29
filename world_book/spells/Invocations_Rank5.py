"""
Extract Spells from ``invocations.ipynb rank 5 invocations``.
Created by V2025.12.8.dev2 of ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

"""

from opend6_tools.magic2 import *



location_object = Miracle(
    name="Locate Object",  # R2
    skill="Divination",
    notes="The people touched by the priest will have an enhanced search skill within a small 20 m radius area.",
    effect=SkillEffect("search", 1*D),
    duration=DurationAspect("15 min"),
    range=RangeAspect("touch"),
    speed=SpeedAspect.based_on(("range",), ""),
    casting_time=CastingTimeAspect("2 rounds"),
    other_aspects = {
        "area_effect": AreaEffectAspect("20 meter radius circle")
    }
)

reveal_cure = Miracle(
    name="Cure for illness",  # R2
    skill="Divination",
    notes="The priest will understand the needed cure for an injury, including internal complications. This reveals poisons as well as broken hearts.",
    effect=CompositeEffect(
        "Understand cure",
        SpecialAbilityEffect("Enhanced Sense: Internals", 3),
        SkillEffect("Healing", 3*D),
    ),
    duration=DurationAspect("30 min"),
    range=RangeAspect("touch"),
    speed=SpeedAspect.based_on(("range",), ""),
    casting_time=CastingTimeAspect("2 rounds"),
)

expiration = Miracle(
    name="Expiration",
    skill="Strife",
    notes="The priest can remove any inspiration, reducing physique and charima from a group gathered together in a tight circle.",
    effect=CompositeEffect(
        "Inspiration",
        SkillEffect("decrease Charisma mettle", 1*D, "skill modifier"),
        SkillEffect("decrease Physique stamina", 1*D, "skill modifier"),
        SkillEffect("decrease Extranormal favor", 1*D, "skill modifier"),
        AttributeEffect("decrease Charisma", 1*D),
        AttributeEffect("decrease Physique", 1*D),
    ),
    duration=DurationAspect("10 min"),
    range=RangeAspect("10 m"),
    speed=SpeedAspect.based_on(("range",), ""),
    casting_time=CastingTimeAspect("1 min"),
    other_aspects = {
        "area_effect": AreaEffectAspect("5 meter radius circle")
    }
)
invocations = [ 
    location_object, reveal_cure, expiration, 
]

__test__ = {

    'location_object': '>>> -2 <= location_object.difficulty - 25 < +3\nTrue\n',

    'reveal_cure': '>>> -2 <= reveal_cure.difficulty - 25 < +3\nTrue\n',

    'expiration': '>>> -2 <= expiration.difficulty - 25 < +3\nTrue\n',

}

if __name__ == "__main__":
    app = build_app(invocations)
    app()

