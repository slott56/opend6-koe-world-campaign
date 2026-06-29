"""
CANTRIPS

When run as an app, generates .RST details of each Spell.
"""

from magic1 import Aspect, Spell, detail


spells = [
    Spell(
        effect=Aspect(format="charm skill bonus of +4D", base_difficulty=18, count=1),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Charm",
        other_aspects={
            "Difficulty": Aspect(format="5", base_difficulty=0.0, count=1),
            "Gesture": Aspect(
                format="Smile and make a gesture of welcome or admiration",
                base_difficulty=-2,
                count=1,
            ),
            "Unreal Effect": Aspect(
                format="Difficulty to disbelieve is 13", base_difficulty=-9, count=1
            ),
        },
        other_conditions=[
            Aspect(
                format="May only be used on humanoids who understand the caster's language and can hear the caster",
                base_difficulty=-2,
                count=1,
            ),
        ],
        notes="With a smile and a friendly gesture, the caster improves his charm\nskill by for one minute. (If he no charm skill, add the bonus to the\ncharacter's Charisma attribute.) As this is an illusory spell, if the\nintended target of the charm disbelieves it, any effect the charm\nattempt had wears off immediately.\n",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="+ 1D bonus to one non-Extranormal attribute",
            base_difficulty=6,
            count=1,
        ),
        duration=Aspect(format="5 rounds ", base_difficulty=7, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Heighten Attribute (template)",
        other_aspects={
            "Difficulty": Aspect(format="3", base_difficulty=0.0, count=1),
            "Gesture": Aspect(
                format="Mime an activity using a skill that falls under the attribute to be heightened (complex, action difficulty of 11; examples: sleight of hand for Coordination, lifting for Physique)",
                base_difficulty=-3,
                count=1,
            ),
        },
        other_conditions=[],
        notes="This cantrip gives the target a bonus of+ 1D to one ofhis attributes\nfor 25 seconds, or five rounds - as long as he doesn't move more\nthan a meter from the spot on which he received the bonus.\nNote that this is only a template for a spell and not an actual\nspell, because it does not indicate in the description which attribute\nis affected. The caster must specify which attribute and skill to mime\nbefore learning the spell (which takes one round).\n",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="compare to difficulty to open lock", base_difficulty=18, count=1
        ),
        duration=Aspect(format="1 round", base_difficulty=4, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round", base_difficulty=-4, count=1),
        name="Open Lock",
        other_aspects={
            "Difficulty": Aspect(format="5", base_difficulty=0.0, count=1),
            "Components": Aspect(
                format="Large metal key (common)", base_difficulty=-3, count=1
            ),
            "Gesture": Aspect(
                format="Mime opening the lock with the key (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantation": Aspect(
                format='"Open, Lock, and reveal your secrets." (sentence)',
                base_difficulty=-2,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(format="Physical contact with lock", base_difficulty=-1, count=1),
        ],
        notes="To cast this cantrip, the mage touches the lock with one hand\nwhile, with the key held in it, miming opening the lock with the other\nhand. After reciting the incantation, he touches the lock with the key\nand turns the key. If the spell effect's value is equal to or greater than\nthe difficulty of the lock, it opens. If there are any traps or wards on\nthe lock, they are not circumvented by this spell! Note that this spell\nworks on any kind of mechanical lock.",
        skill="Apportation",
    ),
]


if __name__ == "__main__":
    detail(spells)


__test__ = {
    "Skill Used: Alteration": ">>> spells[0].difficulty\n5",
    "HEIGHTEN ATTRIBUTE (TEMPLATE)": ">>> spells[1].difficulty\n3",
    "OPEN LOCK": ">>> spells[2].difficulty\n5",
}
