"""
Template Character from OpenD6 Fantasy Rulebook.
Used to populate "Introduction" chapter.
"""
from textwrap import dedent
from opend6_tools.character import *

hero = Character(
    occupation="Aspiring Hero",
    race="Human",
    agility=Agility(
        3 * D + 1,
        {
            "acrobatics": 0,
            "climbing": 0,
            "dodge": 0,
            "fighting": 0,
            "flying": 0,
            "jumping": 0,
            "melee combat": 0,
            "stealth": 0,
        },
    ),
    intellect=Intellect(
        2 * D + 2,
        {
            "cultures": 0,
            "healing": 0,
            "navigation": 0,
            "speaking": 0,
            "trading": 0,
            "traps": 0,
        },
    ),
    coordination=Coordination(2 * D + 2, {"marksmanship": 0, "throwing": 0}),
    acumen=Acumen(
        3 * D + 1,
        {
            "crafting": 0,
            "hide": 0,
            "investigation": 0,
            "know-how": 0,
            "search": 0,
            "streetwise": 0,
            "survival": 0,
            "tracking": 0,
        },
    ),
    physique=Physique(3 * D, {"lifting": 0, "running": 0, "swimming": 0, "stamina": 0}),
    charisma=Charisma(
        3 * D, {"charm": 0, "intimidation": 0, "mettle": 0, "persuade": 0}
    ),
    weapons=["Dagger (damage +1D)"],
    armor=["leather jerkin (Armor Value + 2)"],
    equipment=["shoulder bag with cheese, bread, and silver coins in it"],
    description=dedent("""\
        Always fascinated by the traveling sword-showmen that came through
        your little village, you practiced mimicking their techniques (in between your chores
        - and sometimes as part of them). Perhaps inheriting wanderlust from your uncle, you
        have set on to find your fortune in the larger world and maybe gain fame by helping a few
        people along the way"""),
)

all_characters = {
    'Hero': hero
}


if __name__ == "__main__":
    app = build_app(all_characters)
    app()

__test__ = {
    "hero": ">>> hero.attributes\nDieCode(18, 0)\n>>> hero.skills\nDieCode(0, 0)\n",
}
