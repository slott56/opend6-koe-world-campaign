"""
Extract Spells from ``xorn_spells.ipynb``.
Created by V2025.6.27.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

With "test" argument, runs doctest, which uses the __test__ examples.

"""

from opend6_tools.magic import *



demon_fire = Spell(
    name="Demon Fire",
    effect=DamageEffect(2*D, "fire-based", "ignore all armor"),
    duration=DurationAspect("1 sec"),
    range=RangeAspect("20m"),
    speed=SpeedAspect.based_on('range'),
    casting_time=CastingTimeAspect("1 round"),
    other_aspects={
        "incantation": IncantationsAspect("Demon Fire", "litany"),
        "concentration": ConcentrationAspect(measure="1 rounds"),
    },
)

demon_shield = Spell(
    name="Demon Shield",
    effect=ProtectionEffect(2*D, "protection_modifier", "A wall of fire-like shimmer"),
    duration=DurationAspect("1 min"),
    range=RangeAspect("8m"),
    speed=SpeedAspect.based_on('range'),
    casting_time=CastingTimeAspect("1 round"),
    other_aspects={
        'area_effect': AreaEffectAspect('2m radius sphere'),
        "incantation": IncantationsAspect("Demon Shield Chant", "litany"),
        "concentration": ConcentrationAspect(measure="1 rounds"),
    }
)

dispel = Spell(
    name="Demonic Cleansing",
    effect=SkillEffect("Boost Charisma/intimidation", 4*D, "break concentration"),
    duration=DurationAspect("2 rounds"),
    range=RangeAspect("8m"),
    speed=SpeedAspect.based_on('range'),
    casting_time=CastingTimeAspect("1 round"),
    other_aspects={
        'area_effect': AreaEffectAspect('2m radius sphere'),
        "incantation": IncantationsAspect("Mage Intimidation Chant", "litany"),
        "concentration": ConcentrationAspect(measure="2 rounds"),
    }
)

detect = Spell(
    name="Demon Detection",
    effect=SpecialAbilityEffect(
        SpecialAbilityType.enhanced_sense, 3,
    ),
    duration=DurationAspect("2 min"),
    range=RangeAspect("20m"),
    speed=SpeedAspect.based_on('range'),
    casting_time=CastingTimeAspect("2 rounds"),
    other_aspects={
        "incantation": IncantationsAspect("Demon-detection", "litany"),
        "concentration": ConcentrationAspect(measure="2 rounds"),
    },
)

demon_wings = Spell(
    name="Demon Wings",
    effect=SpecialAbilityEffect(
        SpecialAbilityType.flight, 2
    ),
    duration=DurationAspect("5 min"),
    range=RangeAspect("self"),
    speed=SpeedAspect.based_on('range'),
    casting_time=CastingTimeAspect("3 rounds"),
    other_aspects={
        "incantation": IncantationsAspect("Winds of Flight Chant", "litany"),
        "concentration": ConcentrationAspect(measure="3 rounds"),
    },
)

open_veil = Spell(
    name = "Opening the Veil",
    skill = "Apportation",
    notes="Opens the veil; it can be held open for up to 5 min. to allow one Hordling pass through. Each minute has a 1/6 chance of one appearing: roll 5D, one for each minute of duration; at the first 1, a Hordling appears and the veil closes.",
    effect=CompositeEffect(
        "Veil Opening",
       GenericEffect("Apportation to new realm (R4)", 40),
        GenericEffect("Adjustments for experience, knowledge, and aids", 20),
    ),
    duration=DurationAspect(measure="5 min"),
    range=RangeAspect(measure="touch"),
    casting_time=CastingTimeAspect(measure="5 s"),
    speed=SpeedAspect.based_on(("range",), ""),
    other_aspects={
        "incantation": IncantationsAspect("Veil Opening Chant", "litany"),
        "concentration": ConcentrationAspect(measure="5 s"),
        "components": ComponentsAspect("proper resonating artifacts", "rare"),
    },
)
spells = [ 
    demon_fire, demon_shield, dispel, detect, demon_wings, open_veil, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(spells)
    app()

