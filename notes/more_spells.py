"""
more_spells -- From my Fantasy Wargaming notes.

THIS IS THE DRAFT version.

Final copies are in fw_cantrips, fw_rank2, fw_rank3, fw_rank4.

When run as an app, generates .RST details of each Spell.
"""

from opend6_tools.magic2 import *
import logging
import pytest


spells = [
    Spell(
        name="Gradual Heal",
        skill="Alteration: Physique",
        notes="Cures a disease or poison",
        effect=SkillEffect("Heal disease", "5D", "skill"),
        duration=DurationAspect("instantaneous"),
        range=RangeAspect("20 m"),
        casting_time=CastingTimeAspect("1 s"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={"incantation": IncantationsAspect("Healing Chant", "litany")},
        other_conditions=[
            GenericAspect(difficulty=-2, description="Heal only with Body <= 3/4"),
            GenericAspect(difficulty=-1, description="limited to 3 body parts"),
            GenericAspect(difficulty=-1, description="limited to disease cure"),
            GenericAspect(difficulty=0, description="Controller: Hælan Coordination"),
        ],
    ),
    Spell(
        name="Immediate Hurt",
        skill="Alteration: Physique",
        notes="Adds to previously received injuries",
        effect=DamageEffect("Damage", "+5D; physical damage"),
        duration=DurationAspect(measure="1 s"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="1 s"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={"incantation": IncantationsAspect("Damage Chant", "litany")},
        other_conditions=[
            GenericAspect(difficulty=-2, description="Damage only with Body <= 1/2"),
            GenericAspect(difficulty=0, description="Controller: Hælan Coordination"),
        ],
    ),
    Spell(
        name="Illusion of Small Monster",
        skill="Psychic Communication",
        notes="An autonomous illusion of a small monster",
        effect=SkillEffect("Fear", "6D"),
        duration=DurationAspect(measure="5 m"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="1 s"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Illusion Chant", "litany"),
            "other_alterant": GenericAspect(
                difficulty=3, description="illusion is moving"
            ),
            "unreal_effect": UnrealEffectAspect.based_on("effect", "difficulty 13"),
        },
        other_conditions=[
            GenericAspect(difficulty=3, description="illusion limited to 3 colors"),
            GenericAspect(difficulty=0, description="Controller: Baelu Charisma"),
        ],
    ),
    Spell(
        name="Illusion of Rat",
        skill="Psychic Communication",
        notes="An autonomous illusion of a large rat",
        effect=SkillEffect("Fear", "4D"),
        duration=DurationAspect(measure="5 m"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Illusion Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
            "other_alterant": GenericAspect(
                difficulty=3, description="illusion is moving"
            ),
            "unreal_effect": UnrealEffectAspect.based_on("effect", "difficulty 13"),
        },
        other_conditions=[
            GenericAspect(difficulty=-3, description="illusion limited to 1 color"),
            GenericAspect(difficulty=0, description="Controller: Baelu Charisma"),
        ],
    ),
    Spell(
        name="Durable Illusion of Small Monster",
        skill="Psychic Communication",
        notes="This illusion lasts one hour before starting to fade",
        effect=SkillEffect("Fear", "6D"),
        duration=DurationAspect(measure="1 hr"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="1 s"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Illusion Chant", "litany"),
            "other_alterant": GenericAspect(
                difficulty=5, description="illusion is moving"
            ),
            "unreal_effect": UnrealEffectAspect.based_on("effect", "difficulty 13"),
        },
        other_conditions=[
            GenericAspect(difficulty=5, description="illusion limited to 3 colors"),
            GenericAspect(difficulty=0, description="Controller: Baelu Charisma"),
        ],
    ),
    Spell(
        name="Protection from Magic",
        skill="Alteration",
        notes="Distinct from Shield which prevents the link, this mitigates effects",
        effect=ProtectionEffect("Reduce effect (after link)", "2D"),
        duration=DurationAspect(measure="1 s"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 s"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Protection Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 s"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="opposed"),
            GenericAspect(difficulty=0, description="Controller: None"),
        ],
    ),
    Spell(
        name="Halt",
        skill="Psychic Communication",
        notes="The halt duration is short; an agility check is required to keep from stumbling",
        effect=SkillEffect("Halt! with bonus to overcome mettle", "2D"),
        duration=DurationAspect(measure="2 sec"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Control chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Witan Acumen")
        ],
    ),
    Spell(
        name="Freeze",
        skill="Psychic Communication",
        notes="Physique is (temporarily) drained away, making movement difficult",
        effect=DisadvantageEffect("Achilles Heel: movement", 4, "Moving reduces physique by 4D"),
        duration=DurationAspect(measure="2 min"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Control Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Folme Agility")
        ],
    ),
    Spell(
        name="Sleep",
        skill="Psychic Communication",
        notes="Physique, Coordination, Acumen, and Intellect are (temporarily) reduced, leading to fatigue",
        effect=DisadvantageEffect("Narcolepsy", 4, "-4D to mental and physical attributes"),
        duration=DurationAspect(measure="5 min"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Control Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
            "feedback": FeedbackAspect(2),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Folme Agility")
        ],
    ),
    Spell(
        name="Move Wall of Rock",
        skill="Alteration: Earth",
        notes="See Conjure Wall of Rock for a complementary spell",
        effect=MassEffect("Move earth element to a new position", "600kg"),
        duration=DurationAspect(measure="1 min"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Earth Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
            "area_of_effect": AreaEffectAspect("2 m radius sphere"),
        },
        other_conditions=[
            GenericAspect(difficulty=-4, description="elemental already present"),
            GenericAspect(difficulty=0, description="Controller: Hildeþrymm Physique"),
        ],
    ),
    Spell(
        name="Conjure Wall of Rock",
        skill="Conjuration: Earth",
        notes="Creates a wall from free earth elements",
        effect=MassEffect("Move earth element to a new position", "600kg"),
        duration=DurationAspect(measure="5 min"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Earth Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
            "area_of_effect": AreaEffectAspect("2 m radius sphere"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Hildeþrymm Physique")
        ],
    ),
    Spell(
        name="Light Fire",
        skill="Alteration: Fire",
        notes="The fire must exist; this merely moves it to ignite something else",
        effect=DamageEffect("Move small fire element", "2D", "physical damage"),
        duration=DurationAspect(measure="1 s"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="1 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Fire Chant", "litany"),
            "variable_movement": VariableMovementAspect("20m"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Cyþan Intelligence")
        ],
    ),
    Spell(
        name="Move Fire",
        skill="Alteration: Fire",
        notes="The fire must exist; this merely moves it somewhere else",
        effect=DamageEffect("Move large fire element", "5D", "physical damage"),
        duration=DurationAspect(measure="1 s"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Fire Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Cyþan Intelligence")
        ],
    ),
    Spell(
        name="Pass Wall",
        skill="Alteration: Earth",
        notes="The wall doesn't vanish; the target(s) can move through it.",
        effect=SpecialAbilityEffect("Intangibility", 3),
        duration=DurationAspect(measure="10 m"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="1 s"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={"incantation": IncantationsAspect("Earth Chant", "litany")},
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Hildeþrymm Physique")
        ],
    ),
    Spell(
        name="Pass Fire",
        skill="Alteration: Fire",
        notes="The fire doesn't vanish; the target(s) move through it",
        effect=SpecialAbilityEffect("Intangibility", 3),
        duration=DurationAspect(measure="2 min"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Fire Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Cyþan Intelligence")
        ],
    ),
    Spell(
        name="Fire Ball",
        skill="Alteration: Fire",
        notes="Charisma",
        effect=DamageEffect("move fire 2m/s, does damage on contact", "7D", "physical damage", "ignores nonmagical armor"),
        duration=DurationAspect(measure="1 s"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={"incantation": IncantationsAspect("Fire Chant", "litany")},
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Cyþan Intelligence")
        ],
    ),
    Spell(
        name="Lightning",
        skill="Alteration: Air + Fire",
        notes="The balance of elements is mostly air with a touch of fire.",
        effect=DamageEffect("move air+fire 2m/s, does damage", "6D", "physical damage", "ignores all armor"),
        duration=DurationAspect(measure="1 s"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="1 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={"incantation": IncantationsAspect("Fire and Air Chant", "litany")},
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Folme Agility")
        ],
    ),
    Spell(
        name="Earth Quake",
        skill="Alteration: Earth",
        notes="The area is large enough that the mage is barely able to avoid the effects; damage is incidental usually from falling objects",
        effect=MassEffect("shake earth", "1,000 kg"),
        duration=DurationAspect(measure="5 s"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Earth Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
            "area_of_effect": AreaEffectAspect("20m r circle"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Hildeþrymm Physique")
        ],
    ),
    Spell(
        name="Dirt to Mud",
        skill="Alteration: Water",
        notes="The water must be located nearby; the mud starts to revert after 5 minutes, escape is difficult requiring patience and sometimes the help of a shovel or pry-bar",
        effect=DisadvantageEffect("Hindrance", 4, "mired in mud"),
        duration=DurationAspect(measure="5 min"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Earth and Water Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
            "area_of_effect": AreaEffectAspect("10m radius circle"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Hælan Coordination")
        ],
    ),
    Spell(
        name="Wind Gust",
        skill="Alteration: Air",
        notes="A gust that will move 25 kg will unbalance a target unprepared for it",
        effect=MassEffect("Telekinetic Movement", "25 kg"),
        duration=DurationAspect(measure="1 s"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="1 s"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={"incantation": IncantationsAspect("Air Chant", "litany")},
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Folme Agility")
        ],
    ),
    Spell(
        name="Wind Storm",
        skill="Alteration: Air",
        notes="This generally knocks a person down (to stand is Very Difficult 21-25); it batters them for 3 rounds",
        effect=DamageEffect("Wind",  "+3D", "physical damage"),
        duration=DurationAspect(measure="3 rounds"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Air Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Folme Agility")
        ],
    ),
    Spell(
        name="Knock",
        skill="Alteration: [type of wood]",
        notes="This tends to destroy the door",
        effect=DamageEffect("break latch or bar", "3D", "physical damage"),
        duration=DurationAspect(measure="1 s"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="1 s"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={"incantation": IncantationsAspect("Earth and Water Chant", "litany")},
        other_conditions=[
            GenericAspect(difficulty=-1, description="limited to wood"),
            GenericAspect(
                difficulty=0, description="Controller: Depends on type of wood"
            ),
        ],
    ),
    Spell(
        name="Warp Wood",
        skill="Alteration: wood",
        notes="The wood's shape is changed, any damage is incidental",
        effect=MassEffect("Warp wood", "10 kg"),
        duration=DurationAspect(measure="1 s"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="1 s"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={"incantation": IncantationsAspect("Earth and Water Chant", "litany")},
        other_conditions=[
            GenericAspect(difficulty=0, description="limited to wood"),
            GenericAspect(
                difficulty=0, description="Controller: Depends on type of wood"
            ),
        ],
    ),
    Spell(
        name="ESP",
        skill="Divination",
        notes="This provides very general background information",
        effect=SkillEffect("Psionics: Gather general thoughts from hostile target", "+2D", "extranormal skill"),
        duration=DurationAspect(measure="1 s"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Divination Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Witan Acumen")
        ],
    ),
    Spell(
        name="Flesh to Stone",
        skill="Alteration: Earth",
        notes="Displaces 3 elements to surrounding area; replaces with the earth, which must be present",
        effect=SpecialAbilityEffect("Transmutation", 3, note="Drain away water, air, fire, replace with earth", limitations=[Limitation("restricted", 3, "target has no control")]),
        duration=DurationAspect(measure="1 min"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Earth Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
        },
        other_conditions=[
            GenericAspect(difficulty=-1, description="limited to living animal"),
            GenericAspect(difficulty=0, description="Controller: Hildeþrymm Physique"),
        ],
    ),
    Spell(
        name="Charm",
        skill="Psychic Communication",
        notes="Creates favorable feelings; acting as a supplement to common Charisma-based skills",
        effect=SkillEffect("Favorable Feelings", "+4D"),  # See Charm cantrip...
        duration=DurationAspect(measure="5 min"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="1 s"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={"incantation": IncantationsAspect("Control Chant", "litany")},
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Baelu Charisma")
        ],
    ),
    Spell(
        name="Hold Portal",
        skill="Alteration: wood",
        notes="The door is stuck closed, but -- of course -- can be battered down",
        effect=MassEffect("Bind door to frame", "10 kg"),
        duration=DurationAspect(measure="40 min"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="1 s"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={"incantation": IncantationsAspect("Earth and Water Chant", "litany")},
        other_conditions=[
            GenericAspect(difficulty=0, description="limited to wood"),
            GenericAspect(
                difficulty=0, description="Controller: Depends on type of wood"
            ),
        ],
    ),
    Spell(
        name="Light",
        skill="Alteration: Fire",
        notes="This requires the fire from a torch or large lantern; it stays where the mage puts it. It doesn't consume any fuel",
        effect=SkillEffect("A small cold fire to aid in search", "+2D"),  # See Light...
        duration=DurationAspect(measure="40 m"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Fire Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Witan Acumen")
        ],
    ),
    Spell(
        name="Shield",
        skill="Psychic Communication",
        notes="This prevents a link from being formed. See Protection from Magic for a complementary spell to block effects after a link has been formed",
        effect=ProtectionEffect("adds to difficulty in attempting to like", "+2D"),
        duration=DurationAspect(measure="2 min"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Protection Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
        },
        other_conditions=[GenericAspect(difficulty=0, description="Controller: None")],
    ),
    Spell(
        name="Totally Invisible",
        skill="Alteration",
        notes="The thing is almost impossible to see",
        effect=DisadvantageEffect("Perception is ruined", "8"),
        duration=DurationAspect(measure="5 min"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Control Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Witan Acumen")
        ],
    ),
    Spell(
        name="Impervious leather armor",
        skill="Alteration",
        notes="This is a temporary boost in the defensive value of leather armor",
        effect=ProtectionEffect("damage resistance", "+2D", "physical protection"),
        duration=DurationAspect(measure="5 min"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="1 s"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={"incantation": IncantationsAspect("Protection Chant", "litany")},
        other_conditions=[
            GenericAspect(difficulty=-1, description="limited to leather"),
            GenericAspect(difficulty=0, description="Controller: Hildeþrymm Physique"),
        ],
    ),
    Spell(
        name="Levitate",
        skill="Apportation: Depends on elements being levitated",
        notes="Levitation is not flight; this is very risky when used outdoors; 10 min of rising at 1m/s will be followed by a 600' fall",
        effect=MassEffect("Move", "100 kg"),
        duration=DurationAspect(measure="10 min"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="1 s"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={"incantation": IncantationsAspect("Levitation Chant", "litany")},
        other_conditions=[
            GenericAspect(
                difficulty=0,
                description="Controller: Depends on substance being levitated",
            )
        ],
    ),
    Spell(
        name="Infravision",
        skill="Alteration",
        notes="Heat from passing footsteps are difficult (but not impossible) to see",
        effect=SpecialAbilityEffect("infravision/ultravision", 4),
        duration=DurationAspect(measure="1 min"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Divination Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Witan Acumen")
        ],
    ),
    Spell(
        name="Mend Iron",
        skill="Alteration: Earth + Fire",
        notes="This is a slow process and requires a source of fire and earth",
        effect=MassEffect("Reshape iron", "15 kg"),
        duration=DurationAspect(measure="1 hr"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="1 s"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={"incantation": IncantationsAspect("Earth and Fire Chant", "litany")},
        other_conditions=[
            GenericAspect(
                difficulty=0,
                description="Controller: Cyþan Intelligence corresponds with Iron",
            )
        ],
    ),
    Spell(
        name="Shocking Grasp",
        skill="Alteration: Air + Fire",
        notes="A touch that does 6D damage",
        effect=DamageEffect("Electric Damage", "6D", "physical damage", "ignores all armor"),
        duration=DurationAspect(measure="1 s"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="1 s"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={"incantation": IncantationsAspect("Air and Fire Chant", "litany")},
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Hælan Coordination")
        ],
    ),
    Spell(
        name="Pass Plant",
        skill="Alteration: plants",
        notes="Plant matter decomposed to earth, water, air and displaced",
        effect=SpecialAbilityEffect("Intangibility", 3),
        duration=DurationAspect(measure="5 m"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Earth and Water Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
        },
        other_conditions=[
            GenericAspect(difficulty=-1, description="limited to plants"),
            GenericAspect(
                difficulty=0, description="Controller: Depends on type of plant"
            ),
        ],
    ),
    Spell(
        name="Find Path",
        skill="Divination",
        notes="A big boost in locating a path through obstacles",
        effect=SkillEffect("find path", "+3D"),
        duration=DurationAspect(measure="5 m"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Divination Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Witan Acumen")
        ],
    ),
    Spell(
        name="Human Combustion",
        skill="Alteration: Fire",
        notes="This is simply nasty -- up to three rounds of damage",
        effect=DamageEffect(
            "Damage from fire", "+6D; physical damage"
        ),
        duration=DurationAspect(measure="3 r"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Fire Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Cyþan Intelligence")
        ],
    ),
    Spell(
        name="Telekinesis",
        skill="Apportation: Depends on elements being moved",
        notes="Movement is a slow walk",
        effect=MassEffect("Move", "25 kg"),
        duration=DurationAspect(measure="10 sec"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="1 s"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={"incantation": IncantationsAspect("Levitation Chant", "litany")},
        other_conditions=[
            GenericAspect(
                difficulty=0, description="Controller: [substance target is made of]"
            )
        ],
    ),
    Spell(
        name="Silence",
        skill="Alteration: Air",
        notes="This will silence most noises in a small circle around the target",
        effect=DisadvantageEffect("Deafness", 4),
        duration=DurationAspect(measure="5 min"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Air Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
            "area_of_effect": AreaEffectAspect("2m r circle"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Witan Acumen")
        ],
    ),
    Spell(
        name="Communicate w/ Plant/Animal",
        skill="Divination",
        notes="This will gather a bit of common information",
        effect=SkillEffect("Psionics: gather common info; potentially hostile", "+2D", "extranormal skill"),
        duration=DurationAspect(measure="1 s"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 s"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Earth and Water chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 s"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Witan Acumen")
        ],
    ),
]


if __name__ == "__main__":
    app = build_app(spells)
    app()


__test__ = {"placeholder": ">>> pass\n\n"}


# Scenario Outline: Converted spells fall into bands approximating target degrees of difficulty
# Given <spell name>
#  And <target difficulty>
#  When spell difficulty is computed for <spell name>
#  Then computed difficulty is within -2 +3 of <target difficulty>
#  Examples:
_SPELL_DIFFICULTIES = sorted(
    [
        # Cantrip-like (Rank 1), 5 pt (was 1-2)
        ("Protection from Magic", 5),
        ("Halt", 5),
        ("Illusion of Rat", 5),
        ("Communicate w/ Plant/Animal", 5),
        ("Knock", 5),
        ("Shocking Grasp", 5),
        # Rank 2: 10 pt (was 3-4)
        ("Shield", 10),
        ("Light Fire", 10),
        ("Move Fire", 10),
        ("Wind Gust", 10),
        ("ESP", 10),
        ("Light", 10),
        ("Find Path", 10),
        ("Telekinesis", 10),
        ("Gradual Heal", 10),
        ("Freeze", 10),
        ("Pass Fire", 10),
        ("Warp Wood", 10),
        ("Infravision", 10),
        ("Silence", 10),
        ("Immediate Hurt", 10),
        # Rank 3: 15 pt (was 5-6)
        ("Illusion of Small Monster", 15),
        ("Fire Ball", 15),
        ("Wind Storm", 15),
        ("Charm", 15),
        ("Hold Portal", 15),
        ("Impervious leather armor", 15),
        ("Move Wall of Rock", 15),
        ("Pass Wall", 15),
        ("Lightning", 15),
        ("Levitate", 15),
        ("Mend Iron", 15),
        ("Pass Plant", 15),
        ("Human Combustion", 15),
        # Rank 4 and 6: 20 pt and 30 pt (was 7-10)
        ("Dirt to Mud", 20),
        ("Sleep", 20),
        ("Conjure Wall of Rock", 20),
        ("Totally Invisible", 20),
        ("Durable Illusion of Small Monster", 20),
        ("Flesh to Stone", 20),
        ("Earth Quake", 30),
    ],
    key=lambda nm_d: nm_d[1],
)
_SPELL_MAP = {s.name: s for s in spells}


@pytest.mark.parametrize("spell_name,difficulty", _SPELL_DIFFICULTIES)
def test_spell_approx_difficulty(spell_name, difficulty, caplog):
    caplog.set_level(logging.DEBUG, logger="Spell")
    spell = _SPELL_MAP[spell_name]
    actual = spell.difficulty
    assert difficulty - 2 <= actual, f"{actual} too easy, increase {spell.effect} to get {difficulty}"
    assert actual < difficulty + 3, f"{actual} too difficult, decrease {spell.effect} to get {difficulty}"

def test_completeness():
    """Confirm all spells have unique names and all spells have test cases."""
    names = set(s.name for s in spells)
    assert len(names) == len(spells), "Duplicate spell name"
    assert names == set(_SPELL_MAP.keys()), "Missing test case"
