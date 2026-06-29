"""
Extract Characters from ``morcades``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



morcades_witch = Character(
    name='Morcades, Witch',
    agility=Agility(2*D, {'dodge': 3*D}),
    coordination=Coordination(2*D, {'sleight of hand': 3*D+2}),
    physique=Physique(2*D, {}),
    intellect=Intellect(4*D, {'healing': 4*D+2, 'reading/writing': 4*D+1, 'scholar': 4*D+1, 'speaking': 4*D+1, 'trading': 4*D+1}),
    acumen=Acumen(3*D, {'disguise': 4*D, 'hide': 3*D+1, 'know-how': 3*D+1, 'survival': 3*D+1}),
    charisma=Charisma(3*D, {'animal handling': 3*D+1, 'bluff': 4*D, 'charm': 4*D+2, 'intimidation': 4*D, 'mettle': 3*D+1}),
    extranormal=Magic(2*D, {'alteration': 2*D+2, 'conjuration': 2*D+1, 'divination': 3*D}),
    move='10',
    strength_damage=1*D,
    fate_points='1',
    character_points='6',
    body=16,
    disadvantages=[
        Prejudice(R2, 'hated by locals -- being spotted in a village can result in capture and execution (+6 to the difficulty of all interactions skills)')],
    special_abilities=[
        Fear(R2, 'strike viewers with fear (+2 to all intimidation totals)')],
    equipment='various herbs and potions; heavy, clean garments (Armor Value +1)'
)
characters = [ 
    morcades_witch, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

