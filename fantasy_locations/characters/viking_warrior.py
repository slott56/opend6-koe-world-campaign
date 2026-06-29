"""
Extract Characters from ``viking_warrior``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



typical_viking_warrior = Character(
    name='Typical Viking Warrior',
    agility=Agility(3*D+1, {'fighting': 3*D+2, 'melee combat': 3*D+2, 'riding': 3*D+2}),
    coordination=Coordination(3*D+1, {}),
    physique=Physique(4*D+1, {'running': 4*D+2, 'stamina': 4*D+2}),
    intellect=Intellect(2*D, {'navigation': 3*D+1}),
    acumen=Acumen(3*D, {'search': 4*D, 'traps': 4*D}),
    charisma=Charisma(2*D, {'animal handling': 3*D, 'intimidation': 3*D+1}),
    move='10',
    strength_damage=2*D,
    fate_points='0',
    character_points='0',
    body=18,
    disadvantages=[
        Quirk(R2, 'dislikes those who use magic or appear to have supernatural powers (+4 to difficulty when interacting with such people)'),
        Infamy(R1, 'feared as a Viking by many')],
    equipment='hardened leather armor (Armor Value +1D+1); medium shield (armor +2D+1); and broadsword (+2D+2)'
)
characters = [ 
    typical_viking_warrior, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

