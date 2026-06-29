"""
Technomancy
-----------

"""

from textwrap import dedent

from magic1 import Aspect, Spell, detail

spells = [
    Spell(
        effect=Aspect(
            format="Agility/Reflexes  and Physique/Strength of 3D each; movement equal to result points in meters round with minimum of 1 meter per round",
            base_difficulty=27,
            count=1,
        ),
        duration=Aspect(format="1 day ", base_difficulty=25, count=1),
        range=Aspect(format="Touch ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 hour ", base_difficulty=-18, count=1),
        name="Activate Automaton",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="inanimate forces, enchanted, metal", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="15/17", base_difficulty=0, count=1),
            "Components": Aspect(
                format="-6/-3 Robot/automaton without power source (extremely rare/common)",
                base_difficulty=-6,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=10, count=1),
            "Gestures": Aspect(
                format="Program instructions into robot (challenging, devices/tech/robot interface/repair difficulty of 23)",
                base_difficulty=-6,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Activate!” loudly (phrase)", base_difficulty=-2, count=1
            ),
        },
        notes="The game setting determines the components modifier.\nIn fantasy or pre-computer eras, robots are likely to be\nextremely rare, while post-computer or science fiction set -\ntings often have an abundance of robots. In any case, this\nspell does not give life to a machine. Rather, it imbues 3D to\nboth Agility/Reflexes and Physique/Strength. This means that\nthe mechanical device is capable of ambulation (at a rate of\nand physical acts such as lifting or attacking. However, to\ncontrol the device requires programming with the devices/\ntech/robot interface/repair skill. Instructions cannot be called\nout, as the automaton or robot has not been given the ability\nto understand speech. Automatons make useful guards and\nservants, and are occasionally handy in combat.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="Hindrance: Altered Firearm (R4), +12 to marksmanship/firearms difficulties",
            base_difficulty=12,
            count=1,
        ),
        duration=Aspect(format="10 minutes ", base_difficulty=14, count=1),
        range=Aspect(format="100 meters ", base_difficulty=10, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=10, count=1),
        casting_time=Aspect(format="2 rounds ", base_difficulty=-5, count=1),
        name="Alter Trajectory",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Inanimate forces, metal", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="21", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Small, misshapen lead ball (common)",
                base_difficulty=-3,
                count=1,
            ),
            "Focused": Aspect(format="On weapon", base_difficulty=5, count=1),
            "Gestures": Aspect(
                format="Make spiral motion with hand (simple)",
                base_difficulty=-1,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="The target must be a ranged weapon that is manufactured of metal or has a metal component as part of its firing mechanism",
                base_difficulty=-1,
                count=1,
            )
        ],
        notes="With the twist of a hand, the magic user can cause a ranged\nweapon to alter the interior shape of its barrel, bore, rifling and\nso on. Although the imperfection created is minor, requiring\na Moderate search to detect, it is sufficient to create a +12\ndifficulty modifier to marksmanship/firearms.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="Armor Value of 2D, physical only", base_difficulty=6, count=1
        ),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="2.5 seconds ", base_difficulty=-2, count=1),
        name="Armor",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Metal", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="12", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Any type of coin-sized metal: bronze, iron, and so on (very common)",
                base_difficulty=-2,
                count=1,
            ),
            "Focused": Aspect(format="On coin", base_difficulty=4, count=1),
            "Incantations": Aspect(
                format="“Make armor!.” (phrase)", base_difficulty=-1, count=1
            ),
        },
        notes="This spell allows the caster to produce the equivalent of a\nbreastplate and grieves from a coin-sized fragment of metal.\nThis not only works wonderfully when passing through\nmetal detectors, but just as well when entering a monarch’s\nsanctuary. Regardless of the type of metal used, the armor\nis similar to bronze armor in quality and protection. Once\nit is conjured on a target, it cannot be removed unless the\nspell duration ends or the magic user halts it. The armor is\nseamless, and fits any form perfectly.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="Hindrance: Metal Attracts (R1); -6 to damage resistance total",
            base_difficulty=18,
            count=1,
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="10 meters ", base_difficulty=7, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=7, count=1),
        casting_time=Aspect(format="2 rounds ", base_difficulty=-5, count=1),
        name="Attract Metal",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="18", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Small magnet or loadstone (ordinary)",
                base_difficulty=-1,
                count=1,
            ),
            "Concentration": Aspect(
                format="1 round with willpower/mettle difficulty of 8",
                base_difficulty=-2,
                count=1,
            ),
            "Countenance": Aspect(
                format="Target surrounded by faint red glow",
                base_difficulty=-1,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=5, count=1),
            "Gestures": Aspect(
                format="Wave hand, welcoming something (simple)",
                base_difficulty=-1,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="Hindrance only applies to attacks made by metal weapons or spells using metal",
                base_difficulty=-1,
                count=1,
            )
        ],
        notes="If the mage successfully casts this spell, then the victim\nattracts metal weapons, increasing their damage by pulling\nthem toward the character. The spell is not capable of auto-\nmatically causing damage; rather, it decreases the protection\noffered against any melee or magical or projectile weapons\nused against the target. For the duration of the spell, the\nfigure is surrounded by a faint red glow. The effect of this\nspell is not limited to ferrous metals.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="one combat skill of 3D; +2D physical damage",
            base_difficulty=18,
            count=1,
        ),
        duration=Aspect(format="1 day ", base_difficulty=25, count=1),
        range=Aspect(format="40 meters ", base_difficulty=8, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=8, count=1),
        casting_time=Aspect(format="1 hour ", base_difficulty=-18, count=1),
        name="Awaken Machine",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Inanimate Forces", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="18", base_difficulty=0, count=1),
            "Components": Aspect(
                format="A mechanical device that has a weapon (very rare)",
                base_difficulty=-5,
                count=1,
            ),
            "Concentration": Aspect(
                format="1 hour with willpower/mettle difficulty of 12",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Tick! (phrase)", base_difficulty=-1, count=1
            ),
            "Other Alterants": Aspect(
                format="Will attack anything that moves within 3 meters of it",
                base_difficulty=3,
                count=1,
            ),
        },
        notes="The spell only activates any weapon mounted upon the\nmachine, conveying 3D in one combat skill (chosen at cast-\ning with +2D to its weapon’s damage. The weapon used\ndetermines the amount of damage.\nEven though the device may have legs, tracks or another\nform of locomotion, the spell does not cause it to move.\nThe contraption is incapable of thought. But, through magic\nand mechanical gimmickry, once awakened, it fights with\nthe skill of a moderately trained warrior. Often such devices\nare place in corridors for protection, or hidden beneath false\nfloors as a trap.\n\n",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="-2D physical damage modifier", base_difficulty=9, count=1
        ),
        duration=Aspect(format="1.5 minutes ", base_difficulty=10, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Blunt",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Metal", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="12", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Stone (ordinary)", base_difficulty=-1, count=1
            ),
            "Focused": Aspect(format="On weapon", base_difficulty=3, count=1),
            "Gestures": Aspect(
                format="Wave stone as though hammering the edge of a weapon (simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Blunt!.” (phrase, loud)", base_difficulty=-2, count=1
            ),
        },
        other_conditions=[
            Aspect(
                format="Must be a metal, edged, nonmagical weapon", base_difficulty=-1
            ),
        ],
        notes="This spell dulls a weapons edge. When successfully cast,\nthe weapon has a -2D damage modifier, with a minimum\nadjusted damage value for the weapon of +1D. Any blade that\nis blunted to +1D becomes something akin to a metal stick.\nMagic weapons are not affected by this spell.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="8D in device skill, 6D in craft skill, and 10 materials",
            base_difficulty=52,
            count=1,
        ),
        duration=Aspect(format="1 year ", base_difficulty=38, count=1),
        range=Aspect(format="Touch ", base_difficulty=0, count=1),
        speed=Aspect(format="instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 week ", base_difficulty=-29, count=1),
        name="Construct Small Automaton",
        other_aspects={
            "Difficulty": Aspect(format="36", base_difficulty=0, count=1),
            "Components": Aspect(
                format="A variety of materials are needed, ranging from the mundane to a flawless gem or some other such rare item to energize the automaton (uncommon to rare)",
                base_difficulty=-7,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=18, count=1),
            "Incantations": Aspect(
                format="“Understand.” whispered (phrase)", base_difficulty=-1, count=1
            ),
        },
        notes=dedent("""\
            The game setting determines the components needed. The
            automaton is usually a mechanical contraption of limited
            capability. Typically such machines do not possess the faculty
            of cognitive thought. Instead, they are controlled by
            spells such as Activate Automaton, which allow for limited
            function. However, the first step is constructing the device.
            A successful casting of this spell allows for the construction
            of a human sized creation. The gamemaster should have the
            player’s characters follow the rules for the skill  device, and
            possibly make some of the require components very difficult
            to acquire — having a world populated by automatons can
            be interested and dangerous.
         
            The first step is developing the blue prints This is done
            by achieving using the table for Complexity of Device in
            “Example Skill Difficulties” chapter. The gamemaster must
            decide upon the technological level of the culture. In most
            cases, an automaton is as prototype (+10) and is from a much
            higher culture (+10), resulting in a minimum +20 modifier.
            With research, this modifier might be altered. Each roll takes
            one month. The base difficulty for drawing up the blueprints
            is Very Difficult. However, the gamemaster should count
            previous failures as bonus modifiers, as the hero learns from
            her mistakes.
            
            After the blueprints have been created, the construction
            commences. Now the crafting skill is used to construct the
            automaton. Again, the related table from the “Example Skill Difficulties” 
            chapter should be used. The number of
            components that have been gathered, their quality and the
            clarity of the blueprints determine the modifiers used for
            constructing an automaton. The base difficulty is Very Difficult. 
            Each attempt to construct the device takes 2 months.
            The gamemaster should consider previous failures as bonus
            modifiers for future attempts.
            
            At the end of the spell’s duration, the skills are lost, but the
            knowledge is not. If the attempt to build an automaton was
            not successful, then the gamemaster should apply bonuses
            for the next attempt for gained experience.
        """),
        skill="Divination",
    ),
    Spell(
        effect=Aspect(
            format="Skill Bonus (R6), +18 to devices/tech/robot (or computer) interface/repair  totals",
            base_difficulty=18,
            count=1,
        ),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="Touch ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="4 rounds ", base_difficulty=-6, count=1),
        name="Control Machine",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Inanimate forces, metal", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="18", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Wire or similar piece of metal (ordinary)",
                base_difficulty=-1,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=7, count=1),
        },
        other_conditions=[
            Aspect(
                format="The target must be able to touch the device or connect to it electronically",
                base_difficulty=-1,
                count=1,
            )
        ],
        notes="If the caster uses this spell in a setting without the elec -\ntronic networks, then the machine must be within reach of\nthe target. A successful casting provides the target with a +18\nto her devices/tech/robot (or computer) interface/repair totals.\nThe setting and the devices that the caster intends the target\nto affect dictate the skill that gets the bonus.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="5D physical damage to metal; living creatures lose one action if fail resistance roll",
            base_difficulty=15,
            count=1,
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="100 meters ", base_difficulty=10, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=10, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Corrosive Cloud",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Metal", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="20", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Sphere with radius of 1 meter", base_difficulty=5, count=1
            ),
            "Components": Aspect(
                format="Small vile of acidic liquid, such as juice from a lemon or lime (very common)",
                base_difficulty=-2,
                count=1,
            ),
            "Gestures": Aspect(
                format="Point in direction of cloud location (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Incantations": Aspect(
                format="Repeated phrase for duration of spell (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes="Casting this spell creates as green haze. All metal within it\nsuffers 5D of corrosive damage unless magically protected.\nThe cloud is so dense as to require any living creatures inside\nto make a Moderate Physique/Strength o r  stamina roll. Failure\nresults in choking (and the targets lose their next action).\nEach round the cloud remains over a metal target, it suffers\nan additional 5D of damage until it is destroyed\nFor the duration of the spell, the caster must continue the\nlitany that invokes the mystical cloud.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="8D in device skill, 6D in craft skill, and 22 materials",
            base_difficulty=64,
            count=1,
        ),
        duration=Aspect(format="2 year ", base_difficulty=39, count=1),
        range=Aspect(format="Touch ", base_difficulty=0, count=1),
        speed=Aspect(format="instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 week ", base_difficulty=-29, count=1),
        name="Construct Teemendous Automaton",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Inanimate Forces", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="40", base_difficulty=0, count=1),
            "Components": Aspect(
                format="A variety of materials are needed, ranging from the mundane to a flawless gem or some other such rare item to energize the automaton (uncommon to rare)",
                base_difficulty=-7,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=20, count=1),
            "Incantations": Aspect(
                format="“Understand.” whispered (phrase)", base_difficulty=-1, count=1
            ),
        },
        other_conditions=[
            Aspect(
                format="Large quantities and cumbersome materials, tools and devices are needed, as well as funding; additionally, a large location is needed to construct monstrous creation",
                base_difficulty=-6,
                count=1,
            )
        ],
        notes="This spell work identically to Construct Small Automaton See\nthat spell for specifics. Note the differences are in size, casting\ndifficulty and duration. Blueprint design and construction\ntimes are doubled. Otherwise, all other aspects apply.",
        skill="Divination",
    ),
    Spell(
        effect=Aspect(
            format="Skill Bonus (R8), +24 to investigation totals for purposes of determining metal",
            base_difficulty=24,
            count=1,
        ),
        duration=Aspect(format="1 round ", base_difficulty=4, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Discern Alloy",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Metal", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="12", base_difficulty=0, count=1),
            "Gestures": Aspect(
                format="Move hands across the object (simple)",
                base_difficulty=-1,
                count=1,
            ),
        },
        notes="Even if the caster has no knowledge of various metals and\nalloys, this spell allows her to perceive what was used to make\na given object. This is useful when encountering strange alien\nobjects or when attempting to see how strong a weapon, door,\nor similar item is. Upon successfully casting discern alloy, the\nmagic user gains a +24 bonus to her investigation totals in\norder to figure out the type of metal used. The difficulty is\ndetermined by the gamemaster.\n\n",
        skill="Divination",
    ),
    Spell(
        effect=Aspect(format="10D physical damage", base_difficulty=30, count=1),
        duration=Aspect(format="1 round ", base_difficulty=4, count=1),
        range=Aspect(format="100 meters ", base_difficulty=10, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=10, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="EMP",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Inanimate Forces", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="35", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Sphere with 5 meter radius", base_difficulty=25, count=1
            ),
            "Components": Aspect(
                format="Small magnet or loadstone (ordinary)",
                base_difficulty=-1,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Pulse!” (phrase, loud)", base_difficulty=-2, count=1
            ),
        },
        other_conditions=[
            Aspect(
                format="Only affects electrical devices", base_difficulty=-2, count=1
            ),
        ],
        notes="Any electronic equipment in the area effect of this spell\nsuffers 10D damage from an electro-magnetic pulse. As this\neffect is caused by altering the inanimate forces of nature,\ninstead of exploding a bomb, there is no damage done to most\nliving beings or to devices that do not have electronics.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="Skill Bonus (R10), +30 crafting/repair/personal equipment repair totals",
            base_difficulty=30,
            count=1,
        ),
        duration=Aspect(format="1 day ", base_difficulty=25, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 hour ", base_difficulty=-18, count=1),
        name="Forge Perfect Weapon",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Metal", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="16", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Raw material for weapon (common); forging tools and forge (uncommon)",
                base_difficulty=-7,
                count=1,
            ),
            "Concentration": Aspect(
                format="Form image of complete weapon in mind for 1 hour with willpower/mettle difficulty of 12",
                base_difficulty=-6,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=11, count=1),
            "Gestures": Aspect(
                format="Touch raw material with small hammer (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Flawless.” (phrase)", base_difficulty=-1, count=1
            ),
        },
        other_conditions=[
            Aspect(
                format="Must possess some experience in the affected skill",
                base_difficulty=-1,
                count=1,
            )
        ],
        notes="To gain the bonus from a successful casting of this spell,\nthe target must have some training in crafting/repair/personal\nequipment repair; otherwise, the magical knowledge is lost.\nIn order for a perfect weapon to be properly crafted, not\nonly are the raw materials, forge, and ancillary equipment\nneeded, but a crafting/repair/personal equipment repair  roll\nwith a difficulty of Heroic is required to forge the item. The\ngamemaster may use the result points from the forging skill\nroll to give bonuses to the superior pieces of equipment.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="+2D+2 physical damage modifier", base_difficulty=12, count=1
        ),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="3 rounds ", base_difficulty=-6, count=1),
        name="Hone Edge",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Metal", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="15", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Whetstone (common)", base_difficulty=-3, count=1
            ),
            "Countenance": Aspect(
                format="Weapon gains faint blue shine", base_difficulty=-1, count=1
            ),
            "Focused": Aspect(format="On weapon", base_difficulty=6, count=1),
            "Gestures": Aspect(
                format="Move whetstone as though sharpening a weapon (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“I whet your blunt purpose!” (sentence, loud)",
                base_difficulty=-3,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="Only works on a nonmagical, metal, edged weapon",
                base_difficulty=-1,
                count=1,
            )
        ],
        notes="This spell places a magically keen edge upon a weapon,\nincreasing its damage by +2D+2. Any weapon with this spell\ncast upon it gains a faint blue shine to its surface, as the\nmagic reshapes the metal to the molecular level, honing the\nblade’s edge to that of a single atom. For the duration of this\nspell, there is no material that cannot be cut or damaged by\nthe magical edge, even though normal or magical protection\nmight hinder damage.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="search of 4D to detect a single type of metal",
            base_difficulty=12,
            count=1,
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="40 meters ", base_difficulty=8, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=8, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        name="Locate Metal",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Metal", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="18", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Divination sphere with radius of 3.5 meters",
                base_difficulty=9,
                count=1,
            ),
            "Component": Aspect(
                format="Forked stick (ordinary)", base_difficulty=-1, count=1
            ),
            "Concentration": Aspect(
                format="1 minute with willpower/mettle of 10",
                base_difficulty=-4,
                count=1,
            ),
            "Incantations": Aspect(
                format="Name of the metal (phrase)", base_difficulty=-1, count=1
            ),
            "Variable Movement": Aspect(
                format="Bending/unseen target", base_difficulty=5, count=1
            ),
        },
        notes="Once the metal is named, the spell is complete. Immediately,\nthe mage can roll search at 4D to locate the prescribed metal\ninside an item, the earth, or a living being. Sometimes this\nspell is used to locate trace amounts of a particular metal,\nsuch as mercury or uranium. If there is anything of interest\nin the indicated area, a luminous yellow glow surrounds the\nlocation of the metal for up to one minute. The brilliance is\ndetermined by the quantity or density of the metal in searched\nfor. The higher the search total is above the difficulty, the more\ninformation the caster gleans from her  attempt, including\nlocation, depth, quantity, etc. The gamemaster decides on the\ndifficulty, which depends on how well hidden the material is\nand how much is there.",
        skill="Divination",
    ),
    Spell(
        effect=Aspect(format="intimidation of 8D+1", base_difficulty=25, count=1),
        duration=Aspect(format="10 minutes ", base_difficulty=14, count=1),
        range=Aspect(format="100 meters ", base_difficulty=10, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=10, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        name="Machine Terror",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Enchanted", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="28", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Metal shards (ordinary)", base_difficulty=-1, count=1
            ),
            "Focused": Aspect(format="On machine", base_difficulty=7, count=1),
            "Gestures": Aspect(
                format="Point at target (simple)", base_difficulty=-1, count=1
            ),
        },
        notes="Regardless of the type of contraption, the spell make a\nmachine capable of stimulating terror in anyone within sight\nof the device. Anyone who fails an opposed interaction roll\nagainst the machine’s intimdation loses her next action. The\nmachine terrorizes once per round for the duration of the\nspell. This is a way of making a trap, automaton, robot, and\nso on appear far more frightening than it may actually be.\n\n",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="moves up to 100 kilograms", base_difficulty=10, count=1),
        duration=Aspect(format="1 week ", base_difficulty=29, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-18, count=1),
        name="Magic Platter",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Inanimate Forces", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="15", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Circle with radius of 1 meter", base_difficulty=2, count=1
            ),
            "Components": Aspect(
                format="Small piece of metal or coin (ordinary)",
                base_difficulty=-1,
                count=1,
            ),
            "Focused": Aspect(format="On metal", base_difficulty=7, count=1),
            "Gestures": Aspect(format="Point (simple)", base_difficulty=-1, count=1),
            "Incantations": Aspect(
                format="“Carry.” (phrase)", base_difficulty=-1, count=1
            ),
            "Variable Movement": Aspect(
                format="Movement of 12.5 meters per round", base_difficulty=3, count=1
            ),
        },
        notes="The caster transforms a coin into a floating platter capable\nof carrying 100 kilograms of weight. To direct it, all that needs\nto be done is to point. If the magic user indicates herself, then\nthe tray follows her. Otherwise, she must guide it. Providing\na character is 100 kilograms or less, it is possible for her to\nride or be carried by the platter.",
        skill="Apportation",
    ),
    Spell(
        effect=Aspect(
            format="difficulty to resist the pull", base_difficulty=20, count=1
        ),
        duration=Aspect(format="5 rounds ", base_difficulty=7, count=1),
        range=Aspect(format="Touch ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Magnetism",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Inanimate Forces", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="28", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Sphere with radius of 5 meters", base_difficulty=25, count=1
            ),
            "Components": Aspect(
                format="Small magnet or loadstone (ordinary)",
                base_difficulty=-1,
                count=1,
            ),
            "Focused": Aspect(format="On magnet", base_difficulty=5, count=1),
            "Gestures": Aspect(
                format="Throw loadstone (complex; throwing roll with difficulty of 11)",
                base_difficulty=-3,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Pull!.” (phrase, loud)", base_difficulty=-1, count=1
            ),
            "Other Alterants": Aspect(
                format="Metal objects move toward magnet at rate of 1 meter per round; mechanical devices within spell’s influence stop working for duration of spell",
                base_difficulty=8,
                count=1,
            ),
        },
        notes="Once cast, this spell is not very discerning: All ferrous\nobjects within its radius are pulled toward the loadstone. The\nmagic user throws the stone in a direction that works best\nagainst any enemy, making sure to stay clear herself. Anyone\nwearing metal must make a Physique/Strength or lifting/lift\nagainst the effect’s difficulty. Failure means the affected object\nis yanked free and pulled toward the loadstone at a speed of\none meter per round. If ferrous armor is being worn, then the\ncharacter wearing the armor moves as well. (Non-character\nobjects automatically move toward the stone.)\nAnother effect this spell has is to cause all mechanical\ndevices with metals influenced by magnetism to stop func-\ntioning, as well as being pulled toward the loadstone.\n\n",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="12D physical damage, ignores nonmagical armor",
            base_difficulty=54,
            count=1,
        ),
        duration=Aspect(format="1 second ", base_difficulty=0, count=1),
        range=Aspect(format="5 meters ", base_difficulty=4, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=4, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Make Statue",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Metal", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="27", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Iron statue (uncommon)", base_difficulty=-4, count=1
            ),
            "Gestures": Aspect(
                format="Point at target with statue (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Statue!.” (phrase, loud)", base_difficulty=-2, count=1
            ),
            "Other Alterant": Aspect(
                format="Target turns into a statue if she dies",
                base_difficulty=3,
                count=1,
            ),
        },
        notes="A mage who successfully casts this spell and makes the\nnecessary targeting roll causes 12D damage that nonmagi -\ncal armor offers no protection against. The spell alters the\ncomposition of the target, attempting to refigure her into\nan iron statue. If the damage is sufficient to cause death,\nthen she becomes a statue. This is permanent damage. The\ncharacter cannot be resurrected, as there is no living material\nto bring back to life. Instead, she has become an ornament\nfor someone’s garden or great hall.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(format="6D damage against machines", base_difficulty=18, count=1),
        duration=Aspect(format="1 second ", base_difficulty=0, count=1),
        range=Aspect(format="60 meters ", base_difficulty=9, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=9, count=1),
        casting_time=Aspect(format="2.5 seconds ", base_difficulty=-2, count=1),
        name="Malfunction",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Inanimate Forces", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="14", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Small iron ball (common)", base_difficulty=-2, count=1
            ),
            "Gestures": Aspect(
                format="Throw component in direction of target (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Stop!” loudly (phrase)", base_difficulty=-2, count=1
            ),
        },
        other_conditions=[
            Aspect(format="Only harms mechanical devices", base_difficulty=-1, count=1)
        ],
        notes="Sometimes it is best to fight metal with metal. When cast,\nthis spell sends a searing bolt of energy at the target, doing\n6D damage. This spell has only works against machines, as it\nuses the same forces of physics (and sometimes magic) that\nproduced the construct to destroy it. No harm comes to a\nliving, undead, or any other creature that is not mechanical\nin nature. Certainly robots are affected by this spell, as are\ncyborgs. However, only the mechanical parts of a cyborg are\ndamaged; the living flesh is unharmed.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="Compare to item’s Toughness or damage resistance",
            base_difficulty=25,
            count=1,
        ),
        duration=Aspect(format="1 round ", base_difficulty=4, count=1),
        range=Aspect(format="60 meters ", base_difficulty=9, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=9, count=1),
        casting_time=Aspect(format="2 rounds ", base_difficulty=-5, count=1),
        name="Malleable",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Metal", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="17", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Malleable clay (very common)", base_difficulty=-2, count=1
            ),
            "Concentration": Aspect(
                format="2 rounds with willpower/mettle difficulty of 8",
                base_difficulty=-2,
                count=1,
            ),
            "Gestures": Aspect(
                format="Shape the clay (fairly simple)", base_difficulty=-2, count=1
            ),
            "Incantations": Aspect(
                format="“Alter.” (phrase)", base_difficulty=-1, count=1
            ),
        },
        other_conditions=[
            Aspect(
                format="The target must be nonmagical, metal, and no more than 5 kilograms",
                base_difficulty=-1,
                count=1,
            )
        ],
        notes="Any targeted metal object that has a mass of five kilograms\nor less can be permanently altered in shape. For instance, the\ncaster could transform a shield into a ball, thereby negating\nits protection. Or, the length of a metal rod could be extended\nto twice its length, although doing this makes it very thin.\nJust as easily could the barrel of a gun be twisted closed.\nBasically, whatever shape the magic user makes with the clay\ncomponent is paralleled with the target. (The player speci -\nfies the target and the shape, and the gamemaster compares\nthe effect’s value plus the casting’s result point bonus to the\nobject’s Toughness or damage resistance to determine whether\nthe object takes the new shape.) Magically imbued metal or\nmagically protected metal cannot be altered.",
        skill="Alteration",
    ),
    # Spell(
    #     effect=Aspect(format="6D damage against machines", base_difficulty=18, count=1),
    #     duration=Aspect(format="1 second ", base_difficulty=0, count=1),
    #     range=Aspect(format="60 meters ", base_difficulty=9, count=1),
    #     speed=Aspect(format="Instantaneous ", base_difficulty=9, count=1),
    #     casting_time=Aspect(format="2.5 seconds ", base_difficulty=-2, count=1),
    #     name="Malfunction",
    #     other_aspects={
    #         "Arcane Knowledge": Aspect(
    #             format="Inanimate Forces", base_difficulty=0, count=1
    #         ),
    #         "Difficulty": Aspect(format="14", base_difficulty=0, count=1),
    #         "Components": Aspect(
    #             format="Small iron ball (common)", base_difficulty=-2, count=1
    #         ),
    #         "Gestures": Aspect(
    #             format="Throw component in direction of target (fairly simple)",
    #             base_difficulty=-2,
    #             count=1,
    #         ),
    #         "Incantations": Aspect(
    #             format="“Stop!” loudly (phrase)", base_difficulty=-2, count=1
    #         ),
    #     },
    #     other_conditions=[Aspect(
    #         format="Only harms mechanical devices", base_difficulty=-1, count=1
    #     )],
    #     notes="Any targeted metal object that has a mass of five kilograms\nor less can be permanently altered in shape. For instance, the\ncaster could transform a shield into a ball, thereby negating\nits protection. Or, the length of a metal rod could be extended\nto twice its length, although doing this makes it very thin.\nJust as easily could the barrel of a gun be twisted closed.\nBasically, whatever shape the magic user makes with the clay\ncomponent is paralleled with the target. (The player speci -\nfies the target and the shape, and the gamemaster compares\nthe effect’s value plus the casting’s result point bonus to the\nobject’s Toughness or damage resistance to determine whether\nthe object takes the new shape.) Magically imbued metal or\nmagically protected metal cannot be altered.",
    #     skill="unknown",
    # ),
    Spell(
        effect=Aspect(
            format="Natural Armor: Bronze Skin (R2), +2D Armor Value; +2D to charm/persuasion",
            base_difficulty=27,
            count=1,
        ),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        name="Man of Bronze",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Folk, metal", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="19", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Powdered bronze (uncommon, destroyed)",
                base_difficulty=-4,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=9, count=1),
            "Gestures": Aspect(
                format="Sprinkle powdered bronze over target (simple)",
                base_difficulty=-1,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="Deteriorates when exposed to moisture",
                base_difficulty=-2,
                count=1,
            )
        ],
        notes="Though bronze can be a fairly precious commodity, the\nvalue of this spell is well worth the expense. After simply\nsprinkling a handful of powdered bronze over a sentient\ntarget, the mage coats that individual’s skin in a thin layer\nof bronze that doesn’t hamper movement. It’s a strong as\nthe actual metal, offering an Armor Value of 2D against all\ntypes of physical (not mental) attacks. In addition, because\nof its rich, attractive coloration, the bronzed skin provides\na charm/persuasion skill bonus of +2D. The spell lasts for one\nhour, expect in moist environments where a greenish patina\nquickly forms and causes the spell to deteriorate rapidly.\nIn humid or damp environments (jungles or dungeons, for\nexample), the spell deteriorates at a rate of five minutes for\nevery one minute of exposure. In water, the rate is 10 minutes\nper minute of exposure.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="Natural Hand-to-Hand Weapon: Claws (R2), +2D damage",
            base_difficulty=12,
            count=1,
        ),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Metal Claws",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Metal", base_difficulty=0, count=1),
            "Difficulty": Aspect(
                format="14/20 (one claw/two claws)", base_difficulty=0, count=1
            ),
            "Components": Aspect(
                format="Two of any type of coin-sized metal: bronze, iron, and so on (very common)",
                base_difficulty=-2,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=6, count=1),
            "Incantations": Aspect(
                format="“Grow claws!.” (phrase, loud)", base_difficulty=-2, count=1
            ),
        },
        other_conditions=[
            Aspect(
                format="Target must hold coins in each hand",
                base_difficulty=-1,
                count=1,
            )
        ],
        notes="Once cast, three metal blades extend from each hand of the\ntarget. As these weapons are natural extensions of the char-\nacter, she uses brawling to fight with them. Each confers +2D\ndamage to an attack. Normal armor protection applies.\nAlthough they are not cumbersome, the claws do tend to\nstand out in a crowd.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="Armor Value of 8D, physical only", base_difficulty=24, count=1
        ),
        duration=Aspect(format="25 minutes ", base_difficulty=16, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        name="Metal Flesh",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Metal", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="16", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Iron slug (very common)", base_difficulty=-2, count=1
            ),
            "Countenance": Aspect(
                format="Target appears metallic", base_difficulty=-2, count=1
            ),
            "Focused": Aspect(format="On target", base_difficulty=8, count=1),
            "Incantations": Aspect(
                format="“I give you flesh of metal.” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="Cannot be combined with any other armor",
                base_difficulty=-1,
                count=1,
            )
        ],
        notes="This highly coveted spell transforms fleshy skin into a\nnearly impenetrable metal husk. It protects against normal\nand magical attacks. As the transmuted skin is as malleable\nas human flesh, at least to the target, there are no penalties\nfrom this spell. However, it is not easily disguised as any\ncharacter who has had metal flesh cast upon her is shiny and\nrings if tapped with any solid object.\nIt cannot be combined with any other armor, and the\ntarget cannot wear any form of metal armor when the spell\nis cast.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="6D+2 physical damage", base_difficulty=20, count=1),
        duration=Aspect(format="1 round ", base_difficulty=4, count=1),
        range=Aspect(format="60 meters ", base_difficulty=9, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=9, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Metal Storm",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Inanimate forces", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="29", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Sphere with radius of 5 meters", base_difficulty=25, count=1
            ),
            "Components": Aspect(
                format="A bag of tiny iron or lead pellets (common)",
                base_difficulty=-3,
                count=1,
            ),
            "Gestures": Aspect(
                format="Pour pellets into hand and toss into the air (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes="A rain of metal pellets bombards everyone in the designated\nfive-meter radius. The storm of metal is overwhelming, caus-\ning 6D+2 damage to all within the downpour. Normal and\nmagical armor offer protection, but the sheer volume of pro-\njectiles, and their velocity, is likely to cause severe injury.\n\n",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="Achilles’ Heel (R3), takes 1D in damage each round in contact with metal, increasing by 1D each round",
            base_difficulty=9,
            count=1,
        ),
        duration=Aspect(format="5 rounds ", base_difficulty=7, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Molten Metal",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Metal, inanimate forces", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="11", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Polished mirror (common)", base_difficulty=-3, count=1
            ),
            "Focused": Aspect(format="On target", base_difficulty=3, count=1),
            "Gestures": Aspect(
                format="Point mirror at target (simple)", base_difficulty=-1, count=1
            ),
        },
        notes="This spell is slow to reach its full potential, but it is likely to\ncause a combatant to stop fighting long enough to remove her\narmor or drop a metal weapon. Each round the spell is active,\nthe target receives 1D damage, which increases by 1D.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="damage resistance total of portcullis; 5D physical damage",
            base_difficulty=45,
            count=1,
        ),
        duration=Aspect(format="10 minute ", base_difficulty=14, count=1),
        range=Aspect(format="3.5 meters ", base_difficulty=3, count=1),
        speed=Aspect(
            format="1 meter per second/+2 to dodge total ",
            base_difficulty=2,
            count=1,
        ),
        casting_time=Aspect(format="2 rounds ", base_difficulty=-5, count=1),
        name="Portcullis",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Enchanted", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="28", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Final maximum height of 3 meters and width of 1 meter",
                base_difficulty=2,
                count=1,
            ),
            "Components": Aspect(
                format="Metal rod (common)", base_difficulty=-3, count=1
            ),
            "Gestures": Aspect(
                format="Swing hand in a downward motion (simple)",
                base_difficulty=-1,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="Can only be cast in an open portal", base_difficulty=-1, count=1
            )
        ],
        notes="The mage stands within a meter of an opening and projects\nthe spell upward. After the spell is cast, over the course of a\nround, an iron portcullis comes into existence. Its eventually\nspans up to three meters high and a meter wide.\nBecause the magical barrier is slow moving, it is possible\nto be captured beneath it as it slides to the ground. Any\nunfortunate character in this situation suffers 5D damage\nfrom the portcullis each round that she is trapped beneath its\nunrelenting grip. Unless the character is killed, this prevents\nthe portal from being completely blocked.\nOnce closed, the gate has a damage resistance totoal of\n30.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="Attack Resistance: Radiation (R6), +6D to damage resistance roll against related attacks",
            base_difficulty=36,
            count=1,
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Radiation Shield",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Inanimate forces", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="41", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Sphere with radius of 5 meters", base_difficulty=25, count=1
            ),
            "Components": Aspect(
                format="Small fragment of lead (very common)",
                base_difficulty=-2,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=9, count=1),
            "Gestures": Aspect(
                format="Clasp component in a fist (simple)", base_difficulty=-1, count=1
            ),
        },
        notes="This spell protects against the effects of radiation and\nelectro-magnetic radiation, such as from an EMP spell or\nsimilar device. The protection is granted to all within the\nfive-meter sphere of influence, with corresponding protec -\ntion reduced by 1D for each meter out from the cental target.\nCharacters gain a up to +6D to their resistance rolls against\nrelated damage.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="5D damage to ferrous metal", base_difficulty=15, count=1),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="100 meters ", base_difficulty=10, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=10, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Rain of Rust",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Metal", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="29", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Sphere with radius of 5 meters", base_difficulty=25, count=1
            ),
            "Components": Aspect(
                format="Small, rusting iron spike (very common)",
                base_difficulty=-2,
                count=1,
            ),
            "Gestures": Aspect(
                format="Point in direction of rain (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Incantations": Aspect(
                format="Repeated phrase for duration of spell (complex; willpower/mettle roll with difficulty of 11)",
                base_difficulty=-3,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(format="Affects ferrous metal only", base_difficulty=-1, count=1)
        ],
        notes="The mage produces a 25-meter radius downpour of red\nrain that rusts all ferrous metal. When cast, the mage simply\nindicates the location of the deluge by pointing, and the area\nis drenched with oxidizing water, causing 5Ddamage to all\nferrous metal in the affected area. It is possible to protect\nitems by wrapping them in cloth, skins, or plastic or locking\nthem in waterproof cases. Likewise, vehicles within the area\nsuffer immediate damage, starting from the outside and\nworking to the interior.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="Armor Value of 3D+1, physical only", base_difficulty=10, count=1
        ),
        duration=Aspect(format="1 hour ", base_difficulty=9, count=1),
        range=Aspect(format="10 meters ", base_difficulty=7, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=7, count=1),
        casting_time=Aspect(format="2 rounds ", base_difficulty=-5, count=1),
        name="Repel Metal",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Inanimate Forces", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="13", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Small magnet or loadstone (ordinary)",
                base_difficulty=-1,
                count=1,
            ),
            "Concentration": Aspect(
                format="1 round with willpower/mettle difficulty of 8",
                base_difficulty=-2,
                count=1,
            ),
            "Countenance": Aspect(
                format="Target surrounded by faint blue glow",
                base_difficulty=-1,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=3, count=1),
            "Gestures": Aspect(
                format="Wave hand as though to push aside something (simple)",
                base_difficulty=-1,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="Only works against damage caused by metal",
                base_difficulty=-1,
                count=1,
            )
        ],
        notes="All attacks made by weapons of metal are affected by this\nspell. The mage casts it upon a target, providing a 3D+1\nArmor Value against any attack that uses metal to damage.\nFor example, this spell offers protection against the spell\nmetal st orm, as the projectiles are metallic. For the dura -\ntion of the spell, the protected character is surrounded by\na faint blue glow. The effects of this spell are not limited to\nferrous metals.\n\n",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="5D+2 in appropriate skill, such as tech, devices, etc.",
            base_difficulty=17,
            count=1,
        ),
        duration=Aspect(format="1 day ", base_difficulty=25, count=1),
        range=Aspect(format="Touch ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Understand Inner Workings",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Inanimate forces", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="22", base_difficulty=0, count=1),
            "Focused": Aspect(format="On target", base_difficulty=8, count=1),
            "Gestures": Aspect(
                format="Touch machine and target (simple)", base_difficulty=-1, count=1
            ),
            "Incantations": Aspect(
                format="“Comprehend the secrets of this machine.” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes="Understanding of complex, alien, or arcane technologies\ncan be gained by casting this spell. (The gamemaster detemines\nthe difficulty of understanding the machine, with the result\npoints from the skill conferred by the spell used to determine\nwhat information the character gains.) Unfortunately, this\nknowledge lasts only as long as the spell endures. Once the\nmagic has elapsed, all comprehension of the technology\nvanishes as well.",
        skill="Divination",
    ),
    Spell(
        effect=Aspect(
            format="4D in appropriate skill for operating a specified vehicle",
            base_difficulty=12,
            count=1,
        ),
        duration=Aspect(format="1 day ", base_difficulty=25, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Understand Vehicle",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Inanimate forces", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="19", base_difficulty=0, count=1),
            "Focused": Aspect(format="On target", base_difficulty=7, count=1),
            "Gestures": Aspect(
                format="Touch machine and target (simple)", base_difficulty=-1, count=1
            ),
            "Incantations": Aspect(
                format="“Comprehend the secrets of this vehicle.” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes="A mage can grant the knowledge to pilot a vehicle at a 4D\nability with this spell. No protections or great insights are\nprovided, just the minimal knowledge necessary to operate\nthe vehicle. Should it malfunction or fail, the target does not\nhave the knowledge to repair the mechanical device, unless\nthat knowledge existed otherwise. This spell does not enhance\nan existing skill; it confers a new skill.",
        skill="Divination",
    ),
]

if __name__ == "__main__":
    detail(spells)


__test__ = {
    "Activate Automaton": ">>> spells[0].difficulty\n15",
    "Alter Trajectory": ">>> spells[1].difficulty\n21",
    "Armor": ">>> spells[2].difficulty\n12",
    "Attract Metal": ">>> spells[3].difficulty\n18",
    "Awaken Machine": ">>> spells[4].difficulty\n18",
    "Blunt": ">>> spells[5].difficulty\n11",
    "Skill: Divination": ">>> spells[6].difficulty\n36",
    "Control Machine": ">>> spells[7].difficulty\n18",
    "Corrosive Cloud": ">>> spells[8].difficulty\n20",
    "Automaton": ">>> spells[9].difficulty\n40",
    "Discern Alloy": ">>> spells[10].difficulty\n12",
    "EMP": ">>> spells[11].difficulty\n35",
    "Forge Perfect Weapon": ">>> spells[12].difficulty\n16",
    "Hone Edge": ">>> spells[13].difficulty\n15",
    "Locate Metal": ">>> spells[14].difficulty\n18",
    "Machine Terror": ">>> spells[15].difficulty\n28",
    "Magic Platter": ">>> spells[16].difficulty\n15",
    "Magnetism": ">>> spells[17].difficulty\n28",
    "Make Statue": ">>> spells[18].difficulty\n27",
    "Malfunction": ">>> spells[19].difficulty\n14",
    "Malleable": ">>> spells[20].difficulty\n17",
    "Man of Bronze": ">>> spells[21].difficulty\n19",
    "Metal Claws": ">>> spells[22].difficulty\n14",
    "Metal Flesh": ">>> spells[23].difficulty\n16",
    "Metal Storm": ">>> spells[24].difficulty\n29",
    "Molten Metal": ">>> spells[25].difficulty\n11",
    "Portcullis": ">>> spells[26].difficulty\n28",
    "Radiation Shield": ">>> spells[27].difficulty\n41",
    "Rain of Rust": ">>> spells[28].difficulty\n29",
    "Repel Metal": ">>> spells[29].difficulty\n13",
    "Understand Inner Workings": ">>> spells[30].difficulty\n22",
    "Understand Vehicle": ">>> spells[31].difficulty\n19",
}
