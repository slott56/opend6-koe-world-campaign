"""
ALTERATION SPELLS

When run as an app, generates .RST details of each Spell.
"""

from magic1 import Aspect, Spell, detail


spells = [
    Spell(
        effect=Aspect(
            format="compare to skill total of spell countering",
            base_difficulty=29,
            count=1,
        ),
        duration=Aspect(format="1 round ", base_difficulty=4, count=1),
        range=Aspect(format="60 meters ", base_difficulty=9, count=1),
        speed=Aspect(format="Instantaneous", base_difficulty=9, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Countermagic",
        other_aspects={
            "Difficulty": Aspect(format="19", base_difficulty=0.0, count=1),
            "Concentration": Aspect(
                format="3 seconds with mettle difficulty of7",
                base_difficulty=-1,
                count=1,
            ),
            "Gesture": Aspect(
                format="Wave hand through air as if wiping away something (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Incantation": Aspect(
                format='"Your hold is broken!" (sentence, said loudly)',
                base_difficulty=-3,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="One spell, which the caster must specify when casting this spell",
                base_difficulty=-4,
                count=1,
            ),
        ],
        notes="Tue caster concentrates on the spell he wishes to counter, waving\nhis band and shouting the required incantation. The effect's value\nplus the result points bonus are compared to the skill total used to\ncreate the targeted spell If the countermagic number is equal to or\nhigher than the target spell's skill total, the spell is broken.\n",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="compare to skill total of spell countering",
            base_difficulty=29,
            count=1,
        ),
        duration=Aspect(format="1 round ", base_difficulty=4, count=1),
        range=Aspect(
            format="Self or a target within 1 meter ", base_difficulty=0, count=1
        ),
        speed=Aspect(format="Instantaneous", base_difficulty=0, count=1),
        casting_time=Aspect(format="25 minutes ", base_difficulty=-16, count=1),
        name="Countermagic Ward",
        other_aspects={
            "Difficulty": Aspect(format="11", base_difficulty=0.0, count=1),
        },
        other_conditions=[],
        notes='Concentration (-4): 10 minutes with mettle difficulty of 10\nFocused (+6): On target\nGesture (-1): Wave hand through air as if wiping away something (simple)\nIncantation (-3): "Let no spell touch me!" (sentence, said loudly)\nSimilar to the countermagic spell, this spell gives the target a gen\xad\neral protection against spells. It is triggered by a spell "hitting" the\ntarget. Up to six spells can be countered in this fashion. The effect\'s\nvalue plus result points bonus are compared to the skill total used\nto create the targeted spell If the countermagic ward numberis equal\nto or higher than the target spell\'s skill total, the spell is broken.\nRegardless of the success of the ward , one charge is lost.\n',
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(format="+4D in damage", base_difficulty=18, count=1),
        duration=Aspect(format="5 rounds", base_difficulty=7, count=1),
        range=Aspect(format="100m ", base_difficulty=10, count=1),
        speed=Aspect(format="Instantaneous", base_difficulty=10, count=1),
        casting_time=Aspect(format="40 min", base_difficulty=-17, count=1),
        name="Deadly Dart",
        other_aspects={
            "Difficulty": Aspect(format="11", base_difficulty=0.0, count=1),
            "Charges": Aspect(format="1 charge", base_difficulty=1),
            "Components": Aspect(
                format="Black obsidian (uncommon, destroyed), dart (common)",
                base_difficulty=-11,
            ),
            "Feedback": Aspect(
                format="-3 to damage resistance total", base_difficulty=-3
            ),
            "Gesture": Aspect(
                format="Rub the tip of the bullet on the stone (simple)",
                base_difficulty=-1,
            ),
            "Incantation": Aspect(
                format='"Darkness of death." (a few words)', base_difficulty=-1
            ),
            "Variable Movement": Aspect(format="+2 accuracy bonus", base_difficulty=4),
            "Focused": Aspect(format="Focused", base_difficulty=5),
        },
        other_conditions=[],
        notes="This spell uses a piece of black obsidian to increase the deadliness\nof a dart. The mage utters a short, dark phrase while gently stroking\nthe tip of the dart across the stone. The darkness travels into the\ndart, draining the stone of its pigment.\nTo release the spell, the caster throws the dart within five rounds\nof casting the spell. He generate an marksmanship total, adding a + 2\nbonus for the increased accuracy of the spell, against the combat dif\xad\nficulty for the target. The target must be within range of the spell, or\nthe dart merely does its normal effect. The target takes an additional\n40 in damage in the round the dart hits and for the nextfour rounds.\nThe spell ends if the target moves beyond the spell's range.\n",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="intimidation skill bonus at +60+2", base_difficulty=30, count=1
        ),
        duration=Aspect(format="2.5 minute ", base_difficulty=11, count=1),
        range=Aspect(format="100 meters ", base_difficulty=10, count=1),
        speed=Aspect(format="Instantaneous", base_difficulty=10, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        name="Fear",
        other_aspects={
            "Difficulty": Aspect(format="19", base_difficulty=0.0, count=1),
            "Components": Aspect(
                format="An item owned for at least a month by the target (very rare)",
                base_difficulty=-5,
                count=1,
            ),
            "Gesture": Aspect(
                format="Point item at target (simple)", base_difficulty=-1, count=1
            ),
            "Incantation": Aspect(
                format="Frightening words (a few words)", base_difficulty=-1, count=1
            ),
            "Unreal Effect": Aspect(
                format="Difficulty to disbelieve is 13", base_difficulty=-8, count=1
            ),
        },
        other_conditions=[],
        notes="To cast the spell, the mage first needs something belonging to\nher target - bis comb, his watch, a lock of his hair. Mutter a few\nwords of power, point the item at the target, and watch the fun. This\nspell gives the caster an intimidation skill bonus of +60+2, but only\ntowards that target. The target may disbelieve it with a Charisma or\nmettle roll of 13.\n",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(format="4D damage", base_difficulty=12, count=1),
        duration=Aspect(format="3 rounds ", base_difficulty=6, count=1),
        range=Aspect(format="15 m", base_difficulty=+6, count=1),
        speed=Aspect(format="Instantaneous", base_difficulty=0, count=1),
        casting_time=Aspect(format="5 sec", base_difficulty=-4, count=1),
        name="Water Spray",
        other_aspects={
            "Difficulty": Aspect(format="10", base_difficulty=0.0, count=1),
            "Components": Aspect(
                format="Liter of water( ordinary, destroyed), squeezable container (uncommon)",
                base_difficulty=-6,
                count=1,
            ),
        },
        other_conditions=[],
        notes="The mage needs a liter of water in a container that she can\nsqueeze to produce a spray. As she casts the spell, the mage squirts\nthe water onto her hand, letting it run off in the direction of her\ntarget. The volume and force behind the water spray increases\ndramatically. The spray lasts for three rounds of combat. The\nspell does 40 in damage per round and requires a marksmanship\nroll each round to hit the target. The caster may only select one\ntarget per spell duration.",
        skill="Alteration",
    ),
]


if __name__ == "__main__":
    detail(spells)
