r"""
Spells from OpenD6 Fantasy Locations.

Note the problems with these spells -- Area of Effect is a right awful mess because the
"hut-like shape" is undefined.

A close match is the unpublished Magic Guide "cuboid" shape which has no
sensible difficulty computation.

However, the volumes of 4 cubic meters, 32 cubic meters, and 268 cubic meters are very close fits
for the volumes of spheres with radii of 1, 2 and and 4 meters.
These have difficulty of 5, 10, and 20.

This suggests two spells (**Basic Shelter** and **Improved Shelter**)
have the wrong difficulties for their areas of effect.

Further, it also suggests the various  shapes in the Magic Guide have faulty computations for area of effect.
It appears that the idea is to normalize based a kind of equivalent spherical radius.
"""

from textwrap import dedent
from opend6_tools.magic2 import *


# BASIC SHELTER SPELL
# ====================

basic_shelter = Spell(
    name="Basic Shelter",
    skill="Conjuration",
    effect=CompositeEffect(
        "shelter",
        ProtectionEffect(1*D),
        SpecialAbilityEffect(SpecialAbilityType.environmental_resistance, 1, note="+3D to stamina or Physique against heat, cold, or pressure"),
    ),
    range=RangeAspect("1m"),
    speed=SpeedAspect.based_on('range'),
    duration=DurationAspect("10 hours"),
    casting_time=CastingTimeAspect("1 min."),
    other_aspects={
        "area_effect": AreaEffectAspect("1.25m width 2m depth 2m height cuboid", "fluid shape"),
        "components": ComponentsAspect("pinch of brick, stone, wood, paper, or cloth", "ordinary", "destroyed"),
        "focused": FocusedAspect.based_on(("effect", "duration"), "on ground"),
        "gestures": GesturesAspect("slowly sprinkle pinch in circle around caster", "simple"),
        "incantation": IncantationsAspect("Give me shelter", "sentence"),
        "other_alterant": OtherAlterant(2, "features...")
    },
    notes=dedent("""\
        This spell is quite useful for the single, traveling
        caster. This creates a cramped shelter around the caster.
        The shelter has a door to exit it and a small fireplace
        in one corner so a fire can be set to create warmth and
        light. The thin walls, seemingly made of the same material 
        as the component, give the caster some protection
        from the elements and physical attacks. As the spell is
        focused, the caster may leave the hut without worrying
        about it disappearing.    
    """)
)

# Skill Used: Conjuration
# Difficulty : 14
# Effect : 6 (Armor Value of 1D and Environmental Resistance (R1), +3D to stamina or Physique against heat, cold, or pressure)
# Range : Self (O)
# Speed :O
# Duration : 10 hours (+23)
# Casting Time : 1 minute (-8)
# Other Aspects:
# Area of Effect (+6): Hut-shaped area about 1.25 meters wide, 2 meters wide, and 2 meters tall
# Components (-2): Pinch of brick, stone, wood, paper, or cloth (ordinary, destroyed)
# Focused (+S): On ground
# Gesture (-2): Slowly sprinkle pinch in circle around caster (fairly simple)
# Incantation (-2): "Give me shelter." (sentence)
# Other Alterant (+2): Hut features - see description

# This spell is quite useful for the single, traveling
# caster. This creates a cramped shelter around the caster.
# The shelter has a door to exit it and a small fireplace
# in one corner so a fire can be set to create warmth and
# light. The thin walls, seemingly made of the same mate ­
# rial as the component, give the caster some protectio n
# from the elements and physical attacks. As the spell is
# focused, the caster may leave the hut without worrying
# about it disappearing.

# IMPROVED HUT SPELL
# ====================

improved_hut = Spell(
    name="Improved Hut",
    skill="Conjuration",
    effect=CompositeEffect(
        "shelter",
        ProtectionEffect(5 * D),
        SpecialAbilityEffect(SpecialAbilityType.environmental_resistance, 2, note="+6D to stamina or Physique against heat, cold, or pressure"),
        # AttributeEffect(6 * D,
        #                "stamina or Physique against heat, cold, or pressure"),
    ),
    range=RangeAspect("1m"),
    speed=SpeedAspect.based_on('range'),
    duration=DurationAspect("1 day"),
    casting_time=CastingTimeAspect("5 min."),
    other_aspects={
        "area_effect": AreaEffectAspect("4m width 4m depth 1m height cuboid", "fluid shape"),
        "components": ComponentsAspect("painted toy house", "uncommon"),
        "concentration": ConcentrationAspect("3.5 sec"),
        "focused": FocusedAspect.based_on(("effect", "duration"), "on toy house"),
        "gestures": GesturesAspect("place toy house on the ground and pretend to shape a larger house around it", "simple"),
        "incantation": IncantationsAspect("Give me protection from the elements", "sentence"),
        "other_alterant": OtherAlterant(2, "features...")
    },
    notes=dedent("""\
        Designed to accommodate a small band of close
        adventuring comrades, this improved version of
        the basic hut spell creates a domicile with thin walls
        apparently composed of the same mater ial as the toy
        house. Inside is a small fireplace, and there are uncovered 
        windows and door, allowing in light. The shelter
        offers excellent protection against the weather and predators.
    """)
)

