"""
Extract Spells from ``fantasy_CANTRIPS.ipynb``.
Created by V2025.6.27.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

With "test" argument, runs doctest, which uses the __test__ examples.

"""

from opend6_tools.magic import *



charm = Spell(
        name="Charm",
        skill="Temperamental Alteration",
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
    )

heighten_attribute =     Spell(
        name="Heighten Attribute (Template)",
        skill="Temperamental Alteration",
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
    )

open_lock =    Spell(
        name="Open Lock",
        skill="Elemental Alteration",
        notes=[
            "To cast this cantrip, the mage touches the lock with one hand while, with the key held in it, miming opening the lock with the other hand. After reciting the incantation, he touches the lock with the key and turns the key. If the spell effect’s value is equal to or greater than the difficulty of the lock, it opens. If there are any traps or wards on the lock, they are not circumvented by this spell! Note that this spell works on any kind of mechanical lock. The interior is partially destroyed."
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
    )
spells = [ 
    charm, heighten_attribute, open_lock, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(spells)
    app()

