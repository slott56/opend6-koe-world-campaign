"""
Wizardry
--------

"""

from magic1 import Aspect, Spell, detail

spells = [
    Spell(
        effect=Aspect(
            format="Shapeshifting (R1), form of caster’s choosing, with Restricted (R2), ability uncontrolled by target; plus up to 19 points — not ranks — of related Special Abilities, with additional ranks in a Special Ability equalling the point cost of the first rank",
            base_difficulty=60,
            count=1,
        ),
        duration=Aspect(format="1 day ", base_difficulty=25, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        name="Alter Shape",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Enchanted", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="47", base_difficulty=0, count=1),
            "Charges": Aspect(
                format="1 improved charge, memorized by caster",
                base_difficulty=5,
                count=1,
            ),
            "Components": Aspect(
                format="Clay and stone (very common)", base_difficulty=-2, count=1
            ),
            "Focused": Aspect(format="On target", base_difficulty=17, count=1),
            "Gestures": Aspect(
                format="Shape clay into rough version of desired form (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes="This spell changes the physical form of the target. For all\nintentions, the character becomes the creature. However,\nhe maintains his disposition to friends and enemies, and\nhas a vague sense of identity. Additionally, while he might\nnot be able to directly communicate, he can understand\nbasic instructions, and respond with sounds, gestures, or\nmovements.\n\n",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="animal handling  of 6D; use persuasion: animals in D6 Space",
            base_difficulty=18,
            count=1,
        ),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Befriend Animal",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Enchanted", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="18", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Shiny trinket (ordinary)", base_difficulty=-1, count=1
            ),
            "Focused": Aspect(format="On target", base_difficulty=7, count=1),
            "Gestures": Aspect(
                format="Swing or move trinket back and forth (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Incantations": Aspect(
                format="Soothing sounds (phrase)", base_difficulty=-1, count=1
            ),
        },
        notes="Sometimes a canny mage can turn a bad situation into a\ngood one. In this case, by using the 6D in animal handling\n(persuasion: animals  in D6 Space) granted by the spell, the\ncharacter could befriend creatures, hostile or otherwise.\nThe spell’s target makes an opposed difficulty roll against a\ncreature’s willpower/mettle (or the governing attribute) plus\n5. If successful, an unfriendly creature can be converted into\nan ally — one that fights for the caster. Any attack against\nthe creature by the caster or one of her allies immediately\nends the spell.",
        skill="Divination",
    ),
    Spell(
        effect=Aspect(
            format="Blur (R1), +1 to dodge, sneak/stealth, and hide: self totals, plus +1 to default search, tracking, investigation, and attack difficulties against character",
            base_difficulty=9,
            count=1,
        ),
        duration=Aspect(format="10 minutes ", base_difficulty=14, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Blur",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="13", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Strip of cloth (ordinary); bit of glass (ordinary",
                base_difficulty=-2,
                count=1,
            ),
            "Feedback": Aspect(
                format="-3 to damage resistance total", base_difficulty=-3, count=1
            ),
            "Focused": Aspect(format="On target", base_difficulty=4, count=1),
            "Gestures": Aspect(
                format="Polish glass with cloth (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Blur.” (phrase)", base_difficulty=-1, count=1
            ),
        },
        notes="By  sacrificing some of her life energy, the mage grants\na target 10 minutes of the bonus given by the Blur Special\nAbility at rank 1. See the description of this Special Ability in\nthe “Character Options” chapter for additional details.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="5 kilograms", base_difficulty=4, count=1),
        duration=Aspect(format="1 day ", base_difficulty=25, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 hour ", base_difficulty=-18, count=1),
        name="Change Material",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="11", base_difficulty=0, count=1),
            "Feedback": Aspect(
                format="-1 to damage resistance total", base_difficulty=-1, count=1
            ),
            "Focused": Aspect(format="On target", base_difficulty=5, count=1),
            "Incantations": Aspect(
                format="“You will become...” followed by new material’s name (sentence)",
                base_difficulty=-2,
                count=1,
            ),
            "Other Alterants": Aspect(
                format="Transmute to new form", base_difficulty=9, count=1
            ),
        },
        other_conditions=[
            Aspect(
                format="Simple, inanimate material only", base_difficulty=-1, count=1
            )
        ],
        notes="This spell allows the caster to transform one simple, non-\nliving substance into another simple, nonliving substance.\nLead into gold is a popular transformation. The drawback is\nthat the change is not permanent, but for the duration, the\nitem possesses the attributes and qualities of the transformed\nmaterial. How well the item mimics its new state depends\non the material’s complexity; the gamemaster uses the result\npoints of the spell’s skill roll to determine how successful\nthe transformation was. When the spell ends, it reverts to\nthe original state.\nUp to five kilograms of material can be altered by this\nspell. It will pass most — if not all — tests appropriate for\nits new state. However, if a spell that detects magic is per -\nformed, the new material reveals that unnatural forces are\nacting upon it.\nChanged matter can be used as spell components providing\nthey are used within the spell’s duration. Nontheless, there\nis an increased risk of spell failure. When using transformed\nmaterial, a Critical Failure always indicates that something\nwent wrong wtih the spell.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="Skill Bonus (R9), +27 to marksmanship/firearms totals",
            base_difficulty=27,
            count=1,
        ),
        duration=Aspect(format="2 rounds ", base_difficulty=5, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Deadeye",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="14", base_difficulty=0, count=1),
            "Incantations": Aspect(
                format="“Aim.” (phrase)", base_difficulty=-1, count=1
            ),
        },
        notes="If a caster successfully casts this spell, she can temporarily\nincrease a target’s marksmanship/firearms skill by +27. While\nthis has no direct effect on damage, it provides for highly\naccurate ranged weapon attacks, and it can be combined\nwith other modifiers. The spell is ideally used for snipers or\nassassination attempts but can serve on any occasion when\nthe need for a precise shot is required.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="Hindrance: Deafness (R9), +6 to difficulties of all hearing-dependent actions",
            base_difficulty=27,
            count=1,
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="40 meters ", base_difficulty=8, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=8, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Deafen",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="36", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Sphere with radius of 4 meters", base_difficulty=20, count=1
            ),
            "Components": Aspect(
                format="Small chime or bell (common)", base_difficulty=-3, count=1
            ),
            "Focused": Aspect(format="On targets", base_difficulty=7, count=1),
            "Gestures": Aspect(
                format="Ring chime or bell (simple)", base_difficulty=-1, count=1
            ),
        },
        notes="When the caster rings a small bell, a loud noise can be\nheard, deafening all in the designated area of effect. This\nis likely to hinder all actions, as the inability to hear is not\nonly startling but unsettling. All hearing-based actions are\nperformed with a +6 difficulty modifier. Nothing can be heard\nwhile affected by the spell.\n\n",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="search of 6D to locate living beings", base_difficulty=18, count=1
        ),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="5 meters ", base_difficulty=4, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=4, count=1),
        casting_time=Aspect(format="2 round ", base_difficulty=-5, count=1),
        name="Detect Presence",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="26", base_difficulty=0, count=1),
            "Focused": Aspect(format="On caster", base_difficulty=7, count=1),
            "Incantations": Aspect(
                format="“See all.” (phrase)", base_difficulty=-1, count=1
            ),
            "Variable Movement": Aspect(
                format="Bending/unseen target", base_difficulty=5, count=1
            ),
            "Other Alterant": Aspect(
                format="Reveal cyborgs", base_difficulty=1, count=1
            ),
        },
        notes="This spell can locate someone who is hiding. The spell\nconfers 6D search dedicated to finding living entities only.\nThe difficulty is determined by either the target’s (or targets’)\nhide total or the gamemaster. A success causes the located\nsubject to glow in a faint blue light, only visible to the caster.\nThe mage can look in a different direction once per round.\nBesides hunting down people secreted away in a dark\nroom, it is also possible to determine the difference between\na human and a cyborg. In situations where cyborgs appear\nhuman, they glow, revealing their nonliving nature.",
        skill="Divination",
    ),
    Spell(
        effect=Aspect(format="persuasion of 6D", base_difficulty=18, count=1),
        duration=Aspect(format="1 day ", base_difficulty=25, count=1),
        range=Aspect(format="5 meters ", base_difficulty=4, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=4, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Distract",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(
                format="22", base_difficulty=0, count=1
            ),  # Should be 23
            "Components": Aspect(
                format="Shiny trinket (ordinary)", base_difficulty=-1, count=1
            ),
            "Focused": Aspect(format="On target", base_difficulty=8, count=1),
            "Gestures": Aspect(
                format="Display the trinket while saying incantation (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Incantations": Aspect(
                format="Simple instruction (sentence)", base_difficulty=-2, count=1
            ),
            "Unreal Effect": Aspect(
                format="Disbelief difficulty of 13", base_difficulty=-5, count=1
            ),
        },
        notes="This spell allows a magic user to distract a target, making\nthat character believe there are other more pressing matters\nto attend to. By the display of a mesmerizing bauble and a\nsimple suggestion, the caster could cause an attacker to sud-\ndenly halt and depart, or to make an enemy go on a journey\nfor the duration of the spell. The distracted character follows\nany single command, within reason. Possibilities include “go\nhome,” “climb a tree,” “run to the nearest town,” and so on.\nA successful roll of the skill given by the spell against the\ntarget’s willpower/mettle (or the governing attribute) indicates\nthat the suggestion took hold.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="Skill Bonus: Animal Insight (R3), +9 to riding totals",
            base_difficulty=9,
            count=1,
        ),
        duration=Aspect(format="1 day ", base_difficulty=25, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Fancy Riding",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="16", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Hair or fur of a beast of burden (ordinary, destroyed)",
                base_difficulty=-2,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=6, count=1),
            "Incantations": Aspect(
                format="“Convey!.” (phrase, loud)", base_difficulty=-2, count=1
            ),
        },
        notes="A target with this spell cast upon her recieves a +9 bonus\nto her riding totals. For the duration of the spell, the target\nhas an understanding of beasts of burdens and their natures,\nknowing how to handle them and keep them under control\nin nearly any condition.",
        skill="Divination",
    ),
    Spell(
        effect=Aspect(
            format="Luck: Great (R1), confers 1 additional Fate Point only",
            base_difficulty=9,
            count=1,
        ),
        duration=Aspect(format="1 round ", base_difficulty=4, count=1),
        range=Aspect(format="25 meters ", base_difficulty=15, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=15, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Fate",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(
                format="16", base_difficulty=0, count=1
            ),  # Should be 18
            "Component": Aspect(
                format="Common die (very common)", base_difficulty=-2, count=1
            ),
            "Concentration": Aspect(
                format="1 round with willpower/mettle difficulty of 8",
                base_difficulty=-1,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Hero.” (phrase)", base_difficulty=-1, count=1
            ),
        },
        notes="With this spell, the mage persuasdes the Fates to smile\nupon the hero (by granting the player one Fate Point that\nmay be used on any one action in the round following the\ncasting of the spell).\nThose who attempt to abuse this spell should note that\nFate suffers no challenges lightly, and playing such games\ncan result in the demise of a character.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="search of 6D for finding traps", base_difficulty=18, count=1
        ),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="2 rounds ", base_difficulty=-5, count=1),
        name="Find Trap",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="23", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Divination sphere with radius of 3.5 meters",
                base_difficulty=9,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=7, count=1),
            "Incantations": Aspect(
                format="“Where’d I put that trap?” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes="The magic of this spell is focused upon devilish devices.\nWhen the caster intonesthe incantation, the spell is activated,\nproviding the target with 6D in search that is limited in focus\nto traps of any sort within 3.5 meters of the user. If the skill\nroll is a success, then the spell user sees the located trap glow\ngreen. The finder can point out the trap to others, but it is not\nsimilarly revealed to them. For example, if the trap is invisible,\nthen it remains invisible after detected. Furthermore, seeing\na trap does not convey the ability to disarm it.\n\n\n\n",
        skill="Divination",
    ),
    Spell(
        effect=Aspect(format="+3D to navigation", base_difficulty=14, count=1),
        duration=Aspect(format="1 day ", base_difficulty=25, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Find Way",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="18", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Compass or astrolabe (common)", base_difficulty=-3, count=1
            ),
            "Focused": Aspect(format="On target", base_difficulty=7, count=1),
            "Incantations": Aspect(
                format="“Find me a way to go!” (sentence, loud)",
                base_difficulty=-3,
                count=1,
            ),
        },
        notes="The recipient of this spell garners a +3D bonus to her\nnavigation skill. This bonus works under all circumstances,\nincluding at sea, in a city, or in a maze.",
        skill="Divination",
    ),
    Spell(
        effect=Aspect(
            format="Skill Bonus: Weakness Detection (R12), +36 to melee combat totals",
            base_difficulty=36,
            count=1,
        ),
        duration=Aspect(format="2 rounds ", base_difficulty=5, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Insight to Weakness",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="22", base_difficulty=0, count=1),
            "Focused": Aspect(format="On target", base_difficulty=8, count=1),
            "Incantations": Aspect(
                format="“See.” (phrase)", base_difficulty=-1, count=1
            ),
        },
        notes="This spell grants the target +36 to melee combat totals for\ntwo rounds. The magical incantation makes clear an oppo -\nnent’s weaknesse and allows them to be taken advantage\nof. No additional damage is directly conferred by this spell,\nalthough a clever character might use it to strike at a head or\nheart and perform a killing blow on an unwary opponent.",
        skill="Divination",
    ),
    Spell(
        effect=Aspect(
            format="Illiterate (R1) Disadvantage", base_difficulty=3, count=1
        ),
        duration=Aspect(format="1 month ", base_difficulty=32, count=1),
        range=Aspect(format="1 kilometer ", base_difficulty=15, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=15, count=1),
        casting_time=Aspect(format="1 hour ", base_difficulty=-18, count=1),
        name="Illiterate",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="21", base_difficulty=0, count=1),
            "Components": Aspect(
                format="pen or quill (common); sheet of parchment (uncommon)",
                base_difficulty=-7,
                count=1,
            ),
            "Gestures": Aspect(
                format="Write incantation and then repeat the writing in reverse, repeating until the parchment is covered (complex; languages/reading/writing roll with difficulty of 11)",
                base_difficulty=-3,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=7, count=1),
            "Incantations": Aspect(
                format="“I will not remember how to read.” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
            "Unreal Effect": Aspect(
                format="Disbelief difficulty of 13", base_difficulty=-1, count=1
            ),
        },
        notes="This devious spell causes the target to forget how to read.\nWhile to some this is not distressing, to mages and scholars\nit is a nightmare. As  the ability to read has not actually been\nerased, but has only been implanted in the subconscious of\nthe target, it is possible to disbelieve by making a willpower/\nmettle roll (or the governing attribute) at  a difficulty of 13.\nNonetheless, the situation is distressing, and the gamemaster\nmight consider modifiers if the target had recently bumped\nher head or suffered a trauma that might cause her to believe\nthat she had actually lost the ability to read.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(format="up to 1 hour in the future", base_difficulty=18, count=1),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="2 round ", base_difficulty=-5, count=1),
        name="Insight into the Future",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="18", base_difficulty=0, count=1),
            "Focused": Aspect(format="On target", base_difficulty=7, count=1),
            "Incantations": Aspect(
                format="“Reveal the future so that I may slip truly into it.” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes="After casting this spell, the target gains insight into the\nfuture through flashes of images, sounds, and smells. A\ncharacter can possibly bring these insights into focuse by\nasking a question (such as, “Who’s on the other side of the\ndoor I’m about to open?) and making an investigation rolls.\n(She may do this no more than once per round.) The game-\nmaster decides on the difficulty, which should never be less\nthan Moderation, even for a simple yes-or-no question or one\ncentering on the near future. The higher the investigation roll\nis above the difficulty, the clearer the insight becomes.",
        skill="Divination",
    ),
    Spell(
        effect=Aspect(
            format="Skill Bonus: Investigation (R8), +24 to investigation totals",
            base_difficulty=24,
            count=1,
        ),
        duration=Aspect(format="1 week ", base_difficulty=29, count=1),
        range=Aspect(format="5 meters ", base_difficulty=4, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=4, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        name="Investigate",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="30", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Magnifying glass (very common)", base_difficulty=-2, count=1
            ),
            "Focused": Aspect(format="On target", base_difficulty=10, count=1),
            "Incantations": Aspect(
                format="“Learn.” (phrase)", base_difficulty=-1, count=1
            ),
        },
        notes="When research is needed, this spell helps find informa -\ntion. When cast upon a target, he gains a bonus of +24 to\ninvestigation totals.\nWhile this spell doesn’t assist in comprehension, it reveals\nthe best clues to follow up. It is also likely that a Heroic success\nprovides great insight into the matter being delved into.",
        skill="Divination",
    ),
    Spell(
        effect=Aspect(format="persuasion of 5D", base_difficulty=15, count=1),
        duration=Aspect(format="10 minute ", base_difficulty=14, count=1),
        range=Aspect(format="40 meters ", base_difficulty=8, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=8, count=1),
        casting_time=Aspect(format="2 rounds ", base_difficulty=-5, count=1),
        name="Invoke Emotion",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="19", base_difficulty=0, count=1),
            "Components": Aspect(format="Pin (ordinary)", base_difficulty=-1, count=1),
            "Focused": Aspect(format="On target", base_difficulty=5, count=1),
            "Gestures": Aspect(
                format="Use pin to point at target (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Incantations": Aspect(
                format="State simply the desired emotion (phrase)",
                base_difficulty=-1,
                count=1,
            ),
            "Unreal Effect": Aspect(
                format="Disbelief difficulty of 13", base_difficulty=-4, count=1
            ),
        },
        notes="With a successful casting, the target must make an opposed\ninteraction roll against the spell’s persuasion of 5D. Failure\nmeans that she has succumbed to the emotion suggested in\nthe incantation. Some single word examples are angry, happy,\nlaughing, sad, crying, pouting, cold, shy, frightened, amazed,\ninspired, smitten, and so on. If it occurs, the moody target\ncan attempt to disbelieve by using willpower/mettle (or the\ngoverning attribute) at a difficulty number of 13. When the\nspell ends or is disbelieved, the effect discontinues.\n\n",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="Skill Bonus: Frog Legs (R5), +15 to jumping/ climb/jump totals",
            base_difficulty=15,
            count=1,
        ),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Leap",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="16", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Frog legs (very common)", base_difficulty=-2, count=1
            ),
            "Countenance": Aspect(
                format="Target’s legs take on a froggish appearance",
                base_difficulty=-1,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=6, count=1),
            "Incantations": Aspect(
                format="“Bound.” (phrase)", base_difficulty=-1, count=1
            ),
        },
        notes="This spell grants a temporary bonus of +15 to a character’s\njumping/climb/jump totals skill. For the duration of the spell,\nthe legs of the target take on the muscled appearance of those\nof a frog’s legs. Although the bone structure remains the same,\na Moderate investigation roll discerns that there is something\nusual about the muscles of the targeted person’s legs.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="Shapechanging (R1), one specific person; Skill Bonus: In Disguise (R5), +15 to bluff/con totals related to disguise",
            base_difficulty=24,
            count=1,
        ),
        duration=Aspect(format="1 week ", base_difficulty=29, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="25 minutes ", base_difficulty=-16, count=1),
        name="Mistaken Identity",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Magic, folk", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="28", base_difficulty=0, count=1),
            "Focused": Aspect(format="On target", base_difficulty=10, count=1),
            "Incantations": Aspect(
                format="Repeat name of new identity (phrase)",
                base_difficulty=-1,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(format="Target must know person", base_difficulty=-1, count=1)
        ],
        notes="To properly use this spell requires that the target remain\nin place for 30 minutes and that she knows the identity\nshe is going to assume. If the spell is a success, there is not\nonly a physical transformation — there is also a mental\ntransformation.\nOnce magically convinced, the target takes on the manner-\nisms, attitudes, and physical actions of the desired persona.\nAny necessary memories are manufactured, which might\nend up being a trigger to those who know the real person.\nNonetheless, until the spell wears off, as far as the target\nknows, she is that person, so lie detectors and other means\nof detecting fibs are fruitless.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="Skill Bonus: Perfect Touch (R12), +36 to sleight of hand totals",
            base_difficulty=36,
            count=1,
        ),
        duration=Aspect(format="2 rounds ", base_difficulty=5, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Perfect Touch",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="22", base_difficulty=0, count=1),
            "Focused": Aspect(format="On target", base_difficulty=8, count=1),
            "Incantations": Aspect(
                format="“When.” (phrase)", base_difficulty=-1, count=1
            ),
        },
        notes="A successful casting of this spell allows the target to perform\nthe sleight of hand skill with heroic ability, granting a tempo-\nrary bonus of +36 to such totals. This not really an increase\nin ability so much as it is a unique understanding of how to\nincrease finger deftness or when to pick a pocket.",
        skill="Divination",
    ),
    Spell(
        effect=Aspect(
            format="Possession: Partial (R1), with Restricted (R1), may only read target’s mind",
            base_difficulty=21,
            count=1,
        ),
        duration=Aspect(format="1 day ", base_difficulty=25, count=1),
        range=Aspect(format="100 meters ", base_difficulty=10, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=10, count=1),
        casting_time=Aspect(format="1 hour ", base_difficulty=-18, count=1),
        name="Possess the Living Mind",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="24", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Personal possession of target (uncommon); chalk (very common)",
                base_difficulty=-5,
                count=1,
            ),
            "Focused": Aspect(
                format="Mage’s mind stays with target", base_difficulty=9, count=1
            ),
            "Gestures": Aspect(
                format="Draw circles and sigils of possession with chalk (complex; artist roll with difficulty of 11)",
                base_difficulty=-3,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Open your mind to my thoughts.” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes="The canny mage can use this spell to ride along with another\nbeing for a day. The caster perceives the world through the\ntarget’s senses and can possibly read the victim’s thoughts.\n(The result points from casting this spell are used on the\n“Possession Knowledge” chart to determine how much\ninformation the mage gathers.)\nWhen attempting to possess another, the mage must make\na check of willpower/mettle (or the governing attribute) against\nthe standard interaction difficulty. Exceeding the difficulty\nmeans that the target is unaware of the hitchhiker. Meeting\nthe difficulty indicates that the target knows someone else is\nsharing her mind, though she doesn’t know who it is. Failure\nmeans that victim managed to kick out the caster before he\ncould get a foothold.\nIn no case does the caster have any influence on the per-\nson’s actions. Additonally, the caster is only dimly aware of\nwhat is going on around his body.",
        skill="Divination",
    ),
    Spell(
        effect=Aspect(
            format="Hindrance: Slick Surface (R6), +6 to acrobatics, dodge, and running difficulties",
            base_difficulty=18,
            count=1,
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="40 meters ", base_difficulty=8, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=8, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Slip",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="28", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Circle with radius of 10 meters", base_difficulty=20, count=1
            ),
            "Components": Aspect(
                format="Drop of oil (ordinary, destoryed)", base_difficulty=-2, count=1
            ),
            "Gestures": Aspect(
                format="Rub oil between fingers (simple)", base_difficulty=-1, count=1
            ),
            "Incantations": Aspect(
                format="“Slip.” (phrase)", base_difficulty=-1, count=1
            ),
        },
        notes="Upon casting this spell, a oily surface covers the desig -\nnated area. Everyone within the affected area suffers a +6\ndifficulty modifier to most physical actions that involve leg\nand feet movement.\n\n",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="languages/speaking of 6D, for speaking only",
            base_difficulty=18,
            count=1,
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="2 rounds ", base_difficulty=-5, count=1),
        name="Speak Language",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="12", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Fashioned leather tongue (common)", base_difficulty=-2, count=1
            ),
            "Focused": Aspect(format="On target", base_difficulty=5, count=1),
            "Gestures": Aspect(format="Point (simple)", base_difficulty=-1, count=1),
        },
        notes="The recipient of this spell can speak in an unknown tongue\nwith a limited languages/speaking skil of 6D. Unless a spell\nthat permits understanding languages is also cast on the\nsame target, it is not possible to understand a reply in the\nlanguage. The gamemaster determines the difficulty for the\ntarget to express ideas, based upon how common or alien\nthe language is.",
        skill="Divination",
    ),
    Spell(
        effect=Aspect(
            format="compare to skill total of spell countering",
            base_difficulty=24,
            count=1,
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Sphere of Protection",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="19", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Sphere with radius of 3 meters", base_difficulty=15, count=1
            ),
            "Components": Aspect(
                format="Diamond (very rare)", base_difficulty=-4, count=1
            ),
            "Gestures": Aspect(
                format="Drop diamond on ground (simple)", base_difficulty=-1, count=1
            ),
            "Incantations": Aspect(
                format="“Stop magic.” (phrase)", base_difficulty=-1, count=1
            ),
        },
        notes="When the mage casts this spell and drops the diamond up to\na meter from her, a magically disruptive sphere forms around\nit. All who are within the sphere are protected against spells.\nThe spell doesn’t prohibit ranged attacks or fighting of any\nsort within the sphere. However, the skill totals of all spells\ndirected at occupants in the area of effect are compared to\nthe effect’s value plus the result point bonus of the spell. If\nthe defending spell’s total is higher than the intruding spell’s\nskill total, then the opposing spell is completely repulsed.\nAs the spell is not actually focused on the diamond or\nanyone else, friend or foe may enter or leave the area without\ndisrupting the spell.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="Elasticity (R1), +1 to contortion, dodge, and sleight of hand totals, and +1 to disguise totals that target performs on himself — for D6 Space, use acrobatics: contortion and con: disguise instead of the related listed skills",
            base_difficulty=3,
            count=1,
        ),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Stretch",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="14", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Something elastic (ordinary)", base_difficulty=-1, count=1
            ),
            "Focused": Aspect(format="On target", base_difficulty=4, count=1),
            "Gestures": Aspect(
                format="Stretch the component (simple)", base_difficulty=-1, count=1
            ),
            "Incantations": Aspect(
                format="“Stretch.” (phrase)", base_difficulty=-1, count=1
            ),
        },
        notes="This spell grants the target the ability to slip through\ntight spots and wiggle out of harms way, using the Elasticity\nSpecial Ability at rank 1. See the appropriate section in the\n“Character Options” chapter for additional details.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="4D physical damage, stun only, ignores nonmagical armor",
            base_difficulty=15,
            count=1,
        ),
        duration=Aspect(format="1 second ", base_difficulty=0, count=1),
        range=Aspect(format="25 meters ", base_difficulty=15, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=15, count=1),
        casting_time=Aspect(format="3.5 seconds ", base_difficulty=-3, count=1),
        name="Stun",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="21", base_difficulty=0, count=1),
            "Incantations": Aspect(
                format="“Stun.” (phrase)", base_difficulty=-1, count=1
            ),
        },
        notes="With the utterance of a simple word, a mage can stun an\nopponent. The successful casting of this spell causes 4D stun\ndamage to the intended target. All that is required is that\nmental focus be placed upon the intended victim (with a\nsuccessful Moderate willpower/mettle roll). The spell effects\ncannot be protected against by nonmagical armor. However,\nthe damage is treated as stun damage as indicated in the\n“Damage” chapter of the rulebook.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="telepathy of 4D", base_difficulty=24, count=1),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Telepathy",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Folk, magic", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(
                format="16", base_difficulty=0, count=1
            ),  # Should be 22
            "Concentration": Aspect(
                format="1 round with willpower/mettle difficulty of 8",
                base_difficulty=-2,
                count=1,
            ),
            "Focused": Aspect(format="On caster", base_difficulty=8, count=1),
        },
        notes="This spell grants the target 4D in the telepathy skill. It func-\ntions identically to the Psionics skill as described in the D6\nAdventure Rulebook chapter on “Psionics.” Because the skill\nlinks minds, it is possible for one person to read the thoughts\nof another character and determine if a lie is being told or\ndetect fear. When using this skill, refer to the “Empathy and\nTelepathy” table and the “Lie Detecting” table.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="4D languages — speaking or reading/writing in *D6 Fantasy*",
            base_difficulty=12,
            count=1,
        ),
        duration=Aspect(format="1 day ", base_difficulty=25, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="2 rounds ", base_difficulty=-5, count=1),
        name="Understand Gibberish",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="19", base_difficulty=0, count=1),
            "Components": Aspect(format="Wax (ordinary)", base_difficulty=-1, count=1),
            "Focused": Aspect(format="On target", base_difficulty=7, count=1),
            "Gestures": Aspect(format="Point (simple)", base_difficulty=-1, count=1),
        },
        notes="Through the aid of magic, it is possible for a targeted\ncharacter to understand any language or code. Providing the\nspell is successful, the selected character gains 4D languages\n(speaking or reading/writing in D6 Fantasy ) in the specific\nlanguage being heard or read at the moment of casting. This\nincludes a normally unknown or undecipherable language,\nalthough the task is much more difficult. Understand gibberish\nalso works with codes.\nThe gamemaster determines the difficulty, based upon\nhow common or unusual it is.",
        skill="Divination",
    ),
    Spell(
        effect=Aspect(
            format="Skill Bonus: Throw Voice (R8), +24 to bluff/con totals",
            base_difficulty=24,
            count=1,
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="60 meters ", base_difficulty=9, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=9, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Voices",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(
                format="18", base_difficulty=0, count=1
            ),  # Should be 23
            "Area Effect": Aspect(
                format="Sphere with radius of 2 meters", base_difficulty=10, count=1
            ),
            "Components": Aspect(
                format="Leather cord (common)", base_difficulty=-3, count=1
            ),
            "Gestures": Aspect(
                format="Pull on cord (fairly simple)", base_difficulty=-2, count=1
            ),
            "Incantations": Aspect(
                format="Whisper distracting words (phrase)", base_difficulty=-1, count=1
            ),
            "Unreal Effect": Aspect(
                format="Disbelief difficulty of 13", base_difficulty=-6, count=1
            ),
        },
        notes="By uttering a few words, a guard or group of guards can\nbe led astray. If successfully cast, this spell gives the magic\nuser a +24 bonus to the bluff/con total needed for this spell.\nThe results can affect anyone in a specified two-meter radius\nup to 60 meters away.\nAn opposed interaction roll is made against the target or\ntargets. Anyone failing this roll heads toward the direction\nthe caster made the voices appear to come from. For the\nduration of the spell, the incantation words are repeated\nover and over.",
        skill="Conjuration",
    ),
]

