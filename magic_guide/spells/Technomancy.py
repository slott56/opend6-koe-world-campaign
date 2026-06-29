"""
Technomancy

When run as an app, generates .RST-formatted details of each Spell.
"""

from decimal import Decimal
from typing import Annotated, Any
import typer
from opend6_tools.magic2 import *


spells = [
    Spell(
        name="Activate Automaton",
        skill="Conjuration",
        notes="The game setting determines the components modifier.\nIn fantasy or pre-computer eras, robots are likely to be\nextremely rare, while post-computer or science fiction set -\ntings often have an abundance of robots. In any case, this\nspell does not give life to a machine. Rather, it imbues 3D to\nboth Agility/Reflexes and Physique/Strength. This means that\nthe mechanical device is capable of ambulation (at a rate of\nand physical acts such as lifting or attacking. However, to\ncontrol the device requires programming with the devices/\ntech/robot interface/repair skill. Instructions cannot be called\nout, as the automaton or robot has not been given the ability\nto understand speech. Automatons make useful guards and\nservants, and are occasionally handy in combat.",
        effect=SkillEffect(
            "Agility/Reflexes  and Physique/Strength of 3D each; movement equal to result points in meters round with minimum of 1 meter per round",
            *["+6D", "skill modifier"],
        ),
        duration=DurationAspect(measure="1 day"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="1 hour"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("inanimate forces, enchanted, metal"),
            # Two variants... Robot/automaton without power source (extremely rare/common)
            "components": ComponentsAspect(
                "-6 Robot without power source", "extremely rare"
            ),
            "gestures": GesturesAspect(
                "program instructions into robot, using devices/tech/robot interface/repair difficulty of 23",
                *["challenging"],
            ),
            "incantations": IncantationsAspect("'“Activate!” loudly'", *["phrase"]),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 15/17")],
    ),
    Spell(
        name="Alter Trajectory",
        skill="Alteration",
        notes="With the twist of a hand, the magic user can cause a ranged\nweapon to alter the interior shape of its barrel, bore, rifling and\nso on. Although the imperfection created is minor, requiring\na Moderate search to detect, it is sufficient to create a +12\ndifficulty modifier to marksmanship/firearms.",
        effect=DisadvantageEffect(
            "Hindrance: Altered Firearm ",
            4,
            note="+12 to marksmanship/firearms difficulties",
        ),
        duration=DurationAspect(measure="10 minutes"),
        range=RangeAspect(measure="100 meters"),
        casting_time=CastingTimeAspect(measure="2 rounds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Inanimate forces, metal"),
            "components": ComponentsAspect("Small, misshapen lead ball", "common"),
            "gestures": GesturesAspect("Make spiral motion with hand", *["simple"]),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On weapon"
            ),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-1,
                description="The target must be a ranged weapon that is manufactured of metal or has a metal component as part of its firing mechanism",
            ),
            GenericAspect(difficulty=0, description="Difficulty: 21"),
        ],
    ),
    Spell(
        name="Armor",
        skill="Conjuration",
        notes="This spell allows the caster to produce the equivalent of a\nbreastplate and grieves from a coin-sized fragment of metal.\nThis not only works wonderfully when passing through\nmetal detectors, but just as well when entering a monarch’s\nsanctuary. Regardless of the type of metal used, the armor\nis similar to bronze armor in quality and protection. Once\nit is conjured on a target, it cannot be removed unless the\nspell duration ends or the magic user halts it. The armor is\nseamless, and fits any form perfectly.",
        effect=SkillEffect("Armor Value of  , physical only", *["+2D"]),
        duration=DurationAspect(measure="1 hour"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="2.5 seconds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Metal"),
            "components": ComponentsAspect(
                "Any type of coin-sized metal: bronze, iron, and so on", "very common"
            ),
            "incantations": IncantationsAspect("'“Make armor!.”'", *["phrase"]),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On coin"
            ),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 12")],
    ),
    Spell(
        name="Attract Metal",
        skill="Alteration",
        notes="If the mage successfully casts this spell, then the victim\nattracts metal weapons, increasing their damage by pulling\nthem toward the character. The spell is not capable of auto-\nmatically causing damage; rather, it decreases the protection\noffered against any melee or magical or projectile weapons\nused against the target. For the duration of the spell, the\nfigure is surrounded by a faint red glow. The effect of this\nspell is not limited to ferrous metals.",
        effect=DisadvantageEffect(
            "Hindrance: Metal Attracts ", 6, note="; -6 to damage resistance total"
        ),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="10 meters"),
        casting_time=CastingTimeAspect(measure="2 rounds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Magic"),
            "components": ComponentsAspect("Small magnet or lodestone", "ordinary"),
            "concentration": ConcentrationAspect("1 round"),
            "countenance": CountenanceAspect(
                "Target surrounded by faint red glow", "noticeable"
            ),
            "gestures": GesturesAspect("Wave hand, welcoming something", *["simple"]),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-1,
                description="Hindrance only applies to attacks made by metal weapons or spells using metal",
            ),
            GenericAspect(difficulty=0, description="Difficulty: 18"),
        ],
    ),
    Spell(
        name="Awaken Machine",
        skill="Conjuration",
        notes="The spell only activates any weapon mounted upon the\nmachine, conveying 3D in one combat skill (chosen at cast-\ning with +2D to its weapon’s damage. The weapon used\ndetermines the amount of damage.\nEven though the device may have legs, tracks or another\nform of locomotion, the spell does not cause it to move.\nThe contraption is incapable of thought. But, through magic\nand mechanical gimmickry, once awakened, it fights with\nthe skill of a moderately trained warrior. Often such devices\nare place in corridors for protection, or hidden beneath false\nfloors as a trap.\n\n",
        effect=CompositeEffect(
            "Machine",
            SkillEffect("one combat skill", "+3D", "skill modifier"),
            DamageEffect("physical damage", "2D", "physical damage"),
        ),
        duration=DurationAspect(measure="1 day"),
        range=RangeAspect(measure="40 meters"),
        casting_time=CastingTimeAspect(measure="1 hour"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Inanimate Forces"),
            "components": ComponentsAspect(
                "A mechanical device that has a weapon", "very rare"
            ),
            "concentration": ConcentrationAspect("1 hour"),
            "incantations": IncantationsAspect("'“Tick!'", *["phrase"]),
            "other_alterant": OtherAlterant(3, "Will attack anything that moves within 3 meters of it"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Difficulty: 18"),
        ],
    ),
    Spell(
        name="Blunt",
        skill="Alteration",
        notes="This spell dulls a weapons edge. When successfully cast,\nthe weapon has a -2D damage modifier, with a minimum\nadjusted damage value for the weapon of +1D. Any blade that\nis blunted to +1D becomes something akin to a metal stick.\nMagic weapons are not affected by this spell.",
        effect=SkillEffect("physical damage modifier", *["+2D", "damage modifier"]),
        duration=DurationAspect(measure="1.5 minutes"),
        range=RangeAspect(measure="10 meters"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Metal"),
            "components": ComponentsAspect("Stone", "ordinary"),
            "gestures": GesturesAspect(
                "Wave stone as though hammering the edge of a weapon", *["simple"]
            ),
            "incantations": IncantationsAspect("'“Blunt!.”'", *["phrase", "loud"]),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On weapon"
            ),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-1, description="Must be a metal, edged, nonmagical weapon"
            ),
            GenericAspect(difficulty=0, description="Difficulty: 12"),
        ],
    ),
    Spell(
        name="Construct Small Automaton",
        skill="Divination",
        notes="The game setting determines the components needed. The\nautomaton is usually a mechanical contraption of limited\ncapability. Typically such machines do not possess the faculty\nof cognitive thought. Instead, they are controlled by\nspells such as Activate Automaton, which allow for limited\nfunction. However, the first step is constructing the device.\nA successful casting of this spell allows for the construction\nof a human sized creation. The gamemaster should have the\nplayer’s characters follow the rules for the skill  device, and\npossibly make some of the require components very difficult\nto acquire — having a world populated by automatons can\nbe interested and dangerous.\n\nThe first step is developing the blue prints This is done\nby achieving using the table for Complexity of Device in\n“Example Skill Difficulties” chapter. The gamemaster must\ndecide upon the technological level of the culture. In most\ncases, an automaton is as prototype (+10) and is from a much\nhigher culture (+10), resulting in a minimum +20 modifier.\nWith research, this modifier might be altered. Each roll takes\none month. The base difficulty for drawing up the blueprints\nis Very Difficult. However, the gamemaster should count\nprevious failures as bonus modifiers, as the hero learns from\nher mistakes.\n\nAfter the blueprints have been created, the construction\ncommences. Now the crafting skill is used to construct the\nautomaton. Again, the related table from the “Example Skill Difficulties” \nchapter should be used. The number of\ncomponents that have been gathered, their quality and the\nclarity of the blueprints determine the modifiers used for\nconstructing an automaton. The base difficulty is Very Difficult. \nEach attempt to construct the device takes 2 months.\nThe gamemaster should consider previous failures as bonus\nmodifiers for future attempts.\n\nAt the end of the spell’s duration, the skills are lost, but the\nknowledge is not. If the attempt to build an automaton was\nnot successful, then the gamemaster should apply bonuses\nfor the next attempt for gained experience.\n",
        effect=CompositeEffect(
            "Several Skills",
            SkillEffect(
            "device skill", "8D"),
            SkillEffect("craft skill", "6D"),
            Effect("materials", 10)
        ),
        duration=DurationAspect(measure="1 year"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="1 week"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect(
                "A variety of materials are needed, ranging from the mundane to a flawless gem or some other such rare item to energize the automaton", "uncommon; rare"
            ),
            "incantations": IncantationsAspect(
                "'“Understand.” whispered'", *["phrase"]
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 36")],
    ),
    Spell(
        name="Control Machine",
        skill="Alteration",
        notes="If the caster uses this spell in a setting without the elec -\ntronic networks, then the machine must be within reach of\nthe target. A successful casting provides the target with a +18\nto her devices/tech/robot (or computer) interface/repair totals.\nThe setting and the devices that the caster intends the target\nto affect dictate the skill that gets the bonus.",
        effect=SpecialAbilityEffect(
            "Skill Bonus ",
            6,
            note=", +18 to devices/tech/robot (or computer) interface/repair  totals",
        ),
        duration=DurationAspect(measure="1 hour"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="4 rounds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Inanimate forces, metal"),
            "components": ComponentsAspect(
                "Wire or similar piece of metal", "ordinary"
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-1,
                description="The target must be able to touch the device or connect to it electronically",
            ),
            GenericAspect(difficulty=0, description="Difficulty: 18"),
        ],
    ),
    Spell(
        name="Corrosive Cloud",
        skill="Conjuration",
        notes="Casting this spell creates as green haze. All metal within it\nsuffers 5D of corrosive damage unless magically protected.\nThe cloud is so dense as to require any living creatures inside\nto make a Moderate Physique/Strength o r  stamina roll. Failure\nresults in choking (and the targets lose their next action).\nEach round the cloud remains over a metal target, it suffers\nan additional 5D of damage until it is destroyed\nFor the duration of the spell, the caster must continue the\nlitany that invokes the mystical cloud.",
        effect=SkillEffect(
            "physical damage to metal; living creatures lose one action if fail resistance roll",
            *["+5D"],
        ),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="100 meters"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Metal"),
            "area_effect": AreaEffectAspect("1m radius sphere"),
            "components": ComponentsAspect(
                "Small vile of acidic liquid, such as juice from a lemon or lime", "very common"
            ),
            "gestures": GesturesAspect(
                "Point in direction of cloud location", *["simple"]
            ),
            "incantations": IncantationsAspect(
                "'Repeated phrase for duration of spell'", *["sentence"]
            ),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 20")],
    ),
    Spell(
        name="Construct Tremendous Automaton",
        skill="Divination",
        notes="This spell work identically to Construct Small Automaton See\nthat spell for specifics. Note the differences are in size, casting\ndifficulty and duration. Blueprint design and construction\ntimes are doubled. Otherwise, all other aspects apply.",
        effect=CompositeEffect(
            "Skills and Materials",
            SkillEffect("device skill", "8D"),
            SkillEffect("craft skill", "6D"),
            Effect("materials", 22),
        ),
        duration=DurationAspect(measure="2 year"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="1 week"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Inanimate Forces"),
            "components": ComponentsAspect(
                "A variety of materials are needed, ranging from the mundane to a flawless gem or some other such rare item to energize the automaton", "uncommon; rare"
            ),
            "incantations": IncantationsAspect(
                "'“Understand.” whispered'", *["phrase"]
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-6,
                description="Large quantities and cumbersome materials, tools and devices are needed, as well as funding; additionally, a large location is needed to construct monstrous creation",
            ),
            GenericAspect(difficulty=0, description="Difficulty: 40"),
        ],
    ),
    Spell(
        name="Discern Alloy",
        skill="Divination",
        notes="Even if the caster has no knowledge of various metals and\nalloys, this spell allows her to perceive what was used to make\na given object. This is useful when encountering strange alien\nobjects or when attempting to see how strong a weapon, door,\nor similar item is. Upon successfully casting discern alloy, the\nmagic user gains a +24 bonus to her investigation totals in\norder to figure out the type of metal used. The difficulty is\ndetermined by the gamemaster.\n\n",
        effect=SpecialAbilityEffect(
            "Skill Bonus ",
            8,
            note="+24 to investigation totals for purposes of determining metal",
        ),
        duration=DurationAspect(measure="1 round"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Metal"),
            "gestures": GesturesAspect("Move hands across the object", *["simple"]),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 12")],
    ),
    Spell(
        name="EMP",
        skill="Conjuration",
        notes="Any electronic equipment in the area effect of this spell\nsuffers 10D damage from an electro-magnetic pulse. As this\neffect is caused by altering the inanimate forces of nature,\ninstead of exploding a bomb, there is no damage done to most\nliving beings or to devices that do not have electronics.",
        effect=DamageEffect("10D physical damage", *["+10D"]),
        duration=DurationAspect(measure="1 round"),
        range=RangeAspect(measure="100 meters"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Inanimate Forces"),
            "area_effect": AreaEffectAspect("5m radius sphere"),
            "components": ComponentsAspect("Small magnet or lodestone", "ordinary"),
            "incantations": IncantationsAspect("'“Pulse!”'", *["phrase", "loud"]),
        },
        other_conditions=[
            GenericAspect(difficulty=-2, description="Only affects electrical devices"),
            GenericAspect(difficulty=0, description="Difficulty: 35"),
        ],
    ),
    Spell(
        name="Forge Perfect Weapon",
        skill="Alteration",
        notes="To gain the bonus from a successful casting of this spell,\nthe target must have some training in crafting/repair/personal\nequipment repair; otherwise, the magical knowledge is lost.\nIn order for a perfect weapon to be properly crafted, not\nonly are the raw materials, forge, and ancillary equipment\nneeded, but a crafting/repair/personal equipment repair  roll\nwith a difficulty of Heroic is required to forge the item. The\ngamemaster may use the result points from the forging skill\nroll to give bonuses to the superior pieces of equipment.",
        effect=SpecialAbilityEffect(
            "Skill Bonus ",
            10,
            note="+30 crafting/repair/personal equipment repair totals",
        ),
        duration=DurationAspect(measure="1 day"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 hour"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Metal"),
            "components": ComponentsAspect(
                ("Raw material for weapon", "common"),
                ("forging tools and forge", "uncommon"),
            ),
            "concentration": ConcentrationAspect("1 hour"),
            "gestures": GesturesAspect(
                "Touch raw material with small hammer", *["simple"]
            ),
            "incantations": IncantationsAspect("'“Flawless.”'", *["phrase"]),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-1,
                description="Must possess some experience in the affected skill",
            ),
            GenericAspect(difficulty=0, description="Difficulty: 16"),
        ],
    ),
    Spell(
        name="Hone Edge",
        skill="Alteration",
        notes="This spell places a magically keen edge upon a weapon,\nincreasing its damage by +2D+2. Any weapon with this spell\ncast upon it gains a faint blue shine to its surface, as the\nmagic reshapes the metal to the molecular level, honing the\nblade’s edge to that of a single atom. For the duration of this\nspell, there is no material that cannot be cut or damaged by\nthe magical edge, even though normal or magical protection\nmight hinder damage.",
        effect=SkillEffect("physical damage modifier", *["+2D+2", "damage modifier"]),
        duration=DurationAspect(measure="1 hour"),
        range=RangeAspect(measure="10 meters"),
        casting_time=CastingTimeAspect(measure="3 rounds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Metal"),
            "components": ComponentsAspect("Whetstone", "common"),
            "countenance": CountenanceAspect(
                "Weapon gains faint blue shine", "noticeable"
            ),
            "gestures": GesturesAspect(
                "Move whetstone as though sharpening a weapon", *["simple"]
            ),
            "incantations": IncantationsAspect(
                "'“I whet your blunt purpose!”'", *["sentence", "loud"]
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On weapon"
            ),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-1,
                description="Only works on a nonmagical, metal, edged weapon",
            ),
            GenericAspect(difficulty=0, description="Difficulty: 15"),
        ],
    ),
    Spell(
        name="Locate Metal",
        skill="Divination",
        notes="Once the metal is named, the spell is complete. Immediately,\nthe mage can roll search at 4D to locate the prescribed metal\ninside an item, the earth, or a living being. Sometimes this\nspell is used to locate trace amounts of a particular metal,\nsuch as mercury or uranium. If there is anything of interest\nin the indicated area, a luminous yellow glow surrounds the\nlocation of the metal for up to one minute. The brilliance is\ndetermined by the quantity or density of the metal in searched\nfor. The higher the search total is above the difficulty, the more\ninformation the caster gleans from her  attempt, including\nlocation, depth, quantity, etc. The gamemaster decides on the\ndifficulty, which depends on how well hidden the material is\nand how much is there.",
        effect=SkillEffect("search to detect a single type of metal", *["+4D"]),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="40 meters"),
        casting_time=CastingTimeAspect(measure="1 minute"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Metal"),
            "area_effect": AreaEffectAspect("3.5m radius divination sphere"),
            "component": ComponentsAspect("Forked stick", "ordinary"),
            "concentration": ConcentrationAspect("1 minute"),
            "incantations": IncantationsAspect("'Name of the metal'", *["phrase"]),
            "variable_movement": VariableMovementAspect("bend around smaller", "target invisible "),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Difficulty: 18"),
        ],
    ),
    Spell(
        name="Machine Terror",
        skill="Conjuration",
        notes="Regardless of the type of contraption, the spell make a\nmachine capable of stimulating terror in anyone within sight\nof the device. Anyone who fails an opposed interaction roll\nagainst the machine’s intimdation loses her next action. The\nmachine terrorizes once per round for the duration of the\nspell. This is a way of making a trap, automaton, robot, and\nso on appear far more frightening than it may actually be.\n\n",
        effect=SkillEffect("intimidation", *["+8D+1"]),
        duration=DurationAspect(measure="10 minutes"),
        range=RangeAspect(measure="100 meters"),
        casting_time=CastingTimeAspect(measure="1 minute"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Enchanted"),
            "components": ComponentsAspect("Metal shards", "ordinary"),
            "gestures": GesturesAspect("Point at target", *["simple"]),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On machine"
            ),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 28")],
    ),
    Spell(
        name="Magic Platter",
        skill="Apportation",
        notes="The caster transforms a coin into a floating platter capable\nof carrying 100 kilograms of weight. To direct it, all that needs\nto be done is to point. If the magic user indicates herself, then\nthe tray follows her. Otherwise, she must guide it. Providing\na character is 100 kilograms or less, it is possible for her to\nride or be carried by the platter.",
        effect=MassEffect("moves up to", *["100 kilograms"]),
        duration=DurationAspect(measure="1 week"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 hour"),  # Rules have 1 minute, difficulty -18.
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Inanimate Forces"),
            "area_effect": AreaEffectAspect("1m radius circle"),
            "components": ComponentsAspect(
                "Small piece of metal or coin", "ordinary"
            ),
            "gestures": GesturesAspect("Point", *["simple"]),
            "incantations": IncantationsAspect("'“Carry.”'", *["phrase"]),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On metal"
            ),
            "variable_movement": VariableMovementAspect("2.5 meters")
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Difficulty: 15"),
        ],
    ),
    Spell(
        name="Magnetism",
        skill="Conjuration",
        notes="Once cast, this spell is not very discerning: All ferrous\nobjects within its radius are pulled toward the lodestone. The\nmagic user throws the stone in a direction that works best\nagainst any enemy, making sure to stay clear herself. Anyone\nwearing metal must make a Physique/Strength or lifting/lift\nagainst the effect’s difficulty. Failure means the affected object\nis yanked free and pulled toward the lodestone at a speed of\none meter per round. If ferrous armor is being worn, then the\ncharacter wearing the armor moves as well. (Non-character\nobjects automatically move toward the stone.)\nAnother effect this spell has is to cause all mechanical\ndevices with metals influenced by magnetism to stop func-\ntioning, as well as being pulled toward the lodestone.\n\n",
        effect=Effect(description="difficulty to resist the pull", difficulty=20),
        duration=DurationAspect(measure="5 rounds"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Inanimate Forces"),
            "area_effect": AreaEffectAspect("5m radius sphere"),
            "components": ComponentsAspect("Small magnet or lodestone", "ordinary"),
            "gestures": GesturesAspect(
                "Throw lodestone", *["complex (throwing roll with difficulty of 11)"]
            ),
            "incantations": IncantationsAspect("'“Pull!.”'", *["phrase", "loud"]),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On magnet"
            ),
            "other_alterants": OtherAlterant(8, "Metal objects move toward magnet at rate of 1 meter per round; mechanical devices within spell’s influence stop working for duration of spell")
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Difficulty: 28"),
        ],
    ),
    Spell(
        name="Make Statue",
        skill="Alteration",
        notes="A mage who successfully casts this spell and makes the\nnecessary targeting roll causes 12D damage that nonmagi -\ncal armor offers no protection against. The spell alters the\ncomposition of the target, attempting to refigure her into\nan iron statue. If the damage is sufficient to cause death,\nthen she becomes a statue. This is permanent damage. The\ncharacter cannot be resurrected, as there is no living material\nto bring back to life. Instead, she has become an ornament\nfor someone’s garden or great hall.",
        effect=SkillEffect("physical damage", *["+12D", "physical damage", "ignores nonmagical armor"]),
        duration=DurationAspect(measure="1 second"),
        range=RangeAspect(measure="5 meters"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Metal"),
            "components": ComponentsAspect("Iron statue", "uncommon"),
            "gestures": GesturesAspect("Point at target with statue", *["simple"]),
            "incantations": IncantationsAspect("'“Statue!.”'", *["phrase", "loud"]),
            "other_alterant": OtherAlterant(3, "Target turns into a statue if she dies"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Difficulty: 27"),
        ],
    ),
    Spell(
        name="Malfunction",
        skill="Conjuration",
        notes="Sometimes it is best to fight metal with metal. When cast,\nthis spell sends a searing bolt of energy at the target, doing\n6D damage. This spell has only works against machines, as it\nuses the same forces of physics (and sometimes magic) that\nproduced the construct to destroy it. No harm comes to a\nliving, undead, or any other creature that is not mechanical\nin nature. Certainly robots are affected by this spell, as are\ncyborgs. However, only the mechanical parts of a cyborg are\ndamaged; the living flesh is unharmed.",
        effect=SkillEffect("  damage against machines", *["+6D"]),
        duration=DurationAspect(measure="1 second"),
        range=RangeAspect(measure="60 meters"),
        casting_time=CastingTimeAspect(measure="2.5 seconds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Inanimate Forces"),
            "components": ComponentsAspect("Small iron ball", "common"),
            "gestures": GesturesAspect(
                "Throw component in direction of target", *["simple"]
            ),
            "incantations": IncantationsAspect("'“Stop!” loudly'", *["phrase"]),
        },
        other_conditions=[
            GenericAspect(difficulty=-1, description="Only harms mechanical devices"),
            GenericAspect(difficulty=0, description="Difficulty: 14"),
        ],
    ),
    Spell(
        name="Malleable",
        skill="Alteration",
        notes="Any targeted metal object that has a mass of five kilograms\nor less can be permanently altered in shape. For instance, the\ncaster could transform a shield into a ball, thereby negating\nits protection. Or, the length of a metal rod could be extended\nto twice its length, although doing this makes it very thin.\nJust as easily could the barrel of a gun be twisted closed.\nBasically, whatever shape the magic user makes with the clay\ncomponent is paralleled with the target. (The player speci -\nfies the target and the shape, and the gamemaster compares\nthe effect’s value plus the casting’s result point bonus to the\nobject’s Toughness or damage resistance to determine whether\nthe object takes the new shape.) Magically imbued metal or\nmagically protected metal cannot be altered.",
        effect=Effect(
            description="Compare to item’s Toughness or damage resistance", difficulty=25
        ),
        duration=DurationAspect(measure="1 round"),
        range=RangeAspect(measure="60 meters"),
        casting_time=CastingTimeAspect(measure="2 rounds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Metal"),
            "components": ComponentsAspect("Malleable clay", "very common"),
            "concentration": ConcentrationAspect("2 rounds"),
            "gestures": GesturesAspect("Shape the clay", *["simple"]),
            "incantations": IncantationsAspect("'“Alter.”'", *["phrase"]),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-1,
                description="The target must be nonmagical, metal, and no more than 5 kilograms",
            ),
            GenericAspect(difficulty=0, description="Difficulty: 17"),
        ],
    ),
    Spell(
        name="Man of Bronze",
        skill="Conjuration",
        notes="Though bronze can be a fairly precious commodity, the\nvalue of this spell is well worth the expense. After simply\nsprinkling a handful of powdered bronze over a sentient\ntarget, the mage coats that individual’s skin in a thin layer\nof bronze that doesn’t hamper movement. It’s a strong as\nthe actual metal, offering an Armor Value of 2D against all\ntypes of physical (not mental) attacks. In addition, because\nof its rich, attractive coloration, the bronzed skin provides\na charm/persuasion skill bonus of +2D. The spell lasts for one\nhour, expect in moist environments where a greenish patina\nquickly forms and causes the spell to deteriorate rapidly.\nIn humid or damp environments (jungles or dungeons, for\nexample), the spell deteriorates at a rate of five minutes for\nevery one minute of exposure. In water, the rate is 10 minutes\nper minute of exposure.",
        effect=CompositeEffect(
            "Skin of bronze",
            SpecialAbilityEffect("Natural Armor: Bronze Skin", 2, note="+2D Armor Value"),
            SkillEffect("charm/persuasion", *["+2D", "skill modifier"]),

        ),
        duration=DurationAspect(measure="1 hour"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 minute"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Folk, metal"),
            "components": ComponentsAspect("Powdered bronze", "uncommon"),
            "gestures": GesturesAspect(
                "Sprinkle powdered bronze over target", *["simple"]
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-2, description="Deteriorates when exposed to moisture"
            ),
            GenericAspect(difficulty=0, description="Difficulty: 19"),
        ],
    ),
    Spell(
        name="Metal Claws",
        skill="Conjuration",
        notes="Once cast, three metal blades extend from each hand of the\ntarget. As these weapons are natural extensions of the char-\nacter, she uses brawling to fight with them. Each confers +2D\ndamage to an attack. Normal armor protection applies.\nAlthough they are not cumbersome, the claws do tend to\nstand out in a crowd.",
        effect=SpecialAbilityEffect(
            "Natural Hand-to-Hand Weapon: Claws", 2, note="damage +2D"
        ),
        duration=DurationAspect(measure="1 hour"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Metal"),
            "components": ComponentsAspect(
                "Two of any type of coin-sized metal: bronze, iron, and so on", "very common"
            ),
            "incantations": IncantationsAspect("'“Grow claws!.”'", *["phrase", "loud"]),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-1, description="Target must hold coins in each hand"
            ),
            GenericAspect(
                difficulty=0, description="Difficulty: 12/18 (one claw/two claws)"
            ),
        ],
    ),
    Spell(
        name="Metal Flesh",
        skill="Conjuration",
        notes="This highly coveted spell transforms fleshy skin into a\nnearly impenetrable metal husk. It protects against normal\nand magical attacks. As the transmuted skin is as malleable\nas human flesh, at least to the target, there are no penalties\nfrom this spell. However, it is not easily disguised as any\ncharacter who has had metal flesh cast upon her is shiny and\nrings if tapped with any solid object.\nIt cannot be combined with any other armor, and the\ntarget cannot wear any form of metal armor when the spell\nis cast.",
        effect=SkillEffect("Armor Value of  , physical only", *["+8D"]),
        duration=DurationAspect(measure="25 minutes"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 minute"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Metal"),
            "components": ComponentsAspect("Iron slug", "very common"),
            "countenance": CountenanceAspect("Target appears metallic", "noticeable"),
            "incantations": IncantationsAspect(
                "'“I give you flesh of metal.”'", *["sentence"]
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-1, description="Cannot be combined with any other armor"
            ),
            GenericAspect(difficulty=0, description="Difficulty: 16"),
        ],
    ),
    Spell(
        name="Metal Storm",
        skill="Alteration",
        notes="A rain of metal pellets bombards everyone in the designated\nfive-meter radius. The storm of metal is overwhelming, caus-\ning 6D+2 damage to all within the downpour. Normal and\nmagical armor offer protection, but the sheer volume of pro-\njectiles, and their velocity, is likely to cause severe injury.\n\n",
        effect=SkillEffect("physical damage", *["+6D+2", "physical damage"]),
        duration=DurationAspect(measure="1 round"),
        range=RangeAspect(measure="60 meters"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Inanimate forces"),
            "area_effect": AreaEffectAspect("5m radius sphere"),
            "components": ComponentsAspect(
                "A bag of tiny iron or lead pellets", "common"
            ),
            "gestures": GesturesAspect(
                "Pour pellets into hand and toss into the air", *["simple"]
            ),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 29")],
    ),
    Spell(
        name="Molten Metal",
        skill="Alteration",
        notes="This spell is slow to reach its full potential, but it is likely to\ncause a combatant to stop fighting long enough to remove her\narmor or drop a metal weapon. Each round the spell is active,\nthe target receives 1D damage, which increases by 1D.",
        effect=DisadvantageEffect(
            "Achilles’ Heel", 3, note="takes   in damage each round in contact with metal, increasing by 1D each round",
        ),
        duration=DurationAspect(measure="5 rounds"),
        range=RangeAspect(measure="10 meters"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Metal, inanimate forces"),
            "components": ComponentsAspect("Polished mirror", "common"),
            "gestures": GesturesAspect("Point mirror at target", *["simple"]),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 11")],
    ),
    Spell(
        name="Portcullis",
        skill="Conjuration",
        notes="The mage stands within a meter of an opening and projects\nthe spell upward. After the spell is cast, over the course of a\nround, an iron portcullis comes into existence. Its eventually\nspans up to three meters high and a meter wide.\nBecause the magical barrier is slow moving, it is possible\nto be captured beneath it as it slides to the ground. Any\nunfortunate character in this situation suffers 5D damage\nfrom the portcullis each round that she is trapped beneath its\nunrelenting grip. Unless the character is killed, this prevents\nthe portal from being completely blocked.\nOnce closed, the gate has a damage resistance totoal of\n30.",
        effect=CompositeEffect(
            "Portcullis Slides to the Ground",
            ProtectionEffect(
            "damage resistance total of portcullis", "10D"),
            DamageEffect("physical damage", *["+5D", "physical damage"]),
        ),
        duration=DurationAspect(measure="10 minute"),
        range=RangeAspect(measure="3.5 meters"),
        casting_time=CastingTimeAspect(measure="2 rounds"),
        speed=SpeedAspect(measure="1 meter", note="+2 to dodge total "),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Enchanted"),
            "area_effect": AreaEffectAspect("3m height 1m width wall"),
            "components": ComponentsAspect("Metal rod", "common"),
            "gestures": GesturesAspect("Swing hand in a downward motion", *["simple"]),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-1, description="Can only be cast in an open portal"
            ),
            GenericAspect(difficulty=0, description="Difficulty: 28"),
        ],
    ),
    Spell(
        name="Radiation Shield",
        skill="Conjuration",
        notes="This spell protects against the effects of radiation and\nelectro-magnetic radiation, such as from an EMP spell or\nsimilar device. The protection is granted to all within the\nfive-meter sphere of influence, with corresponding protec -\ntion reduced by 1D for each meter out from the cental target.\nCharacters gain a up to +6D to their resistance rolls against\nrelated damage.",
        effect=SpecialAbilityEffect(
            "Attack Resistance: Radiation", 6, note="+6D to damage resistance roll against related attacks",
        ),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="10 meters"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Inanimate forces"),
            "area_effect": AreaEffectAspect("5m radius sphere"),
            "components": ComponentsAspect("Small fragment of lead", "very common"),
            "gestures": GesturesAspect("Clasp component in a fist", *["simple"]),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 41")],
    ),
    Spell(
        name="Rain of Rust",
        skill="Conjuration",
        notes="The mage produces a 25-meter radius downpour of red\nrain that rusts all ferrous metal. When cast, the mage simply\nindicates the location of the deluge by pointing, and the area\nis drenched with oxidizing water, causing 5Ddamage to all\nferrous metal in the affected area. It is possible to protect\nitems by wrapping them in cloth, skins, or plastic or locking\nthem in waterproof cases. Likewise, vehicles within the area\nsuffer immediate damage, starting from the outside and\nworking to the interior.",
        effect=SkillEffect("  damage to ferrous metal", *["+5D"]),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="100 meters"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Metal"),
            "area_effect": AreaEffectAspect("5m radius sphere"),
            "components": ComponentsAspect(
                "Small, rusting iron spike", "very common"
            ),
            "gestures": GesturesAspect("Point in direction of rain", *["simple"]),
            "incantations": IncantationsAspect(
                "'Repeated phrase for duration of spell'",
                *["complex (willpower/mettle roll with difficulty of 11)"],
            ),
        },
        other_conditions=[
            GenericAspect(difficulty=-1, description="Affects ferrous metal only"),
            GenericAspect(difficulty=0, description="Difficulty: 29"),
        ],
    ),
    Spell(
        name="Repel Metal",
        skill="Alteration",
        notes="All attacks made by weapons of metal are affected by this\nspell. The mage casts it upon a target, providing a 3D+1\nArmor Value against any attack that uses metal to damage.\nFor example, this spell offers protection against the spell\nmetal st orm, as the projectiles are metallic. For the dura -\ntion of the spell, the protected character is surrounded by\na faint blue glow. The effects of this spell are not limited to\nferrous metals.\n\n",
        effect=SkillEffect("Armor", *["+3D+1", "physical only"]),
        duration=DurationAspect(measure="1 hour"),
        range=RangeAspect(measure="10 meters"),
        casting_time=CastingTimeAspect(measure="2 rounds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Inanimate Forces"),
            "components": ComponentsAspect("Small magnet or lodestone", "ordinary"),
            "concentration": ConcentrationAspect("1 round"),
            "countenance": CountenanceAspect(
                "Target surrounded by faint blue glow", "noticeable"
            ),
            "gestures": GesturesAspect(
                "Wave hand as though to push aside something", *["simple"]
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-1, description="Only works against damage caused by metal"
            ),
            GenericAspect(difficulty=0, description="Difficulty: 13"),
        ],
    ),
    Spell(
        name="Understand Inner Workings",
        skill="Divination",
        notes="Understanding of complex, alien, or arcane technologies\ncan be gained by casting this spell. (The gamemaster detemines\nthe difficulty of understanding the machine, with the result\npoints from the skill conferred by the spell used to determine\nwhat information the character gains.) Unfortunately, this\nknowledge lasts only as long as the spell endures. Once the\nmagic has elapsed, all comprehension of the technology\nvanishes as well.",
        effect=SkillEffect(
            "Boost appropriate skill, such as tech, devices, etc.", *["+5D+2"]
        ),
        duration=DurationAspect(measure="1 day"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Inanimate forces"),
            "gestures": GesturesAspect("Touch machine and target", *["simple"]),
            "incantations": IncantationsAspect(
                "'“Comprehend the secrets of this machine.”'", *["sentence"]
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 22")],
    ),
    Spell(
        name="Understand Vehicle",
        skill="Divination",
        notes="A mage can grant the knowledge to pilot a vehicle at a 4D\nability with this spell. No protections or great insights are\nprovided, just the minimal knowledge necessary to operate\nthe vehicle. Should it malfunction or fail, the target does not\nhave the knowledge to repair the mechanical device, unless\nthat knowledge existed otherwise. This spell does not enhance\nan existing skill; it confers a new skill.",
        effect=SkillEffect(
            "Gain appropriate skill for operating a specified vehicle", *["+4D"]
        ),
        duration=DurationAspect(measure="1 day"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Inanimate forces"),
            "gestures": GesturesAspect("Touch machine and target", *["simple"]),
            "incantations": IncantationsAspect(
                "'“Comprehend the secrets of this vehicle.”'", *["sentence"]
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Difficulty: 19")],
    ),
]


__test__ = {
    "Activate Automaton": ">>> spells[0].difficulty\n16",  # Rules say 17
    "Alter Trajectory": ">>> spells[1].difficulty\n20", # Rules say 21
    "Armor": ">>> spells[2].difficulty\n12",
    "Attract Metal": ">>> spells[3].difficulty\n15",  # Rules say 18, range is wrong
    "Awaken Machine": ">>> spells[4].difficulty\n17",  # Rules say 18
    "Blunt": ">>> spells[5].difficulty\n12",
    "Construct Small Automaton": ">>> spells[6].difficulty\n35",  # Rules say 36
    "Control Machine": ">>> spells[7].difficulty\n17", # Rules say 18
    "Corrosive Cloud": ">>> spells[8].difficulty\n20",
    "Construct Tremendous Automaton": ">>> spells[9].difficulty\n40",
    "Discern Alloy": ">>> spells[10].difficulty\n11",  # Rules say 12
    "EMP": ">>> spells[11].difficulty\n35",
    "Forge Perfect Weapon": ">>> spells[12].difficulty\n16",
    "Hone Edge": ">>> spells[13].difficulty\n15",
    "Locate Metal": ">>> spells[14].difficulty\n19",  # Rules say 18
    "Machine Terror": ">>> spells[15].difficulty\n28",
    "Magic Platter": ">>> spells[16].difficulty\n15",  # Rules have casting time wrong
    "Magnetism": ">>> spells[17].difficulty\n28",
    "Make Statue": ">>> spells[18].difficulty\n27",
    "Malfunction": ">>> spells[19].difficulty\n14",
    "Malleable": ">>> spells[20].difficulty\n17",
    "Man of Bronze": ">>> spells[21].difficulty\n19",
    "Metal Claws": ">>> spells[22].difficulty\n14",  # Rules say 12 for 1, 18 for 2,
    "Metal Flesh": ">>> spells[23].difficulty\n17",  # Rules say 16
    "Metal Storm": ">>> spells[24].difficulty\n29",
    "Molten Metal": ">>> spells[25].difficulty\n10",  # Rules say 11
    "Portcullis": ">>> spells[26].difficulty\n27",  # Rules say 28
    "Radiation Shield": ">>> spells[27].difficulty\n41",
    "Rain of Rust": ">>> spells[28].difficulty\n29",
    "Repel Metal": ">>> spells[29].difficulty\n16",  # Rules say 13, duration and range are wrong
    "Understand Inner Workings": ">>> spells[30].difficulty\n21",  # Rules say 22
    "Understand Vehicle": ">>> spells[31].difficulty\n18",  # Rules say 19
}

if __name__ == "__main__":
    app = build_app(spells)
    app()
