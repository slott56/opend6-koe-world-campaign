"""
Peregrination
-------------

"""

from magic1 import Aspect, Spell, detail

spells = [
    Spell(
        effect=Aspect(format="moves up to 250 kilograms", base_difficulty=12, count=1),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        name="Alter Gravity",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Inanimate Forces", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="12", base_difficulty=0, count=1),
            "Focused": Aspect(format="On caster", base_difficulty=6, count=1),
            "Gestures": Aspect(
                format="Point up and then down (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Alter.” (phrase)", base_difficulty=-1, count=1
            ),
        },
        notes="With this spell, a magic user can walk on walls or ceilings\nby changing the direction of gravity for herself. Each time\nshe wishes to change direction, she merely needs to say,\n“Alter.”\n\n",
        skill="Apportation",
    ),
    Spell(
        effect=Aspect(
            format="+4D to willpower/mettle when bead used as planar homing beacon",
            base_difficulty=18,
            count=1,
        ),
        duration=Aspect(format="1 day ", base_difficulty=25, count=1),
        range=Aspect(format="Touch ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 hour ", base_difficulty=-18, count=1),
        name="Beacon",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Enchanted", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="13", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Glass bead (very common)", base_difficulty=-2, count=1
            ),
            "Concentration": Aspect(
                format="1 hour with willpower/mettle difficulty of 12",
                base_difficulty=-6,
                count=1,
            ),
            "Focused": Aspect(format="On glass bead", base_difficulty=8, count=1),
        },
        notes="This spell serves little purpose on its own, but when used\nin conjunction with the shift planes spell (or a similar spell),\nit gives the caster +4D to her willpower/mettle roll when\nattempting to return from another plane. The same magic\nuser must cast both spells, as the spells are attuned to her\nsenses.\nSo long as the glass bead  remains in the originating\ndimension, the bonus is granted to the caster. If the glass\nbead is destroyed or shifted to another plane, then all trace\nof it is lost.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="compared to roll of target’s willpower/mettle or governing attribute",
            base_difficulty=24,
            count=1,
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="10 kilometers ", base_difficulty=20, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=20, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Beckon Creature",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Animal, entity, folk", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="36", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Fur, feather, or tooth (ordinary)", base_difficulty=-1, count=1
            ),
            "Gestures": Aspect(
                format="Welcoming gestures (simple)", base_difficulty=-1, count=1
            ),
            "Incantations": Aspect(
                format="“Arrive.” (phrase)", base_difficulty=-1, count=1
            ),
            "Variable Movement": Aspect(
                format="Bending/unseen target", base_difficulty=5, count=1
            ),
        },
        notes="Any creature of the gamemaster’s choice, or randomly\ndetermined, can be called upon with this spell. The effect’s\nvalue plus the spell’s result point bonus is compared to a roll\nof the target’s willpower/mettle (or the governing attribute) to\nsee if the spell successfully latches on. If it does, the beckoned\nbeast arrives instantly — and, if the caster can convince it,\nto assist her in combat for the duration of the spell.",
        skill="Apportation",
    ),
    Spell(
        effect=Aspect(
            format="compare to spell total of dimension-hopping spell",
            base_difficulty=27,
            count=1,
        ),
        duration=Aspect(format="1 day ", base_difficulty=25, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="2.5 hours ", base_difficulty=-20, count=1),
        name="Bind Reality",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Dimension", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="35", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Sphere with radius of 10 meters", base_difficulty=50, count=1
            ),
            "Concentration": Aspect(
                format="1 hour with willpower/mettle difficulty of 12",
                base_difficulty=-6,
                count=1,
            ),
            "Gestures": Aspect(
                format="Make an encompassing gesture (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Other Alterant": Aspect(
                format="Sphere glows when triggered", base_difficulty=1, count=1
            ),
        },
        other_conditions=[
            Aspect(
                format="Difficult scholar roll to recall information about the protected dimension",
                base_difficulty=-5,
                count=1,
            ),
        ],
        notes="With this spell, a magic user can seal a 10-meter sphere,\npreventing the opening or portals going to or coming from\nother planes. Any caster or creature attempting to open a\ngateway or shift into the affected area of this spell must\novercome the value of this spell’s effect. Any unsuccessful\nattempt to get in or out warns the caster with a glow on the\nsphere. This spell is useful when trying to prevent a prisoner\nfrom escaping, or an unwanted entity from entering a given\nlocation.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="+1D difficulty modifier to physical and mental attributes",
            base_difficulty=36,
            count=1,
        ),
        duration=Aspect(format="5 minutes ", base_difficulty=13, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        name="Blur Barriers",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Dimension", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="33", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Sphere with radius of 4 meters", base_difficulty=20, count=1
            ),
            "Concentration": Aspect(
                format="1 minute with willpower/mettle difficulty of 9",
                base_difficulty=-3,
                count=1,
            ),
            "Gestures": Aspect(
                format="Wiggle fingers on one hand (simple)",
                base_difficulty=-1,
                count=1,
            ),
        },
        notes="For a short period of time, the magic user forms a nexus\nof dimensions. If successful, the caster weakens the barriers,\nresulting in nothing functioning as it normally does.The natu-\nral, physical laws of the occupied dimension become unstable.\nEveryone within the area of effect is subject to an increase in\nthe difficultiles of all physical and mental actions.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="4D languages/speaking in the language of the target entity; 49 compared to planar distance",
            base_difficulty=61,
            count=1,
        ),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        name="Contact Entity",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="entity, dimension", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(
                format="13", base_difficulty=0, count=1
            ),  # Should be 32
            "Concentration": Aspect(
                format="1 minute with willpower/mettle difficulty of 9",
                base_difficulty=-3,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="Must be knowledgeable of the entity to be contacted, which requires a scholar roll of 11",
                base_difficulty=-3,
                count=1,
            )
        ],
        notes="Provided that the caster has some knowledge of the entity\nor type of entity she wishes to contact, it’s possible to open a\nchannel to that being. If the spell is successful and the distance\nto the entity’s location has a planar value of 49 or less, the\ncaster gains 4D languages in the language of the target. This\nonly lasts for the duration of the spell.\nContacting a creature from another plane does not guar-\nantee that it is willing to communicate. Convincing it is left\nto the caster.",
        skill="Divination",
    ),
    Spell(
        effect=Aspect(
            format="Hindrance: Low Gravity (R5), +5 to acrobatics, brawling/fighting, and melee combat difficulties; Skill Bonus: Low Gravity (R5), +5 to lifting/lift, running,  and throwing totals",
            base_difficulty=30,
            count=1,
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="15 meters ", base_difficulty=6, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=6, count=1),
        casting_time=Aspect(format="2 rounds ", base_difficulty=-5, count=1),
        name="Decrease Gravity",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="inanimate forces", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="34", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Sphere with radius of 5 meters", base_difficulty=25, count=1
            ),
            "Concentration": Aspect(
                format="2 rounds of concentration with willpower/mettle difficulty of of 8",
                base_difficulty=-2,
                count=1,
            ),
            "Gestures": Aspect(
                format="Clench fist and point (simple)", base_difficulty=-1, count=1
            ),
            "Incantations": Aspect(
                format="“Light.” (phrase)", base_difficulty=-1, count=1
            ),
        },
        notes="At the indicated site, the caster decreases gravity for a\n10-meter wide area. This causes certain physical actions to\nreceive modifiers to their difficulties or totals (see the “effect”\ndescription for details).\nAs this is a magical adjustment in gravity, it does not affect\nvictims in exactly the same way as a normal loss of gravity.\nFurthmore, anyone or anything leaving the area of effect\nloses any modifiers given by the spell.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(format="7D physical damage", base_difficulty=21, count=1),
        duration=Aspect(format="1 round ", base_difficulty=4, count=1),
        range=Aspect(format="40 meters ", base_difficulty=8, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=8, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Dimensional Gap",
        other_aspects={
            "Arcane Knowledge": Aspect(format="dimension", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="41", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Hemisphere with radius of 10 meters",
                base_difficulty=50,
                count=1,
            ),
            "Components": Aspect(
                format="Two rocks (ordinary)", base_difficulty=-1, count=1
            ),
            "Concentration": Aspect(
                format="1 round with willpower/mettle at difficulty 9",
                base_difficulty=-3,
                count=1,
            ),
            "Gestures": Aspect(
                format="Slam the components against each other (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes="When the caster brings the components of the spell\ntogether, the targeted location makes a dimensional gap in\nthe earth, creating a large hole in the ground. The shape is\nspherical, thereby causing vehicle or creatures at the edge to\nroll down the side into the center. Should the gap be created\ndirectly beneath a creature, it drops straight down, suffering\n7D damage. Damage to those who are not at ground zero\nis reduced accordingly by the area effect rules discussed in\nthe “Magic” chapter of the D6 Adventure  and D6 Fantasy\nrulebooks.\nWhen the hole disappears, anything that fell into the pit\nis now in a heap on the mysteriously whole ground.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="Atmospheric Tolerance (R2); Environmental Resistance (R2)",
            base_difficulty=18,
            count=1,
        ),
        duration=Aspect(format="1 day ", base_difficulty=25, count=1),
        range=Aspect(format="Self or within 1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Dimensional Survival",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="dimension, folk", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="26", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Circle with radius of 5 meters", base_difficulty=10, count=1
            ),
            "Concentration": Aspect(
                format="1 round with willpower/mettle difficulty of 8",
                base_difficulty=-2,
                count=1,
            ),
            "Focused": Aspect(format="On caster", base_difficulty=8, count=1),
        },
        other_conditions=[
            Aspect(
                format="Must be knowledgeable of the plane in which the morphed characters are to travel, requiring a scholar roll of 15",
                base_difficulty=-4,
                count=1,
            )
        ],
        notes="All who are affected by this spell are transformed physi -\ncally so they can survive on a hostile dimension. Once the\nspell is successfully cast, it operates upon all who are within\nfive meters of the mage, giving them half the ranks in the\nSpecial Abilities as the caster. Anyone who leaves the circle\nof influence loses the immunity and cannot regain it simply\nby getting close the mage again.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="Armor Value of 4D+1, physical only", base_difficulty=13, count=1
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="5 meters ", base_difficulty=4, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=4, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Energy Barrier",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="inanimate forces", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="30", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Circle with radius of 20 meters", base_difficulty=40, count=1
            ),
            "Concentration": Aspect(
                format="1 round with willpower/mettle difficulty of 6",
                base_difficulty=-2,
                count=1,
            ),
            "Gestures": Aspect(
                format="Point at the spot where the barrier is to be formed (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Feedback": Aspect(
                format="-3 to damage resistance total", base_difficulty=-3, count=1
            ),
        },
        notes="The mage can alter the forces that bind and form the\ndimension in which she dwell, shifting them to her will.\nBy simply pointing and concentrating, the mage creates a\nbarrier providing 4D+1 protection from attacks. All beings\nand objects behind the 20-meter area gain this advantage,\ncombining with existing armor. Of course, the limitation\nto this spell is that the defense is 2 dimensional. Once cast,\nbarrier cannot be relocated or altered, allowing for opponents\nto readily move around the side — providing they known\nenough to do this.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="Intangibility (R1), +3D to damage resistance total against physical attacks and movement is halved",
            base_difficulty=15,
            count=1,
        ),
        duration=Aspect(format="10 minutes ", base_difficulty=14, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="3 rounds ", base_difficulty=-6, count=1),
        name="Ethereal",
        other_aspects={
            "Arcane Knowledge": Aspect(format="dimensions", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="18", base_difficulty=0, count=1),
            "Concentration": Aspect(
                format="1 round with willpower/mettle difficulty of 6",
                base_difficulty=-2,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=5, count=1),
        },
        notes="When cast upon a character, the mage shifts the person\nbetween dimensions, making them ethereal. The character\nis visible, and still exists, but her being is spread among\nmany worlds. For the duration of this spell, she gains the\nIntangibility (R1) Special Ability.\n\n",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="10D physical damage, ignore nonmagical armor; up to 100 years in the past",
            base_difficulty=88,
            count=1,
        ),
        duration=Aspect(format="100 years ", base_difficulty=43, count=1),
        range=Aspect(format="Touch ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 hour ", base_difficulty=-18, count=1),
        name="Erase Person",
        other_aspects={
            "Arcane Knowledge": Aspect(format="dimension", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="61", base_difficulty=0, count=1),
            "Concentration": Aspect(
                format="1 hour with willpower/mettle difficulty of 15",
                base_difficulty=-9,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=26, count=1),
        },
        other_conditions=[
            Aspect(
                format="A roll of a 1 on the Wild Die in the caster being erased, even if the difficulty number was equaled or exceeded; may only be used once per target",
                base_difficulty=-8,
                count=1,
            )
        ],
        notes="This deadly spell not only instantly kills the target, but also\nobliterates her history from the universe. Upon contact with\nthe target, by means of a successful brawling/fighting roll, a\nshroud of blackness envelops the victim, erasing her from\nexistence. As each person is linked through time and space,\nthe thread that formed her history is followed and destroyed.\nThis means that all memories, all written words, all history\nis removed. It is as if the character had never existed. This\nspell is not a charged spell. Only one opportunity to erase a\nperson is granted per casting of the spell, and that opportunity\noccurs in the round after the spell’s completion.\nAs with powerful spells, there is the potential for disaster.\nIf the caster rolls a one on the Wild Die, it is the caster who\nsuffers the effect of the spell. Simply knowing this causes many\nmages to shy away from attempting such powerful magic.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="Psionics: astral projection of 4D+1", base_difficulty=26, count=1
        ),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Far Walk",
        other_aspects={
            "Arcane Knowledge": Aspect(format="dimension", base_difficulty=0, count=1),
            "Difficulty": Aspect(
                format="17", base_difficulty=0, count=1
            ),  # Should be 23
            "Concentration": Aspect(
                format="1 round with willpower/mettle difficulty of 8",
                base_difficulty=-2,
                count=1,
            ),
            "Feedback": Aspect(
                format="-1 to damage resistance total", base_difficulty=-1, count=1
            ),
            "Focused": Aspect(format="On caster", base_difficulty=8, count=1),
        },
        notes="By sending her consciousness through the folds of inter-\ndimensional space, the caster can visit other locations by\nleaving her body behind. This spell grants the caster 4D+1 in\nthe Psionics: astral projection skill (detailed in the “Psionics”\nchapter of the D6 Adventure Rulebook).",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="1,000 kilograms", base_difficulty=15, count=1),
        duration=Aspect(format="1 week ", base_difficulty=29, count=1),
        range=Aspect(format="Touch ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        name="Folded Space",
        other_aspects={
            "Arcane Knowledge": Aspect(format="dimension", base_difficulty=0, count=1),
            "Difficulty": Aspect(
                format="18", base_difficulty=0, count=1
            ),  # Should be 19
            "Components": Aspect(
                format="Small chest or bag (very common)", base_difficulty=-2, count=1
            ),
            "Concentration": Aspect(
                format="Every 24 hours, spend 1 round in concentration with willpower/mettle difficulty of 8 to maintain the spell",
                base_difficulty=-3,
                count=1,
            ),
            "Focused": Aspect(format="On container", base_difficulty=8, count=1),
        },
        notes="A chest or bag with this spell cast upon it can hold up\nto 1,000 kilograms of mass. The weight of the container is\nnot increased, as the objects drop into a fold within inter-\ndimensional space. However, it is not possible to sustain\nliving creatures within this area for more than a few minutes.\nNonetheless, it provides plenty of space for carrying items.\nNote that any thing that is larger than the opening of the\ncontainer cannot be placed inside. This means an automobile\ncould not be shoved into a paper lunch bag, but 1,000 kilo-\ngrams of marbles or appropriately sized items do fit.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="telekinesis of 6D", base_difficulty=36, count=1),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        name="Greater Telekinesis",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="inanimate forces", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="27", base_difficulty=0, count=1),
            "Concentration": Aspect(
                format="1 round with willpower/mettle difficulty of 8",
                base_difficulty=-2,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=10, count=1),
        },
        notes="Successfully casting this spell imbues the target with the\nPsionics skill telekinesis at 6D. The target is can move objects\nwith the power of her mind. All the rules for the skill use\napply as dictated in the D6 Adventure Rulebook chapter on\n“Psionics.” The distance moved and weight of an object moved\nis indicated on the “Telekinesis” table. The “Psionics Range”\ntable governs the range of the telekinesis skill.",
        skill="Apportation",
    ),
    Spell(
        effect=Aspect(
            format="Hindrance: High Gravity (R10), +5 to acrobat- ics, brawling/fighting, lifting/lift, melee combat, running,  and throwing difficulties",
            base_difficulty=30,
            count=1,
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="15 meters ", base_difficulty=6, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=6, count=1),
        casting_time=Aspect(format="2 rounds ", base_difficulty=-5, count=1),
        name="Increase Gravity",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="inanimate forces", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="34", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Sphere with radius of 5 meters", base_difficulty=25, count=1
            ),
            "Concentration": Aspect(
                format="2 rounds of concentration with willpower/mettle difficulty of of 8",
                base_difficulty=-2,
                count=1,
            ),
            "Gestures": Aspect(
                format="Clench fist and point (simple)", base_difficulty=-1, count=1
            ),
            "Incantations": Aspect(
                format="“Heavy.” (phrase)", base_difficulty=-1, count=1
            ),
        },
        notes="The caster increases gravity for a 10-meter wide area.\nBecause of this, certain physical actions get difficulty modi-\nfiers (see the “effect” description for details).\nAs this is a magical adjustment in gravity, it does not affect\nvictims in exactly the same way as a normal loss of gravity.\nFurthmore, anyone or anything leaving the area of effect\nloses any modifiers given by the spell.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(format="telekinesis of 3D", base_difficulty=18, count=1),
        duration=Aspect(format="25 minutes ", base_difficulty=16, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Lesser Telekinesis",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="inanimate forces", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(
                format="14", base_difficulty=0, count=1
            ),  # Should be 17
            "Concentration": Aspect(
                format="1 round with willpower/mettle difficulty of 8",
                base_difficulty=-2,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=6, count=1),
        },
        notes="The target can move objects with the power her mind with\nthe successful casting of this spell. The “Psionics” chapter in\nthe D6 Adventure Rulebook describes the game mechanics of\nthis spell. The distance moved and weight of an object moved\nis indicated on the “Telekinesis” table. The “Psionics Range”\ntable governs the range of the telekinesis skill.",
        skill="Apportation",
    ),
    Spell(
        effect=Aspect(format="search of 2D", base_difficulty=6, count=1),
        duration=Aspect(format="1 minute ", base_difficulty=4, count=1),
        range=Aspect(format="10 kilometers ", base_difficulty=20, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=20, count=1),
        casting_time=Aspect(format="1 hour ", base_difficulty=-18, count=1),
        name="Locate Person",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="dimension, folk", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="14", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Personal belonging from target (very rare)",
                base_difficulty=-5,
                count=1,
            ),
            "Concentration": Aspect(
                format="3 rounds with willpower/mettle difficulty of 8",
                base_difficulty=-2,
                count=1,
            ),
            "Gestures": Aspect(
                format="Form goggles with hands over eyes (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Variable Movement": Aspect(
                format="Bending/unseen target", base_difficulty=5, count=1
            ),
        },
        notes="If all the conditions are satisfied, then it is possible for\nthe caster to locate a given person within a 10-kilometer\nrange. Compare the result points of the spell’s search versus\nthe target’s Agility/Reflexes or sneak/stealth to the following\ntable to find how much the mage knows.\nMinimal (0 or less): general direction is determined\nSolid (1–4): direction and an idea of distance are known\nGood (5–8): direction, rough distance, and general features\nof the location are discerned\nSuperior (9 or more): direction, exact distance, and the\nexact location are garnered",
        skill="Divination",
    ),
    Spell(
        effect=Aspect(format="10D physical damage", base_difficulty=30, count=1),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="25 meters ", base_difficulty=7, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=7, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Rend Reality",
        other_aspects={
            "Arcane Knowledge": Aspect(format="dimension", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="29", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Sphere with radius of 3 meters", base_difficulty=15, count=1
            ),
            "Components": Aspect(
                format="2 small magnets (very common)", base_difficulty=-2, count=1
            ),
            "Concentration": Aspect(
                format="1 round with willpower/mettle difficulty of 8",
                base_difficulty=-2,
                count=1,
            ),
            "Gestures": Aspect(
                format="Tearing motion with hands while holding magnets (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes="After casting this powerful spell, the fabric of reality is\ntorn asunder, leaving a gapping tear that is jet black. This is\nthe space between spaces, an utter void. All who are within\nthe area effect of this spell must make an opposed Physique/\nStrength o r  lifting/lift roll against the spell skill total (no other\ntargeting roll is needed). Failure results in being pulled inside.\nThose who lose all of their Body Points or Wounds from the\ndamage caused by the rift are lost forever; it is impossible to\npull an object or a person from this temporarily disrupted\nsection of the universe. Anyone surviving the devestation\nis found after the spell wears off, battered, on the ground\nwhere the tear once was.\n\n",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="move up to 150 kilograms per round 10 meters away",
            base_difficulty=16,
            count=1,
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Secret Passage",
        other_aspects={
            "Arcane Knowledge": Aspect(format="dimension", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="10", base_difficulty=0, count=1),
            "Gestures": Aspect(
                format="Outline circle in the air (simple)", base_difficulty=-1, count=1
            ),
        },
        notes="Casting secret passage opens an interdimensional gateway\nwith an opening within one meter of the caster and an exit\n10 meters away. The exit portal connects as though a straight\nline were drawn from one point to another. This allows pas-\nsage through 10 meters of any material, including air, water,\nrock, and so on. All who enter vanish from sight and instantly\nappear at the exit point.",
        skill="Apportation",
    ),
    Spell(
        effect=Aspect(format="0", base_difficulty=0, count=1),
        duration=Aspect(format="2 rounds ", base_difficulty=5, count=1),
        range=Aspect(format="1 kilometer ", base_difficulty=15, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=15, count=1),
        casting_time=Aspect(format="2 rounds ", base_difficulty=-5, count=1),
        name="Send Whisper",
        other_aspects={
            "Arcane Knowledge": Aspect(format="dimension", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="12", base_difficulty=0, count=1),
            "Concentration": Aspect(
                format="1 round with willpower/mettle difficulty of 8",
                base_difficulty=-2,
                count=1,
            ),
            "Gestures": Aspect(
                format="Make a cone with hands around mouth (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Incantations": Aspect(
                format="Whisper target’s name along with the desired message (complex; languages/speaking roll with difficulty of 11)",
                base_difficulty=-2,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="Must have known the target for at least 1 week; must speak target’s language",
                base_difficulty=-2,
                count=1,
            )
        ],
        notes="Only the target can hear the caster’s words if the spell\nis successful. The communication is one-way, coming from\nthe caster. But because the message is traveling through\nthe barrier between planes, voices often become distorted,\nmaking sending a message much more difficult than normal\nconversation. For this reason, the magic user must make a\nlanguages/speaking attempt in a language the caster speaks\nand the target understands. The distortion creating by sending\na dimensional message creates a difficulty of 11. If the skill\nroll succeeds, the message is automatically heard. If a one is\nrolled on the Wild Die, but the difficulty number is equaled\nor passed, then others within one-meter of the target can\nhear the message as well.\nThe message is limited to what the caster can say in 10\nseconds.\n\n",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="600 kilograms of matter moved to another dimen- sion with a planar distance value of 49 or less",
            base_difficulty=63,
            count=1,
        ),
        duration=Aspect(format="1 round ", base_difficulty=4, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 hour ", base_difficulty=-18, count=1),
        name="Shift Plane",
        other_aspects={
            "Arcane Knowledge": Aspect(format="dimension", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="31", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Sphere with radius of 5 meters", base_difficulty=25, count=1
            ),
            "Concentration": Aspect(
                format="10 minutes with willpower/mettle difficulty of 11",
                base_difficulty=-5,
                count=1,
            ),
            "Gestures": Aspect(
                format="Touch the ground upon the completion of the spell (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Shift.” (phrase)", base_difficulty=-1, count=1
            ),
        },
        other_conditions=[
            Aspect(
                format="Must be knowledgeable of the target dimension, which requires a scholar roll of 20",
                base_difficulty=-6,
                count=1,
            )
        ],
        notes="Up to 600 kilograms of targets within the spell’s radius\nare transported to a given dimension. As this spell uses an\narea effect, the caster may not choose the targets going\nwith him.",
        skill="Apportation",
    ),
    Spell(
        effect=Aspect(format="5 kilograms", base_difficulty=4, count=1),
        duration=Aspect(format="5 rounds ", base_difficulty=6, count=1),
        range=Aspect(format="100 meters ", base_difficulty=10, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=10, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Synchronicity",
        other_aspects={
            "Arcane Knowledge": Aspect(format="dimension", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="13", base_difficulty=0, count=1),
            "Concentration": Aspect(
                format="1 round with willpower/mettle difficulty of 8",
                base_difficulty=-2,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=2, count=1),
            "Gestures": Aspect(
                format="Grasp at air (simple)", base_difficulty=-1, count=1
            ),
            "Incantations": Aspect(
                format="Whisper, “I touch something from afar.” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
            "Variable Movement": Aspect(
                format="Bending/unseen target", base_difficulty=5, count=1
            ),
        },
        other_conditions=[
            Aspect(
                format="Must make a scholar roll at 11, indicating she has sufficient understanding of dimensions",
                base_difficulty=-2,
                count=1,
            )
        ],
        notes="Many occultists and scholars of magic believe that there\nis no such thing as coincidence. Instead, seemingly random\nevents are attributed to interference from other dimensions,\nor an object coming out of a dimension and then re-entering\nthe same dimension at another location. That is to say, if the\ntop of a horseshoe where to be pushed through a sheet of\npaper to the point that only the open ends were visible, those\nunfamiliar with the shape of the horseshoe would see two,\nseparate items poking through the paper. But to those who\nunderstand the shape of a horseshoe, it is known that both\nvisible parts are connected by an unseen bend. This is how\nsynchronicity works. It allows the caster to perform an action,\nbut that action is linked through a multi-dimensional conduit\nthat causes a similar action to occur at a distance.\nAfter completing the spell, the magic user’s physical actions\nare invisibly replicated at a spot of her choosing up to 100\nmeters away. Once the location is designated, it cannot be\naltered. For instance, the mage may decide that when she\nwaves her hands, the glassware in a shop 50 meters away\nwould suddenly clatter to the floor, though it would not\nbreak as this spell causes no damage.\nThe exact results are left to the gamemaster and the circum-\nstances, but the caster should be allowed to be as creative as\npossible. (However, this spell cannot cause injury — though\nperhaps a little pain, such as a tug on the ear — and can\nonly affect up to five kilograms of matter.) Because of this\nunique ability, this spell is often used to distract others for\na brief moment.",
        skill="Apportation",
    ),
    Spell(
        effect=Aspect(format="1 kilogram projectile", base_difficulty=0, count=1),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="150 meters ", base_difficulty=11, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=11, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Unseen Bullet",
        other_aspects={
            "Arcane Knowledge": Aspect(format="dimension", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="15", base_difficulty=0, count=1),
            "Components": Aspect(
                format="physical projectile of any sort, be it rock, arrow, bullet, etc. (ordinary)",
                base_difficulty=-1,
                count=1,
            ),
            "Concentration": Aspect(
                format="1 round with willpower/mettle difficulty of 8",
                base_difficulty=-2,
                count=1,
            ),
            "Focused": Aspect(format="On projectile", base_difficulty=1, count=1),
            "Gestures": Aspect(
                format="Grasp projectile in hand (simple)", base_difficulty=-1, count=1
            ),
            "Variable Movement": Aspect(
                format="Bending with +4D (+12) to targeting skill total",
                base_difficulty=5,
                count=1,
            ),
        },
        notes="Without the ability to see or sense the target, such as\nthrough other magic, this spell is not very useful. If a victim\ncan be located, then the projectile can be thrown or fired\nwith a +4D (+12) to the targeting skill total. The object hits\nthe target on a successful skill roll as though appearing from\nno where. There is no possibility to dodge or take cover, as\nprojectile travels through a wormhole, unhindered by all\nphysical barriers. This means it is possible to shoot through\none or more windows without breaking the glass.",
        skill="Apportation",
    ),
    Spell(
        effect=Aspect(
            format="Invisibility (R3), +3 to dodge, sneak/stealth, and hide: self totals and +3 to search, tracking, investigation, and attack difficulties against target; Iron Will (R3), +3D to will- power/mettle rolls and +6 to default interaction attempts and mental attacks against character; Natural Armor: In Other Dimension (R3), +3D to damage resistance roll against physi- cal and energy attacks",
            base_difficulty=21,
            count=1,
        ),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="Touch ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="2 rounds ", base_difficulty=-5, count=1),
        name="Vanish",
        other_aspects={
            "Arcane Knowledge": Aspect(format="dimension", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="15", base_difficulty=0, count=1),
            "Concentration": Aspect(
                format="1 round with willpower/mettle difficulty of 8",
                base_difficulty=-2,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="Anything that affects other dimensional creatures affects the target",
                base_difficulty=-2,
                count=1,
            )
        ],
        notes="Any living or nonliving item up to 150 kilograms can be\nfolded into a small, temporary dimension created by the\ncaster. By all appearances, the object or person simply van-\nishes from sight. Time passes normally for the duration of\nthe spell; the target can do whatever she wishes, as long as\nshe does not move from the spot where she vanished. There\nis always enough air to breath for at least one hour. The\natmosphere must be present at the location where the spell\nis cast; it cannot be created by the magic user.",
        skill="Apportation",
    ),
    Spell(
        effect=Aspect(
            format="5D physical damage, ignores nonmagical armor",
            base_difficulty=23,
            count=1,
        ),
        duration=Aspect(format="5 rounds ", base_difficulty=7, count=1),
        range=Aspect(format="25 meters ", base_difficulty=7, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=7, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Void Shield",
        other_aspects={
            "Arcane Knowledge": Aspect(format="dimension", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="29", base_difficulty=0, count=1),
            "Change Target": Aspect(
                format="up to 5 times (once per round or when attacked)",
                base_difficulty=25,
                count=1,
            ),
            "Gestures": Aspect(
                format="draw circle in the air (simple)", base_difficulty=-2, count=1
            ),
        },
        other_conditions=[
            Aspect(
                format="Willpower/mettle  roll of 14 is required each time the spell is moved; target must be alive",
                base_difficulty=-5,
                count=1,
            )
        ],
        notes="Casting void shield  creates a one-meter radius circle of\nnegative energy that causes 5D damage to up to five targets\nthat come in contact with it. Its name is misleading in that\nit doesn’t improve Armor Value; rather, it is a weapon. While\nthe spell is active, the “shield” thrums, as the caster directs it\nfrom target to target. It is only capable of causing damage to\nthose who possess positive energy, who are alive. It can pass\nthrough a character, causing damage, moving to the next to\ncontinue with another attack.\nStriking at the void shield is the as being attack. The attack-\ning weapon and the attacker suffer 5D of damage, split\nbetween them (but only one of the change targets is used\nup). Nonmagical armor does not protect against the damage\ncaused by this spell.\n\n",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="6D+1 physical damage, ignores nonmagical armor",
            base_difficulty=29,
            count=1,
        ),
        duration=Aspect(format="3 rounds ", base_difficulty=6, count=1),
        range=Aspect(format="40 meters ", base_difficulty=8, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=8, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Vortex",
        other_aspects={
            "Arcane Knowledge": Aspect(format="dimensions", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="34", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Sphere with radius of 5 meters", base_difficulty=25, count=1
            ),
            "Concentration": Aspect(
                format="1 round with willpower/mettle difficulty of 8",
                base_difficulty=-2,
                count=1,
            ),
            "Feedback": Aspect(
                format="-3 to damage resistance total", base_difficulty=-3, count=1
            ),
            "Variable Movement": Aspect(
                format="Movement of 5 meters per round", base_difficulty=1, count=1
            ),
        },
        notes="By knowledge of the planes and will, a mage can focus\nher mental energy upon a location visible to her and open\na swirling vortex. This is an interdimensional juncture that\ncreates havoc in nearly any plane it is created. The opening\nof the shimmering vortex is announced by a deep rumbling\nsound not unlike thunder. By the time the spell is completed,\nall within several meters can hear and feel the roar and quake\nof this unnatural creation. Any object that comes into contact\nwith it suffers 6D+1 damage, with no damage being absorbed\nby nonmagical armor. Additionally, the caster can move the\nvortex five meter per round.\nShould two vortices come into contact, they cancel each\nother, immediately ending the spell.",
        skill="Conjuration",
    ),
]

if __name__ == "__main__":
    detail(spells)

__test__ = {
    "Alter Gravity": ">>> spells[0].difficulty\n12",
    "Beacon": ">>> spells[1].difficulty\n13",
    "Beckon Creature": ">>> spells[2].difficulty\n36",
    "Bind Reality": ">>> spells[3].difficulty\n35",
    "Blur Barriers": ">>> spells[4].difficulty\n33",
    "Contact Entity": ">>> spells[5].difficulty\n32",
    "Decrease Gravity": ">>> spells[6].difficulty\n34",
    "Dimensional Gap": ">>> spells[7].difficulty\n41",
    "Dimensional Survival": ">>> spells[8].difficulty\n26",
    "Energy Barrier": ">>> spells[9].difficulty\n30",
    "Ethereal": ">>> spells[10].difficulty\n18",
    "Erase Person": ">>> spells[11].difficulty\n61",
    "Far Walk": ">>> spells[12].difficulty\n23",
    "Folded Space": ">>> spells[13].difficulty\n19",
    "Greater Telekinesis": ">>> spells[14].difficulty\n27",
    "Increase Gravity": ">>> spells[15].difficulty\n34",
    "Lesser Telekinesis": ">>> spells[16].difficulty\n17",
    "Locate Person": ">>> spells[17].difficulty\n14",
    "Rend Reality": ">>> spells[18].difficulty\n29",
    "Secret Passage": ">>> spells[19].difficulty\n10",
    "Send Whisper": ">>> spells[20].difficulty\n12",
    "Shift Plane": ">>> spells[21].difficulty\n31",
    "Synchronicity": ">>> spells[22].difficulty\n13",
    "Unseen Bullet": ">>> spells[23].difficulty\n15",
    "Vanish": ">>> spells[24].difficulty\n15",
    "Void Shield": ">>> spells[25].difficulty\n29",
    "Vortex": ">>> spells[26].difficulty\n34",
}
