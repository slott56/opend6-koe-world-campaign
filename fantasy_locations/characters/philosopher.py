"""
Extract Characters from ``philsopher``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



exceptional_greek_philosopher = Character(
    name='Exceptional Greek Philosopher',
    agility=Agility(2*D, {}),
    coordination=Coordination(2*D, {}),
    physique=Physique(2*D, {}),
    intellect=Intellect(5*D, {'cultures': 5*D+1, 'know-how': 5*D+1, 'reading/writing': 5*D+2, 'scholar': 6*D, 'speaking': 5*D+1}),
    acumen=Acumen(4*D, {'investigation': 4*D+1, 'search': 4*D}),
    charisma=Charisma(3*D, {'bluff': 4*D+2, 'charm': 4*D+1, 'mettle': 4*D, 'persuasion': 5*D+1}),
    move='10',
    strength_damage=1*D,
    fate_points='1',
    character_points='7',
    body=16,
    disadvantages=[
        Devotion(R3, 'to learning'),
        Enemy(R1, 'some ideas are unpopular among the nobles')],
    advantages=[Contacts(R1, 'students')],
    equipment='robes; goblet of wine'
)
characters = [ 
    exceptional_greek_philosopher, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

