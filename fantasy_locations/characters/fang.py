"""
Extract Characters from ``fang``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



fang = Character(
    name='Fang',
    agility=Agility(4*D+1, {'acrobatics': 6*D, 'dodge': 7*D+1, 'fighting': 7*D+2}),
    coordination=Coordination(3*D, {'throwing': 3*D+1}),
    physique=Physique(3*D, {'stamina': 4*D}),
    intellect=Intellect(2*D, {'scholar snakes': 4*D}),
    acumen=Acumen(2*D+2, {'survival': 3*D}),
    charisma=Charisma(3*D, {'animal handling': 6*D, 'charm': 4*D+2, 'mettle': 4*D+1}),
    strength_damage=2*D,
    move='10',
    fate_points='0',
    character_points='4',
    body=24,
    disadvantages=[
        Quirk(R1, 'no sense of taste or smell'),
        Quirk(R2, 'does everything in a snakelike manner')],
    advantages=[
        TrademarkSpecialization(R1, 'throwing a snake at someone with one hand at the same time he does a piercing thrust with the other hand')],
    special_abilities=[
        IronWill(R2, '+2D to mettle totals and +4 difficulty modifier to all interaction attempts and mental attacks')]
)

characters = [ 
    fang, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

