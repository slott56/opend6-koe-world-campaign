"""
fantasy_CANTRIPS

When run as an app, generates .RST details of each Spell.
"""

from magic2 import *
from decimal import Decimal


spells = [
    Spell(
        name="Charm",
        skill="Alteration",
        notes=[
            "With a smile and a friendly gesture, the caster improves his charm skill by for one minute. (If he no charm skill, add the bonus to the character’s Charisma attribute.) As this is an illusory spell, if the intended target of the charm disbelieves it, any effect the charm attempt had wears off immediately."
        ],
        effect=SkillEffect("charm skill", "+4D"),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "gesture": GesturesAspect(
                "Smile and make a gesture of welcome or admiration", "simple"
            ),
            "unreal_effect": UnrealEffectAspect.based_on(("effect",), "difficulty 13"),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-2,
                description="May only be used on humanoids who understand the caster’s language and can hear the caster",
            ),
        ],
    ),
    Spell(
        name="Heighten Attribute (Template)",
        skill="Alteration",
        notes=[
            "This cantrip gives the target a bonus of +1D to one of his attributes for 25 seconds, or five rounds — as long as he doesn’t move more than a meter from the spot on which he received the bonus.",
            "Note that this is only a template for a spell and not an actual spell, because it does not indicate in the description which attribute is affected. The caster must specify which attribute and skill to mime before learning the spell (which takes one round).",
        ],
        effect=SkillEffect("bonus to one non-Extranormal attribute", "+1D", "skill modifier"),
        duration=DurationAspect(measure="5 rounds"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "gesture": GesturesAspect(
                "Mime an activity using a skill that falls under the attribute to be heightened", "complex (action difficulty of 11. Examples: sleight of hand for Coordination, lifting for Physique)",
            )
        },
        other_conditions=[],
    ),


    # It's not at all clear what this effect really is.
    # The rules assign difficulty of 18.
    # It seems like (temporary) physical damage to the lock. 10 pts over 2D. Which would be Alteration.
    # Another possibility is an alteration to create a new skill in lockpicking. It doesn't fit the description well, but, the effect is easy to define.
    # +4D lock picking as a skill modifier (1.5 multiplier). Which would be Alteration.
    #
    # Apportation suggests the lock's internals are rearranged, but apportation of a lock 1 kg or less is trivial.
    # Maybe the real difficulty is skilled apportation of selected parts of the lock? No provision for this in the rules.
    Spell(
        name="Open Lock",
        skill="Apportation",
        notes=[
            "To cast this cantrip, the mage touches the lock with one hand while, with the key held in it, miming opening the lock with the other hand. After reciting the incantation, he touches the lock with the key and turns the key. If the spell effect’s value is equal to or greater than the difficulty of the lock, it opens. If there are any traps or wards on the lock, they are not circumvented by this spell! Note that this spell works on any kind of mechanical lock."
        ],
        #effect=DamageEffect("Temporary Physical Damage (A lock is 10 pts with 2D resistance)", "5D+2"),
        effect=SkillEffect("Lock picking", "4D", "Skill modifier"),
        duration=DurationAspect(measure="1 round"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect("Large metal key", "common"),
            "gesture": GesturesAspect(
                "Mime opening the lock with the key", "simple",
            ),
            "incantation": IncantationsAspect("Open, Lock, and reveal your secrets.", "sentence"),
        },
        other_conditions=[GenericAspect(difficulty=-1, description="Physical contact with lock")],
    ),
]


if __name__ == "__main__":
    detail(spells)

__test__ = {
    "Charm": ">>> spells[0].difficulty\n5",
    "Heighten Attribute (template)": ">>> spells[1].difficulty\n3",
    "Open Lock": ">>> spells[2].difficulty\n5",
}
