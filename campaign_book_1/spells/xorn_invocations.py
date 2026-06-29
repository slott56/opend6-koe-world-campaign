"""
Extract Spells from ``xorn_invocations.ipynb``.
Created by V2025.6.27.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

With "test" argument, runs doctest, which uses the __test__ examples.

"""

from opend6_tools.magic import *



base_invocation = Miracle(
    name="Invocation of the Jackal",
    effect=SkillEffect(0*D+2, "Combat"),
    duration=DurationAspect("1 hr"),
    range=RangeAspect("10m"),
    speed=SpeedAspect.based_on('range'),
    casting_time=CastingTimeAspect("10 min"),
    other_aspects={
        'area_effect': AreaEffectAspect('20m radius circle'),
        "incantation": IncantationsAspect("Be the Jackal", "litany"),
        "gestures": GesturesAspect("Jackal Dance", "complex"),
        "concentration": ConcentrationAspect.based_on('casting_time'),
        "components": ComponentsAspect("Holy Symbols: ritual beads", "rare"),
        "community": CommunityAspect("2 helpers", "difficulty_13_action"),
    },
)

praise_invocation = Miracle(
    name="Praise the Jackal",
    effect=AttributeEffect(2*D, "Physique"),
    duration=DurationAspect("10 min"),
    range=RangeAspect("touch"),
    speed=SpeedAspect.based_on('range'),
    casting_time=CastingTimeAspect("1 round"),
    other_aspects={
        "multiple_targets": MultipleTargetAspect("2 targets"),
        "incantation": IncantationsAspect("Fight like the Jackal", "litany"),
        # "concentration": ConcentrationAspect.based_on('casting_time'),
        "components": ComponentsAspect("Holy Symbols: ritual beads", "rare"),
        # "gestures": GesturesAspect("Jackal Dance", "complex"),
        # "community": CommunityAspect("2 helpers", "difficulty_13_action"),
    },
)

communion_invocation = Miracle(
    name="One with the Jackal",
    effect=AttributeEffect(1*D, "Charisma"),
    duration=DurationAspect("20 min"),
    range=RangeAspect("touch"),
    speed=SpeedAspect.based_on('range'),
    casting_time=CastingTimeAspect("1 round"),
    other_aspects={
        "multiple_targets": MultipleTargetAspect("2 targets"),
        "incantation": IncantationsAspect("Bark like the Jackal", "litany"),
        # "concentration": ConcentrationAspect.based_on('casting_time'),
        "components": ComponentsAspect("Holy Symbols: ritual beads", "rare"),
        # "gestures": GesturesAspect("Jackal Dance", "complex"),
        # "community": CommunityAspect("2 helpers", "difficulty_13_action"),
    },
)

intercession_invocation = Miracle(
    name="Intercession of the Jackal",
    effect=SpecialAbilityEffect(SpecialAbilityType.luck_good, 3),
    duration=DurationAspect("20 min"),
    range=RangeAspect("touch"),
    speed=SpeedAspect.based_on('range'),
    casting_time=CastingTimeAspect("1 round"),
    other_aspects={
        "area_effect": AreaEffectAspect("3m radius circle"),
        "incantation": IncantationsAspect("Live like the Jackal", "litany"),
        # "concentration": ConcentrationAspect.based_on('casting_time'),
        "components": ComponentsAspect("Holy Symbols: ritual beads", "rare"),
        # "gestures": GesturesAspect("Jackal Dance", "complex"),
        # "community": CommunityAspect("2 helpers", "difficulty_13_action"),
    },
)
spells = [ 
    base_invocation, praise_invocation, communion_invocation, intercession_invocation, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(spells)
    app()

