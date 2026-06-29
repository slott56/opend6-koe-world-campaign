"""
Extract Characters from ``healfdene``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



healfdene_thane = Character(
    name='Healfdene, Thane',
    agility=Agility(3*D, {'fighting': 4*D, 'melee combat': 5*D, 'riding': 3*D+2}),
    coordination=Coordination(2*D+2, {'throwing': 3*D+1}),
    physique=Physique(4*D+1, {'running': 5*D+2, 'stamina': 5*D+1}),
    intellect=Intellect(2*D, {'navigation': 3*D, 'traps': 2*D+2}),
    acumen=Acumen(3*D, {'search': 3*D+1}),
    charisma=Charisma(3*D, {'animal handling': 3*D+2, 'intimidation': 4*D+1}),
    move='10',
    strength_damage=3*D,
    fate_points='1',
    character_points='3',
    body=28,
    disadvantages=[
        Quirk(R2, 'dislikes those who use magic or appear to have supernatural powers (+4 to difficulty when interacting with such people)'),
        Enemy(R1, 'at least one king has vowed revenge'),
        Infamy(R1, 'feared as a Viking by many')],
    advantages=[
        Authority(R3, 'ruler'),
        Wealth(R4)],
    equipment='ring mail armor (Armor Value +1D+1); battle axe (damage +3D)'
)
characters = [ 
    healfdene_thane, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

