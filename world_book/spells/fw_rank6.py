"""
Extract Spells from ``Rank6 Workbook.ipynb``.
Created by V2025.12.6.dev3 of ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

"""

from opend6_tools.magic2 import *



earth_quake = Spell(
        name="Earth Quake",
        skill="Elemental Alteration",
        notes="The area is large enough that the mage is barely able to avoid the effects; damage is incidental usually from falling objects",
        effect=MassEffect("shake earth", "1,000 kg"),
        duration=DurationAspect(measure="5 s"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Earth Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
            "area_of_effect": AreaEffectAspect("20m r circle"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Hildeþrymm Physique")
        ],
    )

open_veil = Spell(
    name = "Opening the Veil",
    skill = "Apportation",
    notes="Opens the veil; it will remain open for others to pass through.",
    effect=CompositeEffect(
        "Veil Opening",
        Effect("Apportation to new realm (R4)", 40),
        Effect("Adjustments for experience, knowledge, and aids", 20),
    ),
    duration=DurationAspect(measure="5 min"),
    range=RangeAspect(measure="touch"),
    casting_time=CastingTimeAspect(measure="5 s"),
    speed=SpeedAspect.based_on(("range",), ""),
    other_aspects={
        "incantation": IncantationsAspect("Veil Opening Chant", "litany"),
        "concentration": ConcentrationAspect(measure="5 s"),
        "components": ComponentsAspect("any resonating artifacts", "rare"),
    },
    other_conditions=[
        GenericAspect(difficulty=0, description="Controller: None"),
    ],
)
spells = [ 
    earth_quake, open_veil, 
]

__test__ = {
    "Earth Quake": ">>> spells[0].difficulty\n32",
    "Opening the Veil": ">>> spells[1].difficulty\n29",
}

if __name__ == "__main__":
    app = build_app(spells)
    app()

