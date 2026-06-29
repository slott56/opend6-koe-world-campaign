"""
Extract Spells from ``fantasy_Rank5.ipynb``.
Created by V2025.6.27.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

With "test" argument, runs doctest, which uses the __test__ examples.

"""

from opend6_tools.magic import *



cage = Spell(
        name="Cage",
        skill="Elemental Conjuration",
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
    )

sense_past = Spell(
        name="Sense Past",
        skill="Divination",
        notes=[
            "The mage can learn about the past of a single object he touches. He’ll see visions of events that occurred in a five-meter radius around the object in the past. The mage can view events that took place in a past period of time whose value (as read on the “Spell Measures” table) is less than or equal to the effect’s value plus the result points bonus. The mage can scan back to that period at a rate of one week’s worth of images per minute of the spell."
        ],
        effect=TimeEffect("view the past", "66 weeks"),
        duration=DurationAspect(measure="66 min"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="25 min"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "area_effect": AreaEffectAspect("5 meter radius sphere"),
            "concentration": ConcentrationAspect("10 minutes", note="mettle difficulty of 11"),
            "components": ComponentsAspect(
                ("Magnifying glass", "uncommon"),
                ("expensive pocket watch", "very rare"),
            ),
            "countenance": CountenanceAspect("Skin turns sickly gray color for duration of spell", "noticeable"),
        },
        other_conditions=[
            GenericAspect(difficulty=-1, description="Physical contact with object"),
        ],
    )
spells = [ 
    cage, sense_past, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(spells)
    app()