if __name__ == "__main__":
    detail(spells)

__test__ = {
    "Alter Shape": ">>> spells[0].difficulty\n47",
    "Befriend Animal": ">>> spells[1].difficulty\n18",
    "Blur": ">>> spells[2].difficulty\n13",
    "Change Material": ">>> spells[3].difficulty\n11",
    "Deadeye": ">>> spells[4].difficulty\n14",
    "Deafen": ">>> spells[5].difficulty\n36",
    "Detect Presence": ">>> spells[6].difficulty\n26",
    "Distract": ">>> spells[7].difficulty\n23",
    "Fancy Riding": ">>> spells[8].difficulty\n16",
    "Fate": ">>> spells[9].difficulty\n18",
    "Find Trap": ">>> spells[10].difficulty\n23",
    "Find Way": ">>> spells[11].difficulty\n18",
    "Insight to Weakness": ">>> spells[12].difficulty\n22",
    "Illiterate": ">>> spells[13].difficulty\n21",
    "Insight into the Future": ">>> spells[14].difficulty\n18",
    "Investigate": ">>> spells[15].difficulty\n30",
    "Invoke Emotion": ">>> spells[16].difficulty\n19",
    "Leap": ">>> spells[17].difficulty\n16",
    "Mistaken Identity": ">>> spells[18].difficulty\n28",
    "Perfect Touch": ">>> spells[19].difficulty\n22",
    "Possess the Living Mind": ">>> spells[20].difficulty\n24",
    "Slip": ">>> spells[21].difficulty\n28",
    "Speak Language": ">>> spells[22].difficulty\n12",
    "Sphere of Protection": ">>> spells[23].difficulty\n19",
    "Stretch": ">>> spells[24].difficulty\n14",
    "Stun": ">>> spells[25].difficulty\n21",
    "Telepathy": ">>> spells[26].difficulty\n22",
    "Understand Gibberish": ">>> spells[27].difficulty\n19",
    "Voices": ">>> spells[28].difficulty\n23",
}
