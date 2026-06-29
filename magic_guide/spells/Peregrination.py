"""
Peregrination

When run as an app, generates .RST-formatted details of each Spell.
"""

from decimal import Decimal
from typing import Annotated, Any
import typer
from opend6_tools.magic2 import *


spells = [
    Spell(
        name="Alter Gravity",
        skill="Apportation",
        notes="With this spell, a magic user can walk on walls or ceilings\nby changing the direction of gravity for herself. Each time\nshe wishes to change direction, she merely needs to say,\n“Alter.”\n\n",
        effect=MassEffect("moves up to  -- ", *["250 kilograms"]),
        duration=DurationAspect(measure="1 hour"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 minute"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Inanimate Forces"),
            "gestures": GesturesAspect("Point up and then down", *["simple"]),
            "incantations": IncantationsAspect("'“Alter.”'", *["phrase"]),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On caster"
            ),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 12")],
    ),
    Spell(
        name="Beacon",
        skill="Alteration",
        notes="This spell serves little purpose on its own, but when used\nin conjunction with the shift planes spell (or a similar spell),\nit gives the caster +4D to her willpower/mettle roll when\nattempting to return from another plane. The same magic\nuser must cast both spells, as the spells are attuned to her\nsenses.\nSo long as the glass bead  remains in the originating\ndimension, the bonus is granted to the caster. If the glass\nbead is destroyed or shifted to another plane, then all trace\nof it is lost.",
        effect=SkillEffect(
            "+  to willpower/mettle when bead used as planar homing beacon", *["+4D", "skill modifier"]
        ),
        duration=DurationAspect(measure="1 day"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="1 hour"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Enchanted"),
            "components": ComponentsAspect("Glass bead", "very common"),
            "concentration": ConcentrationAspect("1 hour"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On glass bead"
            ),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 13")],
    ),
    Spell(
        name="Beckon Creature",
        skill="Apportation",
        notes="Any creature of the gamemaster’s choice, or randomly\ndetermined, can be called upon with this spell. The effect’s\nvalue plus the spell’s result point bonus is compared to a roll\nof the target’s willpower/mettle (or the governing attribute) to\nsee if the spell successfully latches on. If it does, the beckoned\nbeast arrives instantly — and, if the caster can convince it,\nto assist her in combat for the duration of the spell.",
        effect=Effect(
            description="compared to roll of target’s willpower/mettle or governing attribute",
            difficulty=24,
        ),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="10 kilometers"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Animal, entity, folk"),
            "components": ComponentsAspect("Fur, feather, or tooth", "ordinary"),
            "gestures": GesturesAspect("Welcoming gestures", *["simple"]),
            "incantations": IncantationsAspect("'“Arrive.”'", *["phrase"]),
            "variable_movement": VariableMovementAspect("bend around smaller", "target invisible"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Difficulty: 36"),
        ],
    ),
    Spell(
        name="Bind Reality",
        skill="Alteration",
        notes="With this spell, a magic user can seal a 10-meter sphere,\npreventing the opening or portals going to or coming from\nother planes. Any caster or creature attempting to open a\ngateway or shift into the affected area of this spell must\novercome the value of this spell’s effect. Any unsuccessful\nattempt to get in or out warns the caster with a glow on the\nsphere. This spell is useful when trying to prevent a prisoner\nfrom escaping, or an unwanted entity from entering a given\nlocation.",
        effect=Effect(
            description="compare to spell total of dimension-hopping spell", difficulty=27
        ),
        duration=DurationAspect(measure="1 day"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="2.5 hours"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Dimension"),
            "area_effect": AreaEffectAspect("10m radius sphere"),
            "concentration": ConcentrationAspect("1 hour"),
            "gestures": GesturesAspect("Make an encompassing gesture", *["simple"]),
            "other_alterant": OtherAlterant(
                difficulty=1,
                description="Sphere glows when triggered"
            ),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-5,
                description="Difficult scholar roll to recall information about the protected dimension",
            ),
            GenericAspect(difficulty=0, description="Difficulty: 35"),
        ],
    ),
    Spell(
        name="Blur Barriers",
        skill="Conjuration",
        notes="For a short period of time, the magic user forms a nexus\nof dimensions. If successful, the caster weakens the barriers,\nresulting in nothing functioning as it normally does.The natural, physical laws of the occupied dimension become unstable.\nEveryone within the area of effect is subject to an increase in\nthe difficultiles of all physical and mental actions.",
        effect=SkillEffect(
            "modifier to all 6 physical and mental attributes","+6D", "attribute modifier"),
        duration=DurationAspect(measure="5 minutes"),
        range=RangeAspect(measure="10 meters"),
        casting_time=CastingTimeAspect(measure="1 minute"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Dimension"),
            "area_effect": AreaEffectAspect("4m radius sphere"),
            "concentration": ConcentrationAspect("1 minute"),
            "gestures": GesturesAspect("Wiggle fingers on one hand", *["simple"]),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 33")],
    ),
    Spell(
        name="Contact Entity",
        skill="Divination",
        notes="Provided that the caster has some knowledge of the entity\nor type of entity she wishes to contact, it’s possible to open a\nchannel to that being. If the spell is successful and the distance\nto the entity’s location has a planar value of 49 or less, the\ncaster gains 4D languages in the language of the target. This\nonly lasts for the duration of the spell.\nContacting a creature from another plane does not guar-\nantee that it is willing to communicate. Convincing it is left\nto the caster.",
        effect=CompositeEffect(
            "Content Entity in another plane",
            SkillEffect(
            "  languages/speaking in the language of the target entity",
            *["+4D"],
            ),
            Effect("Planar distance", 49),
        ),
        duration=DurationAspect(measure="1 hour"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 minute"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("entity, dimension"),
            "concentration": ConcentrationAspect("1 minute"),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-3,
                description="Must be knowledgeable of the entity to be contacted, which requires a scholar roll of 11",
            ),
            GenericAspect(difficulty=0, description="Difficulty: 13"),
        ],
    ),
    Spell(
        name="Decrease Gravity",
        skill="Alteration",
        notes="At the indicated site, the caster decreases gravity for a\n10-meter wide area. This causes certain physical actions to\nreceive modifiers to their difficulties or totals (see the “effect”\ndescription for details).\nAs this is a magical adjustment in gravity, it does not affect\nvictims in exactly the same way as a normal loss of gravity.\nFurthmore, anyone or anything leaving the area of effect\nloses any modifiers given by the spell.",
        effect=CompositeEffect(
            "Reduced gravity",
            DisadvantageEffect("Hindrance: Low Gravity (+5 to acrobatics, brawling/fighting, and melee combat difficulties)",5,),
            SkillEffect("Skill Bonus: Low Gravity (+5 to lifting/lift, running, and throwing totals)", "5D"),
        ),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="15 meters"),
        casting_time=CastingTimeAspect(measure="2 rounds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("inanimate forces"),
            "area_effect": AreaEffectAspect("5m radius sphere"),
            "concentration": ConcentrationAspect("2 rounds"),
            "gestures": GesturesAspect("Clench fist and point", *["simple"]),
            "incantations": IncantationsAspect("'“Light.”'", *["phrase"]),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 34")],
    ),
    Spell(
        name="Dimensional Gap",
        skill="Conjuration",
        notes="When the caster brings the components of the spell\ntogether, the targeted location makes a dimensional gap in\nthe earth, creating a large hole in the ground. The shape is\nspherical, thereby causing vehicle or creatures at the edge to\nroll down the side into the center. Should the gap be created\ndirectly beneath a creature, it drops straight down, suffering\n7D damage. Damage to those who are not at ground zero\nis reduced accordingly by the area effect rules discussed in\nthe “Magic” chapter of the D6 Adventure  and D6 Fantasy\nrulebooks.\nWhen the hole disappears, anything that fell into the pit\nis now in a heap on the mysteriously whole ground.",
        effect=SkillEffect("  physical damage", *["+7D"]),
        duration=DurationAspect(measure="1 round"),
        range=RangeAspect(measure="40 meters"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("dimension"),
            "area_effect": AreaEffectAspect("10m radius hemisphere"),
            "components": ComponentsAspect("Two rocks", "ordinary"),
            "concentration": ConcentrationAspect("1 round"),
            "gestures": GesturesAspect(
                "Slam the components against each other", *["simple"]
            ),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 41")],
    ),
    Spell(
        name="Dimensional Survival",
        skill="Alteration",
        notes="All who are affected by this spell are transformed physi -\ncally so they can survive on a hostile dimension. Once the\nspell is successfully cast, it operates upon all who are within\nfive meters of the mage, giving them half the ranks in the\nSpecial Abilities as the caster. Anyone who leaves the circle\nof influence loses the immunity and cannot regain it simply\nby getting close the mage again.",
        effect=CompositeEffect(
            "Survival",
            SpecialAbilityEffect(
            "Atmospheric Tolerance ", 2),
            SpecialAbilityEffect("Environmental Resistance", 2),
        ),
        duration=DurationAspect(measure="1 day"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("dimension, folk"),
            "area_effect": AreaEffectAspect("5m radius circle"),
            "concentration": ConcentrationAspect("1 round"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On caster"
            ),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-4,
                description="Must be knowledgeable of the plane in which the morphed characters are to travel, requiring a scholar roll of 15",
            ),
            GenericAspect(difficulty=0, description="Difficulty: 26"),
        ],
    ),
    Spell(
        name="Energy Barrier",
        skill="Conjuration",
        notes="The mage can alter the forces that bind and form the\ndimension in which she dwell, shifting them to her will.\nBy simply pointing and concentrating, the mage creates a\nbarrier providing 4D+1 protection from attacks. All beings\nand objects behind the 20-meter area gain this advantage,\ncombining with existing armor. Of course, the limitation\nto this spell is that the defense is 2 dimensional. Once cast,\nbarrier cannot be relocated or altered, allowing for opponents\nto readily move around the side — providing they known\nenough to do this.",
        effect=SkillEffect("Armor Value of  1, physical only", *["+4D"]),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="5 meters"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("inanimate forces"),
            "area_effect": AreaEffectAspect("20m radius circle"),
            "concentration": ConcentrationAspect("1 round"),
            "gestures": GesturesAspect(
                "Point at the spot where the barrier is to be formed", *["simple"]
            ),
            "feedback": FeedbackAspect(3),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 30")],
    ),
    Spell(
        name="Ethereal",
        skill="Alteration",
        notes="When cast upon a character, the mage shifts the person\nbetween dimensions, making them ethereal. The character\nis visible, and still exists, but her being is spread among\nmany worlds. For the duration of this spell, she gains the\nIntangibility (R1) Special Ability.\n\n",
        effect=SpecialAbilityEffect(
            "Intangibility", 1,
            note="+3D to damage resistance total against physical attacks and movement is halved"
        ),
        duration=DurationAspect(measure="10 minutes"),
        range=RangeAspect(measure="10 meters"),
        casting_time=CastingTimeAspect(measure="3 rounds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("dimensions"),
            "concentration": ConcentrationAspect("1 round"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 18")],
    ),
    Spell(
        name="Erase Person",
        skill="Alteration",
        notes="This deadly spell not only instantly kills the target, but also\nobliterates her history from the universe. Upon contact with\nthe target, by means of a successful brawling/fighting roll, a\nshroud of blackness envelops the victim, erasing her from\nexistence. As each person is linked through time and space,\nthe thread that formed her history is followed and destroyed.\nThis means that all memories, all written words, all history\nis removed. It is as if the character had never existed. This\nspell is not a charged spell. Only one opportunity to erase a\nperson is granted per casting of the spell, and that opportunity\noccurs in the round after the spell’s completion.\nAs with powerful spells, there is the potential for disaster.\nIf the caster rolls a one on the Wild Die, it is the caster who\nsuffers the effect of the spell. Simply knowing this causes many\nmages to shy away from attempting such powerful magic.",
        effect=CompositeEffect(
            "Erase Person",
            DamageEffect("physical damage","+10D", "ignore nonmagical armor"),
            TimeEffect("In the past", "100 years"),
        ),
        duration=DurationAspect(measure="100 years"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="1 hour"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("dimension"),
            "concentration": ConcentrationAspect("1 hour", modifier=3, note="willpower difficulty 15"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-8,
                description="A roll of a 1 on the Wild Die in the caster being erased, even if the difficulty number was equaled or exceeded; may only be used once per target",
            ),
            GenericAspect(difficulty=0, description="Difficulty: 61"),
        ],
    ),
    Spell(
        name="Far Walk",
        skill="Conjuration",
        notes="By sending her consciousness through the folds of inter-\ndimensional space, the caster can visit other locations by\nleaving her body behind. This spell grants the caster 4D+1 in\nthe Psionics: astral projection skill (detailed in the “Psionics”\nchapter of the D6 Adventure Rulebook).",
        effect=SkillEffect("Psionics: astral projection", *["+4D+1", "extranormal skill"]),
        duration=DurationAspect(measure="1 hour"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("dimension"),
            "concentration": ConcentrationAspect("1 round"),
            "feedback": FeedbackAspect(1),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On caster"
            ),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 17")],
    ),
    Spell(
        name="Folded Space",
        skill="Conjuration",
        notes="A chest or bag with this spell cast upon it can hold up\nto 1,000 kilograms of mass. The weight of the container is\nnot increased, as the objects drop into a fold within inter-\ndimensional space. However, it is not possible to sustain\nliving creatures within this area for more than a few minutes.\nNonetheless, it provides plenty of space for carrying items.\nNote that any thing that is larger than the opening of the\ncontainer cannot be placed inside. This means an automobile\ncould not be shoved into a paper lunch bag, but 1,000 kilo-\ngrams of marbles or appropriately sized items do fit.",
        effect=MassEffect("Objects hidden away", *["1000 kilograms"]),
        duration=DurationAspect(measure="1 week"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="1 minute"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("dimension"),
            "components": ComponentsAspect("Small chest or bag", "very common"),
            "concentration": ConcentrationAspect("1 round", modifier=1, note="willpower difficulty 8"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On container"
            ),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 18")],
    ),
    Spell(
        name="Greater Telekinesis",
        skill="Apportation",
        notes="Successfully casting this spell imbues the target with the\nPsionics skill telekinesis at 6D. The target is can move objects\nwith the power of her mind. All the rules for the skill use\napply as dictated in the D6 Adventure Rulebook chapter on\n“Psionics.” The distance moved and weight of an object moved\nis indicated on the “Telekinesis” table. The “Psionics Range”\ntable governs the range of the telekinesis skill.",
        effect=SkillEffect("telekinesis of  ", *["+6D", "extranormal skill"]),
        duration=DurationAspect(measure="1 hour"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 minute"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("inanimate forces"),
            "concentration": ConcentrationAspect("1 round"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 27")],
    ),
    Spell(
        name="Increase Gravity",
        skill="Alteration",
        notes="The caster increases gravity for a 10-meter wide area.\nBecause of this, certain physical actions get difficulty modi-\nfiers (see the “effect” description for details).\nAs this is a magical adjustment in gravity, it does not affect\nvictims in exactly the same way as a normal loss of gravity.\nFurthmore, anyone or anything leaving the area of effect\nloses any modifiers given by the spell.",
        effect=DisadvantageEffect(
            "Hindrance: High Gravity ",
            10,
            note=", +5 to acrobatics, brawling/fighting, lifting/lift, melee combat, running,  and throwing difficulties",
        ),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="15 meters"),
        casting_time=CastingTimeAspect(measure="2 rounds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("inanimate forces"),
            "area_effect": AreaEffectAspect("5m radius sphere"),
            "concentration": ConcentrationAspect("2 rounds"),
            "gestures": GesturesAspect("Clench fist and point", *["simple"]),
            "incantations": IncantationsAspect("'“Heavy.”'", *["phrase"]),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 34")],
    ),
    Spell(
        name="Lesser Telekinesis",
        skill="Apportation",
        notes="The target can move objects with the power her mind with\nthe successful casting of this spell. The “Psionics” chapter in\nthe D6 Adventure Rulebook describes the game mechanics of\nthis spell. The distance moved and weight of an object moved\nis indicated on the “Telekinesis” table. The “Psionics Range”\ntable governs the range of the telekinesis skill.",
        effect=SkillEffect("telekinesis of  ", *["+3D", "extranormal skill"]),
        duration=DurationAspect(measure="25 minutes"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("inanimate forces"),
            "concentration": ConcentrationAspect("1 round"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 14")],
    ),
    Spell(
        name="Locate Person",
        skill="Divination",
        notes="If all the conditions are satisfied, then it is possible for\nthe caster to locate a given person within a 10-kilometer\nrange. Compare the result points of the spell’s search versus\nthe target’s Agility/Reflexes or sneak/stealth to the following\ntable to find how much the mage knows.\nMinimal (0 or less): general direction is determined\nSolid (1–4): direction and an idea of distance are known\nGood (5–8): direction, rough distance, and general features\nof the location are discerned\nSuperior (9 or more): direction, exact distance, and the\nexact location are garnered",
        effect=SkillEffect("search of  ", *["+2D"]),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="10 kilometers"),
        casting_time=CastingTimeAspect(measure="1 hour"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("dimension, folk"),
            "components": ComponentsAspect(
                "Personal belonging from target", "very rare"
            ),
            "concentration": ConcentrationAspect("3 rounds"),
            "gestures": GesturesAspect(
                "Form goggles with hands over eyes", *["simple"]
            ),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Difficulty: 14"),
            GenericAspect(
                difficulty=5, description="Variable Movement: Bending/unseen target"
            ),
        ],
    ),
    Spell(
        name="Rend Reality",
        skill="Conjuration",
        notes="After casting this powerful spell, the fabric of reality is\ntorn asunder, leaving a gapping tear that is jet black. This is\nthe space between spaces, an utter void. All who are within\nthe area effect of this spell must make an opposed Physique/\nStrength o r  lifting/lift roll against the spell skill total (no other\ntargeting roll is needed). Failure results in being pulled inside.\nThose who lose all of their Body Points or Wounds from the\ndamage caused by the rift are lost forever; it is impossible to\npull an object or a person from this temporarily disrupted\nsection of the universe. Anyone surviving the devestation\nis found after the spell wears off, battered, on the ground\nwhere the tear once was.\n\n",
        effect=DamageEffect("10D physical damage", *["+10D"]),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="25 meters"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("dimension"),
            "area_effect": AreaEffectAspect("3m radius sphere"),
            "components": ComponentsAspect("2 small magnets", "very common"),
            "concentration": ConcentrationAspect("1 round"),
            "gestures": GesturesAspect(
                "Tearing motion with hands while holding magnets", *["simple"]
            ),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 29")],
    ),
    Spell(
        name="Secret Passage",
        skill="Apportation",
        notes="Casting secret passage opens an interdimensional gateway\nwith an opening within one meter of the caster and an exit\n10 meters away. The exit portal connects as though a straight\nline were drawn from one point to another. This allows pas-\nsage through 10 meters of any material, including air, water,\nrock, and so on. All who enter vanish from sight and instantly\nappear at the exit point.",
        effect=CompositeEffect(
            "Move Mass",
            MassEffect("move up to  --  per round ", *["150 kilograms"]),
            DistanceEffect("up to", "10 meters"),
        ),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("dimension"),
            "gestures": GesturesAspect("Outline circle in the air", *["simple"]),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 10")],
    ),
    Spell(
        name="Send Whisper",
        skill="Conjuration",
        notes="Only the target can hear the caster’s words if the spell\nis successful. The communication is one-way, coming from\nthe caster. But because the message is traveling through\nthe barrier between planes, voices often become distorted,\nmaking sending a message much more difficult than normal\nconversation. For this reason, the magic user must make a\nlanguages/speaking attempt in a language the caster speaks\nand the target understands. The distortion creating by sending\na dimensional message creates a difficulty of 11. If the skill\nroll succeeds, the message is automatically heard. If a one is\nrolled on the Wild Die, but the difficulty number is equaled\nor passed, then others within one-meter of the target can\nhear the message as well.\nThe message is limited to what the caster can say in 10\nseconds.\n\n",
        effect=Effect(description="Psionic Communication", difficulty=0),
        duration=DurationAspect(measure="2 rounds"),
        range=RangeAspect(measure="1 kilometer"),
        casting_time=CastingTimeAspect(measure="2 rounds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("dimension"),
            "concentration": ConcentrationAspect("1 round"),
            "gestures": GesturesAspect(
                "Make a cone with hands around mouth", *["simple"]
            ),
            "incantations": IncantationsAspect(
                "'Whisper target’s name along with the desired message'",
                *["complex (languages/speaking roll with difficulty of 11)"],
            ),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-2,
                description="Must have known the target for at least 1 week; must speak target’s language",
            ),
            GenericAspect(difficulty=0, description="Difficulty: 12"),
        ],
    ),
    Spell(
        name="Shift Plane",
        skill="Apportation",
        notes="Up to 600 kilograms of targets within the spell’s radius\nare transported to a given dimension. As this spell uses an\narea effect, the caster may not choose the targets going\nwith him.",
        effect=CompositeEffect(
            "Move Mass to Another Plane",
            MassEffect(
            "matter moved to another dimension",
            *["600 kilograms"]),
            Effect("with a planar distance value of 49 or less", 49),
        ),
        duration=DurationAspect(measure="1 round"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 hour"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("dimension"),
            "area_effect": AreaEffectAspect("5m radius sphere"),
            "concentration": ConcentrationAspect("10 minutes"),
            "gestures": GesturesAspect(
                "Touch the ground upon the completion of the spell", *["simple"]
            ),
            "incantations": IncantationsAspect("'“Shift.”'", *["phrase"]),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-6,
                description="Must be knowledgeable of the target dimension, which requires a scholar roll of 20",
            ),
            GenericAspect(difficulty=0, description="Difficulty: 31"),
        ],
    ),
    Spell(
        name="Synchronicity",
        skill="Apportation",
        notes="Many occultists and scholars of magic believe that there\nis no such thing as coincidence. Instead, seemingly random\nevents are attributed to interference from other dimensions,\nor an object coming out of a dimension and then re-entering\nthe same dimension at another location. That is to say, if the\ntop of a horseshoe where to be pushed through a sheet of\npaper to the point that only the open ends were visible, those\nunfamiliar with the shape of the horseshoe would see two,\nseparate items poking through the paper. But to those who\nunderstand the shape of a horseshoe, it is known that both\nvisible parts are connected by an unseen bend. This is how\nsynchronicity works. It allows the caster to perform an action,\nbut that action is linked through a multi-dimensional conduit\nthat causes a similar action to occur at a distance.\nAfter completing the spell, the magic user’s physical actions\nare invisibly replicated at a spot of her choosing up to 100\nmeters away. Once the location is designated, it cannot be\naltered. For instance, the mage may decide that when she\nwaves her hands, the glassware in a shop 50 meters away\nwould suddenly clatter to the floor, though it would not\nbreak as this spell causes no damage.\nThe exact results are left to the gamemaster and the circum-\nstances, but the caster should be allowed to be as creative as\npossible. (However, this spell cannot cause injury — though\nperhaps a little pain, such as a tug on the ear — and can\nonly affect up to five kilograms of matter.) Because of this\nunique ability, this spell is often used to distract others for\na brief moment.",
        effect=MassEffect("Move mass", *["5 kilograms"]),
        duration=DurationAspect(measure="5 rounds"),
        range=RangeAspect(measure="100 meters"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("dimension"),
            "concentration": ConcentrationAspect("1 round"),
            "gestures": GesturesAspect("Grasp at air", *["simple"]),
            "incantations": IncantationsAspect(
                "'Whisper, “I touch something from afar.”'", *["sentence"]
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
            "variable_movement": VariableMovementAspect("bend around smaller", "target invisible")
        },
        other_conditions=[
            GenericAspect(
                difficulty=-2,
                description="Must make a scholar roll at 11, indicating she has sufficient understanding of dimensions",
            ),
            GenericAspect(difficulty=0, description="Difficulty: 13"),
        ],
    ),
    Spell(
        name="Unseen Bullet",
        skill="Apportation",
        notes="Without the ability to see or sense the target, such as\nthrough other magic, this spell is not very useful. If a victim\ncan be located, then the projectile can be thrown or fired\nwith a +4D (+12) to the targeting skill total. The object hits\nthe target on a successful skill roll as though appearing from\nno where. There is no possibility to dodge or take cover, as\nprojectile travels through a wormhole, unhindered by all\nphysical barriers. This means it is possible to shoot through\none or more windows without breaking the glass.",
        effect=MassEffect("projectile", *["1 kilogram"]),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="150 meters"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("dimension"),
            "components": ComponentsAspect(
                "physical projectile of any sort, be it rock, arrow, bullet, etc.", "ordinary"
            ),
            "concentration": ConcentrationAspect("1 round"),
            "gestures": GesturesAspect("Grasp projectile in hand", *["simple"]),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On projectile"
            ),
            "variable_movement": VariableMovementAspect("bend around smaller",
                                                        "target invisible")
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Difficulty: 15"),
        ],
    ),
    Spell(
        name="Vanish",
        skill="Apportation",
        notes="Any living or nonliving item up to 150 kilograms can be\nfolded into a small, temporary dimension created by the\ncaster. By all appearances, the object or person simply van-\nishes from sight. Time passes normally for the duration of\nthe spell; the target can do whatever she wishes, as long as\nshe does not move from the spot where she vanished. There\nis always enough air to breath for at least one hour. The\natmosphere must be present at the location where the spell\nis cast; it cannot be created by the magic user.",
        effect=CompositeEffect(
            "Invisibility",
            # The originals do not appear correct in the rules.  Effect should be 81.
            # SpecialAbilityEffect(
            #     "Invisibility", 3, "+3 to dodge, sneak/stealth, and hide: self totals and +3 to search, tracking, investigation, and attack difficulties against target"),
            # SpecialAbilityEffect(
            #     "Iron Will", 3, "+3 to willpower/mettle rolls and +6 to default interaction attempts and mental attacks against character"),
            # SpecialAbilityEffect(
            #     "Natural Armor: In Other Dimension", 4, "+3D to damage resistance roll against physical and energy attacks"),
            # These give closer to the right difficulty.
            SpecialAbilityEffect(
                "Invisibility", 1,
                "+1 to dodge, sneak/stealth, and hide: self totals and +1 to search, tracking, investigation, and attack difficulties against target"),
            SpecialAbilityEffect(
                "Iron Will", 1,
                "+1 to willpower/mettle rolls and +2 to default interaction attempts and mental attacks against character"),
            SpecialAbilityEffect(
                "Natural Armor: In Other Dimension", 1, "+D to damage resistance roll against physical and energy attacks"),
            ),
        duration=DurationAspect(measure="1 hour"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="2 rounds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("dimension"),
            "concentration": ConcentrationAspect("1 round"),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-2,
                description="Anything that affects other dimensional creatures affects the target",
            ),
            GenericAspect(difficulty=0, description="Difficulty: 15"),
        ],
    ),
    Spell(
        name="Void Shield",
        skill="Conjuration",
        notes="Casting void shield  creates a one-meter radius circle of\nnegative energy that causes 5D damage to up to five targets\nthat come in contact with it. Its name is misleading in that\nit doesn’t improve Armor Value; rather, it is a weapon. While\nthe spell is active, the “shield” thrums, as the caster directs it\nfrom target to target. It is only capable of causing damage to\nthose who possess positive energy, who are alive. It can pass\nthrough a character, causing damage, moving to the next to\ncontinue with another attack.\nStriking at the void shield is the as being attack. The attack-\ning weapon and the attacker suffer 5D of damage, split\nbetween them (but only one of the change targets is used\nup). Nonmagical armor does not protect against the damage\ncaused by this spell.\n\n",
        effect=ProtectionEffect("Protective Shield", *["+5D", "physical damage", "ignores nonmagical armor"]),
        duration=DurationAspect(measure="5 rounds"),
        range=RangeAspect(measure="25 meters"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("dimension"),
            "change_target": ChangeTargetAspect("5 times"),
            "gestures": GesturesAspect("draw circle in the air", *["simple"]),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-5,
                description="Willpower/mettle  roll of 14 is required each time the spell is moved; target must be alive",
            ),
            GenericAspect(difficulty=0, description="Difficulty: 29"),
        ],
    ),
    Spell(
        name="Vortex",
        skill="Conjuration",
        notes="By knowledge of the planes and will, a mage can focus\nher mental energy upon a location visible to her and open\na swirling vortex. This is an interdimensional juncture that\ncreates havoc in nearly any plane it is created. The opening\nof the shimmering vortex is announced by a deep rumbling\nsound not unlike thunder. By the time the spell is completed,\nall within several meters can hear and feel the roar and quake\nof this unnatural creation. Any object that comes into contact\nwith it suffers 6D+1 damage, with no damage being absorbed\nby nonmagical armor. Additionally, the caster can move the\nvortex five meter per round.\nShould two vortices come into contact, they cancel each\nother, immediately ending the spell.",
        effect=DamageEffect("massive physical damage", *["+6D+1", "ignores nonmagical armor"]),
        duration=DurationAspect(measure="3 rounds"),
        range=RangeAspect(measure="40 meters"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("dimensions"),
            "area_effect": AreaEffectAspect("5m radius sphere"),
            "concentration": ConcentrationAspect("1 round"),
            "feedback": FeedbackAspect(3),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Difficulty: 34"),
            GenericAspect(
                difficulty=1,
                description="Variable Movement: Movement of 5 meters per round",
            ),
        ],
    ),
]



