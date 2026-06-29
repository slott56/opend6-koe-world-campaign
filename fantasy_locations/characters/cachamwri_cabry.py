"""
Extract Characters from ``cachamwri_cabry``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



cachamwri_cabry_inn_keeper = Character(
    name='Cachamwri Cabry, Inn Keeper',
    agility=Agility(3*D, {'dodge': 4*D, 'fighting': 3*D+2, 'stealth': 4*D}),
    coordination=Coordination(4*D, {'lockpicking': 4*D+1, 'sleight of hand': 4*D+2, 'throwing': 4*D+1}),
    physique=Physique(4*D, {'lifting': 4*D+1, 'stamina': '4D +2'}),
    charisma=Charisma(2*D, {'bluff': 3*D}),
    intellect=Intellect(2*D, {'devices': 3*D, 'trading': 4*D}),
    acumen=Acumen(3*D, {'crafting': 3*D+2, 'know -how': 3*D+1, 'streetwise': 4*D}),
    move='8',
    strength_damage=2*D,
    fate_points='0',
    character_points='2',
    body=17,
    disadvantages=[
        Hindrance(R1, '2-meter reduction to running, swimming, and jumping Move'),
        Quirk(R1, 'easily angered by mispronunciation of name')],
    advantages=[
        Contacts(R1, 'people of the village'),
        Size(R1, 'scale value of 3')],
    special_abilities=[
        SkillBonus(R1, '+1 to crafting, devices, and traps totals')],
    equipment='keys to various buildings in the town; fine clothes; staff of authority (damage +1D)'
)
characters = [ 
    cachamwri_cabry_inn_keeper, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

