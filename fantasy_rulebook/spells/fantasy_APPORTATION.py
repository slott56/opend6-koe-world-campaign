"""
fantasy_APPORTATION

When run as an app, generates .RST details of each Spell.
"""

from opend6_tools.magic2 import *


spells = [
    Spell(
        name="Alter Movement",
        skill="Apportation",
        notes=[
            "The caster makes her target either hurry up or slow down, depending on how she words her command. The target’s movement is altered by the measure of the spell effect’s value plus any result points bonus (as read on the “Spell Measures” chart).",
            "**Example**",
            "A magic user casts the alter movement spell to slow down a charging bull. At casting time, he decided to use the spell effect’s value plus the full variable amount, for a minimum change value of 9, or 60 meters per second (12 meters per round). If his skill total was one point over the difficulty, the new change value would be 10, or 100 meters per second (10 meters per round). This rate would then be subtracted from the bull’s current movement rate, causing the raging animal to come to a complete and shockingly sudden stop.",
        ],
        effect=SkillEffect("Movement change", "5D"),  # "1 meter per round"), == 0.2 m/s
        duration=DurationAspect(measure="4 min"),
        range=RangeAspect(measure="25 m"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "focused": FocusedAspect.based_on(("effect", "duration"), target="on target"),
            "gesture": GesturesAspect(
                "Point at target, then make running motion with fingers", "simple",
            ),
            "incantation": IncantationsAspect(
                "First say, “I command your speed,” followed by whether the target should slow or quicken", "sentence"
            ),
            "other_alterant": OtherAlterant(
                1, "At time of casting, mage may choose to speed up or slow down target (small)"
            ),
        },
        other_conditions=[
            GenericAspect(
                difficulty=5,
                description="Variable Effect: Caster may increase effect’s value by up to 5 points on the “Spell Measures” chart",
            ),
        ],
    ),

    Spell(
        name="Carrying Wind",
        skill="Apportation",
        notes=[
            "This is a charged spell. To cast it, the mage goes outside and starts running, jumping, and mimicking flight. The mage should be wearing something loose that can catch the wind. One cast garners the mage six charges of the spell.",
            "When released, the spell causes a wind to rise and lifts the mage into the air. The mage can control the direction of the wind and its speed (up to 25 meters a round). The spell can carry as if it had a lifting of 5D.",
            "The wind forms a three-meter sphere around the mage’s body, and nothing can be carried that won’t fit in that sphere.",
        ],
        effect=SkillEffect("wind with a lifting skill", "5D"),
        duration=DurationAspect(measure="1 hr"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 hr"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "area_effect": AreaEffectAspect("3 meter radius sphere"),
            "charges": ChargesAspect(6),
            "component": ComponentsAspect(
                ("May only be cast outdoors, in a clear area", "ordinary"),
                ("mage wears loose clothes", "common"),
            ),
            "feedback": FeedbackAspect(8),
            "gesture": GesturesAspect("Mimic a fight", "simple"),
            "incantation": IncantationsAspect("I subdue you and I command you, O wind!", "sentence"),
            "variable_movement": VariableMovementAspect("25 meters"),
        },
        other_conditions=[],
    ),

    Spell(
        name="Relocate Person",
        skill="Apportation",
        notes=[
            "After the mage casts the spell, she has firmly fixed in her mind three uses of it. When she releases the spell, she points at her intended target, which will be instantly teleported to the range of the spell. The result points bonus may be added either to the value of the weight transported or the distance traveled; read the new value on the “Spell Measures” chart. The spell will not allow anything to appear inside a solid object. Remember that a target who is aware of the potential relocation may roll her Physique or lifting and add it to her weight. The caster’s spell roll must then beat that difficulty as well as the spell’s difficulty.",
            "**Note**",
            "A similar spell, Relocate Item, is identical in every way except that the effect is to carry an item weighing no more than 10 kilograms, with a value of 5, and thus the difficulty is 11.",
        ],
        effect=MassEffect("teleport", "150 kilograms"),
        duration=DurationAspect(measure="1.5 r"),
        range=RangeAspect(measure="100 m"),
        casting_time=CastingTimeAspect(measure="1 r"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "charges": ChargesAspect(3),
            "gesture": GesturesAspect(
                "Point to target then point in direction of new location", "simple",
            ),
            "incantation": IncantationsAspect("Go there.", "phrase"),
        },
        other_conditions=[],
    ),
]


__test__ = {
    "Alter Movement": ">>> spells[0].difficulty\n17",  # Rules say 15
    "Carrying Wind": ">>> spells[1].difficulty\n13",
    "Relocate Person": ">>> spells[2].difficulty\n16",  # Rules say 14
}

if __name__ == "__main__":
    app = build_app(spells)
    app()
