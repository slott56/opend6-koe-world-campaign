"""
"OpenD6 Project" Spells

See *The OpenD6 Project*, https://opend6project.wordpress.com.

Most of the OpenD6 project contains spells from the *OpenD6 Fantasy Rulebook*, "PRECALCULATED SPELLS" chapter.
A few are unique to the OpenD6 project.

When run as an app, generates .RST details of each Spell.
"""

from opend6_tools.magic2 import *

cantrips = [
    Spell(
        name="Aid",
        skill="Conjuration",
        notes=["By touching an injured being, the magic user can use this cantrip to heal harm as if he had 5D+2 in the medicine skill."],
        effect=SkillEffect("medicine skill", "5D+2"),  # "skill modifier"), ?
        duration=DurationAspect(measure="1.5 seconds"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={},
        other_conditions=[
            GenericAspect(
                difficulty=-3,
                description="Physical contact with creature; may only be used on living creatures",
            )
        ],
    ),
    Spell(
        name="Meal",
        skill="Conjuration",
        notes=[
            "With this cantrip, the mage creates a simple meal of bread and water, which sticks around in the system long enough to be digested and actually provide nourishment."],
        effect=Effect(description="1 kilogram of bread and water"),
        duration=DurationAspect(measure="4 hours"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect(
                "A plain, cloth napkin, a small metal cup", "common; common"
            ),
            "gestures": GesturesAspect(
                "Wave hands several times over napkin and cup", "simple",
            ),
            "incantation": IncantationsAspect("Fill these with food and drink.",
                                              "sentence"),
        },
        other_conditions=[],
    ),
]

alteration_spells = [
    Spell(
        name="Deadly Bullet",
        skill="Alteration",
        notes=[
            "This spell uses a piece of black obsidian to increase the deadliness of a bullet. The mage utters a short, dark phrase while gently stroking the tip of the bullet across the stone. The darkness travels into the bullet, draining the stone of its pigment.",
            "To release the spell, the caster inserts it into an appropriate gun within five rounds of casting the spell. The gun’s user must generate an marksmanship total, adding a +2 bonus for the increased accuracy of the spell, against the combat difficulty for the target. The target must be within range of the spell, or the bullet merely does its normal effect. The target takes an additional 4D in damage in the round the bullet hits and for the next four rounds. The spell ends if the target moves beyond the spell’s range.",
        ],
        effect=DamageEffect("Bullet", "+4D", "physical damage; damage modifier"),
        duration=DurationAspect(measure="5 rounds"),
        range=RangeAspect(measure="100 m"),
        casting_time=CastingTimeAspect(measure="1 hr"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "component": ComponentsAspect(
                ("Black obsidian", "uncommon; destroyed"),
                ("bullet", "common"),
            ),
            "feedback": FeedbackAspect(3),
            "focused": FocusedAspect.based_on(("effect", "duration"), target="on terget"),
            "gesture": GesturesAspect("Rub the tip of the bullet on the stone", "very simple"),
            "incantation": IncantationsAspect("Darkness of death.", "phrase"),
            "variable_movement": VariableMovementAspect("accuracy bonus"),
        },
        other_conditions=[],
    ),

    Spell(
        name="Drain Toughness",
        skill="Alteration",
        notes=[
            "Caster focuses magical energies into a funnel, with the large end facing the target. When activated, the funnel pulls energy from the target, and sends it to the source of the spell. The spell itself is not visible, but it can be felt. It requires a marksmanship roll to focus on a target.",
            "Compare the spell effect’s value to a roll of the target’s Physique. Multiply the difference by 3. This is the target’s negative damage resistance total modifier. If this number is greater than 3 times the die code in the target’s Physique (ignore the pips), the target is unconscious for eight hours. The negative modifier vanishes after one minute.",
            "The caster receives one-half (rounded up) of the negative damage resistance total modifier as a positive modifier to her damage resistance. When the spell wears off after one minute, the resistance total bonus goes with it.",
        ],
        effect=SkillEffect("drain damage resistance", "8D"),
        duration=DurationAspect(measure="1 min"),
        range=RangeAspect(measure="40 m"),
        casting_time=CastingTimeAspect(measure="15 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect(
                ("Blood of a great cat", "very rare; destroyed"),
                ("funnel", "common; destroyed"),
            ),
            "gesture": GesturesAspect("Pick up an item and pull it closer", "very simple"),
            "incantation": IncantationsAspect("Weaken and perish before my hand.", "sentence"),
        },
        other_conditions=[],
    ),
]

