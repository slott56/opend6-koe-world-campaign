"""
Extract Characters from ``minotaur``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



aischros_the_minotaur = Character(
    name='Aischros, the Minotaur',
    agility=Agility(3*D+2, {'fighting': 4*D+2, 'dodge': 4*D, 'melee combat': 4*D}),
    coordination=Coordination(2*D, {'throwing': 2*D+2}),
    physique=Physique(5*D, {'lifting': 7*D, 'running': 5*D+2, 'stamina': 6*D}),
    intellect=Intellect(3*D, {'navigation': 5*D+1}),
    acumen=Acumen(2*D, {'survival': 3*D, 'tracking': 4*D}),
    charisma=Charisma(2*D+1, {'intimidation': 4*D, 'persuasion': '2D + 2', 'mettle': 4*D}),
    strength_damage=4*D,
    move='10',
    fate_points='1',
    character_points='4',
    body=25,
    advantages=[
        Size(R1, 'scale value 3')],
    disadvantages=[
        Quirk(R2, '+6 bonus to those trying to trick or anger into blind rage'),
        Quirk(R3, 'part of him wants to escape , while part wants to stay forever')],
    special_abilities=[
        Longevity(R1, 'with Burn-out (R2) if Aischros ever leaves his labyrinth'),
        NaturalHandWeapon(R1, '+1D damage'),
        Omnivorous(R1, "with Additional Effect (R3) doesn't need to eat or drink"),
        SenseOfDirection(R4, '+4D to navigation and tracking')
    ],
    equipment='Large axe (damage +3D)'
)
characters = [ 
    aischros_the_minotaur, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

