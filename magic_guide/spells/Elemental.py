"""
Elemental

When run as an app, generates .RST details of each Spell.
"""

from typing import Annotated, Any
import typer
from opend6_tools.magic2 import *

spells = [
    Spell(
        name="Acidic Attack",
        skill="Alteration",
        notes="When a mage casts acidic attack, the spell lasts for 5 rounds.\nEach round, damage continues, but is reduced by 1D. This\nrepresents the acid’s potency gradually decreasing.  Nonmagi-\ncal armor does not offer a defense against this spell, as the\nmystical corrosive promptly burns through metal, leather,\nclothing, and so on.\n\nAs the attack is magical, there is no way to extinguish the\nacid except to dispel it.\n",
        effect=DamageEffect(
            "Acid",
            "5D",
            "physical damage; ignores nonmagical armor",
        ),
        duration=DurationAspect(measure="5 rounds"),
        range=RangeAspect(measure="25 meters"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "component": ComponentsAspect("Small vile of acid", "uncommon"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="on target"
            ),
            "gestures": GesturesAspect("Shaking the vile at the target", "simple"),
            "incantations": IncantationsAspect("Burn!", "word"),
        },
        other_conditions=[
            ArcaneKnowledgeAspect("Water"),
            GenericAspect(difficulty=0, description="Difficulty: 20"),
        ],
    ),
    Spell(
        name="Burrow",
        skill="Apportation",
        notes="The burrow spell allows the caster to move through all types\nof soil at a rapid pace. When the spell is completed, the caster\nsinks into the earth in a fountain of dirt and sand. As he\ntravels through the earth, the soil in front of him is pushed\nbehind, collapsing the tunnel he creates. The mage using the\nspell will have a rudimentary idea of which way he is going,\nbut he may need to poke his head back above the surface from\ntime to time to make sure he is not going off track.\n\nThe spell does not allow the caster to move through stone\nor any material harder than clay. He usually travels one meter\nunder the surface, but if he encounters stone that he cannot\npenetrate, he may go up or down in the strata to avoid it.\n\nThere is a small pocket of air that travels with the user,\nallowing him to breathe as he wriggles through the soil.\nSeveral trips to the surface during the duration are necessary\nto refresh this air pocket.\n",
        effect=MassEffect("moves", "150 kilograms"),
        duration=DurationAspect(measure="1 hour"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="2.5 seconds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect("A mole skull", "common"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="on caster"
            ),
            "gestures": GesturesAspect("Digging motions with hands", "simple"),
            "incantations": IncantationsAspect("Dig.", "word"),
            "variable_movement": VariableMovementAspect("1 meters"),
        },
        other_conditions=[
            ArcaneKnowledgeAspect("Earth"),
            GenericAspect(difficulty=0, description="Difficulty: 18"),
        ],
    ),
    Spell(
        name="Cone of Wind",
        skill="Conjuration",
        notes="This spell is a favorite of mages who want to knock down\nopponents without doing any permanent injury. When the\nspell is cast a cone of powerful wind blasts from the caster’s\nhands out to a distance of eight meters. The cone is about\n30 centimeters wide at the casters hands and spreads out to\nfour meters in diameter at its far end.\n\nThe caster rolls the brawling/fighting score that the spell\ngenerates once; this total is used as a knockdown attempt\nagainst the combat difficulty for each target within one meter\nof the caster. (Those over one meter away get a +1 bonus to\ntheir defense totals per full meter distant.)  Anyone who fails\nto withstand the blast fall to the ground and must spend an\naction in the next round getting up.\n\nThis attack affects opponents with a Physique/Strength\ndie code of no more than the spell’s skill total divided by 3\n(ignore any remainder).\n\nThis spell does not require a separate targeting roll.\n",
        effect=SkillEffect("brawling/fighting", "6D"),
        duration=DurationAspect(measure="1 second"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="2.5 seconds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "area_effect": AreaEffectAspect("8m l 2m r cone"),
            "gestures": GesturesAspect(
                "Both hands make a pushing motion in the direction of the wind",
                "simple",
            ),
            "incantations": IncantationsAspect(
                "Mighty wind, drive my enemies before me!",
                "sentence; loud",
            ),
        },
        other_conditions=[
            ArcaneKnowledgeAspect("Air"),
            GenericAspect(difficulty=0, description="Difficulty: 11"),
        ],
    ),
    Spell(
        name="Control Elemental (Template)",
        skill="Conjuration",
        notes="This spell bends the mind and will of an elemental, forcing\nit to do the caster’s bidding. An elemental under the effects\nof this spell becomes a slave to the caster, doing anything\nhe compels it to.\n\nWhen the spell is cast, the caster generates a command:\nelemental skill total and compares it to the willpower/mettle\ntotal generated by the elemental. If the caster’s total is higher,\nthe elemental is his to command for the duration of the spell.\nThe caster will be aware that this spell is about to end just\nbefore the duration expires, giving him time to recast the\nspell if he wishes.\n\nIf the elemental makes a higher total than the caster of the\nspell, the elemental may have a bad reaction to the caster, or\nit may flee the area, depending on its type, relative power,\nand temperament. Fire and water elemental will be more\nlikely to attack, being more mercurial and hostile, while air\nand earth elementals will be more prone to flight.\n",
        effect=SkillEffect("command: elemental", "6D"),
        duration=DurationAspect(measure="1 hour"),
        range=RangeAspect(measure="2.5 meters"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect(
                "Small figurine of elemental type, made of precious metals and jewels",
                "very rare",
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="on caster"
            ),
            "gestures": GesturesAspect(
                "Make a circle with both arms",
                "simple",
            ),
            "incantations": IncantationsAspect(
                "[Type of elemental], bow to my will!",
                "sentence; loud",
            ),
        },
        other_conditions=[
            ArcaneKnowledgeAspect("Entity; any one element: air, earth, fire, or water"),
            GenericAspect(difficulty=0, description="Difficulty: 18"),
        ],
    ),
    Spell(
        name="Control Local Weather",
        skill="Alteration",
        notes="This spell gives the caster the ability to control the weather\nto a limited extent. To cast the spell, the mage concentrates\nfor 10 minutes on what type of weather he wants, and then\nchants the incantation continuously for the remainder of\nan hour.\n\nThe spell manipulates  the temperature, pressure, and\nhumidity within 11 meters of the caster. How successful\nhe is in making the change depends on the result points of\nthe spell, as detailed below. When the duration expires, the\nweather gradually returns to its prespell conditions.\n\nThe gamemaster decides on the local weather conditions\nusing the charts herein. Each level of change from the cur -\nrent conditions requires one result point. Thus, if the day is\nfair with warm temperatures and a light breeze, to make it\ncold and foggy with a strong wind requires four result points.\n(A skill total equalling the difficulty may make one level of\nchange in aspect of the weather.)\n\nThe caster can also change the radius of the effect at a cost\nof three result points for each additional meter.\n\nAs this is a magical change, the weather may not behave\nas it would under normal circumstances.\nIt must always be remembered that changing the weather\nin one place may also change it in some way somewhere\nelse. This can prompt revenge attacks from other mages\nor angry residents, so users of this spell must exercise the\nutmost care.\n\n..  sidebar::             Control Local Weather Effects\n\n    Round all fractions up. Modifiers are cumulative.\n\n    Precipitation Levels\n\n    - None (fair weather)\n    - Fog (all sight-based actions have a difficulty modifier equal to the result points, with a minimum of +1)\n    - Rain (or snow\\*)\n    - Freezing rain\\* (all physical actions have a difficulty modifier equal to one-quarter of the result points, with a minimum of +1)\n    - Sleet\\* (all physical actions have a difficulty modifier equal to one-half of the result points, with a minimum of +1)\n    - Small hail\\*\\* (damage per round equals one-quarter of the result points, with a minimum of 1 point)\n    - Large hail\\*\\* (damage per round equals one-half of the result points, with a minimum of 1 point)\n\n    \\* Temperature must also be freezing.\n\n    \\*\\* Hail can be in combination with rain/snow or no Precipitation, at the caster’s choice.\n\n    Temperature Levels\n\n    - Freezing (damage per round equals the result points, with a minimum of 1 point)\n    - Cold\n    - Warm\n    - Hot (all physical actions have a difficulty modifier equal to one-quarter of the result points, with a minimum of +1)\n    - Very hot (damage per round equals one-half of the result points, with a minimum of 1 point)\n\n    Wind Levels\n\n    - None\n    - Light breeze\n    - Moderate winds\n    - Strong winds (all physical actions have a difficulty modifier equal to one-quarter of the result points, with a minimum of +1)\n    - Gale (all physical actions have a difficulty modifier equal to one-half of the result points, with a minimum of +1)\n    - Storm (all physical actions have a difficulty modifier equal to the result points, with a minimum of +1)\n    - Hurricane/tornado (all physical actions have a difficulty modifier equal to 1.25 times the result points, with a minimum of +1; the gamemaster may also decide that small items are whipped about, causing injury)\n\n    The caster can cause any combination of these changes,\n    as long as the total point cost does not exceed 2 times the\n    result points of the spell casting.\n\n    - Expand the area affected by 1 meter: 5 points\n    - Change the temperature: Look up the desired change in degrees Celsius under the Measures column of the “Spell Measures” table; the equivalent value is the number of points this changes costs\n    - Change the pressure by 0.01 bars: 1 point\n    - Change humidity by 1 degree C\n\n    With a minimal success, the caster may only raise or lower\n    the temperature within 2 degrees Celsius. A slight breeze\n    could be created, and perhaps some wispy, clouds. Average\n    success allows the caster to raise or lower the temperature\n    by 5 degrees, conjure or dispel a moderate amount of cloud\n    cover, and a stiff breeze of less than 10 kph could also be cre-\n    ated or canceled. Good success on the casting roll will allow\n    the mage to cause or cancel light rain or snow, change the\n    temperature by up to 10 degrees, and change the wind speed\n    by up to 20 kph. Truly powerful weather conditions can be\n    created or stopped with a superior success. the temperature\n    can be raised or lowered by 20 degrees, and wind speed can\n    be modified by up to 40 kph. A thunderstorm or snowstorm\n    can be conjured or canceled. Spectacular success allows the\n    temperature to be raised or lowered by 30 degrees, wind\n    changes of up to 80 kph, and the ability to create or cancel\n    powerful storms of rain or snow.\n\n",
        effect=Effect(description="changes based on result points"),
        duration=DurationAspect(measure="1 hour"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 hour"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "area_effect": AreaEffectAspect(
                "11m radius sphere",
            ),
            "components": ComponentsAspect(
                "A rainmaker, a statuette or tube made of wood and designed to sound like rain when shaken",
                "common; destroyed",
            ),
            "concentration": ConcentrationAspect(
                "10 minutes",
                note="willpower/mettle difficulty of 11",
            ),
            "gestures": GesturesAspect(
                "Broad sweeping hand motions toward the sky",
                "simple",
            ),
            "incantations": IncantationsAspect(
                "Powers of nature, make the weather my slave.",
                "litany (willpower/mettle diffiuclty of 15)",
            ),
        },
        other_conditions=[
            ArcaneKnowledgeAspect("Air, inanimate forces, water"),
            GenericAspect(difficulty=0, description="Difficulty: 19"),
        ],
    ),
    Spell(
        name="Create Element (Template)",
        skill="Conjuration",
        notes="This is one of the first spells learned by many elemental\nmages. By casting the spell, the mage conjures a small amount\nof the element in its raw form. Water appears as a puddle if\nthere is no container to hold it; fire burns away merrily without\nfuel; air disperses into the space around it; and earth appears\nin a pile on the ground. None of these conjured elements can\nbe used as a weapon by creating them on or inside a person;\nthe effect of the spell makes the element only in a clear area\nunoccupied by another person or object.\n\nAs this is magically crafted material, it doesn’t have all the\nphysical characteristics as natural elements. For example,\ncreated water does not stay around long enough to be fully\ndigested by the body, but it can be used for cleansing. The\nfire only can be used to shed illumination. Air might aid in\nrespiration. Earth could be used to design a small enclosure.\nThe specific game benefits of these are based on the result\npoints and determined by the gamemaster.\n",
        effect=VolumeEffect("creates", "100 liters"),
        duration=DurationAspect(measure="10 minutes"),
        range=RangeAspect(measure="3.5 meters"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "gestures": GesturesAspect(
                "Cup hands, whisper into them, then mime throwing toward target spot",
                "simple",
            ),
            "incantations": IncantationsAspect(
                "Elemental Powers, create [name of element]!",
                "sentence; loud",
            ),
        },
        other_conditions=[
            ArcaneKnowledgeAspect("any one element: air, earth, fire, or water"),
            GenericAspect(difficulty=0, description="Difficulty: 11"),
        ],
    ),
    Spell(
        name="Create Elemental (Template)",
        skill="Conjuration",
        notes="In many elemental mage circles, the ability to cast this\nspell successfully is what differentiates the true masters of\nthe art from the pretenders. Performing the spell successfully\ncreates a powerful servant composed of the elemental type\nspecified by the spell. The caster dictates the attributes of the\nfinal form that the elemental takes as part of the spell. Some\nsamples are given below of the different type of elementals\nthat can be created.\n\nThe type of gemstone needed for the spell varies with what\ntype of elemental the caster is creating: Air needs a diamond,\nearth requires an emerald, fire specifies a ruby, and water\nuses a blue sapphire.\n\nThe elemental created is not necessarily under the control\nof the caster. A smart mage will be prepared to cast the con-\ntrol elemental spell immediately. Alternately, some casters\nwho have an intimate knowledge of elementals may try to\nuse gifts or promises of future favors to bribe the elemental\ninto serving them.\n\nThe 15 attribute dice may be allocated as the caster sees\nfit, and with the gamemaster’s permission, she may use some\nof the dice to buy Special Abilities to reflect the natural abili-\nties of the elemental. The elemental will have a number of\nBody Points equal to 10 plus the points by which the spell\nbeat the difficulty; Wound levels equal to the points above\nthe difficulty, divided by two, rounded up, minimum of one\nWound level. Movement equals the result points in meters\nper round, with a minimum of one meter per round.\n\n**Sample Elementals**\n\nHere are some sample elementals that could be\ncreated with this spell. Special Abilities are given for\npoint cost reference. The attribute names are from D6\nAdventure; gamemasters and players using other genres\nshould convert the names.\n\n**Air Elemental**: Reflexes 2D, Coordination 2D,\nPhysique 2D, Knowledge 1D, Perception 1D, Charisma\n1D. Move: 1+. Strength Damage: 1D. Body Points: 10+/\nWound levels: 1+. Natural Abilities: Flight (R1, 6 points),\nflying rate equals 2 times Move.\n\n**Earth Elemental**: Reflexes 2D, Coordination 1D,\nPhysique 6D, Knowledge 1D, Perception 1D, Charisma\n1D. Move: 1+.  Strength Damage: 3D. Body Points: 10+/\nWound levels: 1+. Natural Abilities: Natural Armor (R1,\n3 points) +1D to damage resistance totals.\n\n**Fire Elemental**: Reflexes 4D, Coordination 3D,\nPhysique 3D, Knowledge 1D, Perception 1D, Charisma\n1D. Move: 1+.  Strength Damage: 2D. Body Points: 10+/\nWound levels: 1+ . Natural Abilities:  Natural Ranged\nWeapon: Flame (R1, 3 points), 3D damage.\n\n**Water Elemental**: Reflexes 3D, Coordination 3D,\nPhysique 4D, Knowledge 1D, Perception 1D, Charisma\n1D. Move: 1+.  Strength Damage: 2D. Body Points: 10+/\nWound levels: 1+. Natural Abilities: Natural Armor (R1,\n3 points) +1D to damage resistance totals.\n",
        effect=AttributeEffect(
            "Essential attribute dice arranged as the caster likes; Body Points/Wounds and movement based on result points",
            "15D",
            "skill modifier",
        ),
        duration=DurationAspect(measure="1 hour"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="10 minutes"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect(
                "1 carat gemstone, see below for type",
                "very rare; destroyed",
            ),
            "concentration": ConcentrationAspect(
                "10 minutes",
                note="with willpower/mettle difficulty of 11",
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="on created elemental"
            ),
            "gestures": GesturesAspect(
                "Circular hand motions with gemstone com- ponent",
                "simple",
            ),
            "incantations": IncantationsAspect(
                "Long speech explaining exact details of the type of elemental desired",
                "litany (persuasion roll with difficulty of 15)",
            ),
        },
        other_conditions=[
            ArcaneKnowledgeAspect("any one element: air, earth, fire, or water"),
            GenericAspect(difficulty=0, description="Difficulty: 34"),
        ],
    ),
    Spell(
        name="Desiccate",
        skill="Alteration",
        notes="This is a particularly nasty spell, used by sorcerers with\nlittle regard for mercy. The spell is targeted with a marksman-\nship/firearms or apportation roll. If the attack is successful,\nthe target takes 3D of damage each round for the next 12\nrounds. This damage is caused by the rapid desiccation, or\nremoval of fluid, from all of the target’s soft tissues. This is\nan extremely painful and unpleasant process to say the least,\nand if the spell does enough damage to kill the target, all that\nis left is a dried, mummy-like husk.\n\nArmor is ineffective against this damage, since the dam -\nage comes from inside the target’s body. Any creature that\ndoes not have fluid inside of it, like a golem or other creature\nmade of stone, is unaffected.\n",
        effect=DamageEffect(
            "dessication",
            "3D",
            "physical damage; ignores all armor",
        ),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="5 meters"),
        casting_time=CastingTimeAspect(measure="2.5 seconds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "component": ComponentsAspect(
                "Small strip of dried rawhide",
                "very common; destroyed",
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="on target"
            ),
            "gestures": GesturesAspect("Point at target", "simple"),
            "incantations": IncantationsAspect(
                "Drought shall be your death!", "sentence"
            ),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-1,
                description="Ineffective against those without fluid in their bodies",
            ),
            ArcaneKnowledgeAspect("Water"),
            GenericAspect(difficulty=0, description="Difficulty: 16"),
        ],
    ),
    Spell(
        name="Drown",
        skill="Conjuration",
        notes="To cast this spell, the mage fills his mouth with water,\nspits it at the target, and speaks the incantation. The spell\nis aimed with a throwing (not apportation) roll. If it hits suc-\ncessfully, the target’s lungs fill with water and she begins to\ndrown, taking 6D of damage for the next two rounds. Armor\ndoes not help absorb this damage, but the target can make\na stamina roll with a difficulty equal to the caster’s spell skill\ntotal to expel the water from his lungs after the first round.\nIf successful, he takes no damage from the second round of\nthe spell effect.\n",
        effect=DamageEffect(
            "Drowning",
            "6D",
            "physical damage; ignores all armor",
        ),
        duration=DurationAspect(measure="2 rounds"),
        range=RangeAspect(measure="2.5 meters"),
        casting_time=CastingTimeAspect(measure="3.5 seconds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect(
                "A mouthful of water", "ordinary; destroyed"
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="on target"
            ),
            "gestures": GesturesAspect(
                "Spit mouthful of water at target",
                "simple",
            ),
            "incantations": IncantationsAspect(
                "A sailor’s death shall take you!",
                "sentence",
            ),
        },
        other_conditions=[
            ArcaneKnowledgeAspect("Water"),
            GenericAspect(difficulty=0, description="Difficulty: 21"),
        ],
    ),
    Spell(
        name="Earth Muse",
        skill="Divination",
        notes="Although there are many who may choose to think otherwise, there are beings that dwell just beyond the realm of\nhuman perception. These spiritual elemental forces of nature\noften live far longer than the mere mortals who sometimes\nrudely intrude upon their realm. Theirs is the gift of knowl-\nedge, for these enigmatic souls have experienced much dur-\ning their existence. The power of the earth muse spell allows\nthe mage to communicate with elemental forces that dwell\nwithin the ground, untamed stone or stone structures. Such\ncreatures are able to speak of things that have occurred in\nthe spell’s area of effect. Persistent characters who repeat -\nedly question the earthen sages about items or events that\nare out of their range of caring (events that are more than\n2.5 months old) or beyond the area of effect cause the spell\nto abruptly end. The caster has worn out her welcome with\nthe beings that she’s trying to gather information from. If\nthis should happen, no spirits will answer the caster’s call\nfor 24 hours should she attempts to recast earth muse  in\nthe same area. A Critical Failure along with a failed skill roll\nwhen attempting to cast earth muse temporally blights the\nintended area of effect and no earth muse spells will function\nthere for 24 hours.\n",
        effect=TimeEffect("view the past", "2.5 months"),
        duration=DurationAspect(measure="5 minutes"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="40 minutes"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "area_effect": AreaEffectAspect("25m r divination sphere"),
            "components": ComponentsAspect(
                "A miniature sundial; dirt or stone",
                "uncommon; ordinary",
            ),
            "concentration": ConcentrationAspect(
                "1 round",
                note="with a willpower/mettle difficulty of 8",
            ),
            "gestures": GesturesAspect(
                "As the incantation is spoken, place hands on the stone or ground in the center of the area of effect; slowly, draw in the arms and place the palms on closed eyes. After pausing for several seconds, throw hands out wide.",
                "simple",
            ),
            "incantations": IncantationsAspect(
                "Utter the following after meditation: “Oh mighty spirits who have seen all, heed my plea and answer my call. The time grows nigh to share your thoughts; come to me now and show what time has wrought!”",
                "litany (persuasion roll with difficulty of 15)",
            ),
        },
        other_conditions=[
            ArcaneKnowledgeAspect("earth, time"),
            GenericAspect(difficulty=0, description="Difficulty: 19"),
        ],
    ),
    Spell(
        name="Earthquake",
        skill="Alteration",
        notes="Casting this spell causes the ground within the area of\neffect to be shaken by violent tremors. Anything or anyone\ntouching the ground will take 5D of damage for each full\nround they spend inside the area of the quake. Stationary\ntargets — such as trees and buildings — take an additional\n10D of damage per round. Any movement through the area\nof the quake decreases by a number of meters per round equal\nto the result points (minimum adjustment of zero), as the\nshaking throws about objects and heaves the ground.\n\nBecause the area of the spell is so large, no targeting roll\nis necessary. The caster may simply center the quake on any\npoint within the range.\n\nAfter the spell is cast, it takes the quake some time to begin.\nUse the “Spell Measures” chart in the rulebook to find the\nvalue of the range from the caster to the center of the quake,\nsubtract the speed value of 5, and look up this number on the\nchart. Convert the related measure to minutes or seconds to\nsee how long it takes the quake to begin.\n",
        effect=DamageEffect("Earthquake", "5D", "physical damage"),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="1 kilometer"),
        casting_time=CastingTimeAspect(measure="1 hour"),
        speed=SpeedAspect("10m per second"),
        other_aspects={
            "area_effect": AreaEffectAspect("15m r circle"),
            "components": ComponentsAspect(
                "A diamond of at least 1 carat",
                "very rare; destroyed",
            ),
            "concentration": ConcentrationAspect(
                "10 minutes",
                note="with willpower/mettle difficulty of 11",
            ),
            "gestures": GesturesAspect(
                "A series of foot and hand gestures",
                "complex (acrobatics roll with difficulty of 11)",
            ),
            "incantations": IncantationsAspect(
                "Complex litany of elemental names and formulas",
                "litany (languages/speaking roll with difficulty of 15)",
            ),
            "other_alterants": OtherAlterant(
                difficulty=30,
                description="+10D additional damage done to stationary targets",
            ),
        },
        other_conditions=[
            GenericAspect(difficulty=-1, description="Cannot affect anything flying"),
            ArcaneKnowledgeAspect("Earth"),
            GenericAspect(difficulty=0, description="Difficulty: 32"),
        ],
    ),
    Spell(
        name="Elemental Body (Template)",
        skill="Conjuration",
        notes="When cast, this spell covers the body of the target (and\nanything she wears or holds) in a sheath of the element.\nThis sheath provides armor and adds damage to any attacks\nmade with appendages or hand-held weapons. The armor\nand damage effects are doubled if they are used against\nthe opposite element. For example, a mage sheathed in fire\nwould do double damage against water-based creatures, and\nhis armor from the spell would protect him double from\nwater-based attacks.\n",
        effect=CompositeEffect(
            "Sheathed in Elemental",
            DamageEffect("Elemental Attack", "2D"),
            ProtectionEffect("Elemental Armor", "2D"),
        ),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="1.5 seconds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="on target"
            ),
            "gestures": GesturesAspect("Touch subject", "very simple"),
            "incantations": IncantationsAspect(
                "[Name of element], protect me and harm my foe!",
                "sentence",
            ),
            "other_alterants": OtherAlterant(
                difficulty=6,
                description="Effect doubled against one opposite element (specified at time of casting)",
            ),
        },
        other_conditions=[
            ArcaneKnowledgeAspect("any one element: air, earth, fire, or water"),
            GenericAspect(difficulty=0, description="Difficulty: 15"),
        ],
    ),
    Spell(
        name="Elemental Burst (Template)",
        skill="Conjuration",
        notes="A favorite of many combat mages, this spell conjures a\npowerful burst of the element, damaging all the targets within\nits area. The spell does not discern between friend and foe,\nso the caster must use care in aiming the blast.\n\nThe form of the shot depends on the element used: Air is\na concussive inward blast; earth, a hail of rocks; fire, a huge\nburst of flame; and water, a powerful drowning wave.\n\nThe caster generates a throwing or apportation total against\nthe combat difficulty of the main target. The total receives a\n+3, because the spell covers a large area, making it easier to\nhit the target. Those more than a meter away from the center\nwith defense totals greater than the targeting roll (without\nthe bonus) dodge out of the way. For everyone else, reduce the\ndamgae done by 1 for each meter away from the center.\n",
        effect=DamageEffect("Elemental damage", "4D", "physical damage"),
        duration=DurationAspect(measure="1 second"),
        range=RangeAspect(measure="40 meters"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "area_effect": AreaEffectAspect("3m r sphere"),
            "components": ComponentsAspect(
                "A tiny amount of the element used in the burst",
                "ordinary",
            ),
            "gestures": GesturesAspect(
                "Move both hands inward, and then throw them out like an explosion",
                "simple",
            ),
            "incantations": IncantationsAspect(
                "[Name of element], destroy my enemies with your power!",
                "sentence",
            ),
        },
        other_conditions=[
            ArcaneKnowledgeAspect("any one element: air, earth, fire, or water"),
            GenericAspect(difficulty=0, description="Difficulty: 17"),
        ],
    ),
    Spell(
        name="Elemental Edge (Template)",
        skill="Conjuration",
        notes="This simple spell covers the dangerous part of a weapon\nwith a sheath of energy that causes extra damage. The type\nof energy varies depending on the elemental type of the\nspell: Air covers the weapon in electricity, earth is acid, the\nfire sheath is flames, and water is brutally cold ice. For the\nduration of the spell, the weapon inflicts an additional 3D of\ndamage every time it successfully strikes a target.\n",
        effect=DamageEffect(
            "Edge to a weapon", "3D", "physical damage; damage modifier"
        ),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="3.5 seconds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="on target weapon"
            ),
        },
        other_conditions=[
            ArcaneKnowledgeAspect("any one element: air, earth, fire, or water"),
            GenericAspect(difficulty=0, description="Difficulty: 12"),
        ],
    ),
    Spell(
        name="Elemental Scrying",
        skill="Divination",
        notes="According to some philosophies, the entire universe is\ncomposed of the four elements. By drawing upon the con -\nnection of these elements to all things, the caster can pull\nback the veil of time and peer into the future. Because the\nfuture is not set, the visions that the caster sees of the future\nmay or may not come true, and divination is far from an exact\nscience. The act of seeing what will happen in the target’s\nfuture can often change the future as well, so anything seen\nwith this spell should be taken with a grain of salt in the best\nof circumstances.\n\nTo cast the spell, the mage spends one minute murmuring\nthe incnatation over the elements and the bit of the target.\nAt the end of that time, the caster receives a burst of insight,\nhighlighting about five minutes’ worth of events for the next\nmonth of the target’s life. The result points of the casting roll\ndetermine how much information the caster can get about\nthe target’s future.\n\nZero points reveals small details and perhaps a few flashes of\nimportant facts. One to four points allows the most important\nor dangerous event to be revealed, without a great amount of\ndetail. Five to eight points gives more information about the\nkey event, and a much closer timeframe, along with minor\ndetails. Nine to 12 points allows even more details and vague\ninformation about the remainder of the day surrounding the\nkey as well. More than 12 points reveals up to five minutes\nof the most important event like a movie, plus gives a decent\nrecounting of the remainder of the month, even if that would\nmake duration longer than five minutes.\n\n**Example**: Morgan the mage wants to see into her com -\npanion Bator’s future. She successfully casts the spell. If\nshe achieved a minimal success, she would know that Bator\nwill be in grave danger during the next month. On a solid\nsuccess, she would know that the fighter was going to be\nambushed some time in the afternoon of the following day.\nGood success would tell Morgan that Bator was going to be\nambushed by a large group; sometime in the early afternoon.\nSuperior success would tell the mage that the rest of Bator’s\nmonth will be uneventful, and that the ambush was going\nto be from a group of 15 goblins at 2:00 p.m. Finally, if the\nmage manages to achieve Spectacular success, she will see the\nambush as if it were happening in front of her, with a good\namount of exacting detail.\n\nNote that in the example above the mage was never told\nexactly where the ambush would happen, or how to avoid it.\nEven if Bator stays right where he is for a month, the ambush\ncould still happen, but the details would change slightly from\nthe vision seen by the scrying mage. The gamemaster should\nnever let a good roll on a divination spell disrupt the game.\n",
        effect=TimeEffect("View the future", "1 month"),
        duration=DurationAspect(measure="5 minutes"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 minute"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect(
                "A small piece of the target of the spell, such as nail clippings, a few hairs, or a drop of blood (common); small amount of each of the four elements",
                "very common; destroyed",
            ),
            "gestures": GesturesAspect("Wave hands over components", "simple"),
            "incantations": IncantationsAspect(
                "Elements of the universe, show me this person’s future.",
                "sentence",
            ),
        },
        other_conditions=[
            ArcaneKnowledgeAspect("Time, earth, air, fire, water"),
            GenericAspect(difficulty=0, description="Difficulty: 13"),
        ],
    ),
    Spell(
        name="Flame Jet",
        skill="Conjuration",
        notes="This spell causes a roaring line of fire to erupt from the\ncaster’s fingertip. The jet is only a few centimeters across,\nbut it extends out to about three meters from the caster.\nThe caster can freely turn the effect on and off during the\none minute duration, to avoid accidentally burning things\nhe does not want to. Marksmanship/firearms or apportation is\nused to aim the jet if it is being used as an attack. The caster\ncan make one attack with it per round.",
        effect=DamageEffect(
            "Fire Attack",
            "4D",
            "physical damage",
        ),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="3 meters"),
        casting_time=CastingTimeAspect(measure="2.5 seconds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect("A small open flame", "ordinary; destroyed"),
            "gestures": GesturesAspect("Point finger", "simple"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="on caster's finger"
            ),
            "incantations": IncantationsAspect("Burn!", "word"),
            "variable_duration": VariableDurationAspect("on/off switch"),
        },
        other_conditions=[
            ArcaneKnowledgeAspect("Fire"),
            GenericAspect(difficulty=0, description="Difficulty: 17"),
        ],
    ),
    Spell(
        name="Lightning Bolt",
        skill="Conjuration",
        notes="This spell generates a powerful stroke of lightning. The\ncaster must aim the bolt using throwing or apportation. If\nthe target of spell is wearing large amounts of metal, (a suit\nof chain or plate armor, for example), she is much easier to\nhit, giving a modifier of +3 to the targeting total. If a large\npiece of metal is within a meter of the caster or the target,\na modifier of +3 should be added to the difficulty to hit the\ntarget, because the metal will tend to pull the lightning away\nfrom its intended path.\n\n",
        effect=DamageEffect(
            "Electrical Damage -- air plus fire", "6D", "physical damage"
        ),
        duration=DurationAspect(measure="1 second"),
        range=RangeAspect(measure="100 meters"),
        casting_time=CastingTimeAspect(measure="2.5 seconds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect(
                "A small steel or iron rod; a piece of wool",
                "very common; very common",
            ),
            "gestures": GesturesAspect(
                "Rub the wool on the steel rod, and then mimic flinging a bolt",
                "simple",
            ),
            "incantation": IncantationsAspect(
                "Power of lightning, smite my foe!",
                "sentence; loud",
            ),
            "other_alterant": OtherAlterant(
                difficulty=3,
                description="Gain a bonus against targets wearing metal",
            ),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-1,
                description="Targeting difficulty increased when used near large amounts of metal",
            ),
            ArcaneKnowledgeAspect("Inanimate Forces"),
            GenericAspect(difficulty=0, description="Difficulty: 15"),
        ],
    ),
    Spell(
        name="Miasma",
        skill="Conjuration",
        notes="A thick, black pall appears at the targeted location. Each\nround that a character is within the dense cloud, she suffers\n5D damage. The miasma also obscures sight, so all attacks\nare done blind. All damage comes from inhaling.\n\n",
        effect=CompositeEffect(
            "Miasma",
            DamageEffect("Inhaling Damage", "5D", "ignores all armor"),
            DisadvantageEffect(
                "Hindrance: Blindness",
                12,
                "+4 to difficulties of all sight-dependent actions",
            ),
        ),
        duration=DurationAspect(measure="3 rounds"),
        range=RangeAspect(measure="40 meters"),
        casting_time=CastingTimeAspect(measure="2 rounds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "area_effect": AreaEffectAspect("3m r sphere"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="on targets"
            ),
            "components": ComponentsAspect("Rotten egg", "common"),
            "gestures": GesturesAspect("Point", "simple"),
        },
        other_conditions=[
            ArcaneKnowledgeAspect("Air, darkness"),
            GenericAspect(difficulty=0, description="Difficulty: 54"),
        ],
    ),
]


