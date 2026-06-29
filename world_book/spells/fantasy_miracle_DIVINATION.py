"""
Extract Spells from ``fantasy_miracle_DIVINATION.ipynb``.
Created by V2025.6.27.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

With "test" argument, runs doctest, which uses the __test__ examples.

"""

from opend6_tools.magic import *



detect_living = Miracle(
        name="Detect the Living",
        skill="Divination",
        notes="Before invoking, the devotee decides what sort of being he seeks.\nShould the cleric successfully invoke the miracle, he can detect the\npresence of any such being within a 10-meter radius for two rounds,\nwhether he can see it or not. The higher the search skill total is above\nthe difficulty, the more information the caster knows about the beings\nhe seeks (such as location, number, gender, etc.). The difficulty starts\nat 10 for a Human-sized creature, and goes down for larger creatures,\nup for smaller ones, and up for the number of other types of creatures\nin the area. Add the miracle success bonus to the search total.\n",
        effect=GenericEffect(
            description="search of 8D to locate a single type of creature", difficulty=24
        ),
        duration=DurationAspect("10 seconds"),
        range=RangeAspect("self"),
        speed=SpeedAspect.based_on(("range",), ""),
        casting_time=CastingTimeAspect("1 min"),
        other_aspects={"area_effect": AreaEffectAspect( "10 meter radius circle")},
        other_conditions=[
            GenericAspect(-1, "Limited to one type of creature"),
            GenericAspect(0, "Difficulty: 20"),
        ],
    )

foresight = Miracle(
        name="Foresight",
        skill="Divination",
        notes="When the cleric invokes this miracle, he chooses to look for a condition that could occur up to two and a half months into the future.\nHe can see one minute's worth of the future. Use the success level\nto determine the information received: Minimal reveals confusing\nimages. Average allows one useful fact to be gleaned from the vision.\nGood provides the cleric with a few useful facts, including the time\nof the occurrence. Superior allows the cleric to note more details,\nincluding time and location. Spectacular lets the cleric see the scene\nas if he were present, though in shades of gray.",
        effect=TimeEffect("2.5 months"),
        duration=DurationAspect("1 minute"),
        range=RangeAspect("self"),
        speed=SpeedAspect.based_on(("range",), ""),
        casting_time=CastingTimeAspect("2 rounds"),
        other_aspects={},
        other_conditions=[GenericAspect(0, "Difficulty: 19")],
    )

detect_enemy = Miracle(
        name="Detect Enemies",
        skill="Divination",
        notes="This can only find those with active animosity or hunters who consider the caster to be prey",
        effect=GenericEffect(
            description="search of 8D to locate active enemies", difficulty=24,
        ),
        duration=DurationAspect("10 seconds"),
        range=RangeAspect("self"),
        speed=SpeedAspect.based_on(("range",), ""),
        casting_time=CastingTimeAspect("1 min"),
        other_aspects={"area_effect": AreaEffectAspect( "10 meter radius circle")},
        other_conditions=[
            GenericAspect(-1, "Limited to those with malicious intent"),
        ],
    )
spells = [ 
    detect_living, foresight, detect_enemy, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(spells)
    app()