apportation_spells = [

    Spell(
        name="Doorway Home",
        skill="Apportation",
        notes=[
            "After the mage casts the spell, she has firmly fixed in her mind three uses of it. When she releases the spell, she opens a doorway in front of her through which she may step through and instantly be transported somewhere else. The points the skill total is above the difficulty may be added to the effect’s value (thus increasing the amount that can travel through the doorway). An unbreakable barrier over the doorway resists weight of a greater amount than what the spell can handle to go through the doorway. The doorway remains open for two rounds, allowing up to two passages of material weighing no more than 150 kilograms."
        ],
        effect=MassEffect("passage can handle", "150 kg"),
        duration=DurationAspect(measure="2 rounds"),
        range=RangeAspect(measure="100 km"),
        casting_time=CastingTimeAspect(measure="2.75 hr"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "charges": ChargesAspect(3),
            "components": ComponentsAspect(
                "Something from the location", "ordinary; destroyed",
            ),
            "concentration": ConcentrationAspect("40 minutes", note="willpower difficulty of 12"),
            "incantations": IncantationsAspect("A statement describing the place", "sentence"),
            "gestures": GesturesAspect(
                "Pantomime building a doorway", "complex (artist roll with difficulty of 11)",
            ),
        },
        other_conditions=[],
    ),

    Spell(
        name="Retrieve",
        skill="Apportation",
        notes=[
            "Through the use of this spell, the caster can target something he’s seen through a view spell and bring it to his current location (assuming he’s no more than one kilometer from the object). The object can weigh no more than the effect’s value (including bonuses) as read on the “Spell Measures” table."
        ],
        effect=MassEffect("move an object", "10 kilograms"),
        duration=DurationAspect(measure="2.5 sec"),
        range=RangeAspect(measure="1 km"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "gesture": GesturesAspect(
                "Stand on tiptoes, point out to imaginary objects and then reach to pick them up.", "simple",
            ),
            "incantation": IncantationsAspect("I want to reach out beyond the boundaries of the time and space. I want that object to return with me.", "sentence"),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-5,
                description="May only be cast in conjunction with View (spell described herein)",
            )
        ],
    ),
]


conjuration_spells = [
    Spell(
        name="Bad Luck Curse",
        skill="Conjuration",
        notes=["With a minimal amount of pain to himself, the caster curses a Human target with 10 minutes of Bad Luck (R2). See the description of this Disadvantage in the “Character Options” chapter for details."],
        effect=DisadvantageEffect("Bad Luck", 2),
        duration=DurationAspect(measure="10 min"),
        range=RangeAspect(measure="10 m"),
        casting_time=CastingTimeAspect(measure="2 rounds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "focused": FocusedAspect.based_on(("effect", "duration"), target="on target"),
            "feedback": FeedbackAspect(3),
            "concentration": ConcentrationAspect("1 round", note="willpower difficulty of 8"),
        },
        other_conditions=[GenericAspect(difficulty=-3, description="Limited to Humans")],
    ),

    Spell(
        name="Displacement",
        skill="Conjuration",
        notes=[
            "By bending the light around the target, an image of the person or thing is transferred up to 2.5 meters away from his actual location. He becomes invisible to normal sight at his true location, and his image appears and copies all of his movements and actions until the end of the duration. A character must beat a difficulty of 20 with a Perception or search roll or a location spell to find the displaced target.",
            "Anyone touching the image recognizes it for what it really is. This does not give them the ability to see where the target is standing. Any area effect attacks and spells will hit the target should he be in the radius. Otherwise, only using items or other spells discloses the true location of the target.",
        ],
        effect=CompositeEffect(
            "Displaced image",
            DisadvantageEffect("Hindrance: search", 7, "difficulty of 20"),
               DistanceEffect("image transfer", "2.5 meters"),
        ),
        duration=DurationAspect(measure="100 sec"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 r"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "gesture": GesturesAspect(
                "Turn around and then start hopping from one location to another, while looking back at previous spot before jumping again", "complex (acrobatics roll with difficulty of 11)",
            ),
            "incantation": IncantationsAspect("Hide my true location from sight.", "sentence"),
        },
        other_conditions=[],
    ),

    Spell(
        name="Flight",
        skill="Conjuration",
        notes=[
            "This spell provides the target, who must be within one meter of the caster, the ability to fly and the knowledge to use it for 10 minutes. There is no visible means of convenience; the target can simply move through the air by force of will. The rate equals twice the target’s normal movement rate."
        ],
        effect=CompositeEffect(
            "Skilled Flight",
           SpecialAbilityEffect("Flight", 1),
            SkillEffect("flying skill", "+1D"),
        ),
        duration=DurationAspect(measure="10 min"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="3 r"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "concentration": ConcentrationAspect("1 round", note="willpower difficulty of 8"),
            "component": ComponentsAspect("Bird’s feather", "very common"),
            "focused": FocusedAspect.based_on(("effect", "duration"), target="on target"),
            "gesture": GesturesAspect("Point at target", "very simple"),
            "incantation": IncantationsAspect("Fly!", "phrase"),
        },
        other_conditions=[],
    ),

    Spell(
        name="Helping Hand",
        skill="Conjuration",
        notes=["The caster can move items without touching them, as if he had the Psionics telekinesis skill at 4D+1. See the description of the telekinesis skill in the “Psionics” chapter for difficulties and ranges."],
        effect=SkillEffect("Psionics: telekinesis", "4D+1"),
        duration=DurationAspect(measure="5 rounds"),
        range=RangeAspect(measure="1 m"),
        casting_time=CastingTimeAspect(measure="1 r"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "focused": FocusedAspect.based_on(("effect", "duration"), target="on caster"),
        },
        other_conditions=[],
    ),
    Spell(
        name="Light",
        skill="Conjuration",
        notes=[
            "The magic user casts this spell on a small, white stone, making it glow with a fierce radiance that extends for one meter in all directions around the pebble. The effect lasts for 10 minutes. Once the duration wears off, the pebble turns to dust."
        ],
        effect=SkillEffect("negates darkness modifier", "4D"),
        duration=DurationAspect(measure="10 min"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="2 rounds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "area_effect": AreaEffectAspect("1m radius sphere"),
            "components": ComponentsAspect("white pebble", "common; destroyed"),
            "focused": FocusedAspect.based_on(("effect", "duration"), target="on pebble"),
            "gestures": GesturesAspect(
                "Hold pebble between thumb and forefinger", "very simple",
            ),
            "incantation": IncantationsAspect("Stone of white, give us light.", "sentence"),
        },
        other_conditions=[],
    ),

    Spell(
        name="Voodoo Curse",
        skill="Conjuration",
        notes=[
            "With a few simple items and a spell inspired by the rites of the vodun religion, the caster can cause great pain to his target. First the caster attaches the scrap of clothing or the lock of hair to the doll. Then, while placing pins in appropriate places, the caster describes the kind of pain he desires his target to feel. For 10 minutes after the completion of the spell, the target receives a +2 difficulty modifier to the caster’s choice of any three skills."
        ],
        effect=DisadvantageEffect("Hindrance", 2),
        duration=DurationAspect(measure="10 min"),
        range=RangeAspect(measure="1 km"),
        casting_time=CastingTimeAspect(measure="2 r"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect(
                ("Scrap from clothing target wore recently or lock of hair", "very rare"),
                ("doll in the shape of Human", "common"),
                ("several large, thick pins", "common"),
            ),
            "concentration": ConcentrationAspect("1 round", note="willpower difficulty of 8"),
            "incantation": IncantationsAspect("Description of what caster wants the target to feel", "sentence",
            ),
            "focused": FocusedAspect.based_on(("effect", "duration"), target="on target"),
        },
        other_conditions=[],
    ),
]


