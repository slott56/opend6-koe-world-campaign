"""
Chronomancy

When run as an app, generates .RST details of each Spell.
"""

from typing import Annotated, Any
import typer
from opend6_tools.magic2 import *


spells = [
    Spell(
        name="Chronal Fog",
        skill="Conjuration",
        notes="Upon the dispersal of the spell component, a foglike haze\nsurrounds the magic wielder. The haze is formed by the chronal\nechoes that emanate from the fluctuating temporal fields that\nthe mage summons to deflect physical damage. The barrier\nis centered upon the caster and provides an Armor Value of\n5D against all types of physical (not mental) attacks. The\nfog effect of the spell offers the same visibility limitations\nof light fog for both the magic wielder and those who wish\nto peer through it.",
        effect=ProtectionEffect("Armor, physical only", "5D"),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), "Instantanous"),
        other_aspects={
            "area effect": AreaEffectAspect("2m sphere"),
            "components": ComponentsAspect(
                "Three grams of mica flakes",
                "uncommon; destroyed",
            ),
            "focused": FocusedAspect.based_on(("effect", "duration"), target="caster"),
            "gestures": GesturesAspect(
                "Twirls arms around while dispersing the mica flakes to form a ring around the caster",
                "simple",
            ),
            "incantations": IncantationsAspect(
                "Mists of time, clouds of fate, shield me now, for the hour is late!",
                "sentence; loud",
            ),
        },
        other_conditions=[
            ArcaneKnowledgeAspect( "magic, time"),
            GenericAspect(difficulty=0, description="Difficulty: 11"),
        ],
    ),
    Spell(
        name="Chronobolt",
        skill="Conjuration",
        notes="The successful casting of a chronobolt allows the temporal\nmanipulator to create an aura that causes a portion of the\nintended target to move slightly forward in time. (This also\nmeans that no armor protects against the bolt.) The chronal\ndisturbance does 5D in damage to the victim from a range\nof up to 10 meters from the caster. She must make a marks-\nmanship/firearms or apportation roll to hit the target. The bolt\nmust be fired in the same round that the spell is cast. After\nspell effects have been resolved, the target suffers no further\nill effects from the temporal disturbance.\nThe caster cannot choose which portion of the victim is\nmoved further in time. Such things are totally random, and\nin some cases, may be portions of the target’s molecular\nstructure instead of a limb or section of the body.\n\n",
        effect=DamageEffect("Bolt", "5D", "physical damage; ignores all armor"),
        duration=DurationAspect(measure="1 second"),
        range=RangeAspect(measure="10 meters"),
        casting_time=CastingTimeAspect(measure="1 second"),
        speed=SpeedAspect.based_on(("range",), "Instantaneous"),
        other_aspects={
            "components": ComponentsAspect("A small hourglass", "uncommon"),
            "gestures": GesturesAspect(
                "Hold an hourglass before the intended target and shake the sand inside it",
                "simple",
            ),
            "incantations": IncantationsAspect(
                "The future beckons, come and embrace the pain. You now shall suffer, tis victory I gain!",
                "sentence",
            ),
        },
        other_conditions=[
            ArcaneKnowledgeAspect( "death, time"),
            GenericAspect(difficulty=0, description="Difficulty: 16"),
        ],
    ),
    Spell(
        name="Detect Resonance",
        skill="Divination",
        notes="When successfully cast, the arcane aid can provide a mage\nwith one of the following pieces of information, which the\nmage chooses at casting.\n1. He could discover the existence of things that are out\nof sync with the time stream in a given area, such as time\ntravelers or extradimensional creatures that exist out the\nnormal range of vision.\n2. He could reveal the existence of active chronal enchant-\nments that are bedeviling a tortured soul.\n3. He could decide to employ this magic to discover hid -\nden chronal gates and gain entrance to other times. Such\nventures have their own risk however, as those who travel\nthrough such devices to other times without taking proper\nprecautions could unwittingly release time-lost horrors.\nThe difficulty to find the chronal energy is 11, with higher\nresults indication more information. The range and area of\neffect of the spell indicate the maximum effectiveness of the\nnewly acquired sense.",
        effect=SpecialAbilityEffect(
            "Extra Sense: Chronal Energy",
            3,
            "for search and investigation",
        ),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="10 meters"),
        casting_time=CastingTimeAspect(measure="1 minute"),
        speed=SpeedAspect.based_on(("range",), "Instantaneous"),
        other_aspects={
            "area of effect": AreaEffectAspect(
                "4 m radius sphere",
            ),
            "components": ComponentsAspect(
                ("An astrolabe with quartz lenses", "uncommon"),
                ("18 grams of diamond dust", "uncommon; destroyed"),
            ),
            "gestures": GesturesAspect(
                "Toss the diamond dust in the air and views the area with the astrolabe",
                "complex (requires investigation roll difficulty of 11)",
            ),
            "incantations": IncantationsAspect(
                "Though the temporal winds run wild and free, through its shadowy wake, I now clearly see!",
                "sentence",
            ),
        },
        other_conditions=[
            ArcaneKnowledgeAspect( "time"),
            GenericAspect(difficulty=0, description="Difficulty: 11"),
        ],
    ),
    Spell(
        name="Devolution",
        skill="Alteration",
        notes="Devolution digs deep into the ancestral memories of the\nintended victim in order to flood her mind with horrific\nimages of what her primordial ancestors once were. The oft\nbarbaric visions can deliver a devastating blow to the victim’s\npsyche and rattle her resolve.\nWhen casting this spell, the mage crushes the brain matter\nin his hand and flings the remains at the target. If the target\ncannot beat the caster’s spell skill total with a willpower/\nmettle roll, the victim loses up to 4D of Knowledge/Intellect\n(minimum adjust attribute value of 1D) for five rounds while\nher mind reels as it psychically regresses.",
        # Variable Effect from R4 to an additional 9 ranks (3 dice, giving 4D+1, R13)
        # That's a little high; 12 ranks seems right.
        effect=DisadvantageEffect(
            "Reduced Attribute: Knowledge/Intellect", 12, "-4D to the attribute"
        ),
        duration=DurationAspect(measure="5 rounds"),
        range=RangeAspect(measure="10 meters"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect(
                "60 grams of brain matter, which may come any recently deceased creature as long as the matter retains at least its cranial fluid",
                "common; destroyed",
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="on target"
            ),
            "gestures": GesturesAspect(
                "Crush brain matter and fling at the target", "simple"
            ),
            "incantations": IncantationsAspect(
                "Time rolls back to reveal the shame of your lowly ancestors!",
                "sentence",
            ),
        },
        other_conditions=[
            ArcaneKnowledgeAspect("animal, folk, time"),
            GenericAspect(difficulty=0, description="Difficulty: 23"),
            GenericAspect(
                difficulty=0,
                description="Variable Effect: Up to an additional nine ranks of Reduced Attribute: Knowledge/Intellect (which means up to an additional -3D to the attribute)",
            ),
        ],
    ),
    Spell(
        name="Diminish",
        skill="Alteration",
        notes="The successful casting of diminish reduces the duration\nof the targeted spell by up to 10 minutes. When a caster\nattempts to affect a given spell, compare the skill total used\nto cast diminish to the skill total used to create the offend -\ning spell. If the diminish spell total is equal or higher than\nthe targeted spell’s skill total, the spell duration is reduced.\nSpells with 10 minutes or less of duration left on them cease\nto function. Only one diminish spell can reduce the duration\nof any particular spell.",
        effect=TimeEffect("reduces the duration of a chosen spell", "10 minutes"),
        duration=DurationAspect(measure="1 second"),
        range=RangeAspect(measure="15 meters"),
        casting_time=CastingTimeAspect(measure="2.5 seconds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect("1-decimeter square cloth", "ordinary"),
            "gestures": GesturesAspect(
                "Mime wiping away something with the cloth",
                "simple",
            ),
            "incantations": IncantationsAspect(
                "Arcane blight, begone!",
                "phrase",
            ),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-1,
                description="Must specify at casting a single spell to target",
            ),
            ArcaneKnowledgeAspect( "magic, time"),
            GenericAspect(difficulty=0, description="Difficulty: 10"),
        ],
    ),
    Spell(
        name="Erosion",
        skill="Alteration",
        notes="Erosion allows the chronomancer to rapidly accelerate the\nbreakdown of nonliving matter. Upon the successful casting\nof this spell, a mage may cause a small sphere’s worth of\nmaterial to crumble to dust as it succumbs to the onslaught\nof time. Any living matter in the affected area is unharmed\nby the spell, although any structural effects caused by the\nmagic may still be dangerous. Erosion can be utilized topple\nlarge structures and cause general chaos for the unwary.\nThe availability of erosion’s material component makes the\nmagic popular for mages who find themselves imprisoned.\nThus, it is not uncommon for jailers who have experience in\nconfining wizards to bind and sometimes keep their charges\nblindfolded for the duration of their incarceration.\n\n",
        effect=DamageEffect("Erosion", "6D; physical damage"),
        duration=DurationAspect(measure="1 second"),
        range=RangeAspect(measure="40 meters"),
        casting_time=CastingTimeAspect(measure="1 minute"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "area effect": AreaEffectAspect("1m sphere"),
            "components": ComponentsAspect("A gram of sand", "ordinary; destroyed"),
            "gestures": GesturesAspect(
                "Fling sand at the target area while the incantation is uttered",
                "simple",
            ),
            "incantations": IncantationsAspect(
                "Time the healer, time the stealer, once thought by all to forever last, now it is most assuredly past.",
                "sentence",
            ),
        },
        other_conditions=[
            GenericAspect(difficulty=-1, description="Affects nonliving matter only"),
            ArcaneKnowledgeAspect( "death, time"),
            GenericAspect(difficulty=0, description="Difficulty: 12"),
        ],
    ),
    Spell(
        name="Loophole",
        skill="Apportation",
        notes="Every once in a while, one just does not have enough time\nto deal with the current situation and needs a little help from\na friend. Loophole serves just this purpose as it causes time\naround the intended target to “blink.” This effect hastens\nthe recipient forward in time, which allows the person to\nshorten the casting time of one spell by 75% (round up, with\na maximum reduced casting time ofone minute). The spell\ndifficulty increases by +20, but the target’s skill increases\nby 6D to compensate for this. The recipient of this spell\ncan perform no other action outside of the casting of the\nintended spell.\nThe ink disappears once the target casts the spell.",
        effect=SkillEffect(
            "one Magic skill and affecting one spell, specified at spell casting, that the target wishes to cast quickly",
            "+6D; extranormal skill modifier",
        ),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="3.5 meters"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect(
                "A 30 cubic centimeter vial of ink",
                "very common; destroyed",
            ),
            "feedback": FeedbackAspect(1),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="on target"
            ),
            "gestures": GesturesAspect(
                "Fling the ink at target while uttering the incantation",
                "simple",
            ),
            "incantations": IncantationsAspect(
                "Quickly cast quiet creations.", "phrase"
            ),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-1,
                description="Not usable on spells with incantations, gestures, or concentration requirements",
            ),
            ArcaneKnowledgeAspect( "magic, time"),
            GenericAspect(difficulty=0, description="Difficulty: 29"),
        ],
    ),
    Spell(
        name="Lotus Dreams",
        skill="Alteration",
        notes="When this magic is successfully cast upon a willing recipient, the target falls into a deep, coma-like slumber that lasts\nfor a full 24 hours. After the recipient awakens from his life-\nrenewing respite, the spell’s effect grants him a +7D modifier\nto natural healing roll for the day.\nDuring the spell’s duration it is impossible for the recipient\nto waken or be awakened normally. Those with telepathic or\nsimilar powers can contact them mentally but the answers\ngiven come sluggishly and are typically one or two words.\nThis is in addition to aging from the normal passage of\ntime. Although uncommon, it is not unheard of for those\nwho emerge from the lotus dreams induced sleep to complain\nof experiencing a vertigo effect during the spell. Some are\nhesitant to receive the benefits of the spell a second time\nunless they are near death.",
        # Per the original rules; this seems wrong; the cost of the ability is 63
        # effect=SpecialAbilityEffect(
        #    "Accelerated Healing", 7, "+7D bonus to natural healing attempts",
        # ),
        # This makes more sense...
        effect=SpecialAbilityEffect(
            "Accelerated Healing",
            3,
            "+3D bonus to natural healing attempts",
        ),
        duration=DurationAspect(measure="1 day"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="1 minute"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect(
                "3 grams of incense made from crushed lotus petals",
                "uncommon; destroyed",
            ),
            "countenance": CountenanceAspect(
                "Skin turns an unhealthy pale tone for the duration of the spell",
                "noticeable",
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="on Target"
            ),
            "gestures": GesturesAspect(
                "Gently closes the eyes of the recipient and traces the lines of the bony plates that compose the skull of the intended recipient as the incantation is uttered",
                "complex (requires sleight of hand roll with difficulty of 11)",
            ),
            "incantations": IncantationsAspect(
                "Though your mortal form has been rent asunder, embrace life and drink deeply from the draught of endless slumber.",
                "sentence",
            ),
        },
        other_conditions=[
            ArcaneKnowledgeAspect( "dreams, time"),
            GenericAspect(difficulty=0, description="Difficulty: 18"),
            GenericAspect(
                difficulty=4, description="Other Alterants: Target cannot be awakened"
            ),
        ],
    ),
    Spell(
        name="Perceptive Flux",
        skill="Alteration",
        notes="Perceptive flux is an extremely useful spell for covert operations as it can give strike teams a definite tactical advantage.\nAlthough it takes some time to prepare the magic, the spell’s\nlack of verbal aspects can make it well worth casting.\nAt the end of a successful casting, the opponents think it’s\na different time than it actually is, causing several seconds\nof disorientation.\nThe minimum initiative total an opponent can generate is\nzero, which means that he goes last in the round.",
        effect=DisadvantageEffect(
            "Hindrance: Initiative", 5, "-10 to all initiative totals"
        ),
        duration=DurationAspect(measure="1 round"),
        range=RangeAspect(measure="10 meters"),
        casting_time=CastingTimeAspect(measure="1 minute"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect(
                "A gram of sandstone",
                "very common; destroyed",
            ),
            "countenance": CountenanceAspect(
                "Skin turns a sickly gray color for the duration of the spell",
                "noticeable",
            ),
            "gestures": GesturesAspect(
                "Crush sandstone and drop it to the floor",
                "simple",
            ),
            "multiple_targets": MultipleTargetAspect("5 targets"),
        },
        other_conditions=[
            ArcaneKnowledgeAspect( "time"),
            GenericAspect(difficulty=0, description="Difficulty: 14"),
        ],
    ),
    Spell(
        name="Push",
        skill="Apportation",
        notes="Even the most subtle of things can sometimes make all the\ndifference in the world. Push takes an object of a kilogram or\nless in weight and transports it up to 10 minutes forward in\ntime. The spell is popular with charlatans, con artists, stage\nmagicians, and pranksters. Once the spell runs its course,\nthe pushed object appears exactly where it was before the\nspell was cast. It is affected by any environmental changes\nupon its return.\n\n",
        effect=TimeEffect("sends a small object into the future", "10 min"),
        duration=DurationAspect(measure="10 minutes"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "gestures": GesturesAspect(
                "Wave one hand across the object to be pushed and then touch it",
                "simple",
            ),
            "incantations": IncantationsAspect("Where did it go?", "sentence"),
        },
        other_conditions=[
            ArcaneKnowledgeAspect( "time"),
            GenericAspect(difficulty=0, description="Difficulty: 10"),
        ],
    ),
    Spell(
        name="Seize the Day!",
        skill="Conjuration",
        notes="This spell allows someone of the caster’s choosing to gain an\nextra action and a +1D bonus to initiatve for one round. This\nboon occurs even if the target has already acted in the given\nround. To cast the spell, the mage swallows the gunpowder,\nlooks at the target, and shouts the incantation.",
        effect=SpecialAbilityEffect(
            "Fast Reactions", 1, "+1D to initiative roll and one additional free action"
        ),
        duration=DurationAspect(measure="1 round"),
        range=RangeAspect(measure="25 meters"),
        casting_time=CastingTimeAspect(measure="1 second"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect(
                "A pinch of gunpowder", "very common; destroyed"
            ),
            "gestures": GesturesAspect(
                "Swallow gunpowder while looking at target",
                "simple",
            ),
            "incantations": IncantationsAspect("Go!", "phrase; loud"),
        },
        other_conditions=[
            ArcaneKnowledgeAspect("inanimate forces"),
            GenericAspect(difficulty=0, description="Difficulty: 10"),
        ],
    ),
    Spell(
        name="Sequester",
        skill="Apportation",
        notes="When things look their bleakest, it is good to have an ace\nup one’s sleeve. Sequester allows a mage to gain protection by\nsliding between the present and future. The successful cast-\ning of the spell removes her from the flow of time for up to\none week and deposits her in an alternate dimension where\ntime stands still. During this period in the alien realm, she\ndoes not age, nor can she perform any actions. Her form is\nundetectable by normal means, although a detect resonance\nreveals her presence.\nWhen the caster turns off the spell or the spell runs its\ncourse, the mage is returned to the exact spot she started\nfrom when she fled from her current time. The re-emergence\ninto the normal time stream could be quite perilous for the\ntemporal traveler, as she must survive any changes to her\ncurrent environment.\nSome chronomancers fear the time spent in sequester\nbecause their subconscious is tormented with horrible psychic\nimages as it attempts to adjust to it current state. In rare cases,\nthose who seek refuge through sequester develop emotional\nquirks and in sometimes never fully regain their sanity.",
        effect=MassEffect("moves up to", "150 kilograms"),
        duration=DurationAspect(measure="1 week"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 minute"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect("A platinum ankh", "very rare; destroyed"),
            "concentration": ConcentrationAspect(
                "25 seconds",
                note="with a willpower/mettle difficulty of 9",
            ),
            "countenance": CountenanceAspect(
                "Skin takes on a bluish shade for the duration of the spell and the subconscious is haunted by psychic images",
                "extreme",
            ),
            "gestures": GesturesAspect(
                "Make a circling motion above head with one hand, then quickly casts the ankh away after pushing it against her forehead",
                "complex (acrobatics roll with a difficulty of 11)",
            ),
            "feedback": FeedbackAspect(4),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="on caster"
            ),
            "incantations": IncantationsAspect(
                "Safe from all harm but as close as a whisper, untouchable now for I am sequestered.",
                "sentence",
            ),
            "other_alterant": OtherAlterant(
                difficulty=29,
                description="Other Alterants: Moves caster out of space and time",
            ),
            "variable_duration": VariableDurationAspect("on/off switch"),
        },
        other_conditions=[
            ArcaneKnowledgeAspect("dimension, time"),
            GenericAspect(difficulty=0, description="Difficulty: 26"),
        ],
    ),
    Spell(
        name="Soulecho",
        skill="Conjuration",
        notes="Although time often heals wounds, it seldom ever forgets\nthe misery it has been forced to endure in ages past. The pain\nof horrible events left buried by the sands of time seethes\nand festers as it cries out for vengeance. This volatile, ter -\nrible power is the chronomancer’s to wield. Such wizards can\ngather the twisted fragments of tortured chronal resonances\nand vent the destructive force upon the object of their wrath.\nPower such as this is not unleashed lightly, though, and usu-\nally done quite covertly. Wise temporal magicians choose to\ntread carefully because many people would prefer to forget\nthe sorrows of the past and leave the undisturbed misery of\nages long gone buried by the dust of the passing years. Those\nwho disregard the potential danger of daring to manipulate\nsorrows of other times run the risk of angering the local\npopulace. Fools of this nature are not often long lived and\nhave found themselves burnt at the stake or worse as they\npay the ultimate price for their haughtiness.\nThe successful casting of a soulecho creates a field of eldritch\nenergy that feeds upon the pain of the past and forces it\nupon the affected area. Those who are unfortunate enough\nthe pass through the temporal blighted area (upt to eight\nvictims) attract the Bad Luck (R3) Disadvantage (for the\nduration of the spell).\n\n",
        effect=DisadvantageEffect("Bad Luck", 3),
        duration=DurationAspect(measure="25 minutes"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="10 minutes"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect(
                "100 grams of bone dust",
                "uncommon; destroyed",
            ),
            "gestures": GesturesAspect(
                "After the incantation is uttered, the bone dust is used to mark the area of effect. The caster then spends the rest of the casting time touching the area of effect and slowly acting as if pulling malevolent energy from the ground.",
                "complex (acrobatics roll with a difficulty of 11)",
            ),
            "feedback": FeedbackAspect(4),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="on target"
            ),
            "incantations": IncantationsAspect(
                "The sins of the past shall surely last. Sorrow forever surrounds us all. Ne’er let one forget how the die was cast. Come ye forth, oh misery; heed my call!",
                "litany (persuasion roll with difficulty of 15)",
            ),
            "multiple_targets": MultipleTargetAspect("8 targets"),
        },
        other_conditions=[
            ArcaneKnowledgeAspect( "death, time"),
            GenericAspect(difficulty=0, description="Difficulty: 11"),
        ],
    ),
    Spell(
        name="Suppress",
        skill="Alteration",
        notes="This powerful mystic manipulation allows the chronomancer to deftly manipulate the temporal fields around a\ngiven target, much like a skilled surgeon is able to separate\nand extract malignant tissue without harming the patient.\nWhen suppress is successfully cast, the victim is moved slightly\nout of sync with the normal time stream, which temporarily\nweakens the ability to cause harm to others with magic.\nWhen this spell is cast, the wizard chooses a specific school\nof magic to affect. For the duration of the spell, any spells\nthat cause physical damage from the chosen school and cast\nby the victim have the damage roll reduced by 4D (with a\nminimum total of zero).",
        effect=ProtectionEffect(
            "suppress damage from attack spells only",
            "4D; damage modifier",
        ),
        duration=DurationAspect(measure="1 round"),
        range=RangeAspect(measure="40 meters"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect(
                "Three dried leaves of any variety",
                "ordinary; destroyed",
            ),
            "feedback": FeedbackAspect(2),
            "gestures": GesturesAspect(
                "Crush the leaves and flick them at the target",
                "simple",
            ),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-1,
                description="Must specify one school to be affected by casting",
            ),
            ArcaneKnowledgeAspect( "magic, time"),
            GenericAspect(difficulty=0, description="Difficulty: 14"),
        ],
    ),
    Spell(
        name="Temporal Shackles",
        skill="Conjuration",
        notes="Those who are not familiar with the intricacies of time\ncan often fall prey to the machinations of those who have\nmastered it. Temporal shackles holds a victim fast with bands\nof chronal energy that alternate between past and future\nwaves of power. If a mage’s marksmanship/firearms or apport-\nation total is greater than the target’s combat difficulty, his\nquarry is trapped.\nThe effect’s value plus the result point bonus serve as\nthe damage resistance total of the shackles. The target can\ndisbelieve and thus free herself with a Perception/Acumen or\ninvestigation total of 13.",
        # Effect based on what?
        # Could be 15 * 1.5 (5D toughness with a 1.5 protection modifier)
        effect=ProtectionEffect(
            "damage resistance total of the shackles", "5D; protection modifier"
        ),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="15 meters"),
        casting_time=CastingTimeAspect(measure="1 minute"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect(
                "A 3-centimeter-long piece of quartz",
                "uncommon; destroyed",
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="on target"
            ),
            "gestures": GesturesAspect(
                "Simulate a whirlpool motion with hands while uttering the incantation and then appear to toss the spell toward the target",
                "simple",
            ),
            "incantations": IncantationsAspect(
                "A past full of suffering, echoes of futures bleak, though you vainly strain ’gainst my power, your will grows weak!",
                "sentence",
            ),
            "unreal_effect": UnrealEffectAspect.based_on("effect", "difficulty 13"),
        },
        other_conditions=[
            ArcaneKnowledgeAspect( "magic, time"),
            GenericAspect(difficulty=0, description="Difficulty: 12"),
        ],
    ),
    Spell(
        name="Time Out of Mind",
        skill="Alteration",
        notes="Time out of mind allows the mage to reach out mentally\nand feel the chronal waves that surround the spell’s intended\nbeneficiary. Through this temporal gift, the caster can free a\nbedeviled soul from a malicious spell or enchantment that\nhas been cast upon her. If the mage’s efforts are successful,\nthe subject is released from the harmful magic by temporarily having her chronal essence backwards in time to a point\nwhere it was free of the baneful magic. Once the spells target\nis loosed from arcane tribulation and the spell is broken, the\nessence rises forward in time and returns to the proper place\nin the time stream.",
        # Effect based on what? 37 is a strange number. 12D+1?  21 * 1.75 modifier
        # 36 (8D with a 1.5 protection modifier makes more sense.)
        effect=ProtectionEffect(
            "compare to the skill total of the spell countering",
            "8D; protection modifier",
        ),
        duration=DurationAspect(measure="1 round"),
        range=RangeAspect(measure="10 meters"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect("2 candles", "very common; destroyed"),
            "concentration": ConcentrationAspect(
                "1 minute",
                note="with a willpower/mettle difficulty of 10",
            ),
            "feedback": FeedbackAspect(3),
            "gestures": GesturesAspect(
                "Once the incantation is complete, stretch arms out over the center of the target, then spread arms out wide while holding the candles and tracing the surface of the afflicted. Finally, quickly reach upward and then make a slashing movement as the arms are quickly dropped.",
                "complex (acrobatics roll with difficulty of 11)",
            ),
            "incantations": IncantationsAspect(
                "Time unyielding, destinies past. Forever onward, the die has been cast. Through fate’s dire portal, great powers await. Fear thee not, mere mortal: it is not yet too late!",
                "complex (persuasion roll with difficulty of 15)",
            ),
        },
        other_conditions=[
            ArcaneKnowledgeAspect( "magic, time"),
            GenericAspect(difficulty=0, description="Difficulty: 15"),
        ],
    ),
    Spell(
        name="Time Sink",
        skill="Alteration",
        notes="Sometimes to save the day, one must seize the moment —\nliterally — and bring everything to a sudden halt. Time sink\nwas designed just for this purpose. The successful casting this\nspell temporarily stops the effects of time in a limited area.\nThe spell affects both living and nonlinving targets, up to\n1,000 kilograms total, including rain, flying projectiles, and\ncollapsing structures. The caster is also subject to the spell’s\neffect if he includes himself in the area of effect.\nAdditionally, anything entering the area of effect stops\n— bullets or shrapnel hitting the edge halt as they enter\nthe area, people pause as soon as they’re completely inside,\nand so on.\nOnce the duration of the spell wears off, the snail shell frac-\ntures and crumbles to dust. When this occurs, all temporally\nsuspended objects and effects resume their prior course and\nmotion: Bullets and shrapnel continue toward their intended\ntargets, people finish their actions, and the like.",
        effect=MassEffect("material stopped", "1 metric ton"),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="10 meters"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect("A snail shell", "ordinary; destroyed"),
            "gestures": GesturesAspect(
                "Spreads arms wide in a circle, mimicking the sphere to be created",
                "simple",
            ),
            "incantations": IncantationsAspect("Apart from time!", "phrase"),
            "area_effect": AreaEffectAspect("3m r sphere"),
            "other_alterants": OtherAlterant(
                difficulty=9, description="time stopped in area of effect"
            ),
        },
        other_conditions=[
            ArcaneKnowledgeAspect( "time"),
            GenericAspect(difficulty=0, description="Difficulty: 25"),
        ],
    ),
    Spell(
        name="Withering Sand",
        skill="Alteration",
        notes="Angered chronomancers are often wicked, vindictive crea-\ntures, and one crosses them at his own peril. Withering sand\nis but a sample of the serving of pain the temporal titans can\ndish out to those who draw their ire. The successful casting\nof this spell temporarily afflicts the target with the Age: Old (R2) Disadvantage. This spell only affects living creatures\nand bestows a +1 penalty to the difficulty of physical actions\nand +3 to any attempts to interact with those who would\nbe prejudiced against elderly people. Those who are already\naffected by the Age: Old (R2) Disadvantage have all related\nmodifiers doubled.\n\n",
        effect=DisadvantageEffect(
            "Age: Old",
            2,
            note="+1 to difficulties of physical actions and +3 to interaction difficulties when attempting to deal with much younger people",
        ),
        duration=DurationAspect(measure="10 minutes"),
        range=RangeAspect(measure="25 meters"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect(
                "60 grams of refined white sand",
                "common; destroyed",
            ),
            "gestures": GesturesAspect(
                "Toss sand at intended target and then run fingers of the same hand across the mage’s scalp from front to back",
                "simple",
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="on target"
            ),
            "incantations": IncantationsAspect(
                "Youth’s sweet flower soon fades and grows sour. Life is often lived in vane, for in the end all must wane. Your essence I draw hither. Before your sight, watch it wither!",
                "complex (persuasion roll with difficulty of 11)",
            ),
        },
        other_conditions=[
            ArcaneKnowledgeAspect("death, folk, time"),
            GenericAspect(difficulty=0, description="Difficulty: 12"),
        ],
    ),
]

