"""
Extract Characters from ``sofronius``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



sofronius_ruler = Character(
    name='Sofronius, Ruler',
    agility=Agility(3*D, {'melee combat': 4*D+2, 'riding': 4*D+1}),
    coordination=Coordination(2*D, {'marksmanship': 3*D+2}),
    physique=Physique(3*D, {'running': 4*D, 'stamina': 4*D}),
    intellect=Intellect(3*D+2, {'cultures': 3*D, 'reading/writing': 3*D+1, 'speaking': 4*D}),
    acumen=Acumen(3*D, {'investigation': 3*D+2, 'streetwise': 3*D+1, 'search': 3*D+1}),
    charisma=Charisma(3*D+1, {'bluff': 3*D+2, 'persuasion': 4*D}),
    move='10',
    strength_damage=2*D,
    fate_points='1',
    character_points='4',
    body=27,
    disadvantages=[Enemy(R1, 'there are those who envy his power')],
    advantages=[
        Authority(R3, 'ruler'),
        Contacts(R1, 'members of the Assembly')],
    equipment='robes; small dagger (damage +2)'
)
characters = [ 
    sofronius_ruler, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

