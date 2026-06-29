"""
Photomancy

When run as an app, generates .RST-formatted details of each Spell.
"""

from decimal import Decimal
from typing import Annotated, Any
import typer
from opend6_tools.magic2 import *

spells = [
    Spell(
        name="Aura of Visibility",
        skill="Alteration",
        notes="With an intended target in sight and not more than 10\nmeters distant, the magic user waves an owl’s feather before\nhis eyes several times and utters an incantation. The feather\nis then consumed in a brilliant, momentary flash of fire. Now\nthe target creature is bathed in an aura of shimmering white\nlight that only the magic user can see. The aura is so bright\nthat it negates up to -4D of darkness modifier (including the\neffects of fog, smoke, and mist), allowing the mage to see\nand attack the creature without penalty in even the most\ncomplete darkness.\n\n",
        effect=SkillEffect("negates any darkness modifier up to", *["+4D"]),
        duration=DurationAspect(measure="5 rounds"),
        range=RangeAspect(measure="10 meters"),
        casting_time=CastingTimeAspect(measure="2.5 sec"),
        speed=SpeedAspect.based_on(("range",), "Intantaneous"),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Light"),
            "components": ComponentsAspect("Owl feather", "common; destroyed"),
            "gestures": GesturesAspect(
                "Wave feather before his eyes while looking at intended target",
                *["simple"],
            ),
            "incantations": IncantationsAspect(
                "'“Lift the shroud of darkness that I might see my enemy”'",
                *["sentence"],
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 10")],
    ),
    Spell(
        name="Blur",
        skill="Alteration",
        notes="With a casual swipe of a hand over his eyes, the mage\n(or his chosen target) becomes indistinct to the naked eye\nby bending light over his form. For a period of one minute,\nthe mage adds 2 to his dodge, stealth/sneak, and hide totals,\nas +2 to all default search, tracking, investigation, and attack\ndifficulties against the mage. As this is an illusory spell,\ncharacters may disbelieve the effects with a mettle/willpower\nroll of 13. Those who succeed are thereafter able to see the\nmage distinctly.",
        effect=SpecialAbilityEffect("Blur ", 2, note=" Special Ability"),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Darkness, Folk"),
            "gestures": GesturesAspect("Wipe palm over eyes", *["simple"]),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Difficulty: 11"),
            GenericAspect(
                difficulty=-5, description="Unreal Effect: Disbelief difficulty of 13"
            ),
        ],
    ),
    Spell(
        name="Glowing Eyes",
        skill="Conjuration",
        notes="With a minimal amount of pain to himself, the caster curses\na target with glowing eyes, thereby giving the creature the\nlook of that which is demon possessed or otherwise infernal\nin nature. This makes it extremely difficult for the afflicted\nto interact successfully with other beings, as people become\nill at ease by his unnatural appearance. The target has no\nmeans of knowing that he has been cursed except perhaps\nby looking in a mirror or other reflective surface.\nIn some cases, the spell may actually incur a bonus. If\nthe mage wanted to pass himself off as a demon or use it\nagainst extremely superstitous folk, for example, it might\nprovide some minor skill total bonuses (determined by the\ngamemaster).",
        effect=DisadvantageEffect(
            "Infamy ", 2, note=", feared by most because of glowing eyes"
        ),
        duration=DurationAspect(measure="4 hours"),
        range=RangeAspect(measure="10 meters"),
        casting_time=CastingTimeAspect(measure="2 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Light"),
            "concentration": ConcentrationAspect("1 round"),
            "feedback": FeedbackAspect(3),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 16")],
    ),
    Spell(
        name="Holy Light",
        skill="Conjuration",
        notes="When cast, the magic user creates a bright flare of light\nthat seems to emanate from his being. Up to five evil or\nundead targets within range and looking at the caster are\nblinded by this light. All sight-based actions for the affected\nincrease by +5 for one minute.",
        effect=DisadvantageEffect(
            "Hindrance: Blindness ",
            15,
            note="+5 to difficulties of all sight-dependent actions",
        ),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="10 meters"),
        casting_time=CastingTimeAspect(measure="3.5 seconds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Light"),
            "gestures": GesturesAspect(
                "With head titled back and eyes closed as if basking in the sun’s warmth, extend arms out to the sides",
                *["simple"],
            ),
            "incantations": IncantationsAspect(
                "'“The sun abhors darkness, and evil cowers from the light that is goodness.”'",
                *["sentence", "loud"],
            ),
            "mulitiple_targets": MultipleTargetAspect("5 targets")
        },
        other_conditions=[
            GenericAspect(
                difficulty=-2,
                description="Only affects evil or undead beings who can see the caster",
            ),
            GenericAspect(difficulty=0, description="Difficulty: 35"),
        ],
    ),
    Spell(
        name="Light Chest",
        skill="Conjuration",
        notes="The magic user casts this spell on a glass disc and a finely\ncrafted cube of crystal, which is destroyed and replaced by a\nchest of radiant light. The chest had no weight, but its walls\nand lid are solid and it can be moved.\nWhen the spell is cast, the mage selects a password, and the\nchest cannot be opened by any creature, including the mage,\nunless the password is first spoken. Efforts at lockpicking are\nfutile. Any item, or combination of items, measuring less than\nfour cubic meters can be stored within the magical chest.\nThe chest lasts for one week and then disappears, leaving\nbehind the glass disk and any items that had been stored\nwithin.",
        effect=SkillEffect("Armor Value of  , physical only", *["+6D"]),
        duration=DurationAspect(measure="1 week"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="3.5 minutes"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Light, Dimension"),
            "area_effect": AreaEffectAspect("1 meter height 2 meter width and depth cuboid"),
            "components": ComponentsAspect(
                ("Crystal cube", "very rare; destroyed"),
                ("small glass disc", "very common"),
            ),
            "concentration": ConcentrationAspect("5 seconds"),
            "gestures": GesturesAspect(
                "Hold crystal cube and disk in outstretched hands to catch the light, then place it at feet",
                *["simple"],
            ),
            "incantations": IncantationsAspect(
                "'“Chest of light, secure what’s mine by right.”'", *["sentence"]
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On glass disc"
            ),
            "variable_duration": VariableDurationAspect("on/off switch"),
            "other_alterant": OtherAlterant(2, "Can be carried; resistant to adverse environmental conditions (dust, rain, heat, etc.)"),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-1, description="A source of illumination is present"
            ),
            GenericAspect(difficulty=0, description="Difficulty: 20"),
        ],
    ),
    Spell(
        name="Light Ram",
        skill="Conjuration",
        notes="To cast this spell, the mage releases a tuff of wool into the\nair (which is subsequently consumed by flame), shakes a ram’s\nhorn at an individual target, and utters a simple incantation.\nImmediately thereafter, a shimmering mass of glowing light\nappears, which vaguely discernible as a ram (or, in cultures\nwhere more appropriate, a bull, bison, elephant, or other\npowerful animal known for charging enemies). When this\nunleashed force strikes a target within 15 meters, it deals\n4D damage.\nThe force of the blow is overwhelming; targets hit by the\nspell feel as if they have indeed been impacted by a raging\nram and are staggered, if not thrown back. As a result, a\ncharacter struck by the spell is also subject to a 2D penality\nto Agility/Reflexes-related actions until the target’s turn in\nthe next round.\nIn addition to being used as a weapon, light ram can also\nbe used to batter down doors it strikes. This is particularly\nhandy during dungeon and building explorations.\nThe mage must succeed with a marksmanship/firearms or\napportation roll to hit the target.\n\n",
        effect=CompositeEffect(
            "Light Ram",
            DamageEffect("physical damage", "4D", "physical damage"),
            DisadvantageEffect("Reduced Attribute: Agility/Reflexes", 7, note="-2D to the attribute"),
        ),
        duration=DurationAspect(measure="1 round"),
        range=RangeAspect(measure="15 meters"),
        casting_time=CastingTimeAspect(measure="1.5 seconds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Light, Inanimate Forces"),
            "components": ComponentsAspect(
                ("Horn or tusk of a charging animal", "common"),
                ("tuff of wool", "very common; destroyed"),
            ),
            "countenance": CountenanceAspect(
                "Mage appears drained and winded", "noticeable"
            ),
            "feedback": FeedbackAspect(3),
            "gestures": GesturesAspect(
                "Tuff of wool is released into the air and the horn violently shaken at the target",
                *["simple"],
            ),
            "incantations": IncantationsAspect(
                "'“Unleash the might of light.”'", *["phrase"]
            ),
            "other_alterant": OtherAlterant(1, "Effect appears as a powerful, charging animal"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Difficulty: 17"),
        ],
    ),
    Spell(
        name="Light Show",
        skill="Alteration",
        notes="To cast this spell, the mage must have a jar of living fireflies\nor similar insects. He simply says a few words of power, points\na finger at the target, and releases the fireflies (which die upon\nthe spell expiring). For a period of one minute, the fireflies\nbecome flashing, dancing orbs of glowing light, many times\ngreater in intensity than normal and far more enthralling.\nShould the target fail an opposed interaction roll against\nthe light’s charm/persuasion of 5D+1, the target of the spell\nis compelled to do nothing but watch them.\nIf the entranced creature is harmed, it recovers its senses\nand is no longer affected by the spell.",
        effect=SkillEffect("lights with charm/persuasion of", *["+5D+1"]),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="60 meters"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Light"),
            "components": ComponentsAspect(
                "Jar of fireflies or similar glowing insects",  "uncommon; destroyed"
            ),
            "gestures": GesturesAspect(
                "Point finger at target and release fireflies", *["simple"]
            ),
            "incantations": IncantationsAspect("'“Watch and be amazed.”'", *["phrase"]),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 14")],
    ),
    Spell(
        name="Mass Light Show",
        skill="Conjuration",
        notes="After saying a few words of power and pointing a finger at\nthe center of the intended 10-meter circle area of effect, she\nreleases the fireflies (which die upon the spell expiring). For\na period of one minute the fireflies become flashing, dancing\norbs of bright, enthralling light. All living creatures within\nthe area of effect must make an opposed interaction roll\nagainst the spell’s charm/persuasion of 5D or be compelled to\ndo nothing but watch them. Harming any entranced creature\nbreaks the spell.",
        effect=SkillEffect("lights with charm/persuasion of  ", *["+5D"]),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="100 meters"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Light"),
            "area_effect": AreaEffectAspect("10 meter radius circle"),
            "components": ComponentsAspect(
                "Jar of fireflies or similar glowing insects", "uncommon; destroyed"
            ),
            "gestures": GesturesAspect(
                "Point finger at target and release fireflies", *["simple"]
            ),
            "incantations": IncantationsAspect(
                "'“Watch and be amazed, one and all”'", *["sentence"]
            ),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Difficulty: 24"),
        ],
    ),
    Spell(
        name="Night Vigilance",
        skill="Alteration",
        notes="This spell uses an owl’s eye to increase the nighttime\nvigilance and acuity of a single individual. The mage utters\na short phrase while passing the component over the eyes\nof the intended target. When the spell is cast, the owl’s eye\nturns to dust.\nThe subject of this spell becomes extremely attuned to the\nnight and unusually aware of his surroundings for a period\nof four-hours. During this time, the character gains a search\nbonus of +5D. However, this spell in no way reduces the need\nfor sleep or the negative effects resulting from lack of rest.\nThe target of the spell must still sleep 4+ hours or suffer the\neffects of fatigue.",
        effect=SkillEffect("to search skill", *["+4D", "skill modifier"]),
        duration=DurationAspect(measure="4 hours"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Darkness"),
            "components": ComponentsAspect("Owl’s eye", "uncommon; destroyed"),
            "gestures": GesturesAspect(
                "Pass the owl eye over the eyes of the target", *["simple"]
            ),
            "incantations": IncantationsAspect("'“See better.”'", *["phrase"]),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[
            GenericAspect(difficulty=-1, description="Can only be cast at night"),
            GenericAspect(difficulty=0, description="Difficulty: 15"),
        ],
    ),
    Spell(
        name="Nyctophobia",
        skill="Conjuration",
        notes="Though the caster of this spell endures some pain to herself\n, she curses a person with a severe case of nyctophobia\n(fear of the dark or night) for 10 minutes. Characters that\nare overcome by their fright dissolve into quivering wrecks.\nThey can take no actions until the darkness is eliminated or\nthey’re removed from the darkened environment (at which\npoint they may make another attempt to overcome the\nfright using willpower/mettle or the default attribute). The\nexpiration of the spell’s duration immediately returns the\ntarget to normal.\n\n",
        effect=DisadvantageEffect(
            "Quirk ",
            3,
            note=", nyctophobia with Very Difficult will-power/mettle roll to overcome",
        ),
        duration=DurationAspect(measure="10 minutes"),
        range=RangeAspect(measure="10 meters"),
        casting_time=CastingTimeAspect(measure="2 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Darkness, Folk"),
            "concentration": ConcentrationAspect("1 round"),
            "feedback": FeedbackAspect(3),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[
            GenericAspect(difficulty=-1, description="Limited to sentient beings"),
            GenericAspect(difficulty=0, description="Difficulty: 19"),
        ],
    ),
    Spell(
        name="Shadow Surface",
        skill="Conjuration",
        notes="Shadow surface allows a mage to create illusionary walls,\nfloors, ceilings, or other surfaces out of darkness. To cast\nit, the wizard outlines the illusionary surface’s dimensions\nwith a charcoal stick.\nThe surface appears absolutely real when viewed, but\nphysical objects may pass through it effortlessly. The spell\nis often used to mask doors, pits, or traps within tombs,\nfortresses, or other areas intended to be secure. Touch or\nprobing searches  always reveal the true nature of the surface,\nthough they do not cause the illusion to disappear. The only\nmeans by which the illusion might be removed, save for its\nduration expiring, is by exposure to a light source strong\nenough to negate it.",
        effect=Effect(
            description="difficulty to view hidden area or dispel darkness shrouding it",
            difficulty=20,
        ),
        duration=DurationAspect(measure="1 year"),
        range=RangeAspect(measure="2.5 meters"),
        casting_time=CastingTimeAspect(measure="1 hour"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Darkness"),
            "area_effect": AreaEffectAspect("3 meter radius sphere"),
            "components": ComponentsAspect(
                "Stick of charcoal", "very common, destroyed"
            ),
            "countenance": CountenanceAspect(
                "Caster develops dark rings under eyes during casting time",
                "noticeable",
            ),
            "gestures": GesturesAspect(
                "Outline the area of effect with charcoal", *["simple"]
            ),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-2,
                description="Limited to areas continuously in darkness or shadow",
            ),
            GenericAspect(difficulty=0, description="Difficulty: 27"),
        ],
    ),
    Spell(
        name="Shroud of Shade",
        skill="Conjuration",
        notes="Typically, this spell is used on vampires and demons. By\nholding a fragment of a burial shroud over herself or another\nbeing within a meter range, the caster creates an ethereal\nshroud that protects the target from the damaging rays of\nthe sun. The shroud appears as a dark and filmy cape and\nhood that covers the target’s entire body. As a result, the\ntarget is nearly immune to the effects of normal sunlight\nfor a short time and might walk about unaffected, a valuable\nboon for vampires.\nAt the time of casting, the mage can convert the result\npoints from the casting into a bonus to protection or dura-\ntion. Convert the bonus points put into the effect into dice\nand pips of Armor Value (three points per die; one point\nper pip). Use the “Spell Measures” chart in the D6 Fantasy\nor D6 Adventure rulebooks to determine the addition to the\nduration in seconds.",
        effect=SkillEffect("Armor Value of  , physical only", *["+4D"]),
        duration=DurationAspect(measure="2.5 hours"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Darkness, light, entity"),
            "components": ComponentsAspect(
                "Fragment of a funeral shroud from an occupied grave", "uncommon; destroyed"
            ),
            "gestures": GesturesAspect(
                "Hold shroud fragment over the target’s head", *["simple"]
            ),
            "incantations": IncantationsAspect(
                "'“Dark force rising, protect thee from the light.”'", *["sentence"]
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-3,
                description="Limited to those creatures physically harmed by exposure to sunlight or bright light; only protects against light",
            ),
            GenericAspect(difficulty=0, description="Difficulty: 10"),
        ],
    ),
    Spell(
        name="Sight of Darkness",
        skill="Conjuration",
        notes="By the magic user sacrificing some of her life energy, she\ngrants a target with 24 hours of three ranks in Infravision\nor Ultravision (which the caster chooses before casting the\nspell). See the description of this Special Abilities in the\n“Character Options” chapter for more details.",
        effect=DisadvantageEffect(
            "Infravision or Ultravision ",
            3,
            note=", negates up to 6 points of modifiers for dim or dark conditions",
        ),
        duration=DurationAspect(measure="1 day"),
        range=RangeAspect(measure="10 meters"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Light, darkness"),
            "components": ComponentsAspect("Flint and tinder", "common"),
            "feedback": FeedbackAspect(3),
            "incantations": IncantationsAspect("'“See.”'", *["phrase"]),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 20")],
    ),
    Spell(
        name="Sinister Pall",
        skill="Alteration",
        notes="With a scowl and general menacing countenance, the\ncaster improves her intimidation skill for one minute. Her\nfeatures become shadowed and sinister, like the villain from\na horror movie. People are naturally unsettled by the cast -\ners appearance and therefore more prone to bending to the\nforce of his will.\n\n",
        effect=SkillEffect("+  to intimidation", *["+4D", "skill modifier"]),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Darkness"),
            "gestures": GesturesAspect(
                "Scowl darkly and clench fists menacingly", *["simple", "offensive"]
            ),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 11")],
    ),
    Spell(
        name="Sniper Light Beam",
        skill="Alteration",
        notes="This spell creates a light beam that extends down the sights\nof a projectile weapon, effectively serving as a sniper’s laser\nsight. This improves the mage’s related ranged combat skill\nwhen using that weapon for a period of one minute. This\nbonus cannot be used with weapons that depend strength\nfor their power, such as bows or slings.",
        effect=SkillEffect("one targeting skill", *["+4D", "skill modifier"]),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="3.5 seconds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Light"),
            "gestures": GesturesAspect(
                "Run trigger finger down the length of weapon", *["simple"]
            ),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-2,
                description="May only be used with a single direct-fire, self-powered projectile weapon, such as a crossbow or a gun",
            ),
            GenericAspect(difficulty=0, description="Difficulty: 10"),
        ],
    ),
    Spell(
        name="Stunt Plant",
        skill="Alteration",
        notes="The caster literally presses back plant life before her,\ndiminishing or even killing them through the deprivation\nof light. All plants require light to grow. The effect lasts for\nthree and a half minutes. Vegetation (grasses, briars, shrubs,\ntrees) within five meters of the caster shrink a quarter of its\nnormal size each round, becoming less bushy and entangling.\nThis allows for freer movement within the area of effect.\nAssuming plants haven’t died completely, they begin to\nslowly rejuvenate as soon as the spell is complete, growing\nas per normal for the plant species in question. Trees may\ntake years or even decades to return to their previous state,\nwhile grass may require only a few weeks.",
        effect=Effect(
            description="reduce movement difficulty modifiery by up to -5", difficulty=5
        ),
        duration=DurationAspect(measure="3.5 minutes"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Darkness, Plant"),
            "area_effect": AreaEffectAspect("5m radius circle"),
            "countenance": CountenanceAspect(
                "Caster takes on a gray pallor", "noticeable"
            ),
            "gestures": GesturesAspect(
                "Spread hands in intended direction and lower as if pressing down on something",
                *["simple"],
            ),
            "incantations": IncantationsAspect(
                "'“Diminish, plants! Shrivel and die!”'", *["sentence", "loud"]
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On caster"
            ),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 10")],
    ),
    Spell(
        name="Sun Scourge",
        skill="Conjuration",
        notes="Other Conditions (-2) Can only be cast when the sun is visible\nThe mage makes an offering of ashes to the sun and calls\nupon its power, which she channels through her body. Then,\nwith a minimal amount of pain to herself and a simple\ntouch, the caster inflicts pain to an opponent as if he were\nbeing burnt by the sun’s searing rays. It also makes him\nunusually susceptible to the harsh effects of the sun. If the\nvictim opposes the touch —as most aware and able-bodied\nbeings would — the mage must make a successful brawling/\nfighting attack.",
        effect=DisadvantageEffect(
            "Achilles’s Heel", 3,  "+5D damage and +20 to survival and stamina difficulties in desert environments each day the character is in the sun — values are not cumulative",
        ),
        duration=DurationAspect(measure="1 week"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Light, Fire"),
            "components": ComponentsAspect(
                "Ashes of creature desiccated by the sun", "uncommon"
            ),
            "feedback": FeedbackAspect(2),
            "gestures": GesturesAspect(
                "Raise arms toward the sun and sprinkle the ashes to the wind",
                *["simple"],
            ),
            "incantations": IncantationsAspect(
                "'“Like a scythe, O mighty sun; cut down thy enemies.”'", *["sentence"]
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 16")],
    ),
    Spell(
        name="Sun Cage",
        skill="Conjuration",
        notes="Light cage traps a target in a prison of magical sunlight.\nAfter miming escaping from a cell and indicating the intended\ntarget, the mage must make a marksmanship/firearms or ap-\nportation roll that beats the combat difficulty for the target.\nIf she succeeds, the target is trapped in a sphere with a radius\nof three meters. (Creatures larger than that cannot be con-\nfined by this spell.) The cage glows radiantly, bright enough\nto illuminate within one meter in all directions.\nThe result point bonus plus 15 serves as the damage resis-\ntance totals of the bars. The target can disbelieve and thus\nfree himself by generating a disbelief total of 13.",
        effect=CompositeEffect(
            "Bars",
            ProtectionEffect("Resistance total of bars", "5D", "protection modifier"), # was literal 15
            SkillEffect(
            "negates any darkness modifier up to",
                *["+4D"],
            )
        ),
        duration=DurationAspect(measure="1 hour"),
        range=RangeAspect(measure="25 meters"),
        casting_time=CastingTimeAspect(measure="1 minute"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Light"),
            "area_effect": AreaEffectAspect("3 meter radius sphere"),
            "gestures": GesturesAspect(
                "Mime escaping from a cell with eyes squinted as if blinded by glaring light, then point at target",
                *["complex (acrobatics roll with difficulty of 11)"],
            ),
            "unreal_effect": UnrealEffectAspect.based_on("effect", "difficulty 13")
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Difficulty: 31"),
        ],
    ),
    Spell(
        name="Turn to Shadow",
        skill="Conjuration",
        notes="To cast this spell, the mage must be wearing dark clothes\nand devoid of any shiny objects that would catch and reflect\nlight. He must also be immersed in darkness or shadow at\nthe time of casting. The darkness need not be absolute; even\na shadowy corner of an inn’s common room is enough. When\nthe spell is cast, the mage transforms himself into a living\nshadow. He has no mass and therefore makes no noise and\nleaves no track of his passage, moves at half his normal rate,\nmay assume any general shape (though details are not pos-\nsible), and may flow through tiny openings.\nBecause he is insubstantial, most physical attacks pass\nright through the mage. However, he in turn cannot attack\nin this form, nor can he speak or uses spells that require\nbiological conditions (incantations, for example, or handling\nof material components).",
        effect=CompositeEffect(
            "Shadow form",
            SpecialAbilityEffect("Intangibility", 1, "3D to damage damage resistance total against physical attacks and movement is halved"),
            SpecialAbilityEffect("Invisibility", 3, "+3 to dodge, sneak/stealth, and hide: self totals and +3 to search, tracking,  investigation, and attack difficulties against target"),
        ),
        duration=DurationAspect(measure="5 rounds"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="3.5 minutes"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Darkness"),
            "components": ComponentsAspect("Dark clothes", "very common"),
            "concentration": ConcentrationAspect("3 seconds"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[
            GenericAspect(
                difficulty=1,
                description="Must be immersed in darkness or shadow during casting time",
            ),
            GenericAspect(difficulty=0, description="Difficulty: 16"),
        ],
    ),
    Spell(
        name="Veil of Darkness",
        skill="Conjuration",
        notes="The mage covers his eyes with a hand, drawing energy from\nwithin himself, and then throws a ball of pure darkness at a\ntarget. He must make a marksmanship/firearms or apporta-\ntion roll to hit the target, and may throw the spell up to 10\nmeters distant. Hit targets find themselves blinded by a veil\nof darkness that covers their eyes, imposing a +4D darkness\ndifficulty modifier on all relevant actions performed by this\ncreature for a period of 25 seconds. The bolt of darkness must\nbe fired in the same round that the mage casts the spell.",
        effect=SkillEffect("+  darkness modifier", *["+4D"]),
        duration=DurationAspect(measure="5 rounds"),
        range=RangeAspect(measure="10 meters"),
        casting_time=CastingTimeAspect(measure="2.5 seconds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Folk, Darkness"),
            "countenance": CountenanceAspect(
                "The mage looks drained, with dark rings around eyes", "noticeable"
            ),
            "gestures": GesturesAspect(
                "Cover eyes with a hand, then a throwing mostion at a target",
                *["simple"],
            ),
            "incantations": IncantationsAspect(
                "'“You see NOTHING!”'", *["sentence", "loud"]
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 12")],
    ),
    Spell(
        name="Vengeful Void",
        skill="Conjuration",
        notes="To cast this spell, a void of darkness or dense shadow (such\nas a deep pit, a nonilluminated dungeon room, or a shadowy\nalley) must be present. The mage then shouts some words of\npower and points toward the black spot. Through this spell,\nthe mage animates the darkness of the void into a tidal-wave-\nlike mass that strikes down upon opponents with rage. The\ndarkness grabs an opponent within five meters brawling/fight-\ning of 4D and inflicts 6D damage. Once captured, the target\nis dragged back into the depths of the monster on the next\nround, though the opponent may attempt to escape the void’s\nlifting/lift of 5D. Those dragged into the void obviously must\ncontend with whatever dangers might lurk within (falling\ndamage from a pit, for example). Additionally, the darkness\ninflicts its normal damage on the trapped creature. Creatures\ntrapped within the darkness feel as if they are drowning and\nbeing crushed by the pressures of deep water.\n\n",
        effect=CompositeEffect(
            "The Shadow",
            SkillEffect(
            "brawling/fighting", "4D"),
            SkillEffect("lifting/lift", "5D"),
            DamageEffect("physical damage", "6D", "physical damage"),
        ),
        duration=DurationAspect(measure="3 rounds"),
        range=RangeAspect(measure="5 meters"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Darkness, Water"),
            "gestures": GesturesAspect("Point at an intensely dark area", *["simple"]),
            "incantations": IncantationsAspect(
                "'“Rise, darkness, and avenge me. I command it.”'",
                *["sentence", "loud"],
            ),
        },
        other_conditions=[
            GenericAspect(
                difficulty=3,
                description="A void of darkness in an otherwise illuminated environment",
            ),
            GenericAspect(difficulty=0, description="Difficulty: 24"),
        ],
    ),
    Spell(
        name="Wall of Radiance",
        skill="Conjuration",
        notes="The magic user throws a handful of crystal fragments in\nthe direction in which he wishes to create the wall of radi -\nance. Then he blows the flames of a lit candle into the falling\nshards. A shield-like wall of shimmering white light measuring\nthree meters in diameter appears at a distance of up to 10\nmeters from the caster.\nThe wall is immobile and remains in that position for three\nand a half minutes. The light is so brilliant that it negates\nup to 4D of darkness modifier within one meter. Its bright-\nness provides a +2D cover modifier against anyone attacking\nfrom the other side of the barrier. The wall does not offer\nany physical barrier to attack or movement.\n\n",
        effect=CompositeEffect(
            "Wall",
            SkillEffect(
            "negates any darkness modifier", "4D"),
            ProtectionEffect("cover modifier", "2D"),
        ),
        duration=DurationAspect(measure="3.5 minutes"),
        range=RangeAspect(measure="10 meters"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Light"),
            "area_effect": AreaEffectAspect("3m radius circle"),
            "components": ComponentsAspect(
                ("A handful of crystal shards", "uncommon; destroyed"),
                ("lit candle", "very common"),
            ),
            "gestures": GesturesAspect(
                "Throw crystals into air and blow the flames of a candle toward them",
                *["simple"],
            ),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 15")],
    ),
]


__test__ = {
    "Aura of Visibility": ">>> spells[0].difficulty\n11",  # Rules say 10
    "Blur": ">>> spells[1].difficulty\n11",
    "Glowing Eyes": ">>> spells[2].difficulty\n16",
    "Holy Light": ">>> spells[3].difficulty\n35",
    "Light Chest": ">>> spells[4].difficulty\n20",
    "Light Ram": ">>> spells[5].difficulty\n18",  # Rules say 17
    "Light Show": ">>> spells[6].difficulty\n14",
    "Mass Light Show": ">>> spells[7].difficulty\n24",
    "Night Vigilance": ">>> spells[8].difficulty\n16",  # Rules say 15
    "Nyctophobia": ">>> spells[9].difficulty\n14",  # Rules say 13
    "Shadow Surface": ">>> spells[10].difficulty\n26",  # Rules say 27
    "Shroud of Shade": ">>> spells[11].difficulty\n10",
    "Sight of Darkness": ">>> spells[12].difficulty\n20",
    "Sinister Pall": ">>> spells[13].difficulty\n10",  # Rules say 11
    "Sniper Light Beam": ">>> spells[14].difficulty\n10",
    "Stunt Plant": ">>> spells[15].difficulty\n10",
    "Sun Scourge": ">>> spells[16].difficulty\n16",
    "Sun Cage": ">>> spells[17].difficulty\n31",
    "Turn to Shadow": ">>> spells[18].difficulty\n22",  # Rules say 16, effect isn't very close
    "Veil of Darkness": ">>> spells[19].difficulty\n13",  # Rules say 12
    "Vengeful Void": ">>> spells[20].difficulty\n24",
    "Wall of Radiance": ">>> spells[21].difficulty\n15",
}



if __name__ == "__main__":
    app = build_app(spells)
    app()