__test__ = {
    "Chronal Fog": ">>> spells[0].difficulty\n11",
    "Chronobolt": ">>> spells[1].difficulty\n16",
    "Detect Resonance": ">>> spells[2].difficulty\n11",
    "Devolution": ">>> spells[3].difficulty\n24",
    "Diminish": ">>> spells[4].difficulty\n10",
    "Erosion": ">>> spells[5].difficulty\n12",
    "Loophole": ">>> spells[6].difficulty\n29",
    "Lotus Dreams": ">>> spells[7].difficulty\n18",
    "Perceptive Flux": ">>> spells[8].difficulty\n14",
    "Push": ">>> spells[9].difficulty\n10",
    "Seize the Day!": ">>> spells[10].difficulty\n10",
    "Sequester": ">>> spells[11].difficulty\n26",
    "Soulecho": ">>> spells[12].difficulty\n11",
    "Suppress": ">>> spells[13].difficulty\n14",
    "Temporal Shackles": ">>> spells[14].difficulty\n12",
    "Time Out of Mind": ">>> spells[15].difficulty\n15",
    "Time Sink": ">>> spells[16].difficulty\n25",
    "Withering Sand": ">>> spells[17].difficulty\n12",
}

if __name__ == "__main__":
    app = build_app(spells)
    app()
