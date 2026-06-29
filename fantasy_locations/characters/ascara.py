"""
Extract Characters from ``ascara``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



ascra = Character(
    name='Ascra',
    agility=Agility(3*D, {'acrobatics': 4*D, 'dodge': 4*D+2, 'melee combat': 4*D+1, 'stealth': 4*D}),
    coordination=Coordination(3*D, {'marksmanship': 4*D+2}),
    physique=Physique(2*D, {'running': 2*D+2, 'stamina': 2*D+1, 'swimming': 3*D}),
    intellect=Intellect(3*D, {'healing': 3*D+2, 'navigation': 4*D, 'reading/writing': 3*D+1, 'speaking': 3*D+1}),
    acumen=Acumen(3*D, {'hide': 4*D+1, 'search': 3*D+2, 'survival': 3*D+1, 'tracking': 3*D+1}),
    charisma=Charisma(3*D, {'animal handling': 4*D, 'command': 3*D+1, 'charm': 3*D+2, 'persuasion': 4*D, 'mettle': 4*D}),
    extranormal=Magic(1*D, {'conjuration': 2*D}),
    strength_damage=1*D,
    move='10',
    fate_points='1',
    character_points='3',
    body=21,
    disadvantages=[
        Devotion(R2, 'feel a deep devotion and kinship with trees and plants'),
        Hindrance(R2, '+2 to bluff, charm, and persuasion difficulties'),
        Hindrance(R2, '-2 to damage resistance total')],
    advantages=[],
    special_abilities=[
        EnhancedSense(R1, '+1 to sight-based totals'),
        Longevity(R1),
        SkillBonus(R1, '+1 hide, stealth, and tracking totals')],
    equipment='longbow and 20 arrows (damage +2D+2); Elven forest cloak (1D+1 to hide); dagger (damage +1D)'
)
characters = [ 
    ascra, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

