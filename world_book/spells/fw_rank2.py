"""
Extract Spells from ``Rank2 Workbook.ipynb``.
Created by V2025.12.6.dev3 of ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

"""

from opend6_tools.magic2 import *



shield = Spell(
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
    )

light_fire = Spell(
        name="Light Fire",
        skill="Elemental Alteration",
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
    )

move_fire = Spell(
        name="Move Fire",
        skill="Elemental Alteration",
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
    )

wind_gust = Spell(
        name="Wind Gust",
        skill="Elemental Alteration",
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
    )

esp = Spell(
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
    )

light = Spell(
        name="Light",
        skill="Elemental Alteration",
        notes="This requires the fire from a torch or large lantern; it stays where the mage puts it. It doesn't consume any fuel",
        effect=SkillEffect("A small cold fire to aid in search", "+2D"),  # See Light...
        duration=DurationAspect(measure="30 m"),
        range=RangeAspect(measure="10 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "incantation": IncantationsAspect("Fire Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Witan Acumen")
        ],
    )

find_path = Spell(
        name="Find Path",
        skill="Divination",
        notes="A big boost in locating a path through obstacles",
        effect=SkillEffect("boosts Acumen/search", "+3D", "skill modifier"),
        duration=DurationAspect(measure="5 m"),
        range=RangeAspect(measure="10 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect("A rod or bead on a string", "common"),
            "gestures": GesturesAspect("Moving the search charm", "simple"),
            "incantation": IncantationsAspect("Divination Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Witan Acumen")
        ],
    )

gradual_heal = Spell(
        name="Gradual Heal",
        skill="Temperamental Alteration",
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
    )

freeze = Spell(
        name="Freeze",
        skill="Temperamental Alteration",
        notes="Physique is (temporarily) drained away, making movement difficult",
        effect=DisadvantageEffect("Achilles Heel: movement", 4, "Attempting to move reduces physique by 4D"),
        duration=DurationAspect(measure="2 min"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "gestures": GesturesAspect("Control Gestures", "complex"),
            "incantation": IncantationsAspect("Control Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Folme Agility")
        ],
    )

warp_wood = Spell(
        name="Warp Wood",
        skill="Elemental Alteration",
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
    )

infravision = Spell(
        name="Infravision",
        skill="Temperamental Alteration",
        notes="Heat from passing footsteps are difficult (but not impossible) to see",
        effect=SpecialAbilityEffect("infravision/ultravision", 4),
        duration=DurationAspect(measure="1 min"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect("Thermal Lens", "rare"),
            "incantation": IncantationsAspect("Divination Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Witan Acumen")
        ],
    )

silence = Spell(
        name="Silence",
        skill="Elemental Alteration",
        notes="This will silence most noises in a small circle around the target",
        effect=DisadvantageEffect("Deafness", 2, "+6 do difficulty for hearing"),
        duration=DurationAspect(measure="5 min"),
        range=RangeAspect(measure="10 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "gestures": GesturesAspect("Air Gestures", "complex"),
            "incantation": IncantationsAspect("Air Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
            "area_of_effect": AreaEffectAspect("2m r circle"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Witan Acumen")
        ],
    )

immediate_hurt = Spell(
        name="Immediate Hurt",
        skill="Temperamental Alteration",
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
    )

close_veil = Spell(
    name = "Closing the Veil",
    skill = "Apportation",
    notes="Closes the veil, restoring the universe to it's base state.",
    effect=Effect("Apportation to the caster's original realm (R2)", 20),
    duration=DurationAspect(measure="5 min"),
    range=RangeAspect(measure="touch"),
    casting_time=CastingTimeAspect(measure="5 s"),
    speed=SpeedAspect.based_on(("range",), ""),
    other_aspects={
        "incantation": IncantationsAspect("Veil Closing Chant", "litany"),
        "concentration": ConcentrationAspect(measure="5 s"),
        "components": ComponentsAspect("any resonating artifacts", "rare"),
        "variable_duration": VariableDurationAspect("off-only"),
    },
    other_conditions=[
        GenericAspect(difficulty=0, description="Controller: None"),
    ],
)

reanimation_r1 = Spell(
    name = "Reanimation",
    skill = "Temperamental Conjuration",
    notes="Reanimates one complete human for an hour.",
    effect=Effect("Temperamental Conjuration of 10D human.", 30),
    duration=DurationAspect(measure="1 hr"),
    range=RangeAspect(measure="touch"),
    casting_time=CastingTimeAspect(measure="5 s"),
    speed=SpeedAspect.based_on(("range",), ""),
    other_aspects={
        "incantation": IncantationsAspect("Conjuration Chant", "litany"),
        "concentration": ConcentrationAspect(measure="5 s"),
        "components": ComponentsAspect("a resonating artifact to help the balance", "very rare"),
    },
    other_conditions=[
        GenericAspect(difficulty=0, description="Controller: None"),
        GenericAspect(difficulty=3, description="All four elements present in the environment: fire, flowing water, wind, and loose earth."),
    ],
)
spells = [ 
    shield, light_fire, move_fire, wind_gust, esp, light, find_path, gradual_heal, freeze, warp_wood, infravision, silence, immediate_hurt, close_veil, reanimation_r1, 
]

__test__ = {
    "Shield": ">>> spells[0].difficulty\n10",
    "Light Fire": ">>> spells[1].difficulty\n12",
    "Move Fire": ">>> spells[2].difficulty\n10",
    "Wind Gust": ">>> spells[3].difficulty\n9",
    "ESP": ">>> spells[4].difficulty\n8",
    "Light": ">>> spells[5].difficulty\n11",
    "Find Path": ">>> spells[6].difficulty\n11",
    "Gradual Heal": ">>> spells[7].difficulty\n11",
    "Freeze": ">>> spells[8].difficulty\n12",
    "Warp Wood": ">>> spells[9].difficulty\n8",
    "Infravision": ">>> spells[10].difficulty\n11",
    "Silence": ">>> spells[11].difficulty\n10",
    "Immediate Hurt": ">>> spells[12].difficulty\n12",
    "Closing the Veil": ">>> spells[13].difficulty\n11",
    "Reanimation": ">>> spells[14].difficulty\n15",
}


if __name__ == "__main__":
    app = build_app(spells)
    app()

