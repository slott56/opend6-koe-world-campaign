"""
Sample Spells for *D6 Magic Guidebook* "Alternate Magic Systems" chapter.

Used to create shared/sample_spells.txt.
This is included in the magic_guide/Alternate.rst
"""

from magic1 import *

spells = [
    Spell(
        name="Blink-Away",
        effect=Apportation.move_1km,
        duration=Duration.instant,
        range=Range.self_or_touch,
        casting_time=CastingTime.cast_1r,
    ),
    Spell(
        name="Projectile",
        effect=Conjuration.do_damage * 6,
        range=Range.within_10m,
        duration=Duration.instant,
        casting_time=CastingTime.cast_1s,
        notes="This 6D attack requires marksmanship/firearms or apportation to hit. It takes a form of the caster’s choosing, such as a blast of fire, water, or ice.",
    ),
    Spell(
        name="Protective Sheath",
        effect=Conjuration.prevent_damage * 6,
        range=Range.self_or_touch,
        duration=Duration.duration_1m,
        casting_time=CastingTime.cast_1s,
        notes="The caster or a target within one meter of the caster is coated in an invisible sheath that absorbs up to 6D of any type of damage.",
    ),
    Spell(
        name="Improvement",
        effect=Alteration.add_to_skill * 3,
        range=Range.self_or_touch,
        duration=Duration.duration_1m,
        casting_time=CastingTime.cast_1r,
    ),
    Spell(
        name="Search",
        effect=Divination.search_10m_sphere,
        range=Range.self_or_touch,
        duration=Duration.duration_1r,
        casting_time=CastingTime.cast_1r,
    ),
]

if __name__ == "__main__":
    # import sys
    # logging.basicConfig(level=logging.DEBUG, stream=sys.stderr)
    # for spell in spells:
    #     spell._difficulty()

    detail(spells, spell_heading="-")

__test__ = {
    "Blink-Away": """>>> spells[0].difficulty\n13""",
    "Projectile": """>>> spells[1].difficulty\n14""",
    "Protective Sheath": """>>> spells[2].difficulty\n14""",
    "Improvement": """>>> spells[3].difficulty\n10""",
    "Search": """>>> spells[4].difficulty\n16""",
}
