"""
Somniomancy

When run as an app, generates .RST-formatted details of each Spell.
"""

from decimal import Decimal
from typing import Annotated, Any
import typer
from opend6_tools.magic2 import *


spells = [
    Spell(
        name="Cleansing Sleep",
        skill="Conjuration",
        notes="The mage casts this spell, spending 25 minutes washing\nherself thoroughly with water and drinking plenty of fluids,\nthen she goes to sleep. While she sleeps, her body rids itself\nof toxins and diseases. This spell courses through her veins\nand organs, destroying harmful bacteria, viruses, and natural\nand synthetic toxins, rendering her healthy and fit once again.\nEach hour, the caster can attempt to eliminate a single poison\nor illness within her body by making a medicine/healing roll\nas if she had 9D in the skill. The gamemaster determines the\ndifficulty to eliminate a specific poison or disease; 15 to 20\nis generally a good range.\n\nThe caster may apply her result point bonus to the first\n*medicine/healing* roll she makes with this spell.\n",
        effect=SkillEffect("medicine/healing of  ", *["+9D"]),
        duration=DurationAspect(measure="10 hours"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="25 minutes"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Death, folk"),
            "components": ComponentsAspect("Large amount of water", "ordinary"),
            "gestures": GesturesAspect("Washing with and drinking water", *["simple"]),
        },
        other_conditions=[
            GenericAspect(
                difficulty=11,
                description="Effect may be used once per hour; spell is broken if caster is awakened during the duration",
            ),
            GenericAspect(difficulty=0, description="Difficulty: 10"),
        ],
    ),
    Spell(
        name="Concentration Lapse",
        skill="Alteration",
        notes="The mage waves her hand in a sinuous motion or wiggles\nher fingers slowly.  The target must make a willpower/mettle\nroll with a difficulty of 10. If he fails, his eyelids droop briefly,\nand he experiences a momentary lapse of concentration,\nof the sort he might have if he were very tired. This lapse\nmakes him fumble his defenses: He is too slow on the parry\nor notices the incoming punch half a second too late; the\ndifficulty to hit him is decreased by  until the caster’s turn\nin the next round.\n\nThe caster may apply her result point bonus to the difficulty\nof the target’s willpower/mettle roll to avoid the effect.\n",
        effect=Effect(description="difficult to attack target is at -5", difficulty=5),
        duration=DurationAspect(measure="1 round"),
        range=RangeAspect(measure="5 meters"),
        casting_time=CastingTimeAspect(measure="1 second"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "gestures": GesturesAspect("Waves hand in a hypnotic pattern", *["simple"]),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 8")],
    ),
    Spell(
        name="Detect Slumber",
        skill="Divination",
        notes="The caster’s vision takes on an added quality, providing her\nwith additional information about certain creatures within\nthe area of effect. Simply by looking at a creature within\nthe area of effect, she instantly knows whether or not it is\nasleep. If it is not asleep, the caster has no additional means\nof discerning if it is resting, about to fall asleep, feigning\nsleep, dead, or in any other state; this spell simply reveals\nthat the creature is sleeping or that it is not. Generally, the\ncaster can determine the sleeping condition of all the crea -\ntures within the area of effect unless they are hidden from\nview or there are a great many of them (and thus some are\nconcealing others).\n",
        effect=Effect(description="value to determine state of slumber", difficulty=5),
        duration=DurationAspect(measure="1 round"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 second"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "area_effect": AreaEffectAspect("10 meter radius divination sphere"),
        },
        other_conditions=[
            GenericAspect(
                difficulty=1, description="Only works on sleeping creatures"
            ),
            GenericAspect(difficulty=0, description="Difficulty: 12"),
        ],
    ),
    Spell(
        name="Dream Travel",
        skill="Apportation",
        notes="The caster uses this spell to transport herself great distances\nvia the dreams of other creatures. She moves from dream to\ndream in the time it takes to blink, seeing strange landscapes\nand briefly passing by the hopes and fears of myriad creatures\nbefore arriving at her destination.\n\nWhen she casts this spell, the caster targets a sleeping\ncreature within one kilometer; she must see or otherwise\nbe aware of the sleeper’s location (perhaps by sleep sense, for\ninstance) and it must be the size of a cat or larger. Over the\ncourse of 30 seconds, her physical form fades into translucence\nand disappears entirely as she enters the sleeping creature’s\ndreams. During these 30 seconds, the caster  cannot influence\nevents around her, nor can she move from her position; her\nmind and body are becoming part of the creature’s dreams.\n\nThough she enters the sleeping creature’s dreams, the\ndreamer does not detect her and she cannot deliver mes -\nsages or otherwise influence his dreams, as she could with\nstep into sleep; she is merely along for the ride, using the\ncreature’s sleeping consciousness as a vehicle for her unique\nbrand of magic.\n\nOnce at the new host, the caster’s physical form slowly\nmanifests, fading into translucence and then becoming solid\nin the latest dreamer’s presence. As she was when she first\nentered the dreams, she is not physically present in the area\nuntil her form solidifies over the course of 30 seconds.\n\nNote that the caster has no knowledge of the surroundings\nof her destination dreamer, and she could appear in the midst\nof enemies or in an inhospitable environment — though\nas people do not usually sleep in these sorts of conditions,\nthe odds are slim. The caster usually ends up in a bedroom\nsomewhere and tiptoes out.\n\nNote that though the process of the caster’s physical self\ndiscorporating takes time, the dream travel itself is virtually\ninstantaneous.\n",
        effect=MassEffect("moves up to  -- ", *["150 kilograms"]),
        duration=DurationAspect(measure="40 seconds"),
        range=RangeAspect(measure="1 kilometer"),
        casting_time=CastingTimeAspect(measure="25 seconds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Dreams"),
            "concentration": ConcentrationAspect("25 seconds"),
        },
        other_conditions=[
            GenericAspect(difficulty=2, description="Pass only between dreamers"),
            GenericAspect(difficulty=0, description="Difficulty: 19"),
        ],
    ),
    Spell(
        name="Dream Visions",
        skill="Divination",
        notes="This spell allows the caster to view distant places in her\ndreams, though those places are not exactly as they appear\nin the real world.\n\nThe caster spends one hour in preparation, gazing at the\nphotographs or paintings and envisioning the place she\nwould like to see (which does not have to be the place of\nthe paintings). Then, she goes to sleep. Four hours into her\nsleep (which are part of the casting time), her dreams take\non more meaningful forms. She can observe any one area\nwithin 2.5 kilometers as if she were there herself, using a\nsearch skill of 4D. She can view an area with which she is\nfamiliar or she can specify a direction and distance, such\nas “southwest, 1.22 kilometers,” and view the area at that\ndistance. If the specified location is within the ground, a\nwall, or other obstruction, she sees nothing but darkness.\nHer point of view can appear close to the ground, viewing\nit as she would if she were standing there, or it can appear\nfloating in the air, at ground level, and so on.\n\nThe caster does not see the areas exactly as normal, for\nshe is within the dreamscape. Areas and people within the\ndreamscape appear as they do in the real world, but the\nlighting is indistinct and gray mists hover at the edges of\nvision. Forms are muted and blurred. Most importantly, the\nsubconscious images that people associate with individuals,\nplaces, and things walk the dreamscape. Though these images\nmay have no physical existence in the real world, they are the\nthings people dream about when they visit these areas and\ncreatures in their sleep. For example, a graveyard dreamscape\nmay be haunted by ghosts and the cries of the dead, because\nthese fears lurk in humanity’s subconscious and when people\ndream of graveyards, these images often appear. A sports star\nin the dreamscape may have trophies, women, and dollar bills\nfloating around him, as these are the ideas that other people\nassociate with such a celebrity.\n\nThe ancillary images in the dreamscape can serve both\nto enhance and obscure the caster’s understanding and are\ntools for the gamemaster to use.\n",
        effect=SkillEffect("search of  ", *["+4D",]),
        duration=DurationAspect(measure="10 minutes"),
        range=RangeAspect(measure="2.5 kilometers"),
        casting_time=CastingTimeAspect(measure="5 hours"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Dreams"),
            "area_effect": AreaEffectAspect("5 meter radius divination sphere"),
            "components": ComponentsAspect(
                "Photographs or paintings of exotic locales", "uncommon"
            ),
            "concentration": ConcentrationAspect("1 hour"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Difficulty: 22"),
        ],
    ),
    Spell(
        name="Dreams in Hand",
        skill="Conjuration",
        notes="This spell allows the caster to enter her dreams, envision\nan item, and return to the waking world with that item in\nher possession.\n\nFor one hour, the caster meditates on the spell and the\nitem she wishes to create with her dreams. She can imagine\nanything she likes, though complicated or artistic objects\nrequire skill rolls as determined by the gamemaster. (Failure\non the secondary skill roll indicates that some obvious flaw\nexists in the item; success has no effect beyond the item’s\nsatisfactory creation.)\n\nAftershe awakes from the meditation, the object is in\nher hand, a physical reality. It remains substantial for 40\nminutes; after this time, it grows translucent before it dis -\nappears entirely.\n\nThe caster can use this spell to create items of great intrinsic\nworth, like currency, precious metals, or jewelry, but they\nvanish when the duration expires, which is bound to anger\nshopkeepers.\n\nThe caster can add her result point bonus to the spell’s\nduration value and refigure the measure in seconds.\n",
        effect=MassEffect("creates inanimate material", *["1 kilogram"]),
        duration=DurationAspect(measure="40 minutes"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 hour"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Dreams"),
            "component": ComponentsAspect("A few grains of sand", "ordinary"),
            "concentration": ConcentrationAspect("1 hour"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On sand"
            ),
            "other_alterant": OtherAlterant(25, "Item can be of any complexity or value, but the greater the complexity or value, the greater the secondary skill roll required")
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Difficulty: 10"),
        ],
    ),
    Spell(
        name="Dreamtime",
        skill="Divination",
        notes="This spell allows the caster to use her dreams to view places\nas they appeared in the past or will appear in the future.\n\nThe caster spends one hour in preparation, meditating and\nfocusing, at the end of which she turns the hourglass and\ngoes to sleep. Four hours later (which are part of the casting\ntime), as the sand in the hourglass trickles out, the caster’s\ndreams take on meaning.\n\nIn addition to the ability to view a distant location (up to\n20 kilometers away), the caster can also look up to a year\ninto the past or the future. She makes the decision as to the\narea and the time when she casts the spell. (For example,\n“The playground at Washington Heights Elementary School,\nJanuary 2, 3:31 p.m.”)\n\nIf the caster looks into the past, she sees the area as it\nappeared back then. The dreamscape images, however, are\nthose that modern-day people feel for the area. For example,\nif a terrible murder was committed in a certain house last\nweek, and the caster observes the house as it was one month\nago, before the murder, the dreamscape still shows her shad-\nowy images of death and fear, for that is what people in the\ncurrent time associate with the house.\n\nIf the caster looks into the future, she sees the area as it is\nmost likely to appear. The future is uncertain and many factors\ncan change it, but she sees the area as it will most probably\nappear — assuming that no one does anything significant\nto alter it. Like looking into the past, the dreamscape reveals\nimages that modern-day people associate with the area. For\nexample, the caster may view a coastline as it will appear five\nmonths from now and see the remains of a terrorist attack\n— broken piers, dead bodies, ravaged beaches. Even though\nfive months from now people will associate the coastline with\nhorror and violence, currently they see it as a simple beach,\nand the dreamscape images are people in swimsuits, beach\nballs, and the like (and maybe the odd shark, as a nod to the\nneurotic mothers of the world).\n",
        effect=CompositeEffect(
            "Search in Time",
            TimeEffect("past or future", "1 year"),
            SkillEffect( "search skill", *["+4D"]),
        ),
        duration=DurationAspect(measure="25 minutes"),
        range=RangeAspect(measure="20 kilometers"),
        casting_time=CastingTimeAspect(measure="5 hours"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Dreams"),
            "area_effect": AreaEffectAspect("5 meter radius divination sphere"),
            "components": ComponentsAspect("A 4-hour hourglass", "uncommon"),
            "concentration": ConcentrationAspect("1 hour"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Difficulty: 43"),
            GenericAspect(
                difficulty=2,
                description="Other Alterant: May select time period viewed",
            ),
        ],
    ),
    Spell(
        name="Groggy",
        skill="Alteration",
        notes="The caster yawns hugely and, as all know, yawning is\ncontagious. The target follows suit. This spell magnifies the\ntarget’s feeling of sleepiness, making him momentarily groggy\nand unable to think straight, as if badly in need of rest. His\nreflexes are slowed, his hand-eye coordination decreased,\nand his mind easily distracted. He suffers a -1D penalty on\ntwo mental and two physical attributes (such as Reflexes,\nKnowledge, Co ordination, and Perception in D6 Adventure )\nfor 12 rounds.\n",
        effect=SkillEffect("Subtract 1D from two mental and two physical attributes", *["+4D", "attribute modifier"]),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="10 meters"),
        casting_time=CastingTimeAspect(measure="1.5 seconds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "gestures": GesturesAspect("The caster yawns widely", *["simple"]),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 22")],
    ),
    Spell(
        name="Insomnia",
        skill="Conjuration",
        notes="This spell makes it challenging for the target to sleep. His\nsleeplessness is maddening and dulls his mind and body.\n\nEach night following the end of the casting time, the target\nmust make a willpower/mettle roll versus a roll of the caster’s\nwillpower/mettle or be stricken with insomnia. He is unable\nto sleep for one full night. In addition to being frustrating,\nthe next morning, the victim is mentally drained and physi-\ncally fatigued. He suffers -1 pip to all mental and physical\nattributes. This reduction accumulates for each night the\ncharacter cannot get sleep (by failing to make the roll). Nap-\nping during the day provides no relief.\n\nNo attribute can drop below 1D because of this spell.\n\nThe caster can add her result point bonus to the difficulty of\nthe willpower/mettle checks needed to shake off the spell.\n",
        effect=DisadvantageEffect(
            "Achilles’ Heel",
            3,
            note="insomnia: -1 pip to all mental and physical attributes, increasing by -1 pip for each sleepless night",
        ),
        duration=DurationAspect(measure="1 week"),
        range=RangeAspect(measure="5 meters"),
        casting_time=CastingTimeAspect(measure="1 day"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "charges": ChargesAspect("1 improved charge"),
            "components": ComponentsAspect(
                ("A miniature sheep doll", "common"),
                ("6 pins silver pins", "common; destroyed"),
            ),
            "gestures": GesturesAspect(
                "The caster pushes a pin through the sheep doll's head and pushes an additional pin into the doll after every 24 hours",
                *["simple"],
            ),
            "incantations": IncantationsAspect("'“Sleep no more.”'", *["phrase"]),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 11")],
    ),
    Spell(
        name="Kiss of the Sandman",
        skill="Conjuration",
        notes="This spell drives the targets into a magic sleep. The caster\nscoops up a handful of sand and blows upon it, whereupon it\nbillows out to create a cone with a tip that begins 2.5 meters\nfrom the caster. The cone is three meters long and six meters\nwide at its end. The first target hit by the spell must make\nwillpower/mettle roll with a difficulty of 15 or fall asleep. Those\nup to one meter behind the first target have difficulty of 14,\nthose between one and two meters have a difficulty of 13,\nand those between two and three meters have a difficulty of\n12.  Creatures in combat or some other high-energy situation\nreceive a +4 bonus on their willpower/mettle rolls.\n\nSleeping creatures remain magically asleep and do not\nawaken normally, though other beings can shake them,\nslap them, dump water on their heads, and perform other\nactions in attempts wake them; doing so allows the sleeping\ncreature another chance to awake, again with a willpower/\nmettle roll at the same difficulty that put him to sleep. (The\ngamemaster may allow bonuses on this roll depending on\nthe vigor with which the characters attempt to awaken the\nvictim.) The awakening attempt may be tried once per round\nat most; if one type of action fails, those trying to rose the\nsleeper must find another way.\n\nAfter the spell’s duration expires, the sleeping creatures\nenter normal sleep and awaken normally (from loud noises,\nbeing physically jostled, and so on).\n\nThe caster can add her result point bonus to the difficulty\nof the willpower/mettle rolls to avoid the spell when other\npeople attempt to awaken the victims.\n\nSomniomancers often use this spell as a precursor to other\nspells, such as dream travel, step into sleep, or nightmare.\n",
        effect=Effect(
            description="difficulty for target to resist falling asleep", difficulty=15
        ),
        duration=DurationAspect(measure="5 minutes"),
        range=RangeAspect(measure="2.5 meters"),
        casting_time=CastingTimeAspect(measure="3.5 seconds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "area_effect": AreaEffectAspect("3m height 3m radius cone"),
            "components": ComponentsAspect("Sand", "ordinary, destroyed"),
            "gestures": GesturesAspect(
                "Grab a handful of sand and blow it at the targets", *["simple"]
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On targets"
            ),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Difficulty: 21"),
        ],
    ),
    Spell(
        name="Night Terrors",
        skill="Conjuration",
        notes="This spell puts up to five targets to sleep and then ravages\ntheir minds with lethal nightmares. The targets must each\nmake a willpower/mettle roll with a difficulty of 18 or fall\nasleep. This spell then burrows into the sleepers’ subconscious,\ndrawing forth their greatest fears and forming them into\nhorrific nightmares. They toss and thrash violently, obviously\ndistressed and taking 5D of damage per round until dead or\nthe duration ends. See kiss of the Sandman  for restrictions\non waking magically slumbering creatures.\n\nThe caster may add her result point bonus to the difficulty\nof the willpower/mettle rolls to resist falling asleep or to the\ndamage done each round (not both and chosen once for the\nspell).\n",
        effect=CompositeEffect(
            "Terrors",
            SkillEffect("difficulty of 18 to resist falling asleep", "6D"),
            DamageEffect("physical damage", "5D", "ignores nonmagical armor"),
        ),
        duration=DurationAspect(measure="12 rounds"),
        range=RangeAspect(measure="60 meters"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Dreams, folk"),
            "components": ComponentsAspect("Amber dust", "very rare; destroyed"),
            "multiple_target": MultipleTargetAspect("5 targets"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Difficulty: 30"),
        ],
    ),
    Spell(
        name="Night Visitation",
        skill="Alteration",
        notes="This spell allows the caster to deliver messages to sleep -\ning creatures. The caster names a specific individual and\nformulates an image or series of images, which can be up to\na minute in length, that appears in the named individual’s\ndream. If the individual is not asleep, the spell fails. The\nimages can be anything the caster imagines that’s relatively\nnonfrightening; the caster cannot give the target a nightmare,\nthough she may deliver threats and ultimatums. The caster\ncan use this dream to persuade the target as if she had 4D\nin the persuasion skill.\n\nThe caster chooses whether or not the target remembers\nthe dream when he awakes. If the target does not remember\nthe dream, the dream may still influence him subconsciously,\nat the gamemaster’s discretion.\n\nIn lieu of naming a specific individual, the caster may\nmake physical contact with the target (in which case, the\nrange is irrelevant).\n",
        effect=SkillEffect("persuasion of  ", *["+4D"]),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="2.5 kilometers"),
        casting_time=CastingTimeAspect(measure="1 minute"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Dreams")
        },
        other_conditions=[
            GenericAspect(
                difficulty=-1,
                description="Touch or name single specific target, who must be asleep",
            ),
            GenericAspect(difficulty=0, description="Difficulty: 23"),
        ],
    ),
    Spell(
        name="Nightmare",
        skill="Alteration",
        notes="The caster touches the creature and  uses this spell to dredge\nup his most feared images from his subconscious, using these\nto create a horrific nightmare. The target thrashes, moans,\nand sweats. He must make a willpower/mettle roll against a\nroll of the caster’s willpower/mettle; if he fails, he dies of fear\n(and cardiac arrest).\n\nIf the target is not asleep, this spell fails.\n\nThe caster can apply her result point bonus to the difficulty \nof the willpower/mettle roll the target needs to avoid\nthe effect.\n",
        effect=DamageEffect("Damage","10D", "physical damage", "ignores all armor"),
        duration=DurationAspect(measure="1 round"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="1 second"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Dreams")
        },
        other_conditions=[
            GenericAspect(difficulty=-1, description="Target must be asleep"),
            GenericAspect(difficulty=0, description="Difficulty: 32"),
        ],
    ),
    Spell(
        name="Nightshield",
        skill="Conjuration",
        notes="The mage places a small silver shield on her chest just\nbefore she retires for the night, casting a spell that protects\nher dreams from outside influence (such as the machinations\nof another somniomancer). She adds her result point bonus\nto the spell’s effect value. If a another mage casts a spell that\nattempts to access her dreams or detecting whether she’s\nsleeping, the second caster’s  skill roll  for that spell must\nequal or exceed nightshield’s value (30 plus the caster’s result\npoint bonus) to affect her.\n\n**Example**: Shannon casts nightshield before she goes to\nsleep because she suspects her somniomantic rival, Bruce,\nis on the prowl. She makes a conjuration roll to cast the spell\nand rolls a total of 19. This roll generates a result point bonus\nof 2, which she adds to nightshield’s effect value of 30, for a\ntotal of 32. If Bruce shows up and attempts to cast nightmare\non Shannon, his alteration roll must equal or exceed 32 to\naffect her.        \n",
        effect=ProtectionEffect(
            "compare to spell total of spell attempting to influence caster",
            "10D"
        ),
        duration=DurationAspect(measure="10 hours"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1.5 hours"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "components": ComponentsAspect("A small shield of beaten silver", "rare"),
        },
        other_conditions=[
            GenericAspect(difficulty=-1, description="Awakening disrupts the spell"),
            GenericAspect(difficulty=0, description="Difficulty: 15"),
        ],
    ),
    Spell(
        name="Put the “Rest” in “Restoration”",
        skill="Conjuration",
        notes="The mage casts this spell immediately before going to\nsleep. While she sleeps, her wounds heal at an accelerated\nrate. Each hour, she can heal her physical wounds as if she\nhad 9D in the medicine/healing skill.\n",
        effect=SkillEffect("medicine/healing of  ", *["+9D"]),
        duration=DurationAspect(measure="10 hours"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 minute"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Time, folk")
        },
        other_conditions=[
            GenericAspect(
                difficulty=-11,
                description="Effect may be used once per hour; spell is broken if caster is awakened during the duration",
            ),
            GenericAspect(difficulty=0, description="Difficulty: 15"),
        ],
    ),
    Spell(
        name="Really Comfy Pillow",
        skill="Conjuration",
        notes="The caster touches a pillow, imbuing it with an enchantment\nthat functions up to three times. Whenever a creature rests\non the pillow, whether intending to sleep or merely take a\nshort rest, over the course of one minute, the spell puts the\ncreature to sleep. The user sleeps deeply and well, untroubled\nby nightmares or anxieties, for 10 hours and awakens feeling\nrefreshed and invigorated, providing a +1D bonus to natu -\nral healing attempts. This sleep is not magical, as it is with\nkiss of the Sandman or night terrors; it’s simply a dreamless,\nrefreshing sleep. Loud noises, physical movement, and the\nlike awaken the sleeper normally.\n\nThe pillow can also aid in the casting of somniomancy\nspells that involve the mage being asleep in order to work.\nUsing a really comfy pillow  grants the caster a +2 bonus on\nher appropriate Magic skill checks when she casts spells that\nrequire her to meditate or sleep.\n",
        effect=CompositeEffect(
            "Healing",
            SkillEffect(
            "Accelerated Healing (+1D bonus to natural healing attempts)", *["+1D", "skill modifier"]),
            SkillEffect("Arcane Knowledge: Dreams (+2 to casting of related Magic spells)", "1D", "Extranormal Skill"),
        ),
        duration=DurationAspect(measure="10 hours"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="10 minutes"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("magic"),
            "charges": ChargesAspect("3 improved charges"),
            "components": ComponentsAspect("A really comfortable pillow", "uncommon"),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-2,
                description="Target must want to fall asleep; spell is broken if target is awakened during duration",
            ),
            GenericAspect(difficulty=0, description="Difficulty: 16"),
        ],
    ),
    Spell(
        name="Sleep Eternal",
        skill="Alteration",
        notes="This spell causes the target to enter an endless sleep, effec-\ntively killing him — or at least, killing him until the caster\nchooses to release the curse.\n\nThe target, which must already be asleep, falls even deeper\ninto his sleep, so deep that he never awakens. When the caster\ncasts this spell, the target can make a willpower/mettle roll\nwith a difficulty of 20 to resist its effects; if he succeeds, he\nawakens. If this roll fails, he doesn’t wake up for 10 years.\nHowever, friends may attempt to bestir him; see kiss of the\nSandman for details on reviving a magically slumbering\ncharacter. The sleeper must have his nutrition intravenously\ninjected if he is to survive.\n\nThe caster can choose the nature of the target’s sleep. She\nhas three options:\n\n-   The target’s sleep is full of pleasant dreams. He sleeps gently, with a smile upon his lips.\n\n-   The target’s sleep is dreamless. He appears to be in a coma.\n\n-   The target’s sleep is uneasy, filled with vague nightmares. He moans and twitches, obviously distressed.\n\nThe caster can end this spell at any time. The only other\nway to awaken the target is to design a spell with the express\npurpose of doing so.\n\nThe caster may add her result point bonus to the difficulty\nof the target’s willpower/mettle rolls to resist the spell’s\neffects.\n",
        effect=Effect(description="difficulty to resist falling asleep", difficulty=20),
        duration=DurationAspect(measure="10 years"),
        range=RangeAspect(measure="10 meters"),
        casting_time=CastingTimeAspect(measure="1 minute"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Dreams"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
            "other_alterant": OtherAlterant(1, "Puts target in type of sleep the caster chooses"),
            "variable_duration": VariableDurationAspect("off-only")
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Difficulty: 41"),
        ],
    ),
    Spell(
        name="Sleep of Champions",
        skill="Alteration",
        notes="The caster spends two hours in preparation, then goes\nto sleep. When she awakens, she feels refreshed. Her mind\nis keen, her muscles flushed with energy, and her reflexes\nat their peak. She receives a +1D bonus on all mental and\nphysical attributes for the next 15 hours.",
        effect=SkillEffect("increase all mental and physical attributes 1D", *["+6D", "attribute modifier"]),
        duration=DurationAspect(measure="15 hours"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="10 hours"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On caster"
            ),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 25")],
    ),
    Spell(
        name="Sleep Sense",
        skill="Divination",
        notes="This spell allows the caster to detect sleeping creatures\nwithout actively attempting to do so.\n\nOver a 15-minute period, the caster tosses some small gold\nZs into the air while repeating the incantation. For the spell’s\nduration, the caster always knows the exact locations of all\nsleeping creatures within the area of effect that are the size\nof a cat or larger. Walls and other obstructions do not inhibit\nthis spell, though sleep sense does not convey the knowledge\nof how to access the sleepers, merely their locations.\n\nMost somniomancers cast this spell at the beginning of\nthe day because it helps them find targets for some of their\nother spells, like step into sleep, nightmare, and dream travel.\n",
        effect=SkillEffect("search of   to locate sleeping creatures", *["+8D"]),
        duration=DurationAspect(measure="15 hours"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="15 minutes"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "area_effect": AreaEffectAspect("25 m radius divination sphere"),
            "components": ComponentsAspect(
                "Small letter Zs made of gold", "very rare; destroyed"
            ),
            "gestures": GesturesAspect("Toss the Zs into the air", *["simple"]),
            "incantations": IncantationsAspect(
                "'“I see you when you’re sleeping.”'", *["sentence"]
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On caster"
            ),
            "variable_movement": VariableMovementAspect("bend around smaller", "target invisible")
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Difficulty: 28"),
        ],
    ),
    Spell(
        name="Sleeping Puppet",
        skill="Alteration",
        notes="It is possible for the caster to enter into the dimension\nof dreams and gain control over another sleep character’s\nmind. The target must be capable of cognitive thought and\nbe of similar mind to the caster.\n\nIf the spell is successfully cast, then the magic user gets the\nPossession: Limited (R1) Special Ability and must convince\nor command the target to obey The sleeping target cannot\nuse willpower/mettle, as she is unaware that her mind is being\ninfluenced; rather, she can use Presence. If the caster succeeds,\nthen the sleeper obeys, providing the command does not go\nagainst the personal morals of the target. Walking, talking\nand all normal actions can be executed so long as the mage is\nsuccessful. If a failure occurs, the target awakens from what\nis thought to be a dream or nightmare — possibly far from\nwhere she fell asleep.\n",
        effect=SpecialAbilityEffect("Possession: Limited", 1, note=""),
        duration=DurationAspect(measure="1 hour"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 minute"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Dreams"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On caster"
            ),
        },
        other_conditions=[
            GenericAspect(
                difficulty=2,
                description="Target must be sleeping; target must be sentient",
            ),
            GenericAspect(difficulty=0, description="Difficulty: 15"),
        ],
    ),
    Spell(
        name="Step Into Sleep",
        skill="Alteration",
        notes="This spell allows the caster to become part of the target’s\ndream, delivering messages, showing her power, and perform-\ning many other actions that lesser spells do not allow.\n\nIf the target is not asleep, the spell fails. If he is asleep, the\ncaster enters the target’s dream. While in the target’s dreams,\nthe caster’s body is rigid and vulnerable, similar to a character\nusing the Possession: Limited Special Ability.\n\nWhile within the dream, the caster can speak, cast spells,\nuse skills, and so on, but she cannot affect her surroundings in\nany way. The sleeper continues to dream, and his subconscious\nincorporates the caster into his dreams. The caster cannot\ndirectly harm the target, but she can deliver messages, disrupt\nhis dreams, and so on. Similarly, the target’s dreams pose no\ndanger to the caster, though they may be frightening.\n\nAdditionally, the mage can observe the dreams, which\nmight tell the caster something about the target. Using\nthe “Posession Knowledge” chart and the investigation skill\ngranted by the spell, the somniomancer can gain informa-\ntion about the target, although it may be couched in dream\nterms.\n\nThe caster can add her result point bonus to the investiga-\ntion total.\n",
        effect=CompositeEffect(
            "Enter target's dreams",
            SpecialAbilityEffect("Possession: Limited", 1),
            SkillEffect("investigation", "+5D"),
        ),
        duration=DurationAspect(measure="10 minutes"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="1 minute"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Dreams"),
            "components": ComponentsAspect(
                "An item important to the target", "uncommon"
            ),
            "incantations": IncantationsAspect(
                "'\"Open your dreams to me\".'", *["phrase"]
            ),
        },
        other_conditions=[
            GenericAspect(difficulty=-1, description="Target must be asleep"),
            GenericAspect(difficulty=0, description="Difficulty: 15"),
        ],
    ),
    Spell(
        name="Timeslip",
        skill="Chronomancy",
        notes="In desperate situations, some people are forced into\ntaking drastic actions to save their own skin. By invoking\nthe power of the timeslip, the caster changes place with a\ncounterpart from an alternate reality who returns to their\nproper time when their spell runs its course. When the\nhijacked future relative returns, the caster may choose to\nreappear anywhere up to 150 meters from her previous loca-\ntion. The destination spot must be visible to the caster or at\nthe very least known to them (inner sanctum, the home of\na close friend etc.) when the timeslip is cast. Of course, the\nabducted visitor not think very highly of being so rudely\nabducted and could possibly have the power to revisit their\nalternate self in order to avenge themselves. The payback\ncould be brutally painful.\n",
        effect=MassEffect(
            "timeslip up to  -- , caster’s weight plus their alternate self’s weight",
            *["400 kilograms"],
        ),
        duration=DurationAspect(measure="1.5 rounds"),
        range=RangeAspect(measure="150 meters"),
        casting_time=CastingTimeAspect(measure="1 second"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect(
                "An ounce of quicksilver", "uncommon; destroyed"
            ),
            "countenance": CountenanceAspect(
                "Caster sweats profusely and foams at the mouth (noticeable)",
                "noticeable",
            ),
            "gestures": GesturesAspect(
                "The mage points off into the distance and then pulls the visualized target toward them as she leaps forward.",
                *["complex (difficulty 11)"],
            ),
            "incantations": IncantationsAspect(
                "'“See ya, wouldn’t want to be ya!”'", *["sentence"]
            ),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 22")],
    ),
    Spell(
        name="True Rest",
        skill="Alteration",
        notes="The target, which must be willing and about to go to sleep,\nenters a particularly restful slumber that enhances his natu-\nral healing process. When the target makes natural healing\nroll, he gets +2D on the roll. If the target needs seveal days\nof rest before attempting the natural healing roll, the spell\nshould be cast on the last day of rest, as the effect lasts only\n10 hours.\n\n",
        effect=SpecialAbilityEffect(
            "Accelerated Healing (+2D bonus to natural healing rolls)", 2
        ),
        duration=DurationAspect(measure="10 hours"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="10 minutes"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic, folk")
        },
        other_conditions=[
            GenericAspect(
                difficulty=-2,
                description="Target must be sleeping; awakening target during the duration disrupts the spell",
            ),
            GenericAspect(difficulty=0, description="Difficulty: 13"),
        ],
    ),
    Spell(
        name="Waking Nightmare",
        skill="Conjuration",
        notes="A knowledgeable mage can send her mind into the plane of\ndreams and conjure a waking nightmare that can terrifying\nanyone who believes it. If the spell’s conditions are satisfied,\nand it is successfully cast, the mage inspires fear in a solitary\ntarget or a group of creatures that occupy the radius of the\nspell. This fear manifests itself as a walking nightmore to\nthose within the spell’s radius . The dread sight always stays\nwithin the spell’s proximity of those affected by the spell\n— though, if there’s a reason for them to do so, each target\nmay attempt to disbelieve the manifestation (instead of the\nresistance difficulty listed with the Special Ability).",
        effect=SpecialAbilityEffect(
            "Fear",
            4,
            note="+4 to intimidation totals and -4 to combat difficulties against those affected by the fear",
        ),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="5 meters"),
        casting_time=CastingTimeAspect(measure="2 rounds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Dreams"),
            "area_effect": AreaEffectAspect("5m radius circle"),
            "concentration": ConcentrationAspect("2 rounds"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target (nightmare only)"
            ),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Difficulty: 22"),
            GenericAspect(
                difficulty=-7, description="Unreal Effect: Disbelief difficulty of 13"
            ),
        ],
    ),
    Spell(
        name="Walking Dream",
        skill="Conjuration",
        notes="This spell allows the caster’s dreaming consciousness to\nleave her body, roaming the world while she sleeps. The caster\nspends one hour in preparation, meditating and otherwise\npreparing her mind for its journey, then goes to sleep. Four\nhours into her sleep (which counts as part of the casting\ntime), her dreaming consciousness leaves her body for one\nhour, traveling as if the caster has 5D+2 in the Psionics: astral\nprojection skill.\n\n",
        effect=SkillEffect("Psionics: astral projection", *["+5D+2", "Extranormal Skill"]),
        duration=DurationAspect(measure="1 hour"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="5 hours"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Dreams"),
            "concentration": ConcentrationAspect("1 hour"),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 12")],
    ),
]

