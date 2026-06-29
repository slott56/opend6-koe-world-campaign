"""
fantasy_CONJURATION

When run as an app, generates .RST details of each Spell.
"""

from magic2 import *


spells = [
    Spell(
        name="Cage",
        skill="Conjuration",
        notes=[
            "Cage traps a target in a prison of magical energy. To cast it, the wizard mimics trying to escape from a cell, then points at her target. If a marksmanship total beats the combat difficulty for the target, the quarry is trapped. The cage is a sphere with a radius of three meters. Creatures larger than that can’t be confined by this spell.",
            "The effect’s value plus the result points bonus serves as the damage resistance total of the bars. The target can disbelieve and thus free himself by generating a Acumen or investigation total of 13.",
        ],
        effect=ProtectionEffect("resistance total of bars", "8D"),
        duration=DurationAspect(measure="1 hr"),
        range=RangeAspect(measure="25 m"),
        casting_time=CastingTimeAspect(measure="1 min"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "area_effect": AreaEffectAspect("3 m radius sphere"),
            "gesture": GesturesAspect(
                "Mime escaping from a cell, then point to target", "complex (acrobatics roll with difficulty of 11)",
            ),
            "unreal_effect": UnrealEffectAspect.based_on("effect", "difficulty 13")
        },
        other_conditions=[],
    ),

    Spell(
        name="Communicate with Animals",
        skill="Conjuration",
        notes=[
            "To communicate with an animal, the caster places on the ground the bit of something from that type of animal (lock of horse’s hair, bird’s feather, several strands of dog’s hair). Then she draws a line from it to her and from it in the direction of the animal or animals she wishes to speak to. For about six minutes, she receives the ability to communicate with any of that kind of animal as if she had a specialization in its language at 5D. She may add the result points bonus to her speaking roll total. The caster may not move more than one meter from the casting location."
        ],
        effect=SkillEffect("speaking with specialization in the animal’s “language”", "5D"),
        duration=DurationAspect(measure="6 min"),
        range=RangeAspect(measure="1 m"),
        casting_time=CastingTimeAspect(measure="1 r"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect(
                "Something from the type of animal with which she wants to communicate", "very common",
            ),
            "gesture": GesturesAspect("Draw a line on the ground", "simple"),
        },
        other_conditions=[],
    ),

    Spell(
        name="Evil Eye Curse",
        skill="Conjuration",
        notes=["With a minimal amount of pain to himself, the caster curses a Human target that she can see with 10 minutes of Bad Luck (R2). See the description of this Disadvantage in the “Character Options” chapter for details."],
        effect=DisadvantageEffect("Bad Luck", 2),
        duration=DurationAspect(measure="10 min"),
        range=RangeAspect(measure="10 m"),
        casting_time=CastingTimeAspect(measure="2 rounds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "focused": FocusedAspect.based_on(("effect", "duration"), target="on target"),
            "feedback": FeedbackAspect(3),
            "concentration": ConcentrationAspect("1 round", note="mettle difficulty of 8"),
        },
        other_conditions=[GenericAspect(difficulty=-3, description="Limited to Humans")],
    ),

    Spell(
        name="Glow Stone",
        skill="Conjuration",
        notes=[
            "The magic user casts this spell on a small, white stone, making it glow with a fierce radiance that extends for one meter in all directions around the pebble. The effect lasts for 10 minutes. Once the duration wears off, the pebble turns to dust."
        ],
        effect=SkillEffect("negates darkness modifier", "4D"),
        duration=DurationAspect(measure="10 min"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="2 r"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            'area_effect': AreaEffectAspect("1m radius sphere"),
            "components": ComponentsAspect("white pebble", "common", "destroyed"),
            "focused": FocusedAspect.based_on(("effect", "duration"), target="on pebble"),
            "gesture": GesturesAspect("Hold pebble between thumb and forefinger", "very simple"),
            "incantation": IncantationsAspect("Stone of white, give us light.", "sentence"),
        },
        other_conditions=[],
    ),

    Spell(
        name="Feast",
        skill="Conjuration",
        notes=[
            "With this cantrip, the mage creates a meal for two of pure, clean water; flavorful, hearty bread; fresh vegetables and fruits; and, if desired, cheese wedges and smoked meat slices. The food must be consumed within 10 minutes of its appearance, so that it has a chance to stay in the body long enough to be digested and actually provide nourishment. The result points bonus increases the amount of food appearing or (at the gamemaster’s discretion) the quality of food."
        ],
        effect=MassEffect("Food and water", "5 kilograms"),
        duration=DurationAspect(measure="4 hr"),
        range=RangeAspect(measure="1 m"),
        casting_time=CastingTimeAspect(measure="1 r"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "focused": FocusedAspect.based_on(("effect", "duration"), target="on people eating"),
            "components": CompositeAspect(
                ComponentsAspect(
                "A plain, cloth napkin", "common"),
                ComponentsAspect("a small metal cup", "common"),
            ),
            "gesture": GesturesAspect(
                "Wave hand several times over napkin and cup", "simple",
            ),
            "other_alterants": OtherAlterant(3, "clean water and hearty food"),
        },
        other_conditions=[],
    ),

    Spell(
        name="Mystic Bolt",
        skill="Conjuration",
        notes=[
            "The mage gathers energy from his surroundings and throws the ball at a target. It does 4D in damage at a range of up to 10 meters. He must make a marksmanship roll to hit the target. The bolt must be fired in the same round that the mage casts the spell."
        ],
        effect=DamageEffect("bolt", "4D", "physical damage"),
        duration=DurationAspect(measure="3.5 s"),  # Was 1 d. Why?
        range=RangeAspect(measure="10 m"),
        casting_time=CastingTimeAspect(measure="1.5 s"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "gesture": GesturesAspect(
                "Swirl hand in air as if gathering energy, then throw it at target", "simple",
            ),
            "incantation": IncantationsAspect("Ah!", "word; loud"),
        },
        other_conditions=[],
    ),

    Spell(
        name="Mystical Shield",
        skill="Conjuration",
        notes=[
            "By tossing some sand in a circle in front of her, the caster creates a semi-transparent oval shield of the same color as the sand. The shield, about two meters in diameter, appears up to 1.5 meters away. It is focused on the ring, which the mage must wear. It offers an Armor Value of 6D against all types of physical (not mental) attacks."
        ],
        effect=ProtectionEffect("Armor Value", "6D"),
        duration=DurationAspect(measure="5 r"),
        range=RangeAspect(measure="1.5 m"),
        casting_time=CastingTimeAspect(measure="1.5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "area_effect": AreaEffectAspect("1m radius circle"),
            "components": CompositeAspect(
                ComponentsAspect("A simple ring", "uncommon"),
                ComponentsAspect("handful of colored sand", "common; destroyed"),
            ),
            "focused": FocusedAspect.based_on(("effect", "duration"), target="on ring"),
            "gesture": GesturesAspect(
                "Using colored sand, scribe an oval shape in the air", "simple",
            ),
            "incantation": IncantationsAspect("Protection!", "word"),
        },
        other_conditions=[],
    ),

    Spell(
        name="Stunned Senseless",
        skill="Conjuration",
        notes=["With a gesture and a word, the magic user sends a bolt of mystical energy toward his intended target. However, the bolt isn’t intended to harm the target, instead only doing stun damage."],
        effect=DamageEffect(
            "Bolt of energy",
            "6D+2",
            "stun only",
        ),
        duration=DurationAspect(measure="1.5 sec"),
        range=RangeAspect(measure="10 m"),
        casting_time=CastingTimeAspect(measure="1.5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "gesture": GesturesAspect(
                "Point finger and then palm at intended target", "simple",
            ),
            "incantation": IncantationsAspect("Stop!", "word"),
        },
        other_conditions=[],
    ),

]


if __name__ == "__main__":
    detail(spells)

__test__ = {
    "Cage": ">>> spells[0].difficulty\n27",
    "Communicate With Animals": ">>> spells[1].difficulty\n10",
    "Evil Eye Curse": ">>> spells[2].difficulty\n11",
    "Glow Stone": ">>> spells[3].difficulty\n11",  # Rules say 10
    "Feast": ">>> spells[4].difficulty\n11",  # Rules say 10
    "Mystic Bolt": ">>> spells[5].difficulty\n10",
    "Mystical Shield": ">>> spells[6].difficulty\n10",
    "Stunned Senseless": ">>> spells[7].difficulty\n11",  # Rules say 12
}
