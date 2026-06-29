"""
Necromancy
----------

"""

from magic1 import Aspect, Spell, Cantrip, detail

spells = [
    Spell(
        effect=Aspect(
            format="Skill Bonus: Mindless (R1), +3 to willpower/mettle totals; Skill Bonus: Painless Wounds (R1), +3 to stamina total; attributes based on result points",
            base_difficulty=6,
            count=1,
        ),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="25 meters ", base_difficulty=7, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=7, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        name="Animate Dead",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Enchanted", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="14", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Complete skeleton or body (uncommon)",
                base_difficulty=-4,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=4, count=1),
            "Incantations": Aspect(
                format="“Animate!” (phrase)", base_difficulty=-1, count=1
            ),
        },
        notes="Any type of corporeal dead creature can be used for this\nritual. Whether it has been recently killed or dead for years\nmakes no difference, so long as it is physically intact. Upon\ncompleting the spell, the dead creature is animated but not\nliving.\nThe result points of the spell determine the attributes,\nBody Points, and Wound levels of the animated dead. The\nattributes equal in dice the points above the difficulty. Body\nPoints equal the result points plus 10. Wound levels equal\nthe half of the result points (round up). Movement equals\nthe result points in meters.\nGenerally rather stupid, the caster can attempt to control\nthem through simple commands. Left to their own devices,\nthey attack anything near them.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="+2D to Physique/Strength; +1D to  Acumen/Perception; +1D to attribute for brawling/fighting and melee combat; Skill Bonus: Mindless (R1), +3 to willpower/mettle totals; Skill Bonus: Painless Wounds (R1), +3 to stamina total; attributes and movement based on result points",
            base_difficulty=33,
            count=1,
        ),
        duration=Aspect(format="1 day ", base_difficulty=25, count=1),
        range=Aspect(format="25 meters ", base_difficulty=7, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=7, count=1),
        casting_time=Aspect(format="1 hour ", base_difficulty=-18, count=1),
        name="Animate Superior Undead",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Enchanted", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="25", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Recently dead, complete corpse (very rare)",
                base_difficulty=-5,
                count=1,
            ),
            "Concentration": Aspect(
                format="15 minutes with willpower/mettle difficulty of 11",
                base_difficulty=-5,
                count=1,
            ),
            "Focus": Aspect(format="On target", base_difficulty=11, count=1),
            "Gestures": Aspect(
                format="Repeatedly raise hands above target, as if encouraging it to get up (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Come to life and fight for me, my undead minion!” (sentence, loud)",
                base_difficulty=-3,
                count=1,
            ),
        },
        notes="The body needed for the ritual must be completely intact,\nand dead no longer than 24 hours. After an hour of prepara-\ntion, the corpse takes on a pseudo-life. The result points of\nthe spell determine the attributes, Body Points, and Wound\nlevels of the skeletons. The attributes equal in dice the points\nabove the difficulty. Body Points equal the result points plus\n10. Wound levels equal the half of the result points (round up).\nMovement equals the result points in meters. The Physique/\nStrength attribute also gets +2D to it, the Acumen/Perception\nscore goes up by 1D, and  brawling/fighting and melee combat\neach equal +1D above the related attribute score.\nSuperior undead have minds of their own. Though they\ncan understand more than rudimentary commands, this also\nmeans that they are as likely to turn on their creator should\nshe fail command them properly as they are to continue on\ntheir designated course of action.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="compare to planar distance", base_difficulty=39, count=1),
        duration=Aspect(format="1 day ", base_difficulty=25, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Call Tomb Fiend",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Entity", base_difficulty=0, count=1),
            "Difficulty": Aspect(
                format="20", base_difficulty=0, count=1
            ),  # Appears incorrect. 26.
            "Components": Aspect(
                format="Dried flesh (common)", base_difficulty=-3, count=1
            ),
            "Incantations": Aspect(
                format="“Awaken from the immortal shadow!” (sentence, loud)",
                base_difficulty=-3,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="In a tomb or near a burial ground", base_difficulty=-3, count=1
            ),
        ],
        notes="When summoned, the tomb fiend comes to the aid of the\nmage. The creature is not very sizable, and it does not make\nan ideal combatant. But, for the purpose of being a servant,\nit works wonderfully. Although this stubby and stooped\ncreature has talons, they are for climbing, not fighting. Fur-\nthermore, comprehending the caster’s universe is a difficult\ntask, making commanding the fiend a challenge.\nCommands must be given in simple noun-verb sentences.\nThe tomb fiend can’t understand anything more complex.\n\n\n\n",
        skill="Apportation",
    ),
    Spell(
        effect=Aspect(
            format="1 human-sized being held in stasis", base_difficulty=10, count=1
        ),
        duration=Aspect(format="1 month ", base_difficulty=32, count=1),
        range=Aspect(format="5 meters ", base_difficulty=4, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=4, count=1),
        casting_time=Aspect(format="1 hour ", base_difficulty=-18, count=1),
        name="Capture Life force",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Death", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="17", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Box mad of bone (rare)", base_difficulty=-4, count=1
            ),
            "Concentration": Aspect(
                format="Must concentrate for 30 minutes", base_difficulty=-2, count=1
            ),
            "Focused": Aspect(format="Bone box", base_difficulty=8, count=1),
        },
        notes="This spell allows a magic user to capture the soul of a living\ncreature, and lock it away for the spell’s duration. During this\nperiod, the target’s body is not dead; it is in stasis. When cast,\nthe only visible effect is that the target’s body becomes relaxed\nif the spell is successful. At this point, bone box contains the\nsoul of the person. Time does not pass for those affected by\nthis spell. Dreams and thought are not possible, life simple\nstops and only starts when the spell is ended. The caster can\nchoose to end the spell early if she chooses.\nIf the target’s body is destroyed during the spell’s period,\nthe soul cannot be returned to the living world. Instead,\nat the end of the spell, the soul is lost to the neither world.\nThis spell is not only used to make prisoners of enemies, but\noften used to prolong the life of a dying friend. If it is cast\nbefore death, the body can be carried to someone capable\nof healing the character. However, the lifeforce must be\nreturned to the body before it can be healed. Other uses for\nthis spell are to prevent aging during travel, or the exhaus -\ntion of traveling — allowing someone else to carry the bone\nbox and transporting the body in a casket.",
        skill="Alternation",
    ),
    Spell(
        effect=Aspect(
            format="+4D to disguise [con: disguise in D6 Space] against undead or machines",
            base_difficulty=18,
            count=1,
        ),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="Touch ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        name="Cold Flesh",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Death", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="16", base_difficulty=0, count=1),
            "Components": Aspect(
                format="iron filings (uncommon)", base_difficulty=-1, count=1
            ),
            "Focused": Aspect(format="On target", base_difficulty=7, count=1),
            "Gestures": Aspect(
                format="Sprinkle filings on target (simple)",
                base_difficulty=-1,
                count=1,
            ),
        },
        notes="This spell disguises a living being from detection by the non-\nliving by masking the target’s body ambient temperature.\nUndead creatures or heat sensing device cannot sense the\ntarget. The effects of this spell last until either the duration\nexpires or the target attacks or threatens any non-living\nentity or machine that is being deceived. If the player char-\nacter is trained in disguise, then the modifier from the spell\nis added to the skill.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="6D+2, ignores nonmagical armor", base_difficulty=30, count=1
        ),
        duration=Aspect(format="3 rounds ", base_difficulty=6, count=1),
        range=Aspect(format="15 meters ", base_difficulty=6, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=6, count=1),
        casting_time=Aspect(format="2.5 seconds ", base_difficulty=-2, count=1),
        name="Consuming Sphere",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Death", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="30", base_difficulty=0, count=1),
            "Area Effect": Aspect(format="3-meter sphere", base_difficulty=15, count=1),
            "Feedback": Aspect(
                format="-2 to damage resistance total", base_difficulty=-2, count=1
            ),
            "Gestures": Aspect(
                format="Rolling motion with hands (simple)", base_difficulty=-1, count=1
            ),
            "Incantations": Aspect(
                format="“Consume them!” (sentence)", base_difficulty=-2, count=1
            ),
            "Variable Movement": Aspect(
                format="Movement of 12.5 meters per round", base_difficulty=3, count=1
            ),
        },
        notes="This spell produces a 3-meter sphere of pulsating dark energy\nthat rolls across the ground, doing damage to all living matter\nit encounters. The trajectory of the sphere cannot be changed\nonce the spell is cast. However, as it is not instantaneous,\nthere is a possibility potential targets can avoid encountering\nthis deadly conjuration, providing it is seen. During daylight\nhours, a search of Easy is required; during night, or in dark-\nness, a search of Very Difficult is required. Also, avoidance\nrequires that the character has time to dive clear.\nThe sphere consumes life energy. This means that nonmagi-\ncal armor offers no protection against it. None of this energy\nincreases the damage of the sphere, nor is it conveyed to the\nmagic user. Victims who die as a result, quickly whither, leav-\ning only bones and dust behind. Non-living material such as\narmor weapons and so on are not affected.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="6D+2 damage", base_difficulty=30, count=1),
        duration=Aspect(format="3 weeks ", base_difficulty=31, count=1),
        range=Aspect(format="Touch ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="2 days ", base_difficulty=-27, count=1),
        name="Conqueror Worm",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Death", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="19", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Earthworm (common)", base_difficulty=-3, count=1
            ),
            "Focused": Aspect(format="On target", base_difficulty=12, count=1),
            "Incantations": Aspect(
                format="Repeated incantations of un-life; an willpower/mettle roll with a difficulty 11 must be made during each day of casting (complex)",
                base_difficulty=-3,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="After the spell is cast, the magic user must find a way to get a victim to swallow the foul creation.",
                base_difficulty=-2,
                count=1,
            ),
        ],
        notes="Often the worm can be hidden in food or drink — alcohol\ncannot kill it. If it is not consumed within 24 hours after the\nspell’s casting, the worm dies and is useless. An Acumen or\nPerception roll with a 10 difficulty must be performed by the\nintended victim to detect the presence of the worm.\nThis spell prepares the component for the spell Monstrous\nCreation By transforming the positive living energy of a\nsimple earthworm, the magic user creates an evil seed that is\nusually unwittingly consumed by an intended victim. Often,\nthe victim is one of the caster’s own henchmen, as once the\nworm is ingested, it becomes a parasite, waiting for the proper\nmagic to transform it a fell creature that devours its host. By\nusing a henchman, the spell is ready to be activated at will.\nCertainly there is a cost in acolytes and followers, but those\ncan easily be replaced.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="+D6 to hide", base_difficulty=27, count=1),
        duration=Aspect(format="2 minutes ", base_difficulty=10, count=1),
        range=Aspect(format="60 meters ", base_difficulty=9, count=1),
        speed=Aspect(format="Instantaneous  ", base_difficulty=9, count=1),
        casting_time=Aspect(format="2 rounds ", base_difficulty=-5, count=1),
        name="Corpse Fog *",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Air", base_difficulty=0, count=1),
            "Difficulty": Aspect(
                format="32", base_difficulty=0, count=1
            ),  # should be 31
            "Area Effect": Aspect(
                format="10-meter radius", base_difficulty=20, count=1
            ),
            "Components": Aspect(
                format="Earth from a graveyard (rare)", base_difficulty=-4, count=1
            ),
            "Gestures": Aspect(
                format="Fanning of hands (simple)", base_difficulty=-2, count=1
            ),
            "Variable Movement": Aspect(
                format="Movement of 5 meters per round", base_difficulty=1, count=1
            ),
        },
        other_conditions=[
            Aspect(
                format="While this spell does not require the caster to be standing in a graveyard, it must be a location where the living have fallen and are now beneath the surface. Such areas can be ancient cities, battlefields, potters fields, disaster sites, etc.",
                base_difficulty=-4,
                count=1,
            ),
        ],
        notes="When commencing this spell, the caster must toss the earth\nfrom a graveyard into the air, followed by the prescribed\nhand motions. For this spell to work properly, the caster\nmust be on ground where dead are buried. It is the decaying\nfoulness of the dead that the caster pulls from the earth\nto obscure the surrounding area, creating a dense fog that\nhangs in the air.\nDead Man’s Gaze",
        skill="Conjuration",
    ),
    Cantrip(
        effect=Aspect(format="5 seconds", base_difficulty=4, count=1),
        duration=Aspect(format="1 round ", base_difficulty=4, count=1),
        range=Aspect(format="5 meters ", base_difficulty=4, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=4, count=1),
        casting_time=Aspect(format="2 rounds ", base_difficulty=-5, count=1),
        name="Dead Man's Gaze",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Death", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="3", base_difficulty=0, count=1),
            "Components": Aspect(
                format="2 copper coins (very common)", base_difficulty=-2, count=1
            ),
            "Gestures": Aspect(
                format="Place coins on eyes of the deceased (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Incantations": Aspect(
                format="“What do I see with your eyes?” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes="(Cantrip) If the last moments of a dead man’s life are frozen on his\nretinas, then this spell can reveal them. Once the coins are in\nplace and the spell successfully completed,the caster can try\nto gain information. First the coins are removed, and then\nthe deceased’s eyes gazed upon. The gamemaster determines\nthe result points needed from casting the spell, basing it\nupon how traumatic the final moments were. For example,\nif a character was brutally murdered, then it could require\nup to four points to see the killer’s face, but probably nine\nto 12to discern background details. The reason for this is\ndue to the fact that the victim likely spent his last moments\nof existence fixed upon the murder’s countenance. The spell\nreveals nothing other than the last few seconds of life.",
        skill="Divination",
    ),
    Spell(
        effect=Aspect(format="search skill of 2D", base_difficulty=6, count=1),
        duration=Aspect(format="5 minutes ", base_difficulty=12, count=1),
        range=Aspect(format="100 meters ", base_difficulty=10, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=10, count=1),
        casting_time=Aspect(format="2 rounds ", base_difficulty=-5, count=1),
        name="Dead Sight *",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="14", base_difficulty=0, count=1),
            "Components": Aspect(
                format="2 eyes of a recently killed creature — of the type the spells is targeted on (very rare)",
                base_difficulty=-5,
                count=1,
            ),
            "Concentration": Aspect(
                format="Others can be present when the caster is viewing with this spell, but there is a chance that interacting with the caster will cause a failure; willpower/ mettle roll at 8 once for each interaction to disrupt is required — use.",
                base_difficulty=-2,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=3, count=1),
            "Incantations": Aspect(
                format="“And the dead shall see.” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes="The caster gains the sight of the undead target. While the\ntarget’s movement cannot be controlled without another\nmagic, the eyes of the target become the eyes of the caster,\nreplacing the all-normal vision until the spell is ended or\ndisrupted. During the spells operation, the caster relies upon\nthe 2D search of the undead target, and dark and alien world.\nUntested casters must take a mettle test the first few times\nthis spell is used. Once practiced enough, the morbid nature\nof the “dead vision” no longer disturbs the viewer. How many\ntimes this takes is dependent upon the nature of what is\nbeing seen, and left to the gamemaster’s discretion. Until the\ncaster has become accustomed to this level of morbidity, a\nwillpower/mettle roll should be made after a successful casting\nof the spell. Failure results in the immediately halting the\nmagic, and a visibly shaken mage for several minutes. The\nspell can be ended at any time.",
        skill="Divination",
    ),
    Spell(
        effect=Aspect(
            format="4D languages/speaking, 4D intimidation,  4D investigation",
            base_difficulty=48,
            count=1,
        ),
        duration=Aspect(format="24 hours ", base_difficulty=18, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        name="Deadspeak",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Death", base_difficulty=0, count=1),
            "Difficulty": Aspect(
                format="28", base_difficulty=0, count=1
            ),  # should be 27
            "Components": Aspect(
                format="Dried flesh, writing device, human blood (uncommon)",
                base_difficulty=-8,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=13, count=1),
            "Gestures": Aspect(
                format="Write incantation upon the dried flesh (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="Arcane phrase (phrase)", base_difficulty=-1, count=1
            ),
        },
        other_conditions=[
            Aspect(
                format="Requires a dead body that at least has the skull intact — flesh is not required.",
                base_difficulty=-2,
                count=1,
            ),
        ],
        notes="Once the components of this spell have been used, they are\nuseless for future casting of the spell. New materials must\nbe acquired. But casting this spell grants many benefits. The\ndead have much to say, particularly those who have been\nrecently murdered. As in life, there is an art to interrogat -\ning the unliving; sometimes guile must be used, other times\nforce is required. The approach needed is determined by the\ngamemaster and the situation. The target of the spell gains\n4D in the language of the dead, as well as the skill necessary\nto investigate and intimidate an pulse-less subject. All difficulty\nlevels, whether they are opposed rolls or predetermined are\nset by the gamemaster.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="5D", base_difficulty=23, count=1),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="5 meters ", base_difficulty=10, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=10, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Dead Things",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Death", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="25", base_difficulty=0, count=1),
            "Components": Aspect(
                format="various body parts and extremities (very rare)",
                base_difficulty=-4,
                count=1,
            ),
            "Feedback": Aspect(
                format="-2 to damage resistance total", base_difficulty=-2, count=1
            ),
            "Focused": Aspect(format="On each extremity", base_difficulty=6, count=1),
            "Incantations": Aspect(
                format="“Live! I give you life!” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
            "Multi-Target": Aspect(
                format="1 extremity (cumulative +3 to the Difficulty Number for each additional extremity)",
                base_difficulty=3,
                count=1,
            ),
        },
        notes="The mage can give life to various severed extremities in a\n10 meter radius by sacrificing a part of her life energy. Once\ncast, any once living extremity in the area of effect comes\nto life, crawling, wiggling, scampering or rolling toward any\nliving enemy the caster indicates. Typically this spell is used\nupon hands, legs, fingers, heads, anything that can cause\ndamage. The amount of damage from a claw, bite or scratch\nis determined by the number of points assigned to it.\nTo determine how man dead things come to life, the caster\nassigns up to a total of 5D points to each by rolling. 1 point\nis required for an extremity to move and attack. Likewise, it\ncan suffer only 1 point of damage before being destroyed. This\nmeans if the caster rolls 12, then 2 points can be assigned\nto all potential targets within the spell’s area of effect. In\nthis case, 6 various body parts begin to move and engage in\ncombat. The points can be divided unequally. Regardless of\nhow high the dice rolls, an entire body cannot be animated\n— only extremities. The dead things can be merely bone or\nhave flesh and muscle, it makes no difference. It is the life\nenergy of the caster that gives them life.\n\n",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="10D damage", base_difficulty=30, count=1),
        duration=Aspect(format="1 round ", base_difficulty=4, count=1),
        range=Aspect(format="5 meters ", base_difficulty=4, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=4, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Death’s Hand",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Death", base_difficulty=0, count=1),
            "Difficulty": Aspect(
                format="17", base_difficulty=0, count=1
            ),  # Should be 19
            "Components": Aspect(
                format="skeletal hand (rare)", base_difficulty=-4, count=1
            ),
            "Focused": Aspect(format="On Target", base_difficulty=6, count=1),
            "Gestures": Aspect(
                format="point skeletal hand at target (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Grasp the heart of my enemy.” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes="This spell is of the darkest arts, calling upon the evil powers\nto consume the vital energy of a target’s heart, halting its\nbeating, bringing death. The proper component is needed for\nthe type of a target. To use this spell on a human requires a\nskeletal human hand; to target a specific monster requires\nthe hand (or claw) of the type of targeted monster.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="-2D from Physique attribute", base_difficulty=9, count=1),
        duration=Aspect(format="5 rounds ", base_difficulty=6, count=1),
        range=Aspect(format="3 meters ", base_difficulty=4, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=4, count=1),
        casting_time=Aspect(format="1.5 seconds ", base_difficulty=-1, count=1),
        name="Drain Essence",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Enchanted", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="12", base_difficulty=0, count=1),
            "Focused": Aspect(format="On target", base_difficulty=3, count=1),
            "Gestures": Aspect(format="Point (simple)", base_difficulty=-1, count=1),
            "Incantations": Aspect(
                format="“Wither.” (phrase)", base_difficulty=-1, count=1
            ),
        },
        notes="When the caster utters the incantation, dark arcs of energy\nflash around the target, reducing Physique by -2D. Normal\narmor doesn’t protect against this spell, as the target’s essence\nis pulled from the body through the material. Magical protec-\ntion does hinder the spell, reducing damage as normal. The\nvictim remains in this state for the duration of this spell,\nand the caster does not gain the extracted energy. After the\nspell is disrupted or ends, the target’s Physique returns to\nnormal.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(format="10D disease", base_difficulty=45, count=1),
        duration=Aspect(format="1 year ", base_difficulty=38, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 month ", base_difficulty=-32, count=1),
        name="Duncan’s Malicious Contagion",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Death", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="32", base_difficulty=0, count=1),
            "Components": Aspect(
                format="rotting rodent or other vermin (common)",
                base_difficulty=-3,
                count=1,
            ),
            "Focused": Aspect(format="On Target", base_difficulty=16, count=1),
            "Gestures": Aspect(
                format="Prick thumb with despoiled vermin blood (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Incantations": Aspect(
                format="“By the pricking of my thumb, a malicious contagion this way comes.” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
            "Other Alterants": Aspect(
                format="While the caster is immune to the contagion she has created, she is a vector. All who come in contact must roll Physique at Easy, otherwise they become infected with the illness.",
                base_difficulty=3,
                count=1,
            ),
        },
        notes="Few know this diabolical spell, as those who have learned of\nits existence either promptly destroyed, or used it and were\ndiscovered and in turn were killed by a rampaging populous\nsick with a magical plague. The gamemaster should make\nlearning or finding this spell very difficult and the ramifica-\ntions well known to the caster. It is reasoned that the spell\nwas developed in time of war, a weapon of siege. Others\nventured that the spell served the revenge of its namesake.\nThe truth may never be known. Nonetheless, its effects can\nbe devastating.\nOnce successfully cast, the mage is immune to the conta-\ngion. Still, she is free to roam around a populated area, and\nall who come into physical contact must make a Physique roll\nof Easy. Failure means the person suffers 1D bleeding sores\nwithin 24 hours. Each day these sores spread, increasing by\nanother +1D, eventually covering the entire body in suppu-\nrating wounds to a maximum of 10D wounds; if a character\nsurvives this, then she has survived the sickness. Likewise,\nany person who comes into contact with this infected person\nmust make a Physique/Strength roll at Easy, otherwise suf -\nfer the same fate. Attempts to use medicine/healing produce\ncontact. If the infected are not promptly segregated, then all\nwho around them run the risk of contracting the contagion.\nThis magical malady can only be conveyed by living beings,\nhuman or animal. After 1 year from the day of the casting,\nthe spell halts, regardless of the number of ill. The disease\nstops spreading and promptly heats at a normal rate, vanish-\ning almost as quickly as it appeared.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="charm undead skill bonus at +5D+2", base_difficulty=26, count=1
        ),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Enthrall Undead",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Enchanted", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="18", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Raw flesh (rare)", base_difficulty=-4, count=1
            ),
            "Focused": Aspect(format="On target", base_difficulty=8, count=1),
            "Gestures": Aspect(
                format="Snap fingers while tossing the component on the ground before the target (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Unreal Effect": Aspect(
                format="Disbelief difficulty of 13", base_difficulty=-6, count=1
            ),
        },
        notes="Often it is simpler for a magic user practiced in Necromancy\nto befriend undead, rather than destroy them. This spell\npermits one or more undead to be enthralled, falling under\nthe control of the caster. During this period, the targets\nfollow all instructions given — they naturally understand\nthe character who cast the spell. Mindless creatures such as\nskeletons and zombies can be ordered to destroy themselves\nor each other. But undead with limited cognitive capabilities\nsuch as mummies and vampires are allowed a Very Difficult\nwillpower/mettle roll. A failure results in unquestioning obedi-\nence. A success causes them to ignore the command.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(format="4D+2 armor", base_difficulty=14, count=1),
        duration=Aspect(format="1 day ", base_difficulty=25, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1minute ", base_difficulty=-9, count=1),
        name="Fleshy Armor",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Death", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="15", base_difficulty=0, count=1),
            "Components": Aspect(
                format="The flesh of a dead creature (very rare)",
                base_difficulty=-4,
                count=1,
            ),
            "Concentration": Aspect(
                format="Because of the power of the incantation used, the caster must be alone and uninterrupted for the duration of the casting. No living being, other than the caster, can be within 5 meters.",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="A phrase that animates dead flesh, known only to those who study Death (sentence)",
                base_difficulty=-2,
                count=1,
            ),
            "Focused": Aspect(format="On self", base_difficulty=7, count=1),
        },
        notes="No armor can be worn for this spell to function properly.\nAs the casting commences, the dead flesh appears to meld\ntogether, and crawl across the caster’s body, becoming a sec-\nond layer of skin. As this flesh is dead, it provides protection\nfrom physical attacks. When the spell reaches the end of its\nduration, the dead flesh becomes rank. By the last 30 minutes\nof the spell, the dead flesh is putrid, suppurating nauseating\nfluid. This atrocious odor acts as a warning for the wearer,\nallowing her to know the spell is about to end. It also hinders\nthe protected person’s sense of smell (-1D Perception).\n\n",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(format="Paralyzing Touch (4)", base_difficulty=12, count=1),
        duration=Aspect(format="24 hours ", base_difficulty=18, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Ghoulish Paralysis",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Death", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="12", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Claws of a ghoul (extremely rare)", base_difficulty=-7, count=1
            ),
            "Focused": Aspect(format="On Target", base_difficulty=6, count=1),
            "Incantations": Aspect(
                format="“Ghoul’s touch” (sentence)", base_difficulty=-2, count=1
            ),
        },
        notes="A successful casting of this spell imbues the mage with the\nAdvantage Paralyzing Touch (4) as described in the “Character\nOptions” chapter. Before the victim of an attack can become\nparalyzed, the mage must make find an unprotected location\nthat reveals flesh. The gamemaster might require a Perception\nor a search roll at an appropriate difficulty to find such a spot\nif one is readily evident.\n\n",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(format="human size", base_difficulty=10, count=1),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="Touch ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Ghost Passage",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Dimension", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="13", base_difficulty=0, count=1),
            "Focused": Aspect(format="On target", base_difficulty=5, count=1),
            "Gestures": Aspect(
                format="Touch target upon forehead (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Unreal Effect": Aspect(
                format="Disbelief difficulty of 13", base_difficulty=-3, count=1
            ),
        },
        notes="After this spell is invoked, the target becomes ethereal, as does\nher belongings. This allows her to move without a sound, at\nnormal movement. However, the movement is otherworldly\nin that she appears to glide. Those who do not know she is\nunder the effect of a spell are likely to mistake her for a ghost\nor spirit. Such characters need to make a Charisma/Presence\nroll, or a willpower/mettle roll with a Difficulty of 13. The\nunfortunates who mistake the target as an unearthly entity\nflee until they no longer see the apparent apparition.\nAdditionally, this spell allows a hero to pass through physical\nbarriers up to 0.5 meters thick. For the duration of the spell,\nthe target is unable to talk or physically interact with the\nenvironment, as she no longer possesses a corporeal from.\nThis limitation extends to hearing, as well. Unless the recipi-\nent of the spell is contacted through magical, telepathic or\nsupernatural means, the only form of communication allows\nis through gestures.",
        skill="Apportation",
    ),
    Spell(
        effect=Aspect(format="3D+1 protection", base_difficulty=10, count=1),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Hallowed Ground",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Entity", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="14", base_difficulty=0, count=1),
            "Area Effect": Aspect(format="5-meter radius", base_difficulty=10, count=1),
            "Components": Aspect(
                format="Tooth of an undead being (very rare)",
                base_difficulty=-5,
                count=1,
            ),
            "Gestures": Aspect(
                format="Turn a complete circle with tooth extended in hand (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes="This ritual prohibits entry of undead within the Area Effect\nprescribed. They may amble about, circling the protected\nground, but they are unable to pass across the faint white\nbarrier the magic user erects. While all those within the spell’s\nzone of safety can cast spells and fire missiles at any nearby\nundead without voiding the spells, non-living creatures\noutside the area are unable to do the same.\n\n",
        skill="Apportation",
    ),
    Spell(
        effect=Aspect(format="12D creation", base_difficulty=36, count=1),
        duration=Aspect(format="3 rounds ", base_difficulty=15, count=1),
        range=Aspect(format="100 meters ", base_difficulty=10, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=10, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Monstrous Creation",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Entity", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="33", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Victim who has consumed a Conqueror Worm (rare)",
                base_difficulty=-4,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=10, count=1),
            "Gestures": Aspect(
                format="Point at target (simple)", base_difficulty=-1, count=1
            ),
            "Incantations": Aspect(
                format="“There is something dangerous in you, that wisdom should fear!” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="This spell requires that the target consume a worm transformed by the spell Conqueror Worm.",
                base_difficulty=-5,
                count=1,
            ),
        ],
        notes="Only if this preparation has been performed, then is it pos-\nsible for the spell to function properly. (elaborate)\nWith the gesture and the utterance of the commanding phrase,\nthe Conqueror Worm begins to consume its host at an alarm-\ning rate. In 3 rounds, a human size body can be consumed\nand transformed into a wretched creature that resembles\nthe host only in gross form. As this process kills the host,\nit is a painful process, usually resulting in the writhing and\nscreaming of the victim. If the character is killed before the\ntransformation is complete, the spell is halted.\nIf the process is completed, then the abomination that\nexists is a fleshless, clawed creature (+2D+1 damage) that\nfollows the magic user’s every command. Its basic attributes\nare identical to those of its host, but it can only use its claws to\nattack — it is mindless. However, its Body Points are replaced\nwith a roll of 6D (or it starts with no wounds). Once the foul\nmonstrosity dies, it cannot be brought back to life without\nrepeated the entire process. As a result, magic users often\nhave a few Conqueror Worms nestled inside companions,\njust for emergencies.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(format="6D", base_difficulty=18, count=1),
        duration=Aspect(format="1 second ", base_difficulty=0, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="2.5 seconds ", base_difficulty=2, count=1),
        name="Mortal Blast *",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Entity", base_difficulty=0, count=1),
            "Difficulty": Aspect(
                format="13", base_difficulty=0, count=1
            ),  # Should be 11
            "Components": Aspect(
                format="Crushed pearl and bone dust (rare)", base_difficulty=-4, count=1
            ),
            "Feedback": Aspect(
                format="-3 to damage resistance total", base_difficulty=-3, count=1
            ),
            "Focused": Aspect(format="On target", base_difficulty=3, count=1),
            "Gestures": Aspect(
                format="Point at target (simple)", base_difficulty=-1, count=1
            ),
        },
        notes="A sudden burst of white energy streaks from the caster’s finger\ntoward the undead target, resulting is a brilliant flash of light.\nUpon contact the ball of energy radiates outward, extending\ntoward the earth and any other nearby objects, discharging\nthe negative energy that maintains the un-life of the living\ndead target. All undead, not demons or other types of extra-\ndimensional creatures, suffer 6D damage from the attack. As\ncasting this spell requires the magic user to use her own life\nforce, she receives a -3 to her damage resistance total.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(format="+5D to alteration skill", base_difficulty=23, count=1),
        duration=Aspect(format="5 minutes ", base_difficulty=10, count=1),
        range=Aspect(format="Touch ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Necromantic Sigil",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="13", base_difficulty=0, count=1),
            "Concentration": Aspect(
                format="1 round of meditation; willpower/mettle roll at 13",
                base_difficulty=-7,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=6, count=1),
            "Gestures": Aspect(
                format="Mark necromantic sigil in air before target (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Be protected from the magic of Death.” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes="Any target bearing this necromantic sigil is protected\nagainst all magic of necromancy. Unlike countermagic or a\nWard, this spell is in operation once successfully cast and\nhas a duration. From that point, any other Necromancy spells\nmust have a skill total equal to or greater than the target’s\nroll with the bonus modifier gained from this spell. If the\nattacking spell total is lower, then it is negated. This defense\ncontinues until the duration of the spell is satisfied.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(format="3D", base_difficulty=9, count=1),
        duration=Aspect(format="24 hours ", base_difficulty=18, count=1),
        range=Aspect(format="Touch ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Necrosis",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Death", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="14", base_difficulty=0, count=1),
            "Focused": Aspect(format="On target", base_difficulty=5, count=1),
            "Incantations": Aspect(
                format="“Death” (phrase)", base_difficulty=-1, count=1
            ),
        },
        notes="With a simple touch, the caster can cause 3D damage to a\ntarget. The target’s passive defense is used if the attack is\nunsuspected. If it is anticipated, normal combat rules are\nused.\nBy becoming a pathway for negative life energy, the magic\nuser is able to send negative life energy into the victim. The\ntouched area first becomes pale, as though drained of blood,\nthen it turns blue, eventually becoming black as though\ngangrenous. The effect isn’t permanent; it heals naturally.\nAdditionally, the caster gains no bonuses from using the\nspell. It is an offensive magic known by many who study the\nschool of Necromancy.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(format="Age 3 years", base_difficulty=114, count=1),
        duration=Aspect(format="1.5 seconds ", base_difficulty=1, count=1),
        range=Aspect(format="5 meters ", base_difficulty=4, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=4, count=1),
        casting_time=Aspect(format="3 rounds ", base_difficulty=-6, count=1),
        name="Passing of Years",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Death", base_difficulty=0, count=1),
            "Difficulty": Aspect(
                format="42", base_difficulty=0, count=1
            ),  # Should be 45
            "Components": Aspect(
                format="1 gram of dust from the remains of a living being that has decayed naturally (extremely rare)",
                base_difficulty=-14,
                count=1,
            ),
            "Concentration": Aspect(
                format="Requires 2 rounds of concentration; willpower/mettle roll of 9.",
                base_difficulty=-3,
                count=1,
            ),
            "Gestures": Aspect(
                format="Sifting the dust between fingers (com - plex)",
                base_difficulty=-3,
                count=1,
            ),
            "Incantations": Aspect(
                format="Repeated litany of archaic language learned with the spell; requires artist difficulty 19. Loudly (sentence)",
                base_difficulty=-7,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(format="Only works on living targets", base_difficulty=-1, count=1),
        ],
        notes="When casting this wretched spell, the mage is able to drain\naway the life of a target. The spell requires the caster to obtain\nthe naturally decayed remains of a once living creature. Then,\nwhile uttering the incantation, 1 gram of dust is ground\nbetween the fingers, letting it fall freely. As this happens, a\nblack sphere is formed before the mage. This process takes 2\nrounds. On the third round, the sphere can be grasped by the\none who cast the spell, and thrown at the target. A successful\nmarksmanship/firearms or apportation roll is required. If suc-\ncessful, then 3 years of life is drained from the victim’s body.\nThe living energy is not transferred to the mage, it is merely\nsiphoned away, aging the hapless enemy of the caster. With\neach casting the dust that forms the deadly black sphere is\nconsumed in the process.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="3D in damage from inhaling", base_difficulty=9, count=1),
        duration=Aspect(format="3 rounds ", base_difficulty=7, count=1),
        range=Aspect(format="100 meters ", base_difficulty=10, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=10, count=1),
        casting_time=Aspect(format="2 rounds ", base_difficulty=-6, count=1),
        name="Plague Wind *",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Air", base_difficulty=0, count=1),
            "Difficulty": Aspect(
                format="38", base_difficulty=0, count=1
            ),  # Should be 37
            "Area Effect": Aspect(
                format="10-meter sphere", base_difficulty=50, count=1
            ),
            "Components": Aspect(
                format="Ash from a human corpse (rare)", base_difficulty=-4, count=1
            ),
            "Gestures": Aspect(
                format="Blow ash from hand (complex)", base_difficulty=-2, count=1
            ),
            "Incantations": Aspect(
                format="“Let dire winds blow.” (sentence)", base_difficulty=-2, count=1
            ),
            "Variable Movement": Aspect(
                format="Movement of 5 meters per round", base_difficulty=1, count=1
            ),
        },
        notes="A skilled caster can send this poisonous breeze directly toward\nan enemy. For those who are not otherwise engaged, it is\npossible to see a gray pall of dust moving in the direction\nthe caster desires. If seen, and far enough away, an attempt\nto dodge the dangerous pall can be made. All who inhale its\nfetid air suffer 3D damage.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="Possession: Full (R1)", base_difficulty=30, count=1),
        duration=Aspect(format="1 day ", base_difficulty=25, count=1),
        range=Aspect(format="100 meters ", base_difficulty=10, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=10, count=1),
        casting_time=Aspect(format="1 hour ", base_difficulty=-18, count=1),
        name="Possess the Unliving",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Death, enchanted", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(
                format="30", base_difficulty=0, count=1
            ),  # Should be 28
            "Components": Aspect(
                format="Personal possession or a part of the body of target (uncommon); charcoal (very common)",
                base_difficulty=-6,
                count=1,
            ),
            "Focused": Aspect(
                format="Mage’s mind stays with target", base_difficulty=11, count=1
            ),
            "Gestures": Aspect(
                format="Draw circles and sigils of possession  (complex; artist roll with difficulty of 11)",
                base_difficulty=-3,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Enter the husk and become its mind.” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(format="Target must be unburied", base_difficulty=-1, count=1),
        ],
        notes="By casting this spell, the mage can possess an unliving\ncorpse. She retains her mental attributes, but she takes on\nthe physical attributes of that the corpse formerly possessed\n(possibly reduced, depending on the freshness of the corpse).\nAs there is no mind, she gains no knowledge about the corpse,\nthough she’s in complete control of the body.\nOf course there is always a risk if a mage animates an\ncorpse. Any who see such a thing naturally mistake it for a\nzombie and are likely to attack.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="+8D to various non-Extranormal attributes",
            base_difficulty=36,
            count=1,
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="Touch ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="2 rounds ", base_difficulty=-5, count=1),
        name="Preternaturality",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Enchanted", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="20", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Fresh blood from a sacrifice (rare)",
                base_difficulty=-4,
                count=1,
            ),
            "Focused": Aspect(format="On Target", base_difficulty=9, count=1),
            "Gestures": Aspect(
                format="Mark each part of the body to be enhanced with blood (complex)",
                base_difficulty=-3,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Be anointed with the life’s energy of another.” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes="By using the fresh blood of a similar sacrifice, the target\ngains a bonus to each attribute the caster chooses. The\ncaster must rub the blood on the part of the body to gain\nthe attribute increase. No single attribute can be increased\nby more than +3D.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(format="4D", base_difficulty=12, count=1),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="Touch ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Putrescence",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Death", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="13", base_difficulty=0, count=1),
            "Components": Aspect(
                format="venom from a poisonous creature (rare)",
                base_difficulty=-4,
                count=1,
            ),
            "Feedback": Aspect(
                format="-1 to damage resistance total", base_difficulty=-1, count=1
            ),
            "Focused": Aspect(format="On target", base_difficulty=6, count=1),
            "Incantations": Aspect(
                format="“Imbue with the foulness of Death” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes="In an instant this spell can transforms liquids or consum -\nable solids of any sort into poison that causes 4D damage\neach round for the duration of the spell if the victim is not\ntreated by natural or magical means. The damage commences\nimmediately after ingesting the altered item. A Difficult\nstamina roll is required to naturally overcome the effect. All\nthat needs to be done is for the caster to touch the drink or\nfood for it to be tainted. A Perception roll of Very Difficult is\nrequired to detect the toxin through smell or taste.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="medicine/healing of 6D", base_difficulty=18, count=1),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="Touch ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="2 rounds ", base_difficulty=-5, count=1),
        name="Regeneration",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Death", base_difficulty=0, count=1),
            "Difficulty": Aspect(
                format="17", base_difficulty=0, count=1
            ),  # Should be 16
            "Components": Aspect(
                format="Fresh blood from the specific creature on which the spell is to be cast (uncommon)",
                base_difficulty=-4,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=7, count=1),
            "Gestures": Aspect(
                format="Mark sigil on forehead with blood (comoplex; artist roll with difficulty of 11)",
                base_difficulty=-3,
                count=1,
            ),
        },
        notes="A mage can fend off the approaching death of a hero by suc-\ncessfully casting this spell. But with healing comes pain. In\norder for the spell to work, fresh blood must be drawn from\nthe intended target. This requires a medicine/healing roll at\nModerate difficulty. This also causes 1D damage if the roll\nwas a success. A failure results in 2D damage. A 1 on the Wild\nDie can produce catastrophic bleeding if the gamemaster\ndesires — meddling in dark magics has a price.\nOnce the blood is extracted and the spell is successfully cast,\nthen the target regenerates damage automatically at a with a\n6D medicine/healing skill level. This requires no action on the\ncharacters part. It occurs once every minute for the duration\nof the spell. And its effects are visible noticeable to those take\nthe time to look for them. Another telltale sign is the bloodly\nsigil that must remain in place on the target’s forehead. As\nit is magical in nature, sweat or splashed water or rain will\nnot remove it. However, it can be rubbed away if the target\ndoes so intentionally. Doing this ends the spell.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="+3D+1 damage, 3D+1 intimidation", base_difficulty=25, count=1
        ),
        duration=Aspect(format="3 rounds ", base_difficulty=6, count=1),
        range=Aspect(format="5 meters ", base_difficulty=4, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=4, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Sanguineous Attack",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Death", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="18", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Drop of blood (ordinary)", base_difficulty=-2, count=1
            ),
            "Focused": Aspect(format="On weapon", base_difficulty=4, count=1),
            "Gestures": Aspect(
                format="Flick drop of blood toward living target (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes="By simply pricking her thumb, the caster can cause any\nweapon to gain +3D+1 damage. Such items can be swords,\nknifes, bullets, clubs, anything physical that makes physical\ncontact with a living creature. If the spell is cast on an item that\nsuccessfully causes damage to a target, the effect manifests\nitself as unusually heavy bleeding. Excessive bleeding can be\nalarming, often causing panic. Characters suffering a wound\nfrom this spell must also suffer a 3D+1 intimidation roll.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="3D Perception of Would Level", base_difficulty=14, count=1
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Sense Death",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Death", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="15", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Bloodied cloth (ordinary)", base_difficulty=-1, count=1
            ),
            "Focused": Aspect(format="On target", base_difficulty=4, count=1),
            "Gestures": Aspect(
                format="Close eyes (simple)", base_difficulty=-1, count=1
            ),
        },
        other_conditions=[
            Aspect(
                format="Must make a search roll to see the target; all normal modifiers apply.",
                base_difficulty=-1,
                count=1,
            ),
        ],
        notes="Casting this spell attunes the magic use with the life force of\nthe target, providing 3D Perception roll to determine a target’s\nWound Level. There are no other effects imbued, other than\ndetermining the amount of life remaining in a character.",
        skill="Divination",
    ),
    Spell(
        effect=Aspect(
            format="8D search when attempting to locate spirits or ghosts",
            base_difficulty=24,
            count=1,
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        name="Sense Spirit",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Entity", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="24", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="10 meters radius", base_difficulty=20, count=1
            ),
            "Focused": Aspect(format="On caster", base_difficulty=6, count=1),
            "Incantations": Aspect(
                format="Reveal yourself (sentence)", base_difficulty=-2, count=1
            ),
        },
        notes="Once this spell is cast, the mage can see all undead spirits\nand ghosts within a 10-meter radius. Likewise, the atten -\ntion of any such incorporeal being is drawn to the character\nwho uttered the incantation, as the spell forces the entities\nto reveal themselves to the caster, and only the caster. The\nsearch roll is needed as the spirits are being commanded to\nreveal themselves.",
        skill="Divination",
    ),
    Spell(
        effect=Aspect(format="+2D+1", base_difficulty=11, count=1),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="Touch ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1round ", base_difficulty=-4, count=1),
        name="Unliving Weapon",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Enchanted", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="12", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Weapon of good quality (common)", base_difficulty=-3, count=1
            ),
            "Feedback": Aspect(
                format="-1 to damage resistance total", base_difficulty=-1, count=1
            ),
            "Focused": Aspect(format="On weapon", base_difficulty=5, count=1),
            "Gestures": Aspect(
                format="Run fingers across weapon (simple)", base_difficulty=-2, count=1
            ),
        },
        notes="A weapon upon which this spell is cast is imbued with a nega-\ntive field of energy. A deep red hue radiates from the weapon\nso long as the spell endures. All attacks against living beings\ngain a +2D+1 bonus to the weapon’s normal damage. With\neach successful strike, the aura radiating from the weapon\nspreads across the opponent’s form as life force is drained\naway. No additional damage is conveyed when combating\nundead entities.\n\n",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="10D Body Points", base_difficulty=30, count=1),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="100 meters ", base_difficulty=10, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=10, count=1),
        casting_time=Aspect(format="2 rounds ", base_difficulty=-5, count=1),
        name="Wake the Dead",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Death", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="27", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="10-meter radius", base_difficulty=20, count=1
            ),
            "Components": Aspect(
                format="Skull (uncommon)", base_difficulty=-4, count=1
            ),
            "Concentration": Aspect(
                format="1 round of focused thought upon the dead; willpower/mettle roll at 16",
                base_difficulty=-10,
                count=1,
            ),
            "Gestures": Aspect(
                format="Lifting hand upward (simple)", base_difficulty=-1, count=1
            ),
            "Incantations": Aspect(
                format="“Awaken and walk!” loudly (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="The spell can only be cast in an area where dead exist beneath the earth, such as a graveyard,",
                base_difficulty=-3,
                count=1,
            ),
        ],
        notes="battlefield, or some other such place.\nBy calling upon the arcane knowledge of Death and Necro-\nmancy, the mage is able to wake the dead in a 10-meter radius\nwithin 100 meters. Bones form into skeletons, and recently\nburied corpse become zombies. The total number of dead is\ndetermined by the rolling of the 10D Body Points dice. Each\ncreature is awarded 1 Wound Level or 6 Body Points This means\nif a total of 24 was roll on the dice, then only 4 undead are\ncalled from the earth. The number is rounded down, making\nthe maximum always 6 undead. This spell only brings forth\nskeletons and zombies, no other type of undead creatures.\nThey are likely to have the attributes of the average living\ncreature for the location, as well as possess any clothing or\nweapons that might normally be buried with them.\nEven though the mage is the one who has summoned\nthe dead from their repose, there is no kinship felt toward\nher. Rather, all undead called from their graves attack any\nliving creature within the 10-meter radius the spell’s effect,\nincluding the mage and any associates. Returning from death\nis unpleasant and instills hatred and jealous of the living.\nThese awakened creatures show no mercy when disposing\nof those who live.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="3D6 damage", base_difficulty=18, count=1),
        duration=Aspect(format="3.5 seconds ", base_difficulty=3, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="1.5 seconds ", base_difficulty=-1, count=1),
        name="Withering Blast",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Death", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="14", base_difficulty=0, count=1),
            "Gestures": Aspect(
                format="Makes a thrusting motion with hand (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Devour!” loudly (phrase)", base_difficulty=-1, count=1
            ),
        },
        notes="By calling upon negative energy of life, the mage is able\nto hurl a blast of withering power that consumes the life\nof a target. During the round the spell is cast, a successful\nmarksmanship/firearms or apportation roll is required to hit\nthe target. Nonmagical armor offers no protection from this\ndeath magic. Any character Mortally Wounded by the spell\nloses ages 1 year from the effect. This stolen year, or any\nnumber of years taken by this spell, can only be returned\nby magical means.",
        skill="Conjuration",
    ),
]

