"""
Extract Spells from ``Rank8 Workbook.ipynb``.
Created by V2025.12.6.dev3 of ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

"""

from opend6_tools.magic2 import *



astral_projection = Spell(
    name="Astral Projection",
    skill="Apportation and Psychic Communication",
    notes="Mage can see past the veil and use possession on an inhabitant. A mage can subsequently open the veil to bring the possessed creature through.",
    effect=CompositeEffect(
        "Possession and Apportation",
        Effect("Apportation to another realm (R1)", 10),
        SpecialAbilityEffect("Possession: Full", 1),
        Effect("Adjustments for experience, knowledge, and aids", 20),
    ),
    duration=DurationAspect(measure="15 min"),
    range=RangeAspect(measure="touch"),
    casting_time=CastingTimeAspect(measure="5 s"),
    speed=SpeedAspect.based_on(("range",), ""),
    other_aspects={
        "incantation": IncantationsAspect("Veil Closing Chant", "litany"),
        "concentration": ConcentrationAspect(measure="5 s"),
        "components": ComponentsAspect("any resonating artifacts", "rare"),
        "variable_duration": VariableDurationAspect("off-only"),
        "variable_effect": VariableEffectAspect("Can increase to R2 to transfer possessed inhabitant to this realm", 10),
    },
    other_conditions=[
        GenericAspect(difficulty=0, description="Controller: None"),
    ],
)

reanimation_r3 = Spell(
    name = "Reanimate group of humans",
    skill = "Temperamental Conjuration",
    notes="Reanimates one incomplete human or 3 feeble humans for 20 minutes.",
    effect=Effect("Temperamental Conjuration of 5x5D humans", 72),
    duration=DurationAspect(measure="20 min"),
    range=RangeAspect(measure="2 m"),
    casting_time=CastingTimeAspect(measure="5 s"),
    speed=SpeedAspect.based_on(("range",), ""),
    other_aspects={
        "concentration": ConcentrationAspect(measure="5 s"),
        "components": ComponentsAspect("a resonating artifact to help the balance", "very rare"),
        "feedback": FeedbackAspect(3),
        "focus": FocusedAspect.based_on(("effect", "duration")),
        "incantation": IncantationsAspect("Conjuration Chant", "litany"),
        "gestures": GesturesAspect("Controlling movements", "challenging"),
    },
    other_conditions=[
        GenericAspect(difficulty=0, description="Controller: None"),
        GenericAspect(difficulty=3, description="All four elements present in the environment: fire, flowing water, wind, and loose earth."),
    ],
)
spells = [ 
    astral_projection, reanimation_r3, 
]

__test__ = {
    "Astral Projection": ">>> spells[0].difficulty\n38",
    "Reanimate group of humans": ">>> spells[1].difficulty\n41",
}

if __name__ == "__main__":
    app = build_app(spells)
    app()

