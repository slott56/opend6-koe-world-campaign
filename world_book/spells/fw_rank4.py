"""
Extract Spells from ``Rank4 Workbook.ipynb``.
Created by V2025.12.6.dev3 of ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

"""

from opend6_tools.magic2 import *



sleep = Spell(
        name="Sleep",
        skill="Temperamental Alteration",
        notes="Physique, Coordination, Acumen, and Intellect are (temporarily) reduced, leading to fatique",
        effect=DisadvantageEffect("Narcolepsy", 4, "-4D to mental and physical attributes"),
        duration=DurationAspect(measure="1 hr"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Control Chant", "litany"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Folme Agility")
        ],
    )

conjure_wall_of_rock = Spell(
        name="Conjure Wall of Rock",
        skill="Elemental Conjuration",
        notes="Creates a wall from free earth elements",
        effect=MassEffect("Move earth element to a new position", "600kg"),
        duration=DurationAspect(measure="5 min"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Earth Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
            "area_of_effect": AreaEffectAspect("2 m radius sphere"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Hildeþrymm Physique")
        ],
    )

totally_invisible = Spell(
        name="Totally Invisible",
        skill="Temperamental Alteration",
        notes="The thing is almost impossible to see",
        effect=DisadvantageEffect("Perception is ruined", "8"),
        duration=DurationAspect(measure="5 min"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Control Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Witan Acumen")
        ],
    )

portable_cache = Spell(
    name="Portable Cache",
    skill="Apportation",
    notes="The mage can reach through a portable container's opening into a known space in another realm to keep things. The other realm location is not 100% safe; a critical failure may mean the cache was moved in the other realm. The opening is centered on something moveable, like a a bag or scrip the mage carries.",
    effect=CompositeEffect(
        "Possession and Apportation",
        Effect("Apportation to another realm (R3)", 30),
        MassEffect("Limited to", "50 Kg"),
    ),
    duration=DurationAspect(measure="5 min"),
    range=RangeAspect(measure="touch"),
    casting_time=CastingTimeAspect(measure="5 s"),
    speed=SpeedAspect.based_on(("range",), ""),
    other_aspects={
        "incantation": IncantationsAspect("Veil Opening Chant", "litany"),
        "concentration": ConcentrationAspect(measure="5 s"),
        "components": ComponentsAspect("Movable artifact (e.g. bag)", "common"),
    },
    other_conditions=[
        GenericAspect(difficulty=0, description="Controller: None"),
    ],
)

reanimation_r2 = Spell(
    name = "Reanimate Non-Human",
    skill = "Temperamental Conjuration",
    notes="Reanimates a complete non-human for an hour.",
    effect=Effect("Temperamental Conjuration of one 10D non-human", 24 + 10),
    duration=DurationAspect(measure="1 hr"),
    range=RangeAspect(measure="touch"),
    casting_time=CastingTimeAspect(measure="5 s"),
    speed=SpeedAspect.based_on(("range",), ""),
    other_aspects={
        "incantation": IncantationsAspect("Conjuration Chant", "litany"),
        "concentration": ConcentrationAspect(measure="5 s"),
        "components": ComponentsAspect("a living example", "uncommon"),
    },
    other_conditions=[
        GenericAspect(difficulty=0, description="Controller: None"),
        GenericAspect(difficulty=3, description="All four elements present in the environment: fire, flowing water, wind, and loose earth."),
    ],
)
spells = [ 
    sleep, conjure_wall_of_rock, totally_invisible, portable_cache, reanimation_r2, 
]

__test__ = {
    "Sleep": ">>> spells[0].difficulty\n18",
    "Conjure Wall of Rock": ">>> spells[1].difficulty\n20",
    "Totally Invisible": ">>> spells[2].difficulty\n20",
    "Portable Cache": ">>> spells[3].difficulty\n19",
    "Reanimate Non-Human": ">>> spells[4].difficulty\n18",
}

if __name__ == "__main__":
    app = build_app(spells)
    app()