# Skill Used: Conjuration
# Difficulty: 21
# Effect: 21 (Armor Value of 5D and Environmental Resistance (R2),  +6D to stamina or Physique against heat, cold, or pressure)
# Range : 1 meter (O)
# Speed: O
# Duration : 1 day ( +2S)
# Casting Time: 5 minutes (-13)
# Other Aspects:
# Area ofEffect (+11): Hut-shaped area a little more than 4 meters on  a side and 2 meters tall
# Component (-4): A painted toy  house (uncommon)
# Concentration (-1): 3. S seconds with mettle difficulty of 7
# Focused ( +S): On toy house
# Gesture (-2): Place toy house on ground and pretend  to shape a larger house around it (fairly simple)
# Incantation (-2): "Give me protection from the elements (sentence)
# Other Alterant (+2): Hut features - see description

# Designed to accommodate a small band of dose
# adventuring comrades, this improved version of
# the basic hut spell creates a domicile with thin walls
# apparently composed of the same mater ial as the toy
# house. Inside is a small fireplace, and there are uncov­
# ered windows and door, allowing in light. The shelter
# offers excellent protection against the weathe r and
# predators.

# SMALL LONG-LASTING TOWER SPELL
# ==============================

small_tower = Spell(
    name="Small Tower",
    skill="Conjuration",
    effect=CompositeEffect(
        "shelter",
        ProtectionEffect(5 * D + 1),
        SpecialAbilityEffect(SpecialAbilityType.environmental_resistance, 2),
        # AttributeEffect(6 * D,
        #                "stamina or Physique against heat, cold, or pressure"),
    ),
    range=RangeAspect("1m"),
    speed=SpeedAspect.based_on('range'),
    duration=DurationAspect("25 years"),
    casting_time=CastingTimeAspect("1 week"),
    other_aspects={
        "area_effect": AreaEffectAspect("10.4m width 10.4m depth 2.5m height cuboid", "fluid shape", notes="approximately six rooms 2.5 meters height by 3.75 meters width by 4.75 meters length"),
        "components": ComponentsAspect("Mud brick or stone block from an ancient temple", "extremely rare"),
        "concentration": ConcentrationAspect("1 min"),
        "focused": FocusedAspect.based_on(("effect", "duration"),
                                          "on temple material"),
        "gestures": GesturesAspect(
            "Make hand gestures as if building a tower",
            "complex"),  # difficulty 11
        "incantation": IncantationsAspect(
            "Read or recite loudly prayers related to the religion of the ancient temple", "litany", "loud", "foreign toungue"),  # difficulty 11
        "other_alterant": OtherAlterant(3, "features...")
    },
    notes=dedent("""\
        This spell creates a retreat of any shape that the
        caster desires, including whatever doors, windows or
        stairs that she wants to include. It appears to made of
        an ancient building material, and it provides terrific
        protection for up to 25 years. The caster may change
        the shape of the structure at any time during that
        period. Anything inside will automatically shift without
        breaking, to accommodate the new shape.
    """)
)

# Skill Used : Conjuration
# Difficulty: 31
# Effect: 22 (Armor Value of 5D+1 and Environmental Resistance (R2), +6D to stamina or Physique against heat, cold, or pressure)
# Range: 1 meter (O)
# Speed :O
# Duration: 2S years (+4S)
# Casting Time: 1 week (-29)
# Other Aspects :
# Area ofEffect (+26): Fluid shape of no more than 268 cubic meters - approximately six rooms 2.5 meters tall by 3.75 meters wide by 4.75 meters long
# Component (-6): Mud brick or stone block from an ancient temple (extremely rare)
# Concentration (-3): 1 minute with mettle difficulty of 9
# Focused (+13): On temple material
# Gesture (-4): Make hand gestures as if building a tower (complex, crafting difficulty of 11)
# Incantation (-5): Read or recite loudly prayers related to the religion of the ancient temple (litany, loud, speaking difficulty of 11)
# Other Alterant ( +3): Tower features - see description

