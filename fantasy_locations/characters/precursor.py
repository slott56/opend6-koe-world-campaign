"""
Extract Characters from ``precursor``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



precusor_priest = Character(
    name='Precusor, Priest',
    agility=Agility(2*D+1, {}),
    coordination=Coordination(2*D+1, {}),
    physique=Physique(2*D+2, {}),
    intellect=Intellect(2*D+1, {'scholar': 3*D, 'speaking': 2*D+2}),
    charisma=Charisma(2*D+1, {'charm': 2*D+2, 'command': 3*D+1, 'mettle': 2*D+2, 'persuasion': 2*D+2}),
    acumen=Acumen(2*D, {}),
    extranormal=Miracles(4*D, {'divination': 4*D+2, 'favor': 6*D+2, 'strife': 6*D+2}),
    strength_damage=1*D,
    move='10',
    fate_points='1',
    character_points='5',
    body=28,
    disadvantages=[
        Devotion(R3, 'to the Perpetual Falling Land'),
        Employed(R3, 'to the Perpetual Falling Land')],
    advantages=[
        Authority(R3, 'over the followers of the Perpetual Falling Land')],
    special_abilities=[
        SkillBonus(R1, '+1 bonus to command, intimidation, and persuasion totals')]
)
characters = [ 
    precusor_priest, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

