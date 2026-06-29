"""
Extract Characters from ``jirair_shan``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



jirair_shan_head_curator = Character(
    name='Jirair Shan, Head Curator',
    agility=Agility(3*D, {'stealth': 3*D+1}),
    coordination=Coordination(2*D, {}),
    physique=Physique(2*D, {'lifting': 2*D+2}),
    intellect=Intellect(4*D, {'cultures': 4*D+1, 'reading/writing': 4*D+1, 'scholar SO speaking': 4*D+1, 'trading': 5*D}),
    acumen=Acumen(3*D, {'investigation': 4*D+1, 'search': 3*D+2}),
    charisma=Charisma(4*D, {'bluff': 4*D+2, 'charm': 4*D+1, 'persuasion': 4*D+1}),
    move='10',
    strength_damage=1*D,
    fate_points='1',
    character_points='6',
    body=21,
    disadvantages=[
        Devotion(R3, 'to the library'),
        Employed(R3, "can't leave the library"),
        Enemy(R1, 'those who wish to suppress knowledge')],
    advantages=[
        Authority(R2, 'head of famous library'),
        Contacts(R3, 'those who frequent the library'),
        Equipment(R4, 'the contents of the library')],
    special_abilities=[
        SkillMinimum(R1, 'minimum total for reading/writing, scholar, and investigation')],
    equipment='keys to library and rooms; fine robes (Armor Value +1); pen and ink set; tube of parchment'
)
characters = [ 
    jirair_shan_head_curator, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

