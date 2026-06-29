"""
Extract Characters from ``monks``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



monk = Character(
    name='Monk',
    agility=Agility(2*D, {}),
    coordination=Coordination(2*D, {}),
    physique=Physique(2*D, {}),
    intellect=Intellect(3*D, {'healing': 4*D, 'reading/writing': 4*D, 'scholar': 5*D}),
    acumen=Acumen(2*D+2, {'crafting': 4*D}),
    charisma=Charisma(2*D+1, {'mettle': 3*D}),
    strength_damage=1*D,
    move='10',
    fate_points='0',
    character_points='2',
    body=11,
    disadvantages=[Devotion(R2, 'to the holy order (including a vow of poverty)')],
    advantages=[]
)

brother_nyll = Character(
    name='Brother Nyll',
    agility=Agility(2*D, {}),
    coordination=Coordination(2*D+1, {}),
    physique=Physique(2*D, {}),
    charisma=Charisma(3*D+1, {'charm': 4*D, 'command': 4*D+2, 'mettle': 4*D}),
    intellect=Intellect(4*D+2, {'cultures': 3*D+1, 'healing': 4*D+2, 'reading/writing': 5*D, 'scholar': 6*D}),
    acumen=Acumen(3*D+2, {'crafting': 4*D}),
    strength_damage='1D',
    move='1 O',
    fate_points='0',
    character_points='4',
    body=21,
    disadvantages=[
        Age(R1),
        Devotion(R2, 'to the holy order (including a vow of poverty)'),
        Employed(R2, 'to the holy order')],
    advantages=[
        Authority(R1, 'over the holy order'),
        Contacts(R1, 'within the holy order')]
)
characters = [ 
    monk, brother_nyll, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