__test__ = {
    "Acidic Attack": ">>> spells[0].difficulty\n20",
    "Burrow": ">>> spells[1].difficulty\n14",  # Rules state Effect incorrectly as 18, when it's 11.
    "Cone of Wind": ">>> spells[2].difficulty\n15",  # Riles state area of effect incorrect as 10, when it's 18.
    "Control Elemental (Template)": ">>> spells[3].difficulty\n17",  # Rounding issue -- rules say 18.
    "Control Local Weather": ">>> spells[4].difficulty\n20",
    "Create Element (Template)": ">>> spells[5].difficulty\n11",
    "Create Elemental (Template)": ">>> spells[6].difficulty\n34",
    "Desiccate": ">>> spells[7].difficulty\n15",  # Rounding, rules say 16.
    "Drown": ">>> spells[8].difficulty\n22",  # Round, rules say 21
    "Earth Muse": ">>> spells[9].difficulty\n19",
    "Earthquake": ">>> spells[10].difficulty\n32",
    "Elemental Body (Template)": ">>> spells[11].difficulty\n14",  # Rules say 15
    "Elemental Burst (Template)": ">>> spells[12].difficulty\n17",
    "Elemental Edge (Template)": ">>> spells[13].difficulty\n13", # Rules say 12
    "Elemental Scrying": ">>> spells[14].difficulty\n14",  # Rules say 13
    "Flame Jet": ">>> spells[15].difficulty\n16",  # Rules say 17
    "Lightning Bolt": ">>> spells[16].difficulty\n15",
    "Miasma": ">>> spells[17].difficulty\n54",
}


if __name__ == "__main__":
    app = build_app(spells)
    app()
