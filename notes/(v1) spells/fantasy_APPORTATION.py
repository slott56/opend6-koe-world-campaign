"""
APPORTATION SPELLS

When run as an app, generates .RST details of each Spell.
"""

from magic1 import Aspect, Spell, detail


spells = [
    Spell(
        effect=Aspect(format="1 meter per round", base_difficulty=4, count=1),
        duration=Aspect(format="4 minutes/SO rounds ", base_difficulty=12, count=1),
        range=Aspect(format="25 meters ", base_difficulty=7, count=1),
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        casting_time=Aspect(format="1 round", base_difficulty=-4, count=1),
        name="Alter Movement",
        other_aspects={
            "Focused": Aspect("On target", base_difficulty=2),
            "Difficulty": Aspect(format="15", base_difficulty=0.0, count=1),
            "Gesture": Aspect(
                format="Point at target, then make running motion with fingers (fairly simple)",
                base_difficulty=-2,
            ),
            "Incantation": Aspect(
                format='First say, "I command your speed," followed by whether the target should slow or quicken (sentence)',
                base_difficulty=-2,
            ),
            "Variable Effect": Aspect(
                format='Caster may increase effect\'s value by up to S points on the "Spell Measures" chart',
                base_difficulty=5,
            ),
            "Other Alterant": Aspect(
                format="At time of casting, mage may choose to speed up or slow down target (small)",
                base_difficulty=1,
            ),
        },
        other_conditions=[],
        notes="The caster makes her target either hurry up or slow down ,\ndepending on how she words her command. The target's movement\nis altered by the measure of the spell effect's value plus any result\npoints bonus (as read on the \"Spell Measures\" chart).\nExample: A magic user casts the alter movement spell to slow\ndown a charging bull. At casting time, he decided to use the spell\neffect's value plus the full variable amount, for a minimum change\nvalue of 9, or 60 meters per second (12 meters per round). If his\nskill total was one point over the difficulty, the new change value\nwould be 10, or 100 meters per second (10 meters per round).\nThis rate would then be subtracted from the bull's current move\xad\nment rate, causing the raging animal to come to a complete and\nshockingly sudden stop.\n",
        skill="Apportation",
    ),
    Spell(
        effect=Aspect(format="wind with a lifting of 5D", base_difficulty=15, count=1),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 hr", base_difficulty=-18, count=1),
        name="Carrying Wind",
        other_aspects={
            "Difficulty": Aspect(format="13", base_difficulty=0.0, count=1),
            "Area Effect": Aspect(format="3-meter sphere", base_difficulty=15, count=1),
            "Charges": Aspect(format="6 charges", base_difficulty=4, count=1),
            "Component": Aspect(
                format="May only be cast outdoors, in a clear area (ordinary), mage wears loose clothes (common)",
                base_difficulty=-4,
                count=1,
            ),
            "Feedback": Aspect(format="points of damage", base_difficulty=-8, count=1),
            "Gesture": Aspect(
                format="Mimic a fight (fairly simple)", base_difficulty=-2, count=1
            ),
            "Incantation": Aspect(
                format='"I subdue you and I command you, 0 wind!" (sentence)',
                base_difficulty=-2,
                count=1,
            ),
            "Variable Movement": Aspect(
                format="2S meters per second", base_difficulty=7, count=1
            ),
        },
        other_conditions=[],
        notes="This is a charged spell. To cast it, the mage goes outside and starts\nrunning, jumping, and mimickingfligh t. The mage should be wearing\nsomething loose that can catch the wind. One cast garners the mage\nsix charges of the spell.\n\nWhen released, the spell causes a wind to rise and lifts the mage\ninto the air. The mage can control the direction of the wind and its\nspeed (up to 2S meters a round). The spell can carry as if it had a\nlifting of SD.\n\nThe wind forms a three-meter sphere around the mage's body,\nand nothing can be carried that won't fit in that sphere.\n",
        skill="Apportation",
    ),
    Spell(
        effect=Aspect(
            format="teleport up to lSO kilograms", base_difficulty=11, count=1
        ),
        duration=Aspect(format="1.S rounds ", base_difficulty=1, count=1),
        range=Aspect(format="100 meters ", base_difficulty=10, count=1),
        speed=Aspect(format="Instantaneous", base_difficulty=10, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Relocate Person",
        other_aspects={
            "Difficulty": Aspect(format="14", base_difficulty=0.0, count=1),
        },
        other_conditions=[],
        notes='Gesture (-2): Point to target then point in direction of new location (fairly simple)\nIncantation (-1): "Go there." (one or two words)\nAfter the mage casts the spell, she has firmly fixed in her mind\nthree uses of it. When she releases the spell, she points at her\nintended target, which will be instantly teleported to the range of\nthe spell. The result points bonus may be added either to the value of\nthe weight transported or the distance traveled; read the new value\non the "Spell Measures" chart. The spell will not allow anything to\nappear inside a solid object. Remember that a target who is aware\nof the potential relocation may roll her Physique or lifting and add it\nto her weight. The caster\'s spell roll must then beat that difficulty as\nwell as the spelfs difficulty.\nNote : A similar spell, relocate item, is identical in every way except\nthat the effect is to carry an item weighing no more than lO kilograms,\nwith a value of 5, and thus the difficulty is 11.',
        skill="Apportation",
    ),
]


if __name__ == "__main__":
    detail(spells)

__test__ = {
    "Alter Movement": ">>> spells[0].difficulty\n15",
    "Carrying Wind": ">>> spells[1].difficulty\n13",
    "Relocate Person": ">>> spells[2].difficulty\n14",
}
