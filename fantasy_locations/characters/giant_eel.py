"""
Extract Characters from ``giant_eel``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



giant_eel = Creature(
    name='Giant Eel',
    agility=Agility(5*D, {'fighting': 5*D, 'contortion': 5*D, 'dodge': 5*D, 'stealth': 5*D+1}),
    coordination=Coordination(2*D, {}),
    physique=Physique(3*D, {'lifting': 4*D+1, 'swimming': 4*D}),
    intellect=Intellect(1*D, {}),
    acumen=Acumen(2*D, {'search': 3*D, 'tracking': 3*D}),
    charisma=Charisma(2*D, {'intimidation': 3*D, 'mettle': 2*D+2}),
    move='10 ( swimming )',
    strength_damage=2*D,
    body=14,
    natural_abilities=[
        NaturalAbility('breathe in water'),
        NaturalAbility('constriction (successful tackle does +1D damage per round, cumulative, after the first round, to a maximum of +3D)'),
        NaturalAbility('jaws (damage +1D)'),
        NaturalAbility('thick hide (Armor Value +2)'),
        NaturalAbility('large size (scale value 1)')]
)

creatures = [
    giant_eel, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(creatures)
    app()

