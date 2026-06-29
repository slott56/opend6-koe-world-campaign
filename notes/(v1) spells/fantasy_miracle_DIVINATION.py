"""
DIVINATION

When run as an app, generates .RST details of each Miracle.
"""

from magic1 import Aspect, Miracle, detail


invocations = [
    Miracle(
        effect=Aspect(
            format="search of 80 to locate a single type of creature",
            base_difficulty=24,
            count=1,
        ),
        duration=Aspect(format="10 seconds ", base_difficulty=5, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 min", base_difficulty=-9, count=1),
        name="Detect the Living",
        other_aspects={
            "Difficulty": Aspect(format="20", base_difficulty=0.0, count=1),
            "Area effect": Aspect(
                format="10-meter radius circle", base_difficulty=20, count=1
            ),
        },
        other_conditions=[
            Aspect(
                format="Limited to one type of creature", base_difficulty=-1, count=1
            ),
        ],
        notes="Before invoking, the devotee decides what sort of being he seeks.\nShould the cleric successfully invoke the miracle, he can detect the\npresence of any such being within a 10-meter radius for two rounds,\nwhether he can see it or not. The higher the search skill total is above\nthe difficulty, the more information the caster knows about the beings\nhe seeks (such as location, number, gender, etc.). The difficulty starts\nat 10 for a Human-sized creature, and goes down for larger creatures,\nup for smaller ones, and up for the number of other types of creatures\nin the area. Add the miracle success bonus to the search total.\n",
        skill="Divination",
    ),
    Miracle(
        effect=Aspect(format="2.5 months", base_difficulty=34, count=1),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous", base_difficulty=0, count=1),
        casting_time=Aspect(format="2 rounds ", base_difficulty=-5, count=1),
        name="Foresight",
        other_aspects={
            "Difficulty": Aspect(format="19", base_difficulty=0.0, count=1),
        },
        other_conditions=[],
        notes="When the cleric invokes this miracle, he chooses to look for a con\xad\ndition that could occur up to two and a half months into the future.\nHe can see one minute's worth of the future. Use the success level\nto determine the information received: Minimal reveals confusing\nimages. Average allows one useful fact to be gleaned from the vision.\nGood provides the cleric with a few useful facts, including the time\nof the occurrence. Superior allows the cleric to note more details,\nincluding time and location. Spectacular lets the cleric see the scene\nas if he were present, though in shades of gray.",
        skill="Divination",
    ),
]


if __name__ == "__main__":
    detail(invocations)

__test__ = {
    "Detect the Living": ">>> invocations[0].difficulty\n20",
    "Foresight": ">>> invocations[1].difficulty\n19",
}
