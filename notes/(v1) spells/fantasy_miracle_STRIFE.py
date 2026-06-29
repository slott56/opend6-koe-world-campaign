"""
STRIFE

When run as an app, generates .RST details of each Miracle.
"""

from magic1 import Aspect, Miracle, detail


invocations = [
    Miracle(
        effect=Aspect(
            format="compare to 2 times the target's Charisma or mettle",
            base_difficulty=12,
            count=1,
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="20 meters ", base_difficulty=7, count=1),
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        casting_time=Aspect(format="2 r", base_difficulty=-5, count=1),
        name="Banish",
        other_aspects={
            "Difficulty": Aspect(format="15", base_difficulty=0.0, count=1),
        },
        other_conditions=[],
        notes="devoted to a different religion/gocl/power or undead controlled by\na character devoted to a different religion/god/power\nThe miracle can only be used against opponents of a different\nreligion. If successfully invoked, compare the effect total to a value\nequal to 2 times the target's Charisma or mettle (including any spe-\nci.al.ization related to religion). If the target has not taken an action\nyet this round, she m ay actively defend by generating a mettle total\n(including her faith specialization), but this is considered her action\nfor the round. For undead without a mettle or Charisma score, use\nthe die code of the creatures' controller.\nIf the target bas a lowe r total, she flees the area (if possible).\n",
        skill="Strife",
    ),
    Miracle(
        effect=Aspect(format="+3D damage bonus", base_difficulty=9, count=1),
        duration=Aspect(format="8 rounds ", base_difficulty=8, count=1),
        range=Aspect(format="10 m", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous", base_difficulty=5, count=1),
        casting_time=Aspect(format="2 sec", base_difficulty=-1, count=1),
        name="Bless Weapon",
        other_aspects={
            "Difficulty": Aspect(format="13", base_difficulty=0.0, count=1),
        },
        other_conditions=[],
        notes="Bless weapon infuses spiritual energy into any one weapo n, as\nlong as the it.em remains within 10 meters of the blessing cleric.\nThe invocation applies the miracle success bonus to the damage of\nthe blessed item.\nA character may enjoy the effects of only one bless at any given\ntime. The cleric may use bless weapon on an item he's holding.\n",
        skill="Strife",
    ),
    Miracle(
        effect=Aspect(format="Bad Luck (R2) Disadvantage", base_difficulty=6, count=1),
        duration=Aspect(format="10 minutes ", base_difficulty=14, count=1),
        range=Aspect(format="10 m", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous", base_difficulty=5, count=1),
        casting_time=Aspect(format="1 r", base_difficulty=-4, count=1),
        name="Curse",
        other_aspects={
            "Difficulty": Aspect(format="14", base_difficulty=0.0, count=1),
            "Focused": Aspect(format="On Target", base_difficulty=4),
        },
        other_conditions=[Aspect(format="Limited to humanoids", base_difficulty=-2)],
        notes="The cleric curses a single humanoid target with 10 minutes of\nBad Luck (R2), which doesn't leave the target even if he moves out\nof range. See the description of this Disadvantage in the MC haracter\nOptions\" chapter for details. Each success Level doubles the amount\nof time that the target has the curse.\n",
        skill="Strife",
    ),
    Miracle(
        effect=Aspect(
            format="compare to skill total of spell countering",
            base_difficulty=29,
            count=1,
        ),
        duration=Aspect(format="1 round ", base_difficulty=4, count=1),
        range=Aspect(format="60 meters ", base_difficulty=9, count=1),
        speed=Aspect(format="Instantaneous", base_difficulty=9, count=1),
        casting_time=Aspect(format="2 sec", base_difficulty=-1, count=1),
        name="Disrupt Spell",
        other_aspects={
            "Difficulty": Aspect(format="25", base_difficulty=0.0, count=1),
        },
        other_conditions=[],
        notes="Theclericconcentrateson tbespellhewishestocounter.Theeffect's\nvalue plus the miracle's miracle success bonus are compared to the\nskill total used tocreatethe targetedspell. lfthe disrupt spell number\nequals or exceeds the target spell's skill total, the spell is broken.\n",
        skill="Strife",
    ),
    Miracle(
        effect=Aspect(
            format="4D in fighting and 4D in damage", base_difficulty=24, count=1
        ),
        duration=Aspect(format="1 hours ", base_difficulty=18, count=1),
        range=Aspect(format="5m", base_difficulty=4, count=1),
        speed=Aspect(format="Instantaneous", base_difficulty=4, count=1),
        casting_time=Aspect(format="2 seconds ", base_difficulty=-1, count=1),
        name="Fighting Tree",
        other_aspects={
            "Difficulty": Aspect(format="23", base_difficulty=0.0, count=1),
            "Components": Aspect(
                format="A long supple tree or one with long branches (common)",
                base_difficulty=-3,
                count=1,
            ),
        },
        other_conditions=[],
        notes="Through this prayer, the cleric can animate the branches of a\ntree to strike at anyone within range. B ranches that hit the target\ninflict 4D of damage. The tree can strike at no more than Short range\n- less if it's small.\n",
        skill="Strife",
    ),
    Miracle(
        effect=Aspect(format="4D in damage", base_difficulty=12, count=1),
        duration=Aspect(format="3.5 seconds ", base_difficulty=3, count=1),
        range=Aspect(format="10m", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous", base_difficulty=5, count=1),
        casting_time=Aspect(format="1.5 sec", base_difficulty=-1, count=1),
        name="Spiritual Bolt",
        other_aspects={
            "Difficulty": Aspect(format="12", base_difficulty=0.0, count=1),
        },
        other_conditions=[],
        notes="The cleric gathers spiritual energy to throw in a bolt at a target.\nIt does 40 in damage at a range of up to 10 meters. She must make\na marksmanship roll to hit the target. The bolt must be fired in the\nsame round that the cleric invokes the invocation.\n",
        skill="Strife",
    ),
    Miracle(
        effect=Aspect(
            format="4D in fighting and lifting; 10 in running",
            base_difficulty=27,
            count=1,
        ),
        duration=Aspect(format="1.5 hours ", base_difficulty=19, count=1),
        range=Aspect(format="25 m", base_difficulty=+7, count=1),
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        casting_time=Aspect(format="2 sec", base_difficulty=-1, count=1),
        name="Undead Warrior",
        other_aspects={
            "Difficulty": Aspect(format="27", base_difficulty=0.0, count=1),
            "Components": Aspect(
                format="Intact dead body or skeleton (very rare)", base_difficulty=-5
            ),
        },
        other_conditions=[],
        notes="This rite causes any one dead creature to rise in its present state\nto serve as a soldier bonded to the cleric. As this is a basic miracle, it\nimbues the creature with select skills; the cleric may add more and\nincrease the difficulty. The reanimated being cannot think for itself, so\nit ignores all Wound level and bit location penalties. It does what.ever\nthe cleric deaands, until the invoker tells it to stop or the duration\nends. At the end of the duration or if the cleric sends it out of range,\nthe creature falls down in a heap. The invocation's miracle success\nbonus may either add to the range or to the amount of damage the\ncreature does (it has a base Strength Damage of2D); which applica\xad\ntion must be decided before invoking the miracle.",
        skill="Strife",
    ),
]


if __name__ == "__main__":
    detail(invocations)


__test__ = {
    "Banish": ">>> invocations[0].difficulty\n15",
    "Bless Weapon": ">>> invocations[1].difficulty\n13",
    "Curse": ">>> invocations[2].difficulty\n14",
    "Disrupt Spell": ">>> invocations[3].difficulty\n25",
    "Fighting Tree": ">>> invocations[4].difficulty\n23",
    "Spiritual Bolt": ">>> invocations[5].difficulty\n12",
    "Undead Warrior": ">>> invocations[6].difficulty\n27",
}
