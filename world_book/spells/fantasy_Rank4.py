"""
Extract Spells from ``fantasy_Rank4.ipynb``.
Created by V2025.6.27.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

With "test" argument, runs doctest, which uses the __test__ examples.

"""

from opend6_tools.magic import *



countermagic = Spell(
        name="Countermagic",
        skill="Elemental Alteration",
        notes=[
            "The caster concentrates on the spell he wishes to counter, waving his hand and shouting the required incantation. The effect’s value plus the result points bonus are compared to the skill total used to create the targeted spell. If the countermagic number is equal to or higher than the target spell’s skill total, the spell is broken."
        ],
        effect=SkillEffect("compare to skill total of spell countering", "6D+1", "protection modifier"),
        duration=DurationAspect(measure="1 round"),
        range=RangeAspect(measure="60 m"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "concentration": ConcentrationAspect("3 seconds", note="mettle difficulty of 7"),
            "gesture": GesturesAspect(
                "Wave hand through air as if wiping away something", "very simple",
            ),
            "incantation": IncantationsAspect("Your hold is broken!", "sentence; loud"),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-4,
                description="One spell, which the caster must specify when casting this spell",
            )
        ],
    )

fear = Spell(
        name="Fear",
        skill="Temperamental Alteration",
        notes=[
            "To cast the spell, the mage first needs something belonging to her target — his comb, his watch, a lock of his hair. Mutter a few words of power, point the item at the target, and watch the fun. This spell gives the caster an intimidation skill bonus of +6D+2, but only towards that target. The target may disbelieve it with a Charisma or mettle roll of 13."
        ],
        effect=SkillEffect("intimidation skill bonus", "+6D+2", "skill modifier"),
        duration=DurationAspect(measure="2.5 min"),
        range=RangeAspect(measure="100 m"),
        casting_time=CastingTimeAspect(measure="1 min"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": ComponentsAspect(
                "An item owned for at least a month by the target", "very rare",
            ),
            "gesture": GesturesAspect("Point item at target", "very simple"),
            "incantation": IncantationsAspect("Frightening words", "phrase"),
            "unreal_effect": UnrealEffectAspect.based_on(("effect",), "difficulty 13")
        },
        other_conditions=[],
    )
spells = [ 
    countermagic, fear, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(spells)
    app()

