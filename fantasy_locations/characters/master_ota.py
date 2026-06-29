"""
Extract Characters from ``master_ota``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook``


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *

master_ota = Character(
    name='Master Ota',
    agility=Agility(4 * D + 2, {'acrobatics': 5*D+2, 'dodge': 5*D+2, 'fighting':  7*D+2, 'melee combat': 6*D+1}),
    coordination=Coordination(2 * D + 2, {}),
    physique=Physique(2 * D + 2, {'lifting': 3 * D, 'running': 3*D, 'stamina': 3*D}),
    intellect=Intellect(2 * D, {'scholar: teaching': 5 * D}),
    acumen=Acumen(2 * D, {'investigation': 3 * D + 1}),
    charisma=Charisma(2 * D, {'command': 2 * D + 2, 'mettle': 4 * D}),
    move='10',
    strength_damage=2 * D,
    fate_points='1',
    character_points='10',
    body=28,
    disadvantages=[Devotion(R3, 'to the Path of Stone'),
                   Enemy(R2, 'foes of his school')],
    advantages=[Fame(R1)],
    special_abilities=[
        Ambidextrous(R1, '+ 1 to select skill totals when using two hands'),
        CombatSense(R1, '-2 to surprise modifier'),
        FastReactions(R1, '+1D to initiative and 3 extra actions per adventure'),
        Hardiness(R1, '+1 to damage resistance total'),
        PainTolerance(R1, 'ignore effects of 1 level of injury'),
    ],
)
characters = [
    master_ota,
]

__test__ = {

    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""

}

if __name__ == "__main__":
    app = build_app(characters)
    app()