# This spell creates a retreat of any shape that the
# caster desires, including whatever doors, windows or
# stairs that she wants to include. It appears to made of
# an ancient building material, and it provides terrific
# protection for up to 25 years. The caster may change
# the shape of the structure at any time during that
# period. Anything inside will automatically shift without
# breaking, to accommodate the new shape.

# KEEP IN THE AIR SPELL
# ==============================

keep_in_the_air = Spell(
    name="Keep in the Air",
    skill="Conjuration",
    effect=CompositeEffect(
        "shelter",
        ProtectionEffect(4 * D),
        SpecialAbilityEffect(SpecialAbilityType.environmental_resistance, 2),
        # AttributeEffect(6 * D,
        #                "stamina or Physique against heat, cold, or pressure"),
    ),
    range=RangeAspect("1m"),
    speed=SpeedAspect.based_on('range'),
    duration=DurationAspect("15 years"),
    casting_time=CastingTimeAspect("10 hours"),
    other_aspects={
        "area_effect": AreaEffectAspect(
            "10.4m width 10.4m depth 2.5m height cuboid", "fluid shape",
            notes="approximately six rooms 2.5 meters height by 3.75 meters width by 4.75 meters length"),
        "components": ComponentsAspect(
            ("Empty glass jar with fitted lid", "common"),
            ("white feathers", "very common", "destroyed"),
            ("gold dust", "uncommon", "destroyed")),
        "concentration": ConcentrationAspect("15 min"),  # Difficulty 11
        "focused": FocusedAspect.based_on(("effect", "duration"),
                                          "on glass jar"),
        "gestures": GesturesAspect("Shake jar with feathers, gold dust, and air", "very simple"),
        "incantation": IncantationsAspect("Blow air into jar", "word"),
        "other_alterant": OtherAlterant(3, "features...")
    },
    notes=dedent("""\
        After less than half a day of preparation, 15 minutes
        of concentration, and a lot of shaking of some feathers,
        gold, and air, the caster creates a movable tower. The
        tower may go up and down or across the landscape at
        a rate of three meters per round. It appears to made of
        white marble flecked with gold and has as many doors,
        windows, and staircases as the caster desires. He may also
        change its shape at any point during its existence, with
        the items quietly moving themselves around without
        damaging themselves. At the end of the duration, the
        feathers and gold dust turn to a fine ash.
    """)
)

# Skill Used : Conjuration
# Difficulty: 30
# Effect: 14 (Armor Value of 4D and Environmental Resistance (R2), +6D to stamina or Physique against heat, cold, or pressure)
# Range: 1 meter (O)
# Speed: O
# Duration: 15 years (+44)
# Casting Time : 10 hours (-23)
# Other Aspects :
# Area ofEffect (+26): Fluid shape of no more than 268 cubic meters - approximately six rooms 2. 5 meters tall by 3. 75 meters wide by 4. 75 meters long
# Component (-15): Empty glass jar with fitted lid (common), white feathers (very common, destroyed); gold dust (uncommon, destroyed)
# Concentration (-5): 15 minutes with mettle difficulty of 11
# Focused ( + 11): On glass jar
# Gesture (-1): Shake lidded jar filled with feathers, gold dust, and air (simple)
# Incantation (-1): Blow air into jar (simple)
# Variable Movement (+7): 15 meters per second/3 meters per round
# Other Alterant ( +3): Tower features - see description

# After less than half a day of preparation, 15 minutes
# of concentration, and a lot of shaking of some feathers,
# gold, and air, the caster creates a movable tower. The
# tower may go up and down or across the landscape at
# a rate of three meters per round. It appears to made of
# white marble flecked with gold and has as many doors,
# windows, and staircases as the caster desires. He may also
# change its shape at any point during its existence, with
# the items quietly moving themselves around without
# damaging themselves. At the end of the duration, the
# feathers and gold dust turn to a fine ash.

spells = [
    basic_shelter,
    improved_hut,
    small_tower,
    keep_in_the_air,
]


__test__ = {
    "basic_shelter": ">>> basic_shelter.difficulty\n17",  # Rules say 14, area effect is wrong
    "improved_hut": ">>> improved_hut.difficulty\n26",  # Rules say 21, but area effect is wrong
    "small_tower": ">>> small_tower.difficulty\n31",
    "keep_in_the_air": ">>> keep_in_the_air.difficulty\n29",  # Rules say 30
}

if __name__ == "__main__":
    app = build_app(spells)
    app()
