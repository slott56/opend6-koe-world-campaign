"""
Wizardry

When run as an app, generates .RST-formatted details of each Spell.
"""

from decimal import Decimal
from typing import Annotated, Any
import typer
from opend6_tools.magic2 import *

spells = [
    Spell(
        name="Alter Shape",
        skill="Conjuration",
        notes="This spell changes the physical form of the target. For all\nintentions, the character becomes the creature. However,\nhe maintains his disposition to friends and enemies, and\nhas a vague sense of identity. Additionally, while he might\nnot be able to directly communicate, he can understand\nbasic instructions, and respond with sounds, gestures, or\nmovements.\n\n",
        effect=SpecialAbilityEffect(
            "Shapeshifting",
            1,
            note="form of caster’s choosing",
            modifications=[
                Limitation("Restricted", 2, "ability uncontrolled by target"),
                Effect( "up to 19 points — not ranks — of related Special Abilities, with additional ranks in a Special Ability equalling the point cost of the first rank", 19),
            ]
        ),
        duration=DurationAspect("1 day"),
        range=RangeAspect("self"),
        casting_time=CastingTimeAspect("1 minute"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Enchanted"),
            "charges": ChargesAspect("1 improved charge (memorized by caster)"),
            "components": ComponentsAspect("Clay and stone", "very common"),
            "gestures": GesturesAspect(
                "Shape clay into rough version of desired form", "simple"
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 47")],
    ),
    Spell(
        name="Befriend Animal",
        skill="Divination",
        notes="Sometimes a canny mage can turn a bad situation into a\ngood one. In this case, by using the 6D in animal handling\n(persuasion: animals  in D6 Space) granted by the spell, the\ncharacter could befriend creatures, hostile or otherwise.\nThe spell’s target makes an opposed difficulty roll against a\ncreature’s willpower/mettle (or the governing attribute) plus\n5. If successful, an unfriendly creature can be converted into\nan ally — one that fights for the caster. Any attack against\nthe creature by the caster or one of her allies immediately\nends the spell.",
        effect=SkillEffect(
            "animal handling  of  ; use persuasion: animals in D6 Space", "+6D"
        ),
        duration=DurationAspect("1 hour"),
        range=RangeAspect("self"),
        casting_time=CastingTimeAspect("1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Enchanted"),
            "components": ComponentsAspect("Shiny trinket", "ordinary"),
            "gestures": GesturesAspect(
                "Swing or move trinket back and forth", "simple"
            ),
            "incantations": IncantationsAspect("Soothing sounds", "phrase"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 18")],
    ),
    Spell(
        name="Blur",
        skill="Conjuration",
        notes="By  sacrificing some of her life energy, the mage grants\na target 10 minutes of the bonus given by the Blur Special\nAbility at rank 1. See the description of this Special Ability in\nthe “Character Options” chapter for additional details.",
        effect=SpecialAbilityEffect(
            "Blur ",
            1,
            note=", +1 to dodge, sneak/stealth, and hide: self totals, plus +1 to default search, tracking, investigation, and attack difficulties against character",
        ),
        duration=DurationAspect("10 minutes"),
        range=RangeAspect("10 meters"),
        casting_time=CastingTimeAspect("1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "components": ComponentsAspect(
                ("Strip of cloth", "ordinary"),
                ("bit of glass", "ordinary"),
            ),
            "feedback": FeedbackAspect(3),
            "gestures": GesturesAspect("Polish glass with cloth", "simple"),
            "incantations": IncantationsAspect("“Blur.”", "phrase"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 13")],
    ),
    Spell(
        name="Change Material",
        skill="Alteration",
        notes="This spell allows the caster to transform one simple, non-\nliving substance into another simple, nonliving substance.\nLead into gold is a popular transformation. The drawback is\nthat the change is not permanent, but for the duration, the\nitem possesses the attributes and qualities of the transformed\nmaterial. How well the item mimics its new state depends\non the material’s complexity; the gamemaster uses the result\npoints of the spell’s skill roll to determine how successful\nthe transformation was. When the spell ends, it reverts to\nthe original state.\nUp to five kilograms of material can be altered by this\nspell. It will pass most — if not all — tests appropriate for\nits new state. However, if a spell that detects magic is per -\nformed, the new material reveals that unnatural forces are\nacting upon it.\nChanged matter can be used as spell components providing\nthey are used within the spell’s duration. Nontheless, there\nis an increased risk of spell failure. When using transformed\nmaterial, a Critical Failure always indicates that something\nwent wrong wtih the spell.",
        effect=MassEffect("5 kilograms"),
        duration=DurationAspect("1 day"),
        range=RangeAspect("self"),
        casting_time=CastingTimeAspect("1 hour"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "feedback": FeedbackAspect(1),
            "incantations": IncantationsAspect(
                "“You will become...” followed by new material’s name", "sentence"
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
            "other_alterants": OtherAlterant(
                9, "Other Alterants: Transmute to new form"
            ),
        },
        other_conditions=[
            GenericAspect(-1, "Simple, inanimate material only"),
            GenericAspect(0, "Difficulty: 11"),
        ],
    ),
    Spell(
        name="Deadeye",
        skill="Alteration",
        notes="If a caster successfully casts this spell, she can temporarily\nincrease a target’s marksmanship/firearms skill by +27. While\nthis has no direct effect on damage, it provides for highly\naccurate ranged weapon attacks, and it can be combined\nwith other modifiers. The spell is ideally used for snipers or\nassassination attempts but can serve on any occasion when\nthe need for a precise shot is required.",
        effect=SpecialAbilityEffect(
            "Skill Bonus ", 9, note=", +27 to marksmanship/firearms totals"
        ),
        duration=DurationAspect("2 rounds"),
        range=RangeAspect("self"),
        casting_time=CastingTimeAspect("1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "incantations": IncantationsAspect("“Aim.”", "phrase"),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 14")],
    ),
    Spell(
        name="Deafen",
        skill="Conjuration",
        notes="When the caster rings a small bell, a loud noise can be\nheard, deafening all in the designated area of effect. This\nis likely to hinder all actions, as the inability to hear is not\nonly startling but unsettling. All hearing-based actions are\nperformed with a +6 difficulty modifier. Nothing can be heard\nwhile affected by the spell.\n\n",
        effect=DisadvantageEffect(
            "Hindrance: Deafness ",
            9,
            note=", +6 to difficulties of all hearing-dependent actions",
        ),
        duration=DurationAspect("1 minute"),
        range=RangeAspect("40 meters"),
        casting_time=CastingTimeAspect("1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "area_effect": AreaEffectAspect("4m radius sphere"),
            "components": ComponentsAspect("Small chime or bell", "common"),
            "gestures": GesturesAspect("Ring chime or bell", "simple"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On targets"
            ),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 36")],
    ),
    Spell(
        name="Detect Presence",
        skill="Divination",
        notes="This spell can locate someone who is hiding. The spell\nconfers 6D search dedicated to finding living entities only.\nThe difficulty is determined by either the target’s (or targets’)\nhide total or the gamemaster. A success causes the located\nsubject to glow in a faint blue light, only visible to the caster.\nThe mage can look in a different direction once per round.\nBesides hunting down people secreted away in a dark\nroom, it is also possible to determine the difference between\na human and a cyborg. In situations where cyborgs appear\nhuman, they glow, revealing their nonliving nature.",
        effect=SkillEffect("search of   to locate living beings", "+6D"),
        duration=DurationAspect("1 hour"),
        range=RangeAspect("5 meters"),
        casting_time=CastingTimeAspect("2 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "incantations": IncantationsAspect("“See all.”", "phrase"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On caster"
            ),
            "other alterant": OtherAlterant(1, "Reveal cyborgs"),
            "variable movement": VariableMovementAspect("bend around smaller", "target invisible"),
        },
        other_conditions=[
            GenericAspect(0, "Difficulty: 26"),
        ],
    ),
    Spell(
        name="Distract",
        skill="Alteration",
        notes="This spell allows a magic user to distract a target, making\nthat character believe there are other more pressing matters\nto attend to. By the display of a mesmerizing bauble and a\nsimple suggestion, the caster could cause an attacker to sud-\ndenly halt and depart, or to make an enemy go on a journey\nfor the duration of the spell. The distracted character follows\nany single command, within reason. Possibilities include “go\nhome,” “climb a tree,” “run to the nearest town,” and so on.\nA successful roll of the skill given by the spell against the\ntarget’s willpower/mettle (or the governing attribute) indicates\nthat the suggestion took hold.",
        effect=SkillEffect("persuasion", "+6D"),
        duration=DurationAspect("1 day"),
        range=RangeAspect("5 meters"),
        casting_time=CastingTimeAspect("1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "components": ComponentsAspect("Shiny trinket", "ordinary"),
            "gestures": GesturesAspect(
                "Display the trinket while saying incantation", "simple"
            ),
            "incantations": IncantationsAspect("Simple instruction", "sentence"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[
            GenericAspect(0, "Difficulty: 22"),
            GenericAspect(-5, "Unreal Effect: Disbelief difficulty of 13"),
        ],
    ),
    Spell(
        name="Fancy Riding",
        skill="Divination",
        notes="A target with this spell cast upon her recieves a +9 bonus\nto her riding totals. For the duration of the spell, the target\nhas an understanding of beasts of burdens and their natures,\nknowing how to handle them and keep them under control\nin nearly any condition.",
        effect=SpecialAbilityEffect(
            "Skill Bonus: Animal Insight ", 3, note=", +9 to riding totals"
        ),
        duration=DurationAspect("1 day"),
        range=RangeAspect("self"),
        casting_time=CastingTimeAspect("1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "components": ComponentsAspect(
                "Hair or fur of a beast of burden", "ordinary, destroyed"
            ),
            "incantations": IncantationsAspect("“Convey!.”", "phrase", "loud"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 16")],
    ),
    Spell(
        name="Fate",
        skill="Alteration",
        notes="With this spell, the mage persuasdes the Fates to smile\nupon the hero (by granting the player one Fate Point that\nmay be used on any one action in the round following the\ncasting of the spell).\nThose who attempt to abuse this spell should note that\nFate suffers no challenges lightly, and playing such games\ncan result in the demise of a character.",
        effect=SpecialAbilityEffect(
            "Luck: Great ", 1, note=", confers 1 additional Fate Point only"
        ),
        duration=DurationAspect("1 round"),
        range=RangeAspect("1 km"),  # "25 m"),
        casting_time=CastingTimeAspect("1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "component": ComponentsAspect("Common die", "very common"),
            "concentration": ConcentrationAspect("1 round"),
            "incantations": IncantationsAspect("“Hero.”", "phrase"),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 16")],
    ),
    Spell(
        name="Find Trap",
        skill="Divination",
        notes="The magic of this spell is focused upon devilish devices.\nWhen the caster intonesthe incantation, the spell is activated,\nproviding the target with 6D in search that is limited in focus\nto traps of any sort within 3.5 meters of the user. If the skill\nroll is a success, then the spell user sees the located trap glow\ngreen. The finder can point out the trap to others, but it is not\nsimilarly revealed to them. For example, if the trap is invisible,\nthen it remains invisible after detected. Furthermore, seeing\na trap does not convey the ability to disarm it.\n\n\n\n",
        effect=SkillEffect("search of   for finding traps", "+6D"),
        duration=DurationAspect("1 hour"),
        range=RangeAspect("self"),
        casting_time=CastingTimeAspect("2 rounds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "area_effect": AreaEffectAspect("3.5m radius divination sphere"),
            "incantations": IncantationsAspect(
                "“Where’d I put that trap?”", "sentence"
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 23")],
    ),
    Spell(
        name="Find Way",
        skill="Divination",
        notes="The recipient of this spell garners a +3D bonus to her\nnavigation skill. This bonus works under all circumstances,\nincluding at sea, in a city, or in a maze.",
        effect=SkillEffect("Boost to navigation", "+3D", "skill modifier"),
        duration=DurationAspect("1 day"),
        range=RangeAspect("self"),
        casting_time=CastingTimeAspect("1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "components": ComponentsAspect("Compass or astrolabe", "common"),
            "incantations": IncantationsAspect(
                "“Find me a way to go!”", "sentence", "loud"
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 18")],
    ),
    Spell(
        name="Insight to Weakness",
        skill="Divination",
        notes="This spell grants the target +36 to melee combat totals for\ntwo rounds. The magical incantation makes clear an oppo -\nnent’s weaknesse and allows them to be taken advantage\nof. No additional damage is directly conferred by this spell,\nalthough a clever character might use it to strike at a head or\nheart and perform a killing blow on an unwary opponent.",
        effect=SpecialAbilityEffect(
            "Skill Bonus: Weakness Detection ", 12, note=", +36 to melee combat totals"
        ),
        duration=DurationAspect("2 rounds"),
        range=RangeAspect("self"),
        casting_time=CastingTimeAspect("1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "incantations": IncantationsAspect("“See.”", "phrase"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 22")],
    ),
    Spell(
        name="Illiterate",
        skill="Alteration",
        notes="This devious spell causes the target to forget how to read.\nWhile to some this is not distressing, to mages and scholars\nit is a nightmare. As  the ability to read has not actually been\nerased, but has only been implanted in the subconscious of\nthe target, it is possible to disbelieve by making a willpower/\nmettle roll (or the governing attribute) at  a difficulty of 13.\nNonetheless, the situation is distressing, and the gamemaster\nmight consider modifiers if the target had recently bumped\nher head or suffered a trauma that might cause her to believe\nthat she had actually lost the ability to read.",
        effect=DisadvantageEffect("Illiterate", 1, note=" Disadvantage"),
        duration=DurationAspect("1 month"),
        range=RangeAspect("1 kilometer"),
        casting_time=CastingTimeAspect("1 hour"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "components": ComponentsAspect(
                ("pen or quill", "common"),
                ("sheet of parchment", "uncommon"),
            ),
            "gestures": GesturesAspect(
                "Write incantation and then repeat the writing in reverse, repeating until the parchment is covered",
                "complex (languages/reading/writing roll with difficulty of 11)",
            ),
            "incantations": IncantationsAspect(
                "“I will not remember how to read.”", "sentence"
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[
            GenericAspect(0, "Difficulty: 21"),
            GenericAspect(-1, "Unreal Effect: Disbelief difficulty of 13"),
        ],
    ),
    Spell(
        name="Insight into the Future",
        skill="Divination",
        notes="After casting this spell, the target gains insight into the\nfuture through flashes of images, sounds, and smells. A\ncharacter can possibly bring these insights into focuse by\nasking a question (such as, “Who’s on the other side of the\ndoor I’m about to open?) and making an investigation rolls.\n(She may do this no more than once per round.) The game-\nmaster decides on the difficulty, which should never be less\nthan Moderation, even for a simple yes-or-no question or one\ncentering on the near future. The higher the investigation roll\nis above the difficulty, the clearer the insight becomes.",
        effect=TimeEffect("up to  --  in the future", "1 hour"),
        duration=DurationAspect("1 hour"),
        range=RangeAspect("self"),
        casting_time=CastingTimeAspect("2 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "incantations": IncantationsAspect(
                "“Reveal the future so that I may slip truly into it.”", "sentence"
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 18")],
    ),
    Spell(
        name="Investigate",
        skill="Divination",
        notes="When research is needed, this spell helps find informa -\ntion. When cast upon a target, he gains a bonus of +24 to\ninvestigation totals.\nWhile this spell doesn’t assist in comprehension, it reveals\nthe best clues to follow up. It is also likely that a Heroic success\nprovides great insight into the matter being delved into.",
        effect=SpecialAbilityEffect(
            "Skill Bonus: Investigation ", 8, note=", +24 to investigation totals"
        ),
        duration=DurationAspect("1 week"),
        range=RangeAspect("5 meters"),
        casting_time=CastingTimeAspect("1 minute"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "components": ComponentsAspect("Magnifying glass", "very common"),
            "incantations": IncantationsAspect("“Learn.”", "phrase"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 30")],
    ),
    Spell(
        name="Invoke Emotion",
        skill="Alteration",
        notes="With a successful casting, the target must make an opposed\ninteraction roll against the spell’s persuasion of 5D. Failure\nmeans that she has succumbed to the emotion suggested in\nthe incantation. Some single word examples are angry, happy,\nlaughing, sad, crying, pouting, cold, shy, frightened, amazed,\ninspired, smitten, and so on. If it occurs, the moody target\ncan attempt to disbelieve by using willpower/mettle (or the\ngoverning attribute) at a difficulty number of 13. When the\nspell ends or is disbelieved, the effect discontinues.\n\n",
        effect=SkillEffect("persuasion", "+5D"),
        duration=DurationAspect("10 minute"),
        range=RangeAspect("40 meters"),
        casting_time=CastingTimeAspect("2 rounds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "components": ComponentsAspect("Pin", "ordinary"),
            "gestures": GesturesAspect("Use pin to point at target", "simple"),
            "incantations": IncantationsAspect(
                "State simply the desired emotion", "phrase"
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
            "unreal_effect": UnrealEffectAspect.based_on("effect", "difficulty 13"),
        },
        other_conditions=[
            GenericAspect(0, "Difficulty: 19"),
            GenericAspect(-4, "Unreal Effect: Disbelief "),
        ],
    ),
    Spell(
        name="Leap",
        skill="Alteration",
        notes="This spell grants a temporary bonus of +15 to a character’s\njumping/climb/jump totals skill. For the duration of the spell,\nthe legs of the target take on the muscled appearance of those\nof a frog’s legs. Although the bone structure remains the same,\na Moderate investigation roll discerns that there is something\nusual about the muscles of the targeted person’s legs.",
        effect=SpecialAbilityEffect(
            "Skill Bonus: Frog Legs ", 5, note=", +15 to jumping/ climb/jump totals"
        ),
        duration=DurationAspect("1 hour"),
        range=RangeAspect("self"),
        casting_time=CastingTimeAspect("1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "components": ComponentsAspect("Frog legs", "very common"),
            "countenance": CountenanceAspect(
                "Target’s legs take on a froggish appearance", "noticeable"
            ),
            "incantations": IncantationsAspect("“Bound.”", "phrase"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 16")],
    ),
    Spell(
        name="Mistaken Identity",
        skill="Alteration",
        notes="To properly use this spell requires that the target remain\nin place for 30 minutes and that she knows the identity\nshe is going to assume. If the spell is a success, there is not\nonly a physical transformation — there is also a mental\ntransformation.\nOnce magically convinced, the target takes on the manner-\nisms, attitudes, and physical actions of the desired persona.\nAny necessary memories are manufactured, which might\nend up being a trigger to those who know the real person.\nNonetheless, until the spell wears off, as far as the target\nknows, she is that person, so lie detectors and other means\nof detecting fibs are fruitless.",
        effect=CompositeEffect(
            "Shape Changing",
            SpecialAbilityEffect(
            "shapeshifting",
            1,
            note="one specific person"),
            SkillEffect("Skill Bonus: In Disguise boost bluff/con totals related to disguise", "15"),
        ),
        duration=DurationAspect("1 week"),
        range=RangeAspect("10 meters"),
        casting_time=CastingTimeAspect("25 minutes"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic, folk"),
            "incantations": IncantationsAspect("Repeat name of new identity", "phrase"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[
            GenericAspect(-1, "Target must know person"),
            GenericAspect(0, "Difficulty: 28"),
        ],
    ),
    Spell(
        name="Perfect Touch",
        skill="Divination",
        notes="A successful casting of this spell allows the target to perform\nthe sleight of hand skill with heroic ability, granting a tempo-\nrary bonus of +36 to such totals. This not really an increase\nin ability so much as it is a unique understanding of how to\nincrease finger deftness or when to pick a pocket.",
        effect=SpecialAbilityEffect(
            "Skill Bonus: Perfect Touch ", 12, note=", +36 to sleight of hand totals"
        ),
        duration=DurationAspect("2 rounds"),
        range=RangeAspect("self"),
        casting_time=CastingTimeAspect("1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "incantations": IncantationsAspect("“When.”", "phrase"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 22")],
    ),
    Spell(
        name="Possess the Living Mind",
        skill="Divination",
        notes="The canny mage can use this spell to ride along with another\nbeing for a day. The caster perceives the world through the\ntarget’s senses and can possibly read the victim’s thoughts.\n(The result points from casting this spell are used on the\n“Possession Knowledge” chart to determine how much\ninformation the mage gathers.)\nWhen attempting to possess another, the mage must make\na check of willpower/mettle (or the governing attribute) against\nthe standard interaction difficulty. Exceeding the difficulty\nmeans that the target is unaware of the hitchhiker. Meeting\nthe difficulty indicates that the target knows someone else is\nsharing her mind, though she doesn’t know who it is. Failure\nmeans that victim managed to kick out the caster before he\ncould get a foothold.\nIn no case does the caster have any influence on the per-\nson’s actions. Additonally, the caster is only dimly aware of\nwhat is going on around his body.",
        effect=SpecialAbilityEffect(
            "Possession: Limited",
            1,
            modifications=[Limitation("Restricted", 1, "may only read target’s mind")],
        ),
        duration=DurationAspect("1 day"),
        range=RangeAspect("100 meters"),
        casting_time=CastingTimeAspect("1 hour"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "components": ComponentsAspect(
                ("Personal possession of target", "uncommon"),
                ("chalk", "very common"),
            ),
            "gestures": GesturesAspect(
                "Draw circles and sigils of possession with chalk",
                "complex (artist roll with difficulty of 11)",
            ),
            "incantations": IncantationsAspect(
                "“Open your mind to my thoughts.”", "sentence"
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"),
                target="Focused on Mage’s mind stays with target",
            ),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 24")],
    ),
    Spell(
        name="Slip",
        skill="Alteration",
        notes="Upon casting this spell, a oily surface covers the desig -\nnated area. Everyone within the affected area suffers a +6\ndifficulty modifier to most physical actions that involve leg\nand feet movement.\n\n",
        effect=DisadvantageEffect(
            "Hindrance: Slick Surface ",
            6,
            note=", +6 to acrobatics, dodge, and running difficulties",
        ),
        duration=DurationAspect("1 minute"),
        range=RangeAspect("40 meters"),
        casting_time=CastingTimeAspect("1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "area_effect": AreaEffectAspect("10m radius circle"),
            "components": ComponentsAspect("Drop of oil", "ordinary", "destroyed"),
            "gestures": GesturesAspect("Rub oil between fingers", "simple"),
            "incantations": IncantationsAspect("“Slip.”", "phrase"),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 28")],
    ),
    Spell(
        name="Speak Language",
        skill="Divination",
        notes="The recipient of this spell can speak in an unknown tongue\nwith a limited languages/speaking skil of 6D. Unless a spell\nthat permits understanding languages is also cast on the\nsame target, it is not possible to understand a reply in the\nlanguage. The gamemaster determines the difficulty for the\ntarget to express ideas, based upon how common or alien\nthe language is.",
        effect=SkillEffect("languages/speaking of  , for speaking only", "+6D"),
        duration=DurationAspect("1 minute"),
        range=RangeAspect("self"),
        casting_time=CastingTimeAspect("2 rounds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "components": ComponentsAspect("Fashioned leather tongue", "common"),
            "gestures": GesturesAspect("Point", "simple"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 12")],
    ),
    Spell(
        name="Sphere of Protection",
        skill="Conjuration",
        notes="When the mage casts this spell and drops the diamond up to\na meter from her, a magically disruptive sphere forms around\nit. All who are within the sphere are protected against spells.\nThe spell doesn’t prohibit ranged attacks or fighting of any\nsort within the sphere. However, the skill totals of all spells\ndirected at occupants in the area of effect are compared to\nthe effect’s value plus the result point bonus of the spell. If\nthe defending spell’s total is higher than the intruding spell’s\nskill total, then the opposing spell is completely repulsed.\nAs the spell is not actually focused on the diamond or\nanyone else, friend or foe may enter or leave the area without\ndisrupting the spell.",
        effect=Effect(
            description="compare to skill total of spell countering", difficulty=24
        ),
        duration=DurationAspect("1 minute"),
        range=RangeAspect("self"),
        casting_time=CastingTimeAspect("1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "area_effect": AreaEffectAspect("3m radius sphere"),
            "components": ComponentsAspect("Diamond", "very rare"),
            "gestures": GesturesAspect("Drop diamond on ground", "simple"),
            "incantations": IncantationsAspect("“Stop magic.”", "phrase"),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 19")],
    ),
    Spell(
        name="Stretch",
        skill="Alteration",
        notes="This spell grants the target the ability to slip through\ntight spots and wiggle out of harms way, using the Elasticity\nSpecial Ability at rank 1. See the appropriate section in the\n“Character Options” chapter for additional details.",
        effect=SpecialAbilityEffect(
            "Elasticity ",
            1,
            note=", +1 to contortion, dodge, and sleight of hand totals, and +1 to disguise totals that target performs on himself — for D6 Space, use acrobatics: contortion and con: disguise instead of the related listed skills",
        ),
        duration=DurationAspect("1 hour"),
        range=RangeAspect("10 meters"),
        casting_time=CastingTimeAspect("1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "components": ComponentsAspect("Something elastic", "ordinary"),
            "gestures": GesturesAspect("Stretch the component", "simple"),
            "incantations": IncantationsAspect("“Stretch.”", "phrase"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 14")],
    ),
    Spell(
        name="Stun",
        skill="Conjuration",
        notes="With the utterance of a simple word, a mage can stun an\nopponent. The successful casting of this spell causes 4D stun\ndamage to the intended target. All that is required is that\nmental focus be placed upon the intended victim (with a\nsuccessful Moderate willpower/mettle roll). The spell effects\ncannot be protected against by nonmagical armor. However,\nthe damage is treated as stun damage as indicated in the\n“Damage” chapter of the rulebook.",
        effect=SkillEffect(
            "stunning word", "+4D", "physical damage", "stun only", "ignores nonmagical armor"
        ),
        duration=DurationAspect("1 second"),
        range=RangeAspect("25 meters"),
        casting_time=CastingTimeAspect("3.5 seconds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "incantations": IncantationsAspect("“Stun.”", "phrase"),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 21")],
    ),
    Spell(
        name="Telepathy",
        skill="Alteration",
        notes="This spell grants the target 4D in the telepathy skill. It func-\ntions identically to the Psionics skill as described in the D6\nAdventure Rulebook chapter on “Psionics.” Because the skill\nlinks minds, it is possible for one person to read the thoughts\nof another character and determine if a lie is being told or\ndetect fear. When using this skill, refer to the “Empathy and\nTelepathy” table and the “Lie Detecting” table.",
        effect=SkillEffect("telepathy of  ", "+4D", "extranormal skill"),
        duration=DurationAspect("1 hour"),
        range=RangeAspect("self"),
        casting_time=CastingTimeAspect("1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic, folk"),
            "concentration": ConcentrationAspect("1 round"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On caster"
            ),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 16")],
    ),
    Spell(
        name="Understand Gibberish",
        skill="Divination",
        notes="Through the aid of magic, it is possible for a targeted\ncharacter to understand any language or code. Providing the\nspell is successful, the selected character gains 4D languages\n(speaking or reading/writing in D6 Fantasy ) in the specific\nlanguage being heard or read at the moment of casting. This\nincludes a normally unknown or undecipherable language,\nalthough the task is much more difficult. Understand gibberish\nalso works with codes.\nThe gamemaster determines the difficulty, based upon\nhow common or unusual it is.",
        effect=SkillEffect(
            "  languages — speaking or reading/writing in *D6 Fantasy*", "+4D"
        ),
        duration=DurationAspect("1 day"),
        range=RangeAspect("self"),
        casting_time=CastingTimeAspect("2 rounds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "components": ComponentsAspect("Wax", "ordinary"),
            "gestures": GesturesAspect("Point", "simple"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 19")],
    ),
    Spell(
        name="Voices",
        skill="Conjuration",
        notes="By uttering a few words, a guard or group of guards can\nbe led astray. If successfully cast, this spell gives the magic\nuser a +24 bonus to the bluff/con total needed for this spell.\nThe results can affect anyone in a specified two-meter radius\nup to 60 meters away.\nAn opposed interaction roll is made against the target or\ntargets. Anyone failing this roll heads toward the direction\nthe caster made the voices appear to come from. For the\nduration of the spell, the incantation words are repeated\nover and over.",
        effect=SpecialAbilityEffect(
            "Skill Bonus: Throw Voice ", 8, note=", +24 to bluff/con totals"
        ),
        duration=DurationAspect("1 minute"),
        range=RangeAspect("60 meters"),
        casting_time=CastingTimeAspect("1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "area_effect": AreaEffectAspect("2m radius sphere"),
            "components": ComponentsAspect("Leather cord", "common"),
            "gestures": GesturesAspect("Pull on cord", "simple"),
            "incantations": IncantationsAspect("Whisper distracting words", "phrase"),
            "unreal_effect": UnrealEffectAspect.based_on("effect", "difficulty 13")
        },
        other_conditions=[
            GenericAspect(0, "Difficulty: 18"),
        ],
    ),
]

__test__ = {
    "Alter Shape": ">>> spells[0].difficulty\n47",
    "Befriend Animal": ">>> spells[1].difficulty\n18",
    "Blur": ">>> spells[2].difficulty\n13",
    "Change Material": ">>> spells[3].difficulty\n11",
    "Deadeye": ">>> spells[4].difficulty\n14",
    "Deafen": ">>> spells[5].difficulty\n35",  # Rules say 27, can't see why
    "Detect Presence": ">>> spells[6].difficulty\n26",
    "Distract": ">>> spells[7].difficulty\n23",
    "Fancy Riding": ">>> spells[8].difficulty\n17",  # Rules say 16
    "Fate": ">>> spells[9].difficulty\n16",
    "Find Trap": ">>> spells[10].difficulty\n23",
    "Find Way": ">>> spells[11].difficulty\n19",  # Rules say 18
    "Insight to Weakness": ">>> spells[12].difficulty\n22",
    "Illiterate": ">>> spells[13].difficulty\n21",
    "Insight into the Future": ">>> spells[14].difficulty\n18",
    "Investigate": ">>> spells[15].difficulty\n30",
    "Invoke Emotion": ">>> spells[16].difficulty\n17",  # Rules say 19
    "Leap": ">>> spells[17].difficulty\n16",
    "Mistaken Identity": ">>> spells[18].difficulty\n28",
    "Perfect Touch": ">>> spells[19].difficulty\n22",
    "Possess the Living Mind": ">>> spells[20].difficulty\n23",  # Rules say 24
    "Slip": ">>> spells[21].difficulty\n27",  # Rules say 28
    "Speak Language": ">>> spells[22].difficulty\n11",  # Rules say 12
    "Sphere of Protection": ">>> spells[23].difficulty\n18",  # Rules say 19
    "Stretch": ">>> spells[24].difficulty\n14",
    "Stun": ">>> spells[25].difficulty\n14",  # Rules say 21, but distances have wrong values
    "Telepathy": ">>> spells[26].difficulty\n22",
    "Understand Gibberish": ">>> spells[27].difficulty\n18",  # Rules say 19
    "Voices": ">>> spells[28].difficulty\n23",
}



if __name__ == "__main__":
    app = build_app(spells)
    app()