__test__ = {
    "Alter Gravity": ">>> spells[0].difficulty\n12",
    "Beacon": ">>> spells[1].difficulty\n13",
    "Beckon Creature": ">>> spells[2].difficulty\n35",  # Rules say 36
    "Bind Reality": ">>> spells[3].difficulty\n35",
    "Blur Barriers": ">>> spells[4].difficulty\n32",  # Rules say 33
    "Contact Entity": ">>> spells[5].difficulty\n32",
    "Decrease Gravity": ">>> spells[6].difficulty\n33", # Rules say 34
    "Dimensional Gap": ">>> spells[7].difficulty\n41",
    "Dimensional Survival": ">>> spells[8].difficulty\n26",
    "Energy Barrier": ">>> spells[9].difficulty\n29",  # Rules say 30
    "Ethereal": ">>> spells[10].difficulty\n19",  # Rules say 18
    "Erase Person": ">>> spells[11].difficulty\n68",  # Rules say 61 -- Effect, Duration, Focused all have errors.
    "Far Walk": ">>> spells[12].difficulty\n23",  # Rules say 17 -- big gap here.
    "Folded Space": ">>> spells[13].difficulty\n20",  # Rules say 18
    "Greater Telekinesis": ">>> spells[14].difficulty\n27",
    "Increase Gravity": ">>> spells[15].difficulty\n33",  # Rules say 34
    "Lesser Telekinesis": ">>> spells[16].difficulty\n18",  # Rules say 14; math is wrong
    "Locate Person": ">>> spells[17].difficulty\n12",  # Rules say 14, duration is incorrect
    "Rend Reality": ">>> spells[18].difficulty\n29",
    "Secret Passage": ">>> spells[19].difficulty\n10",
    "Send Whisper": ">>> spells[20].difficulty\n11",  # Rules say 12
    "Shift Plane": ">>> spells[21].difficulty\n30",  # Rules say 31
    "Synchronicity": ">>> spells[22].difficulty\n13",
    "Unseen Bullet": ">>> spells[23].difficulty\n15",
    "Vanish": ">>> spells[24].difficulty\n17",  # Rules are way out -- the difficulty cost is way wrong
    "Void Shield": ">>> spells[25].difficulty\n29",
    "Vortex": ">>> spells[26].difficulty\n33",  # Rules say 34
}



if __name__ == "__main__":
    app = build_app(spells)
    app()
