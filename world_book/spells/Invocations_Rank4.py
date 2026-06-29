"""
Extract Spells from ``invocations.ipynb rank 4 invocations``.
Created by V2025.12.8.dev2 of ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

"""

from opend6_tools.magic2 import *



enemy_intent = Miracle(
    name="Intent of Enemy",  # R1
    skill="Divination",
    notes="The priest will understand the intent of an enemy through a brief psionic conversation. This will be well-known to any antagonist, but ignored by neutral or friendly individuals.",
    effect=SkillEffect("limited psychic communication", 3*D),
    duration=DurationAspect("2.5 min"),
    range=RangeAspect("100 m"),
    speed=SpeedAspect.based_on(("range",), ""),
    casting_time=CastingTimeAspect("1 round"),
    other_conditions=[
        GenericAspect(1, "Only their intent"),
        GenericAspect(1, "Only if they're antagonistic"),
    ],
)

inspiration = Miracle(
    name="Inspiration",
    skill="Favor",
    notes="The priest can inspire a group gathered together in a tight circle.",
    effect=CompositeEffect(
        "Inspiration",
        SkillEffect("increase Charisma mettle", 2*D, "skill modifier"),
        SkillEffect("increase Physique stamina", 2*D, "skill modifier"),
        SkillEffect("increase Extranormal favor", 1*D, "skill modifier"),
        AttributeEffect("increase Charisma", 1*D),
        AttributeEffect("increase Physique", 1*D),
    ),
    duration=DurationAspect("10 min"),
    range=RangeAspect("self"),
    speed=SpeedAspect.based_on(("range",), ""),
    casting_time=CastingTimeAspect("1 min"),
    other_aspects = {
        "area_effect": AreaEffectAspect("5 meter radius circle")
    }
)
invocations = [ 
    enemy_intent, inspiration, 
]

__test__ = {

    'enemy_intent': '>>> enemy_intent.difficulty\n17\n',

    'inspiration': '>>> -2 <= inspiration.difficulty - 20 < +3\nTrue\n',

}

if __name__ == "__main__":
    app = build_app(invocations)
    app()

