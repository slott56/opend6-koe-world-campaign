"""
Spells for *D6 Fantasy* "PRECALCULATED SPELLS" chapter.

Used to create shared/fantasy_spells.txt.
This is included in the fantasy_rulebook/Spells.rst
"""

from textwrap import dedent

from magic import *

cantrips = [
    Spell(
        name="Charm",
        skill=Alteration,
        effect=Aspect("charm skill bonus of +4D", base_difficulty=18),
        range=Range.self_or_touch,
        # speed = Speed(0)
        duration=time_aspect("1m"),
        casting_time=CastingTime.cast_1s,
        other_aspects={
            "Gesture": Aspect(
                format="Smile and make a gesture of welcome or admiration",
                base_difficulty=-2,
            ),
            "Unreal Effect": Aspect(
                format="Difficulty to disbelieve is 13", base_difficulty=-9
            ),
        },
        other_conditions=[
            Aspect(
                "May only be used on humanoids who understand the caster's language and can hear the caster",
                base_difficulty=-2,
            )
        ],
        notes=dedent(
            """\
            With a smile and a friendly gesture, the caster improves his charm
            skill by for one minute. (If he no charm skill, add the bonus to the
            character's Charisma attribute.) As this is an illusory spell, if the
            intended target of the charm disbelieves it, any effect the charm
            # attempt had wears off immediately."""
        ),
    ),
    Spell(
        name="Heighten Attribute (Template)",
        skill=Alteration,
        effect=Aspect("+1D bonus to one non-Extranormal attribute", base_difficulty=6),
        range=Range.self_or_touch,
        # speed=Speed(0)
        duration=time_aspect("5r"),
        casting_time=CastingTime.cast_1r,
        other_aspects={
            "Gesture": Aspect(
                format="Mime an activity using a skill that falls under the attribute to be heightened (complex, action difficulty of 11; examples: sleight of hand for Coordination, lifting for Physique)",
                base_difficulty=-2,
            ),
        },
        notes=dedent(
            """\
            This cantrip gives the target a bonus of+ 1D to one ofhis attributes
            for 25 seconds, or five rounds - as long as he doesn't move more
            than a meter from the spot on which he received the bonus.
            Note that this is only a template for a spell and not an actual
            spell, because it does not indicate in the description which attribute
            is affected. The caster must specify which attribute and skill to mime
            before learning the spell (which takes one round).
            """
        ),
    ),
    Spell(
        name="Open Lock",
        skill=Apportation,
        effect=Aspect("compare with difficulty to open lock", base_difficulty=18),
        range=Range.self_or_touch,
        # speed = 0 ?
        duration=time_aspect("1r"),
        casting_time=CastingTime.cast_1r,
        other_aspects={
            "Gesture": Aspect(
                format="Mime opening the lock with the key (fairly simple)",
                base_difficulty=-2,
            ),
            "Incantation": Aspect(
                format='"Open, Lock, and reveal your secrets." (sentence)',
                base_difficulty=-2,
            ),
        },
        other_conditions=[
            Aspect(format="Physical contact with lock", base_difficulty=-1)
        ],
        notes=dedent(
            """\
            To cast this cantrip, the mage touches the lock with one hand
            while, with the key held in it, miming opening the lock with the other
            hand. After reciting the incantation, he touches the lock with the key
            and turns the key. If the spell effect's value is equal to or greater than
            the difficulty of the lock, it opens. If there are any traps or wards on
            the lock, they are not circumvented by this spell! Note that this spell
            works on any kind of mechanical lock.
            """
        ),
    ),
]


def report():
    print("Cantrips")
    print("========")
    print()
    for spell in cantrips:
        print(spell.report())
        print()


if __name__ == "__main__":
    report()
