"""
Extract Spells from ``Rank3 Workbook.ipynb``.
Created by V2025.12.6.dev3 of ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

"""

from opend6_tools.magic2 import *



illusion_of_small_monster = Spell(
        name="Illusion of Small Monster",
        skill="Temperamental Conjuration",
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
    )

fireball = Spell(
        name="Fire Ball",
        skill="Elemental Alteration",
        notes="Charisma",
        effect=DamageEffect("move fire 2m/s, does damage on contact", "6D", "physical damage", "ignores nonmagical armor"),
        duration=DurationAspect(measure="1 s"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={"incantation": IncantationsAspect("Fire Chant", "litany")},
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Cyþan Intelligence")
        ],
    )

wind_storm = Spell(
        name="Wind Storm",
        skill="Elemental Alteration",
        notes="This generally knocks a person down and batters them for 3 rounds",
        effect=CompositeEffect(
            "wind everywheter",
            DamageEffect("Wind", "+3D", "physical damage"),
            DisadvantageEffect("Loss of balance", 3, "+9 to any attempt to stand"),
        ),
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
    )

charm = Spell(
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
    )

hold_portal = Spell(
        name="Hold Portal",
        skill="Elemental Alteration",
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
    )

impervious_leather_armor = Spell(
        name="Impervious leather armor",
        skill="Elemental Alteration",
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
    )

move_wall_of_rock = Spell(
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
    )

pass_wall = Spell(
        name="Pass Wall",
        skill="Elemental Alteration",
        notes="The wall doesn't vanish; the target(s) can move through it.",
        effect=SpecialAbilityEffect("Intangibility", 1),
        duration=DurationAspect(measure="1 m"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="1 s"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "area_effect": AreaEffectAspect("2m height 2m width and 5m depth cuboid"),
            "components": ComponentsAspect("small shovel", "uncommon"),
            "gestures": GesturesAspect("Earth Gestures", "complex"),
            "incantation": IncantationsAspect("Earth Chant", "litany"),
        },
        other_conditions=[
            GenericAspect(difficulty=0, description="Controller: Hildeþrymm Physique")
        ],
    )