divination_spells = [

    Spell(
        name="View",
        skill="Divination",
        notes=[
            "The caster opens a tunnel of sorts in space. Nothing may pass through it, but the caster may look through it to the other end. The tunnel starts with a range of one kilometer. This range is determined by the range value of the spell, and can be much longer, depending on the success the caster has throwing the spell. Any bonus from casting goes to both range and speed, being split evenly between them. (To determine the bonus, subtract the skill total from the spell difficulty. Divide by 2, and round up. Add this number to the range and look up the new value on the “Spell Measures” table.)",
            "The effect of the spell takes the place of the character’s search while using the spell, as it is hard to make out minute details.",
        ],
        effect=SkillEffect("search skill", "3D"),
        duration=DurationAspect(measure="10 min"),
        range=RangeAspect(measure="1 km"),
        casting_time=CastingTimeAspect(measure="1 min"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "feedback": FeedbackAspect(3),
            "gesture": GesturesAspect(
                "Make swimming gestures with hands", "simple",
            ),
            "incantation": IncantationsAspect("Let me see beyond what I know to be.", "sentence"),
        },
        other_conditions=[],
    ),
]

books = {
    "Cantrips": cantrips,
    "Alteration Spells": alteration_spells,
    "Apportation Spells": apportation_spells,
    "Conjuration Spells": conjuration_spells,
    "Divination Spells": divination_spells,
}



__test__ = {
    "Aid": ">>> cantrips[0].difficulty\n6",  # Rules say 5
    "Meal": ">>> cantrips[1].difficulty\n4",

    "Deadly Bullet": ">>> alteration_spells[0].difficulty\n9",  # NOT part of original Fantasy rules.
    "Drain Toughness": ">>> alteration_spells[1].difficulty\n12",

    "Doorway Home": ">>> apportation_spells[0].difficulty\n18",
    "Retrieve": ">>> apportation_spells[1].difficulty\n12",

    "Bad Luck Curse": ">>> conjuration_spells[0].difficulty\n11",
    "Displacement": ">>> conjuration_spells[1].difficulty\n12",
    "Flight": ">>> conjuration_spells[2].difficulty\n15",  # Rules say 16
    "Helping Hand": ">>> conjuration_spells[3].difficulty\n10",
    "Light": ">>> conjuration_spells[4].difficulty\n11", # Rules say 12
    "Voodoo Curse": ">>> conjuration_spells[5].difficulty\n17",  # NOT part of original Fantasy rules.

    "View": ">>> divination_spells[0].difficulty\n19",
}

if __name__ == "__main__":
    app = build_app(books)
    app()
