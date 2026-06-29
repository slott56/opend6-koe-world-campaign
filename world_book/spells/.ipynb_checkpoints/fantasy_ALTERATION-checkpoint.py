"""
fantasy_ALTERATION

When run as an app, generates .RST details of each Spell.
"""

from magic2 import *


spells = [
    Spell(
        name="Countermagic",
        skill="Alteration",
        notes=[
            "The caster concentrates on the spell he wishes to counter, waving his hand and shouting the required incantation. The effect’s value plus the result points bonus are compared to the skill total used to create the targeted spell. If the countermagic number is equal to or higher than the target spell’s skill total, the spell is broken."
        ],
        effect=SkillEffect("compare to skill total of spell countering", "6D+1", "protection modifier"),
        duration=DurationAspect(measure="1 round"),
        range=RangeAspect(measure="60 m"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "concentration": ConcentrationAspect("3 seconds", note="mettle difficulty of 7"),
            "gesture": GesturesAspect(
                "Wave hand through air as if wiping away something", "very simple",
            ),
            "incantation": IncantationsAspect("Your hold is broken!", "sentence; loud"),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-4,
                description="One spell, which the caster must specify when casting this spell",
            )
        ],
    ),

    Spell(
        name="Countermagic Ward",
        skill="Alteration",
        notes=[
            "Similar to the countermagic spell, this spell gives the target a general protection against spells. It is triggered by a spell “hitting” the target. Up to six spells can be countered in this fashion. The effect’s value plus result points bonus are compared to the skill total used to create the targeted spell. If the countermagic ward number is equal to or higher than the target spell’s skill total, the spell is broken. Regardless of the success of the ward, one charge is lost."
        ],
        effect=SkillEffect("compare to skill total of spell countering", "6D+1", "protection modifier"),
        duration=DurationAspect(measure="1 r"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="25 minutes"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "charges": ChargesAspect(6, "go off when a spell “hits” the target"),
            "concentration": ConcentrationAspect("10 minutes", note="mettle difficulty of 10"),
            "focused": FocusedAspect.based_on(("effect", "duration"), target="on target"),
            "gesture": GesturesAspect("Wave hand through air as if wiping away something", "very simple"),
            "incantation": IncantationsAspect("Let no spell touch me!", "sentence; loud"),
        },
        other_conditions=[],
    ),

    Spell(
        name="Deadly Dart",
        skill="Alteration",
        notes=[
            "This spell uses a piece of black obsidian to increase the deadliness of a dart. The mage utters a short, dark phrase while gently stroking the tip of the dart across the stone. The darkness travels into the dart, draining the stone of its pigment.",
            "To release the spell, the caster throws the dart within five rounds of casting the spell. He generate an marksmanship total, adding a +2 bonus for the increased accuracy of the spell, against the combat difficulty for the target. The target must be within range of the spell, or the dart merely does its normal effect. The target takes an additional 4D in damage in the round the dart hits and for the next four rounds. The spell ends if the target moves beyond the spell’s range.",
        ],
        effect=DamageEffect("Dart", "+4D", "physical damage; damage modifier"),
        duration=DurationAspect(measure="5 rounds"),
        range=RangeAspect(measure="100 m"),
        casting_time=CastingTimeAspect(measure="40 min"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "charges": ChargesAspect(1),
            "component": CompositeAspect(
                ComponentsAspect("Black obsidian", "uncommon; destroyed"),
                ComponentsAspect("dart", "common"),
            ),
            "feedback": FeedbackAspect(3),
            "focused": FocusedAspect.based_on(("effect", "duration"), target="on target"),
            "gesture": GesturesAspect("Rub the tip of the dart on the stone", "very simple"),
            "incantation": IncantationsAspect("Darkness of death.", "phrase"),
            "variable_movement": VariableMovementAspect("accuracy bonus"),
        },
        other_conditions=[],
    ),

    Spell(
        name="Fear",
        skill="Alteration",
        notes=[
            "To cast the spell, the mage first needs something belonging to her target — his comb, his watch, a lock of his hair. Mutter a few words of power, point the item at the target, and watch the fun. This spell gives the caster an intimidation skill bonus of +6D+2, but only towards that target. The target may disbelieve it with a Charisma or mettle roll of 13."
        ],
        effect=SkillEffect("intimidation skill bonus", "+6D+2", "skill modifier"),
        duration=DurationAspect(measure="2.5 min"),
        range=RangeAspect(measure="100 m"),
        casting_time=CastingTimeAspect(measure="1 min"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect(
                "An item owned for at least a month by the target", "very rare",
            ),
            "gesture": GesturesAspect("Point item at target", "very simple"),
            "incantation": IncantationsAspect("Frightening words", "phrase"),
            "unreal_effect": UnrealEffectAspect.based_on(("effect",), "difficulty 13")
        },
        other_conditions=[],
    ),

    Spell(
        name="Water Spray",
        skill="Alteration",
        notes=[
            "The mage needs a liter of water in a container that she can squeeze to produce a spray. As she casts the spell, the mage squirts the water onto her hand, letting it run off in the direction of her target. The volume and force behind the water spray increases dramatically. The spray lasts for three rounds of combat. The spell does 4D in damage per round and requires a marksmanship roll each round to hit the target. The caster may only select one target per spell duration."
        ],
        effect=DamageEffect("water spray", "4D", "physical damage"),
        duration=DurationAspect(measure="3 rounds"),
        range=RangeAspect(measure="15 m"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": CompositeAspect(
                ComponentsAspect(
                    "Liter of water", "ordinary; destroyed"),
                ComponentsAspect("squeezable container", "uncommon"),
            )
        },
        other_conditions=[],
    ),
]


if __name__ == "__main__":
    detail(spells)

__test__ = {
    "Countermagic": ">>> spells[0].difficulty\n19",
    "Countermagic Ward": ">>> spells[1].difficulty\n9",  # Rules say 11
    "Deadly Dart": ">>> spells[2].difficulty\n10",  # Rules say 11
    "Fear": ">>> spells[3].difficulty\n19",
    "Water Spray": ">>> spells[4].difficulty\n10",
}