if __name__ == "__main__":
    detail(spells)

__test__ = {
    "Animate Dead": ">>> spells[0].difficulty\n14",
    "Animate Superior Undead": ">>> spells[1].difficulty\n25",
    "Call Tomb Fiend": ">>> spells[2].difficulty\n26",
    "Capture Life force": ">>> spells[3].difficulty\n17",
    "Cold Flesh": ">>> spells[4].difficulty\n16",
    "Consuming Sphere": ">>> spells[5].difficulty\n30",
    "Conqueror Worm": ">>> spells[6].difficulty\n19",
    "Corpse Fog *": ">>> spells[7].difficulty\n31",
    "Cantrip": ">>> spells[8].difficulty\n3",
    "Dead Sight *": ">>> spells[9].difficulty\n14",
    "Deadspeak": ">>> spells[10].difficulty\n29",
    "Dead Things": ">>> spells[11].difficulty\n25",
    "Death’s Hand": ">>> spells[12].difficulty\n19",
    "Drain Essence": ">>> spells[13].difficulty\n12",
    "Duncan’s Malicious Contagion": ">>> spells[14].difficulty\n32",
    "Enthrall Undead": ">>> spells[15].difficulty\n18",
    "Fleshy Armor": ">>> spells[16].difficulty\n15",
    "Ghoulish Paralysis": ">>> spells[17].difficulty\n12",
    "Ghost Passage": ">>> spells[18].difficulty\n13",
    "Hallowed Ground": ">>> spells[19].difficulty\n14",
    "Monstrous Creation": ">>> spells[20].difficulty\n33",
    "Mortal Blast *": ">>> spells[21].difficulty\n11",
    "Necromantic Sigil": ">>> spells[22].difficulty\n13",
    "Necrosis": ">>> spells[23].difficulty\n14",
    "Passing of Years": ">>> spells[24].difficulty\n45",
    "Plague Wind *": ">>> spells[25].difficulty\n37",
    "Possess the Unliving": ">>> spells[26].difficulty\n28",
    "Preternaturality": ">>> spells[27].difficulty\n20",
    "Putrescence": ">>> spells[28].difficulty\n13",
    "Regeneration": ">>> spells[29].difficulty\n16",
    "Sanguineous Attack": ">>> spells[30].difficulty\n18",
    "Sense Death": ">>> spells[31].difficulty\n15",
    "Sense Spirit": ">>> spells[32].difficulty\n24",
    "Unliving Weapon": ">>> spells[33].difficulty\n12",
    "Wake the Dead": ">>> spells[34].difficulty\n27",
    "Withering Blast": ">>> spells[35].difficulty\n14",
}
