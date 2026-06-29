"""
Extract Spells from ``fantasy_miracle_STRIFE.ipynb``.
Created by V2025.6.27.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

With "test" argument, runs doctest, which uses the __test__ examples.

"""

from opend6_tools.magic import *



basish = Miracle(
        name="Banish",
        skill="Strife",
        notes="The miracle can only be used against opponents of a different\nreligion. If successfully invoked, compare the effect total to a value\nequal to 2 times the target's Charisma or mettle (including any spe-\nci.al.ization related to religion). If the target has not taken an action\nyet this round, she m ay actively defend by generating a mettle total\n(including her faith specialization), but this is considered her action\nfor the round. For undead without a mettle or Charisma score, use\nthe die code of the creatures' controller.\nIf the target bas a lowe r total, she flees the area (if possible).\n",
        effect=GenericEffect(
            description="compare to 2 times the target's Charisma or mettle", difficulty=12
        ),
        duration=DurationAspect("1 minute"),
        range=RangeAspect("20 meters"),
        speed=SpeedAspect.based_on(("range",), ""),
        casting_time=CastingTimeAspect("2 r"),
        other_aspects={},
        other_conditions=[GenericAspect(0, "Difficulty: 15"),
                          OtherAlterant(-1, "Limited to humanoids (including undead) devoted to a different religion/gocl/power or undead controlled by a character devoted to a different religion/god/power")],
    )

bless_weapon = Miracle(
        name="Bless Weapon",
        skill="Strife",
        notes="Bless weapon infuses spiritual energy into any one weapo n, as\nlong as the it.em remains within 10 meters of the blessing cleric.\nThe invocation applies the miracle success bonus to the damage of\nthe blessed item.\nA character may enjoy the effects of only one bless at any given\ntime. The cleric may use bless weapon on an item he's holding.\n",
        effect=SkillEffect("+  damage bonus", "+3D"),
        duration=DurationAspect("8 rounds"),
        range=RangeAspect("10 m"),
        speed=SpeedAspect.based_on(("range",), ""),
        casting_time=CastingTimeAspect("2 sec"),
        other_aspects={},
        other_conditions=[GenericAspect(0, "Difficulty: 13")],
    )

curse = Miracle(
        name="Curse",
        skill="Strife",
        notes="The cleric curses a single humanoid target with 10 minutes of\nBad Luck (R2), which doesn't leave the target even if he moves out\nof range. See the description of this Disadvantage in the MC haracter\nOptions\" chapter for details. Each success Level doubles the amount\nof time that the target has the curse.\n",
        effect=DisadvantageEffect("Bad Luck ", 2, note=" Disadvantage"),
        duration=DurationAspect("10 minutes"),
        range=RangeAspect("10 m"),
        speed=SpeedAspect.based_on(("range",), ""),
        casting_time=CastingTimeAspect("1 r"),
        other_aspects={
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On Target"
            )
        },
        other_conditions=[
            GenericAspect(-2, "Limited to humans"),
            GenericAspect(0, "Difficulty: 14"),
        ],
    )

disrupt_spell = Miracle(
        name="Disrupt Spell",
        skill="Strife",
        notes="The cleric concentrates on the spell he wishes to counter. The effect's\nvalue plus the miracle's miracle success bonus are compared to the\nskill total used to create the targeted spell. If the disrupt spell number\nequals or exceeds the target spell's skill total, the spell is broken.\n",
        effect=GenericEffect(
            description="compare to skill total of spell countering", difficulty=29
        ),
        duration=DurationAspect("1 round"),
        range=RangeAspect("60 meters"),
        speed=SpeedAspect.based_on(("range",), ""),
        casting_time=CastingTimeAspect("2 sec"),
        other_aspects={},
        other_conditions=[GenericAspect(0, "Difficulty: 25")],
    )

fighting_tree = Miracle(
        name="Fighting Tree",
        skill="Strife",
        notes="Through this prayer, the cleric can animate the branches of a\ntree to strike at anyone within range. Branches that hit the target\ninflict 4D of damage. The tree can strike at no more than Short range\n- less if it's small.\n",
        effect=CompositeEffect("fighting", SkillEffect("fighting", "+4D"), SkillEffect("damage", "4D")),
        duration=DurationAspect("1 hours"),
        range=RangeAspect("5 m"),
        speed=SpeedAspect.based_on(("range",), ""),
        casting_time=CastingTimeAspect("2 seconds"),
        other_aspects={
            "components": ComponentsAspect(
                "A long supple tree or one with long branches", "common"
            )
        },
        other_conditions=[GenericAspect(0, "Difficulty: 23")],
    )

spiritual_bold = Miracle(
        name="Spiritual Bolt",
        skill="Strife",
        notes="The cleric gathers spiritual energy to throw in a bolt at a target.\nIt does 40 in damage at a range of up to 10 meters. She must make\na marksmanship roll to hit the target. The bolt must be fired in the\nsame round that the cleric invokes the invocation.\n",
        effect=SkillEffect("  in damage", "+4D"),
        duration=DurationAspect("3.5 seconds"),
        range=RangeAspect("10 m"),
        speed=SpeedAspect.based_on(("range",), ""),
        casting_time=CastingTimeAspect("1.5 sec"),
        other_aspects={},
        other_conditions=[GenericAspect(0, "Difficulty: 12")],
    )

undead_warrior = Miracle(
        name="Undead Warrior",
        skill="Strife",
        notes="This rite causes any one dead creature to rise in its present state\nto serve as a soldier bonded to the cleric. As this is a basic miracle, it\nimbues the creature with select skills; the cleric may add more and\nincrease the difficulty. The reanimated being cannot think for itself, so\nit ignores all Wound level and bit location penalties. It does what.ever\nthe cleric deaands, until the invoker tells it to stop or the duration\nends. At the end of the duration or if the cleric sends it out of range,\nthe creature falls down in a heap. The invocation's miracle success\nbonus may either add to the range or to the amount of damage the\ncreature does (it has a base Strength Damage of2D); which applica\xad\ntion must be decided before invoking the miracle.",
        effect=CompositeEffect("Warrior",
           SkillEffect("fighting", "+4D"),
           SkillEffect("lifting", "+4D"),
           SkillEffect("running", "1D")
        ),
        duration=DurationAspect("1.5 hours"),
        range=RangeAspect("25 m"),
        speed=SpeedAspect.based_on(("range",), ""),
        casting_time=CastingTimeAspect("2 sec"),
        other_aspects={
            "components": ComponentsAspect("Intact dead body or skeleton", "very rare")
        },
        other_conditions=[GenericAspect(0, "Difficulty: 27")],
    )
spells = [ 
    basish, bless_weapon, curse, disrupt_spell, fighting_tree, spiritual_bold, undead_warrior, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(spells)
    app()