pass_fire = Spell(
        name="Pass Fire",
        skill="Elemental Alteration",
        notes="The fire doesn't vanish; the target moves through it. Note the restriction on Intangibility '... may not pass through fiery or energy barriers.' The mage can pass through fire, but not a wall of fire.",
        effect=SpecialAbilityEffect("Intangibility", 1, "+3D vs Fire"),
        duration=DurationAspect(measure="1 min"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "area_effect": AreaEffectAspect("2m height 2m width and 5m depth cuboid"),
            "components": ComponentsAspect("Metal rod inserted into the fire", "uncommon"),
            "gestures": IncantationsAspect("Fire Gestures", "complex"),
            "incantation": IncantationsAspect("Fire Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
        },
        other_conditions=[
            GenericAspect(0, "Controller: Cyþan Intelligence"),
            GenericAspect(2, "Any followers must form a chain touching the caster"),
        ],
    )

pass_plant = Spell(
        name="Pass Plant",
        skill="Elemental Alteration",
        notes="The plant matter doesn't vanish; the target moves through it",
        effect=SpecialAbilityEffect("Intangibility", 1),
        duration=DurationAspect(measure="1 m"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "area_effect": AreaEffectAspect("2m height 2m width and 5m depth cuboid"),
            "incantation": IncantationsAspect("Earth and Water Chant", "litany"),
            "concentration": ConcentrationAspect(measure="5 sec"),
        },
        other_conditions=[
            GenericAspect(difficulty=-1, description="limited to plants"),
            GenericAspect(
                difficulty=0, description="Controller: Depends on type of plant"
            ),
        ],
    )

lightning = Spell(
        name="Lightning",
        skill="Elemental Alteration",
        notes="The balance of elements is mostly air with a touch of fire.",
        effect=DamageEffect("move air+fire 2m/s, does damage", "5D+1", "physical damage", "ignores all armor"),
        duration=DurationAspect(measure="1 s"),
        range=RangeAspect(measure="20 m"),
        casting_time=CastingTimeAspect(measure="1 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect("Copper rod and wire", "uncommon"),
            "gestures": GesturesAspect("Fire and Air Gestures", "complex"),
            "incantation": IncantationsAspect("Fire and Air Chant", "litany")
        },
        other_conditions=[
            GenericAspect(0, "Controller: Folme Agility"),
            GenericAspect(2, "Difficult to aim, +2 difficulty"),
        ],
    )

mend_iron = Spell(
        name="Mend Iron",
        skill="Elemental Alteration",
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
    )

human_combustion = Spell(
        name="Human Combustion",
        skill="Elemental Alteration",
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
    )

remote_cache = Spell(
    name="Remote Cache",
    skill="Apportation",
    notes="The mage can reach through a small opening into a known space in another realm to keep things. The other realm location is not 100% safe; a critical failure may mean the cache was moved in the other realm. The opening is centered on a specific architectural feature, like a cupboard in the mage's study.",
    effect=CompositeEffect(
        "Possession and Apportation",
        Effect("Apportation to another realm (R3)", 30),
        MassEffect("Limited to", "50 Kg"),
    ),
    duration=DurationAspect(measure="5 min"),
    range=RangeAspect(measure="touch"),
    casting_time=CastingTimeAspect(measure="5 s"),
    speed=SpeedAspect.based_on(("range",), ""),
    other_aspects={
        "incantation": IncantationsAspect("Veil Opening Chant", "litany"),
        "concentration": ConcentrationAspect(measure="5 s"),
        "components": ComponentsAspect("Fixed location (e.g. cupboard)", "common"),
    },
    other_conditions=[
        GenericAspect(difficulty=0, description="Controller: None"),
        GenericAspect(difficulty=3, description="Multiple previous visits"),
        GenericAspect(difficulty=3,
         description="Small chance of loss"),
    ],
)

durable_illusion_of_small_monster = Spell(
        name="Durable Illusion of Small Monster",
        skill="Temperamental Conjuration",
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
    )

flesh_to_stone = Spell(
        name="Flesh to Stone",
        skill="Temperamental Alteration",
        notes="Displaces 3 elements to surrounding area; replaces with the earth, which must be present",
        effect=SpecialAbilityEffect(
            "Transmutation", 3, note="Drain away water, air, fire, replace with earth",
            modifications=[Limitation("restricted", 3, "target has no control")]),
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
    )
spells = [ 
    illusion_of_small_monster, fireball, wind_storm, charm, hold_portal, impervious_leather_armor, move_wall_of_rock, pass_wall, pass_fire, pass_plant, lightning, mend_iron, human_combustion, remote_cache, durable_illusion_of_small_monster, flesh_to_stone, 
]

__test__ = {
    "Illusion of Small Monster": ">>> spells[0].difficulty\n15",
    "Fire Ball": ">>> spells[1].difficulty\n17",
    "Wind Storm": ">>> spells[2].difficulty\n14",
    "Charm": ">>> spells[3].difficulty\n17",
    "Hold Portal": ">>> spells[4].difficulty\n16",
    "Impervious leather armor": ">>> spells[5].difficulty\n14",
    "Move Wall of Rock": ">>> spells[6].difficulty\n17",
    "Pass Wall": ">>> spells[7].difficulty\n17",
    "Pass Fire": ">>> spells[8].difficulty\n13",
    "Pass Plant": ">>> spells[9].difficulty\n17",
    "Lightning": ">>> spells[10].difficulty\n17",
    "Mend Iron": ">>> spells[11].difficulty\n17",
    "Human Combustion": ">>> spells[12].difficulty\n14",
    "Remote Cache": ">>> spells[13].difficulty\n16",
    "Durable Illusion of Small Monster": ">>> spells[14].difficulty\n16",
    "Flesh to Stone": ">>> spells[15].difficulty\n15",
}

if __name__ == "__main__":
    app = build_app(spells)
    app()

