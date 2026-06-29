"""
Extract Spells from ``fantasy_Rank3.ipynb``.
Created by V2025.6.27.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

With "test" argument, runs doctest, which uses the __test__ examples.

"""

from opend6_tools.magic import *



detect_living = Spell(
        name="Detect the Living",
        skill="Divination",
        notes=[
            "Before throwing the spell, the caster should decide what sort of being she’s looking for, because she’ll need a piece of it for the spell to work (a lock of hair from a Human, fur or fangs from an animal, etc.).",
            "The caster sets the object on fire and inhales the smoke while concentrating. Once the casting is done, the mage can detect the presence of any such being within a 10-meter radius for two rounds. The higher the search skill total is above the difficulty, the more information the caster knows about the beings she seeks (such as location, number, gender, etc.). The difficulty starts at 10 for a Human-sized creature, and goes down for larger creatures, up for smaller ones, and up for the number of other types of creatures in the area.",
        ],
        effect=SkillEffect("search to locate a single type of creature", "8D"),
        duration=DurationAspect(measure="10 sec"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 min"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            'area_effect': AreaEffectAspect("10 meter radius circle"),
            "component": ComponentsAspect(
                ("Something from the type of creature being detected", "uncommon; destroyed"),
                ("fire, such as a match or lit coal", "very common; destroyed"),
            ),
            "concentration": ConcentrationAspect("25 seconds", note="mettle difficulty of 9"),
            "gesture": GesturesAspect("Inhale smoke", "very simple"),
            "variable_movement": VariableMovementAspect("target invisible")
        },
        other_conditions=[],
    )
spells = [ 
    detect_living, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(spells)
    app()