__test__ = {
    "Cleansing Sleep": ">>> spells[0].difficulty\n10",
    "Concentration Lapse": ">>> spells[1].difficulty\n8",
    "Detect Slumber": ">>> spells[2].difficulty\n12",
    "Dream Travel": ">>> spells[3].difficulty\n19",
    "Dream Visions": ">>> spells[4].difficulty\n21",  # Rules say 22
    "Dreams in Hand": ">>> spells[5].difficulty\n10",
    "Dreamtime": ">>> spells[6].difficulty\n44",  # Rules say 43
    "Groggy": ">>> spells[7].difficulty\n20",  # Rules say 22
    "Insomnia": ">>> spells[8].difficulty\n11",
    "Kiss of the Sandman": ">>> spells[9].difficulty\n20",  # Rules say 21
    "Night Terrors": ">>> spells[10].difficulty\n35",
    "Night Visitation": ">>> spells[11].difficulty\n23",
    "Nightmare": ">>> spells[12].difficulty\n32",
    "Nightshield": ">>> spells[13].difficulty\n15",
    "Put the “Rest” in “Restoration”": ">>> spells[14].difficulty\n15",
    "Really Comfy Pillow": ">>> spells[15].difficulty\n10",  # Rules say 16, but charges are computed incorrectly.
    "Sleep Eternal": ">>> spells[16].difficulty\n40",  # Rules say 41
    "Sleep of Champions": ">>> spells[17].difficulty\n25",
    "Sleep Sense": ">>> spells[18].difficulty\n28",
    "Sleeping Puppet": ">>> spells[19].difficulty\n20",  # Rules say 15, math is wrong
    "Step Into Sleep": ">>> spells[20].difficulty\n19",
    "Timeslip": ">>> spells[21].difficulty\n13",  # Rules say 22, simply wrong
    "True Rest": ">>> spells[22].difficulty\n13",
    "Waking Nightmare": ">>> spells[23].difficulty\n22",  # Effect in rules was way wrong
    "Walking Dream": ">>> spells[24].difficulty\n13",  # Rules say 12
}



if __name__ == "__main__":
    app = build_app(spells)
    app()

