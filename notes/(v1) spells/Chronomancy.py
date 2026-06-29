"""
Chronomancy
-----------

"""

import logging

from magic1 import Aspect, Spell, detail

spells = [
    Spell(
        effect=Aspect(
            format="Armor Value of 5D, physical only", base_difficulty=15, count=1
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Chronal Fog",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="magic, time", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="11", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Sphere with radius of 2 meters", base_difficulty=10, count=1
            ),
            "Components": Aspect(
                format="Three grams of mica flakes (uncommon, destroyed)",
                base_difficulty=-8,
                count=1,
            ),
            "Focused": Aspect(format="On caster", base_difficulty=4, count=1),
            "Gestures": Aspect(
                format="Twirls arms around while dispersing the mica flakes to form a ring around the caster (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Mists of time, clouds of fate, shield me now, for the hour is late!” (sentence, loud)",
                base_difficulty=-3,
                count=1,
            ),
        },
        notes="Upon the dispersal of the spell component, a foglike haze\nsurrounds the magic wielder. The haze is formed by the chronal\nechoes that emanate from the fluctuating temporal fields that\nthe mage summons to deflect physical damage. The barrier\nis centered upon the caster and provides an Armor Value of\n5D against all types of physical (not mental) attacks. The\nfog effect of the spell offers the same visibility limitations\nof light fog for both the magic wielder and those who wish\nto peer through it.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="5D physical damage, ignores all armor", base_difficulty=30, count=1
        ),
        duration=Aspect(format="1 second ", base_difficulty=0, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="1 second ", base_difficulty=0, count=1),
        name="Chronobolt",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="death, time", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="16", base_difficulty=0, count=1),
            "Components": Aspect(
                format="A small hourglass (uncommon)", base_difficulty=-4, count=1
            ),
            "Gestures": Aspect(
                format="Hold an hourglass before the intended target and shake the sand inside it (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“The future beckons, come and embrace the pain. You now shall suffer, tis victory I gain!” (sen- tence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes="The successful casting of a chronobolt allows the temporal\nmanipulator to create an aura that causes a portion of the\nintended target to move slightly forward in time. (This also\nmeans that no armor protects against the bolt.) The chronal\ndisturbance does 5D in damage to the victim from a range\nof up to 10 meters from the caster. She must make a marks-\nmanship/firearms or apportation roll to hit the target. The bolt\nmust be fired in the same round that the spell is cast. After\nspell effects have been resolved, the target suffers no further\nill effects from the temporal disturbance.\nThe caster cannot choose which portion of the victim is\nmoved further in time. Such things are totally random, and\nin some cases, may be portions of the target’s molecular\nstructure instead of a limb or section of the body.\n\n",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="Extra Sense: Chronal Energy (R3), +3D to search and investigation for chronal energy",
            base_difficulty=9,
            count=1,
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        name="Detect Resonance",
        other_aspects={
            "Arcane Knowledge": Aspect(format="time", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="11", base_difficulty=0, count=1),
            "Area of Effect": Aspect(
                format="Divination sphere with radius of 25 meters",
                base_difficulty=21,
                count=1,
            ),
            "Components": Aspect(
                format="An astrolabe with quartz lenses (uncommon); 18 grams of diamond dust (uncommon, destroyed)",
                base_difficulty=-12,
                count=1,
            ),
            "Gestures": Aspect(
                format="Toss the diamond dust in the air and views the area with the astrolabe (complex;  investigation dif- ficulty of 11)",
                base_difficulty=-4,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Though the temporal winds run wild and free, through its shadowy wake, I now clearly see!” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes="When successfully cast, the arcane aid can provide a mage\nwith one of the following pieces of information, which the\nmage chooses at casting.\n1. He could discover the existence of things that are out\nof sync with the time stream in a given area, such as time\ntravelers or extradimensional creatures that exist out the\nnormal range of vision.\n2. He could reveal the existence of active chronal enchant-\nments that are bedeviling a tortured soul.\n3. He could decide to employ this magic to discover hid -\nden chronal gates and gain entrance to other times. Such\nventures have their own risk however, as those who travel\nthrough such devices to other times without taking proper\nprecautions could unwittingly release time-lost horrors.\nThe difficulty to find the chronal energy is 11, with higher\nresults indication more information. The range and area of\neffect of the spell indicate the maximum effectiveness of the\nnewly acquired sense.",
        skill="Divination",
    ),
    Spell(
        effect=Aspect(
            format="Reduced Attribute: Knowledge/Intellect (R4), -1D to the attribute",
            base_difficulty=12,
            count=1,
        ),
        duration=Aspect(format="5 rounds ", base_difficulty=7, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Devolution",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="animal, folk, time", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="23", base_difficulty=0, count=1),
            "Components": Aspect(
                format="60 grams of brain matter, which may come any recently deceased creature as long as the matter retains at least its cranial fluid (common, destroyed)",
                base_difficulty=-6,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=3, count=1),
            "Gestures": Aspect(
                format="Crush brain matter and fling at the target (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Time rolls back to reveal the shame of your lowly ancestors!” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
            "Variable Effect": Aspect(
                format="Up to an additional nine ranks of Reduced Attribute: Knowledge/Intellect (which means up to an additional -3D to the attribute)",
                base_difficulty=27,
                count=1,
            ),
        },
        notes="Devolution digs deep into the ancestral memories of the\nintended victim in order to flood her mind with horrific\nimages of what her primordial ancestors once were. The oft\nbarbaric visions can deliver a devastating blow to the victim’s\npsyche and rattle her resolve.\nWhen casting this spell, the mage crushes the brain matter\nin his hand and flings the remains at the target. If the target\ncannot beat the caster’s spell skill total with a willpower/\nmettle roll, the victim loses up to 4D of Knowledge/Intellect\n(minimum adjust attribute value of 1D) for five rounds while\nher mind reels as it psychically regresses.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="reduces the duration of a chosen spell by 10 minutes",
            base_difficulty=14,
            count=1,
        ),
        duration=Aspect(format="1 second ", base_difficulty=0, count=1),
        range=Aspect(format="15 meters ", base_difficulty=6, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=6, count=1),
        casting_time=Aspect(format="2.5 seconds ", base_difficulty=-2, count=1),
        name="Diminish",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="magic, time", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="10", base_difficulty=0, count=1),
            "Components": Aspect(
                format="1-decimeter square cloth (ordinary)",
                base_difficulty=-1,
                count=1,
            ),
            "Gestures": Aspect(
                format="Mime wiping away something with the cloth (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Arcane blight, begone!” (phrase)", base_difficulty=-1, count=1
            ),
        },
        other_conditions=[
            Aspect(
                format="Must specify at casting a single spell to target",
                base_difficulty=-1,
                count=1,
            )
        ],
        notes="The successful casting of diminish reduces the duration\nof the targeted spell by up to 10 minutes. When a caster\nattempts to affect a given spell, compare the skill total used\nto cast diminish to the skill total used to create the offend -\ning spell. If the diminish spell total is equal or higher than\nthe targeted spell’s skill total, the spell duration is reduced.\nSpells with 10 minutes or less of duration left on them cease\nto function. Only one diminish spell can reduce the duration\nof any particular spell.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(format="6D physical damage", base_difficulty=18, count=1),
        duration=Aspect(format="1 second ", base_difficulty=0, count=1),
        range=Aspect(format="40 meters ", base_difficulty=8, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=8, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        name="Erosion",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="death, time", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="12", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Sphere with radius of 1 meter", base_difficulty=5, count=1
            ),
            "Components": Aspect(
                format="A gram of sand (ordinary, destroyed)",
                base_difficulty=-2,
                count=1,
            ),
            "Gestures": Aspect(
                format="Fling sand at the target area while the incantation is uttered (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Time the healer, time the stealer, once thought by all to forever last, now it is most assuredly past.” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(format="Affects nonliving matter only", base_difficulty=-1, count=1)
        ],
        notes="Erosion allows the chronomancer to rapidly accelerate the\nbreakdown of nonliving matter. Upon the successful casting\nof this spell, a mage may cause a small sphere’s worth of\nmaterial to crumble to dust as it succumbs to the onslaught\nof time. Any living matter in the affected area is unharmed\nby the spell, although any structural effects caused by the\nmagic may still be dangerous. Erosion can be utilized topple\nlarge structures and cause general chaos for the unwary.\nThe availability of erosion’s material component makes the\nmagic popular for mages who find themselves imprisoned.\nThus, it is not uncommon for jailers who have experience in\nconfining wizards to bind and sometimes keep their charges\nblindfolded for the duration of their incarceration.\n\n",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="+6D to one Magic skill and affecting one spell, specified at spell casting, that the target wishes to cast quickly",
            base_difficulty=45,
            count=1,
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="3.5 meters ", base_difficulty=3, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=3, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Loophole",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="magic, time", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="29", base_difficulty=0, count=1),
            "Components": Aspect(
                format="A 30 cubic centimeter vial of ink (very common, destroyed)",
                base_difficulty=-4,
                count=1,
            ),
            "Feedback": Aspect(
                format="-1 to damage resistance total", base_difficulty=-1, count=1
            ),
            "Focused": Aspect(format="On target", base_difficulty=10, count=1),
            "Gestures": Aspect(
                format="Fling the ink at target while uttering the incantation (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Quickly cast quiet creations.” (phrase)",
                base_difficulty=-1,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="Not usable on spells with incantations, gestures, or concentration requirements",
                base_difficulty=-1,
                count=1,
            )
        ],
        notes="Every once in a while, one just does not have enough time\nto deal with the current situation and needs a little help from\na friend. Loophole serves just this purpose as it causes time\naround the intended target to “blink.” This effect hastens\nthe recipient forward in time, which allows the person to\nshorten the casting time of one spell by 75% (round up, with\na maximum reduced casting time ofone minute). The spell\ndifficulty increases by +20, but the target’s skill increases\nby 6D to compensate for this. The recipient of this spell\ncan perform no other action outside of the casting of the\nintended spell.\nThe ink disappears once the target casts the spell.",
        skill="Apportation",
    ),
    Spell(
        effect=Aspect(
            format="Accelerated Healing (R7), +7D bonus to natural healing attempts",
            base_difficulty=21,
            count=1,
        ),
        duration=Aspect(format="1 day ", base_difficulty=25, count=1),
        range=Aspect(format="Touch ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        name="Lotus Dreams",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="dreams, time", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="18", base_difficulty=0, count=1),
            "Components": Aspect(
                format="3 grams of incense made from crushed lotus petals (uncommon, destroyed)",
                base_difficulty=-8,
                count=1,
            ),
            "Countenance": Aspect(
                format="Skin turns an unhealthy pale tone for the duration of the spell",
                base_difficulty=-1,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=9, count=1),
            "Gestures": Aspect(
                format="Gently closes the eyes of the recipient and traces the lines of the bony plates that compose the skull of the intended recipient as the incantation is uttered (complex; sleight of hand roll with difficulty of 11)",
                base_difficulty=-3,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Though your mortal form has been rent asunder, embrace life and drink deeply from the draught of endless slumber.” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
            "Other Alterants": Aspect(
                format="Target cannot be awakened", base_difficulty=4, count=1
            ),
        },
        notes="When this magic is successfully cast upon a willing recipi-\nent, the target falls into a deep, coma-like slumber that lasts\nfor a full 24 hours. After the recipient awakens from his life-\nrenewing respite, the spell’s effect grants him a +7D modifier\nto natural healing roll for the day.\nDuring the spell’s duration it is impossible for the recipient\nto waken or be awakened normally. Those with telepathic or\nsimilar powers can contact them mentally but the answers\ngiven come sluggishly and are typically one or two words.\nThis is in addition to aging from the normal passage of\ntime. Although uncommon, it is not unheard of for those\nwho emerge from the lotus dreams induced sleep to complain\nof experiencing a vertigo effect during the spell. Some are\nhesitant to receive the benefits of the spell a second time\nunless they are near death.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="Hindrance: Initiative (R5), -10 to all initiative totals",
            base_difficulty=15,
            count=1,
        ),
        duration=Aspect(format="1 round ", base_difficulty=4, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        name="Perceptive Flux",
        other_aspects={
            "Arcane Knowledge": Aspect(format="time", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="14", base_difficulty=0, count=1),
            "Components": Aspect(
                format="A gram of sandstone (very common, destroyed)",
                base_difficulty=-4,
                count=1,
            ),
            "Countenance": Aspect(
                format="Skin turns a sickly gray color for the duration of the spell",
                base_difficulty=-1,
                count=1,
            ),
            "Gestures": Aspect(
                format="Crush sandstone and drop it to the floor (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Multiple Targets": Aspect(
                format="Up to 5 targets", base_difficulty=15, count=1
            ),
        },
        notes="Perceptive flux is an extremely useful spell for covert opera-\ntions as it can give strike teams a definite tactical advantage.\nAlthough it takes some time to prepare the magic, the spell’s\nlack of verbal aspects can make it well worth casting.\nAt the end of a successful casting, the opponents think it’s\na different time than it actually is, causing several seconds\nof disorientation.\nThe minimum initiative total an opponent can generate is\nzero, which means that he goes last in the round.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="sends a small object up to 10 minutes into the future",
            base_difficulty=14,
            count=1,
        ),
        duration=Aspect(format="10 minutes ", base_difficulty=14, count=1),
        range=Aspect(format="Touch ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Push",
        other_aspects={
            "Arcane Knowledge": Aspect(format="time", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="10", base_difficulty=0, count=1),
            "Gestures": Aspect(
                format="Wave one hand across the object to be pushed and then touch it (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Where did it go?” (sentence)", base_difficulty=-2, count=1
            ),
        },
        notes="Even the most subtle of things can sometimes make all the\ndifference in the world. Push takes an object of a kilogram or\nless in weight and transports it up to 10 minutes forward in\ntime. The spell is popular with charlatans, con artists, stage\nmagicians, and pranksters. Once the spell runs its course,\nthe pushed object appears exactly where it was before the\nspell was cast. It is affected by any environmental changes\nupon its return.\n\n",
        skill="Apportation",
    ),
    Spell(
        effect=Aspect(
            format="Fast Reactions (R1), +1D to initiative roll and one additional free action",
            base_difficulty=9,
            count=1,
        ),
        duration=Aspect(format="1 round ", base_difficulty=4, count=1),
        range=Aspect(format="25 meters ", base_difficulty=7, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=7, count=1),
        casting_time=Aspect(format="1 second ", base_difficulty=0, count=1),
        name="Seize the Day!",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="inanimate forces", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="10", base_difficulty=0, count=1),
            "Components": Aspect(
                format="A pinch of gunpowder (very common, destroyed)",
                base_difficulty=-4,
                count=1,
            ),
            "Gestures": Aspect(
                format="Swallow gunpowder while looking at target (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="”Go!” (phrase, loud)", base_difficulty=-2, count=1
            ),
        },
        notes="This spell allows someone of the caster’s choosing to gain an\nextra action and a +1D bonus to initiatve for one round. This\nboon occurs even if the target has already acted in the given\nround. To cast the spell, the mage swallows the gunpowder,\nlooks at the target, and shouts the incantation.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="moves up to 150 kilograms", base_difficulty=11, count=1),
        duration=Aspect(format="1 week ", base_difficulty=29, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        name="Sequester",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="dimension, time", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="26", base_difficulty=0, count=1),
            "Components": Aspect(
                format="A platinum ankh (very rare, destroyed)",
                base_difficulty=-10,
                count=1,
            ),
            "Concentration": Aspect(
                format="25 seconds with a willpower/mettle difficulty of 9",
                base_difficulty=-3,
                count=1,
            ),
            "Countenance": Aspect(
                format="Skin takes on a bluish shade for the duration of the spell and the subconscious is haunted by psychic images",
                base_difficulty=-2,
                count=1,
            ),
            "Gestures": Aspect(
                format="Make a circling motion above head with one hand, then quickly casts the ankh away after pushing it against her forehead (complex; acrobatics roll with a difficulty of 11)",
                base_difficulty=-3,
                count=1,
            ),
            "Feedback": Aspect(
                format="-4 to damage resistance total", base_difficulty=-4, count=1
            ),
            "Focused": Aspect(format="On caster", base_difficulty=8, count=1),
            "Incantations": Aspect(
                format="“Safe from all harm but as close as a whisper, untouchable now for I am sequestered.” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
            "Variable Duration": Aspect(
                format="On/off switch", base_difficulty=8, count=1
            ),
            "Other Alterants": Aspect(
                format="Moves caster out of space and time", base_difficulty=29, count=1
            ),
        },
        notes="When things look their bleakest, it is good to have an ace\nup one’s sleeve. Sequester allows a mage to gain protection by\nsliding between the present and future. The successful cast-\ning of the spell removes her from the flow of time for up to\none week and deposits her in an alternate dimension where\ntime stands still. During this period in the alien realm, she\ndoes not age, nor can she perform any actions. Her form is\nundetectable by normal means, although a detect resonance\nreveals her presence.\nWhen the caster turns off the spell or the spell runs its\ncourse, the mage is returned to the exact spot she started\nfrom when she fled from her current time. The re-emergence\ninto the normal time stream could be quite perilous for the\ntemporal traveler, as she must survive any changes to her\ncurrent environment.\nSome chronomancers fear the time spent in sequester\nbecause their subconscious is tormented with horrible psychic\nimages as it attempts to adjust to it current state. In rare cases,\nthose who seek refuge through sequester develop emotional\nquirks and in sometimes never fully regain their sanity.",
        skill="Apportation",
    ),
    Spell(
        effect=Aspect(format="Bad Luck (R3)", base_difficulty=9, count=1),
        duration=Aspect(format="25 minutes ", base_difficulty=16, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="10 minutes ", base_difficulty=-14, count=1),
        name="Soulecho",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="death, time", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="11", base_difficulty=0, count=1),
            "Components": Aspect(
                format="100 grams of bone dust (uncommon, destroyed)",
                base_difficulty=-8,
                count=1,
            ),
            "Gestures": Aspect(
                format="After the incantation is uttered, the bone dust is used to mark the area of effect. The caster then spends the rest of the casting time touching the area of effect and slowly acting as if pulling malevolent energy from the ground. (complex; acrobatics roll with a difficulty of 11)",
                base_difficulty=-3,
                count=1,
            ),
            "Feedback": Aspect(
                format="-4 to damage resistance total", base_difficulty=-4, count=1
            ),
            "Focused": Aspect(format="On targets", base_difficulty=6, count=1),
            "Incantations": Aspect(
                format="“The sins of the past shall surely last. Sorrow forever surrounds us all. Ne’er let one forget how the die was cast. Come ye forth, oh misery; heed my call!” (litany; persuasion roll with difficulty of 15)",
                base_difficulty=-4,
                count=1,
            ),
            "Multiple Targets": Aspect(
                format="Up to 8 targets", base_difficulty=24, count=1
            ),
        },
        notes="Although time often heals wounds, it seldom ever forgets\nthe misery it has been forced to endure in ages past. The pain\nof horrible events left buried by the sands of time seethes\nand festers as it cries out for vengeance. This volatile, ter -\nrible power is the chronomancer’s to wield. Such wizards can\ngather the twisted fragments of tortured chronal resonances\nand vent the destructive force upon the object of their wrath.\nPower such as this is not unleashed lightly, though, and usu-\nally done quite covertly. Wise temporal magicians choose to\ntread carefully because many people would prefer to forget\nthe sorrows of the past and leave the undisturbed misery of\nages long gone buried by the dust of the passing years. Those\nwho disregard the potential danger of daring to manipulate\nsorrows of other times run the risk of angering the local\npopulace. Fools of this nature are not often long lived and\nhave found themselves burnt at the stake or worse as they\npay the ultimate price for their haughtiness.\nThe successful casting of a soulecho creates a field of eldritch\nenergy that feeds upon the pain of the past and forces it\nupon the affected area. Those who are unfortunate enough\nthe pass through the temporal blighted area (upt to eight\nvictims) attract the Bad Luck (R3) Disadvantage (for the\nduration of the spell).\n\n",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="-4D to physical damage rolls; only affects attack spells",
            base_difficulty=18,
            count=1,
        ),
        duration=Aspect(format="1 round ", base_difficulty=4, count=1),
        range=Aspect(format="40 meters ", base_difficulty=8, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=8, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Suppress",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="magic, time", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="14", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Three dried leaves of any variety (ordinary, destroyed)",
                base_difficulty=-2,
                count=1,
            ),
            "Feedback": Aspect(
                format="-2 to damage resistance total", base_difficulty=-2, count=1
            ),
            "Gestures": Aspect(
                format="Crush the leaves and flick them at the target (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="Must specify one school to be affected by casting",
                base_difficulty=-1,
                count=1,
            )
        ],
        notes="This powerful mystic manipulation allows the chrono -\nmancer to deftly manipulate the temporal fields around a\ngiven target, much like a skilled surgeon is able to separate\nand extract malignant tissue without harming the patient.\nWhen suppress is successfully cast, the victim is moved slightly\nout of sync with the normal time stream, which temporarily\nweakens the ability to cause harm to others with magic.\nWhen this spell is cast, the wizard chooses a specific school\nof magic to affect. For the duration of the spell, any spells\nthat cause physical damage from the chosen school and cast\nby the victim have the damage roll reduced by 4D (with a\nminimum total of zero).",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="damage resistance total of the shackles",
            base_difficulty=23,
            count=1,
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="15 meters ", base_difficulty=6, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=6, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        name="Temporal Shackles",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="magic, time", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="12", base_difficulty=0, count=1),
            "Components": Aspect(
                format="A 3-centimeter-long piece of quartz (uncommon, destroyed)",
                base_difficulty=-8,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=6, count=1),
            "Gestures": Aspect(
                format="Simulate a whirlpool motion with hands while uttering the incantation and then appear to toss the spell toward the target (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“A past full of suffering, echoes of futures bleak, though you vainly strain ’gainst my power, your will grows weak!” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
            "Unreal Effect": Aspect(
                format="Disbelief difficulty of 13", base_difficulty=-6, count=1
            ),
        },
        notes="Those who are not familiar with the intricacies of time\ncan often fall prey to the machinations of those who have\nmastered it. Temporal shackles holds a victim fast with bands\nof chronal energy that alternate between past and future\nwaves of power. If a mage’s marksmanship/firearms or apport-\nation total is greater than the target’s combat difficulty, his\nquarry is trapped.\nThe effect’s value plus the result point bonus serve as\nthe damage resistance total of the shackles. The target can\ndisbelieve and thus free herself with a Perception/Acumen or\ninvestigation total of 13.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="compare to the skill total of the spell countering",
            base_difficulty=37,
            count=1,
        ),
        duration=Aspect(format="1 round ", base_difficulty=4, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Time Out of Mind",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="magic, time", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="15", base_difficulty=0, count=1),
            "Components": Aspect(
                format="2 candles (very common, destroyed)", base_difficulty=-4, count=1
            ),
            "Concentration": Aspect(
                format="1 minute with a willpower/mettle difficulty of 10",
                base_difficulty=-4,
                count=1,
            ),
            "Feedback": Aspect(
                format="-3 to damage resistance total", base_difficulty=-3, count=1
            ),
            "Incantations": Aspect(
                format="“Time unyielding, destinies past. Forever onward, the die has been cast. Through fate’s dire portal, great powers await. Fear thee not, mere mortal: it is not yet too late!” (complex; persuasion roll with difficulty of 15)",
                base_difficulty=-3,
                count=1,
            ),
            "Gestures": Aspect(
                format="Once the incantation is complete, stretch arms out over the center of the target, then spread arms out wide while holding the candles and tracing the surface of the afflicted. Finally, quickly reach upward and then make a slashing movement as the arms are quickly dropped. (complex; acrobatics roll with difficulty of 11)",
                base_difficulty=-3,
                count=1,
            ),
        },
        notes="Time out of mind allows the mage to reach out mentally\nand feel the chronal waves that surround the spell’s intended\nbeneficiary. Through this temporal gift, the caster can free a\nbedeviled soul from a malicious spell or enchantment that\nhas been cast upon her. If the mage’s efforts are successful,\nthe subject is released from the harmful magic by temporar-\nily having her chronal essence backwards in time to a point\nwhere it was free of the baneful magic. Once the spells target\nis loosed from arcane tribulation and the spell is broken, the\nessence rises forward in time and returns to the proper place\nin the time stream.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="1 metric ton of material stopped", base_difficulty=15, count=1
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Time Sink",
        other_aspects={
            "Arcane Knowledge": Aspect(format="time", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="25", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Sphere with a radius of 3 meters", base_difficulty=15, count=1
            ),
            "Components": Aspect(
                format="A snail shell (ordinary, destroyed)",
                base_difficulty=-2,
                count=1,
            ),
            "Gestures": Aspect(
                format="Spreads arms wide in a circle, mimicking the sphere to be created (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Apart from time!” (phrase)", base_difficulty=-1, count=1
            ),
            "Other Alterants": Aspect(
                format="Time stopped in area of effect", base_difficulty=9, count=1
            ),
        },
        notes="Sometimes to save the day, one must seize the moment —\nliterally — and bring everything to a sudden halt. Time sink\nwas designed just for this purpose. The successful casting this\nspell temporarily stops the effects of time in a limited area.\nThe spell affects both living and nonlinving targets, up to\n1,000 kilograms total, including rain, flying projectiles, and\ncollapsing structures. The caster is also subject to the spell’s\neffect if he includes himself in the area of effect.\nAdditionally, anything entering the area of effect stops\n— bullets or shrapnel hitting the edge halt as they enter\nthe area, people pause as soon as they’re completely inside,\nand so on.\nOnce the duration of the spell wears off, the snail shell frac-\ntures and crumbles to dust. When this occurs, all temporally\nsuspended objects and effects resume their prior course and\nmotion: Bullets and shrapnel continue toward their intended\ntargets, people finish their actions, and the like.",
        skill="Alteration",  # Source document says "Chronomancy".
    ),
    Spell(
        effect=Aspect(
            format="Age: Old (R2), +1 to difficulties of physical actions and +3 to interaction difficulties when attempting to deal with much younger people",
            base_difficulty=6,
            count=1,
        ),
        duration=Aspect(format="10 minutes ", base_difficulty=14, count=1),
        range=Aspect(format="25 meters ", base_difficulty=7, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=7, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Withering Sand",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="death, folk, time", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="12", base_difficulty=0, count=1),
            "Components": Aspect(
                format="60 grams of refined white sand (common, destroyed)",
                base_difficulty=-6,
                count=1,
            ),
            "Gestures": Aspect(
                format="Toss sand at intended target and then run fingers of the same hand across the mage’s scalp from front to back (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=4, count=1),
            "Incantations": Aspect(
                format="“Youth’s sweet flower soon fades and grows sour. Life is often lived in vane, for in the end all must wane. Your essence I draw hither. Before your sight, watch it wither!” (complex; persuasion roll with difficulty of 11)",
                base_difficulty=-3,
                count=1,
            ),
        },
        notes="Angered chronomancers are often wicked, vindictive crea-\ntures, and one crosses them at his own peril. Withering sand\nis but a sample of the serving of pain the temporal titans can\ndish out to those who draw their ire. The successful casting\nof this spell temporarily afflicts the target with the Age: Old\n(R2) Disadvantage. This spell only affects living creatures\nand bestows a +1 penalty to the difficulty of physical actions\nand +3 to any attempts to interact with those who would\nbe prejudiced against elderly people. Those who are already\naffected by the Age: Old (R2) Disadvantage have all related\nmodifiers doubled.\n\n",
        skill="Alteration",
    ),
]

if __name__ == "__main__":
    detail(spells)

__test__ = {
    "Chronal Fog": ">>> spells[0].difficulty\n11",
    "Chronobolt": ">>> spells[1].difficulty\n16",
    "Detect Resonance": ">>> spells[2].difficulty\n11",
    "Devolution": ">>> spells[3].difficulty\n23",
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
