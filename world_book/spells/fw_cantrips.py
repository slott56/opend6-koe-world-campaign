"""
Extract from Cantrip Workbook.ipynb.

When run as app with "detail" argument, generates .RST-formatted details of all the Spells.

When run as app with "debug" argument, writes debugging details for selected spells.
"""
from opend6_tools.magic2 import *


protection_from_magic = Spell(
        name="Protection from Magic",
        skill="Elemental Alteration",
        notes="Distinct from Shield which prevents the link, this mitigates effects",
        effect=ProtectionEffect("Reduce effect (after a link)", "2D"),
        duration=DurationAspect(measure="1 s"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 s"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Protection Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 s"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="opposed"),
            GenericAspect(difficulty=0, description="Controller: None"),
        ],
    )

halt = Spell(
        name="Halt",
        skill="Psychic Communication",
        notes="The halt duration is short; an agility check is required to keep from stumbling",
        effect=SkillEffect("Halt! with bonus to overcome mettle", "2D"),
        duration=DurationAspect(measure="2 sec"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Control chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Witan Acumen")
        ],
    )

illusion_of_rat = Spell(
        name="Illusion of Rat",
        skill="Temperamental Conjuration",
        notes="An autonomous illusion of a large rat",
        effect=SkillEffect("Fear", "3D"),
        duration=DurationAspect(measure="5 min"),
        range=RangeAspect(measure="10 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "gestures": GesturesAspect("Illusion Gestures", "simple"),
            "incantation": IncantationsAspect("Illusion Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
            "other_alterant": GenericAspect(
                difficulty=3, description="illusion is moving"
            ),
            "unreal_effect": UnrealEffectAspect.based_on("effect", "difficulty 13"),
        },
        other_conditions=[
            GenericAspect(difficulty=-2, description="illusion limited to 1 color"),
            GenericAspect(difficulty=0, description="Controller: Baelu Charisma"),
        ],
    )

communicate_w_plant_animal = Spell(
        name="Communicate w/ Plant/Animal",
        skill="Divination",
        notes="This will gather a bit of common information",
        effect=SkillEffect("Psionics: gather common info; potentially hostile", "+2D", "extranormal skill"),
        duration=DurationAspect(measure="1 s"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 s"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "gestures": GesturesAspect("Touch target", "simple"),
            "incantation": IncantationsAspect("Earth and Water chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 s"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Witan Acumen")
        ],
    )

knock = Spell(
        name="Knock",
        skill="Elemental Alteration",
        notes="This tends to destroy the door",
        effect=DamageEffect("break latch or bar", "4D", "physical damage"),
        duration=DurationAspect(measure="1 s"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="1 s"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={"incantation": IncantationsAspect("Earth and Water Chant", "litany")},
        other_conditions=[
            GenericAspect(difficulty=-1, description="limited to wood"),
            GenericAspect(
                difficulty=0, description="Controller: Depends on type of wood"
            ),
        ],
    )

shocking_grasp = Spell(
        name="Shocking Grasp",
        skill="Elemental Alteration: Air + Fire",
        notes="A touch that does 6D damage",
        effect=DamageEffect("Electric Damage", "3D+1", "physical damage", "ignores all armor"),
        duration=DurationAspect(measure="1 s"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="1 s"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "gestures": GesturesAspect("Complex motion to grasp", "complex"),
            "incantation": IncantationsAspect("Air and Fire Chant", "litany"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Hælan Coordination")
        ],
    )

spells = [ 
    protection_from_magic, halt, illusion_of_rat, communicate_w_plant_animal, knock, shocking_grasp, 
]

__test__ = {
    "Protection from Magic": ">>> spells[0].difficulty\n5",
    "Halt": ">>> spells[1].difficulty\n6",
    "Illusion of Rat": ">>> spells[2].difficulty\n6",
    "Communicate w/ Plant/Animal": ">>> spells[3].difficulty\n7",
    "Knock": ">>> spells[4].difficulty\n4",
    "Shocking Grasp": ">>> spells[5].difficulty\n7",
}

if __name__ == "__main__":
    app = build_app(spells)
    app()
