"""
Extract Characters from ``labor``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



crafter = Character(
    name='Crafter',
    agility=Agility(2*D, {'melee combat': 3*D}),
    coordination=Coordination(2*D, {'sleight of hand': 2*D+2}),
    physique=Physique(2*D, {'lifting': 3*D+1}),
    intellect=Intellect(2*D, {}),
    acumen=Acumen(2*D, {'artist': 3*D, 'crafting': 4*D}),
    charisma=Charisma(3*D, {}),
    move='10',
    strength_damage=2*D,
    fate_points='0',
    character_points='2',
    body=11,
    equipment='Crafting tools; simple clothing; knife (damage +2)'
)

master_crafter = Character(
    name='Master Crafter',
    agility=Agility(2*D, {'melee combat': 3*D+1}),
    coordination=Coordination(2*D, {'sleight of hand': 3*D+1}),
    physique=Physique(2*D, {'lifting': 3*D+1}),
    intellect=Intellect(2*D, {'scholar specific craft': 5*D, 'trading': 4*D}),
    acumen=Acumen(2*D, {'artist': 4*D, 'crafting': 5*D+2}),
    charisma=Charisma(3*D, {'command': 3*D+2}),
    move='10',
    strength_damage=2*D,
    fate_points='0',
    character_points='3',
    body=11,
    equipment='exceptional crafting tools (+1D to relevant crafting rolls); work-stained clothing; knife (damage +2)'
)

unskilled_laborer = Character(
    name='Unskilled Laborer',
    agility=Agility(2*D, {'fighting': 3*D, 'melee combat': 3*D}),
    coordination=Coordination(2*D, {}),
    physique=Physique(3*D, {'lifting': '3D + 2'}),
    intellect=Intellect(2*D, {}),
    acumen=Acumen(2*D, {'crafting': 2*D+2, 'streetwise': '3D +2'}),
    charisma=Charisma(2*D, {}),
    move='10',
    strength_damage=1*D,
    fate_points='0',
    character_points='1',
    body=14,
    equipment='appropriate tools (such as shovel, pick, or rake); simple clothing; knife (damage +2)'
)

merchant = Character(
    name='Merchant',
    agility=Agility(2*D+1, {'dodge': 2*D+2, 'fighting': 2*D+2, 'melee combat': 2*D+2}),
    coordination=Coordination(2*D, {'sleight of hand': 2*D+1}),
    physique=Physique(2*D, {}),
    intellect=Intellect(3*D+1, {'cultures': 4*D, 'navigation': 4*D, 'reading/writing': 4*D, 'scholar': 3*D+2, 'speaking': 4*D, 'trading': 5*D+2}),
    acumen=Acumen(3*D, {'gambling': 4*D, 'search': 3*D, 'streetwise': 4*D}),
    charisma=Charisma(3*D+2, {'animal handling': 4*D, 'bluff': 4*D, 'charm': 4*D, 'mettle': 4*D}),
    move='10',
    strength_damage=1*D,
    fate_points='0',
    character_points='3',
    body=11,
    equipment='staff (damage +1D+2); fine garments with a heavy brocade vest (Armor Value +1); small bag of coins and jewels'
)

guard = Character(
    name='Guard',
    agility=Agility(2*D+2, {'dodge': 3*D, 'fighting': 3*D, 'melee combat': 3*D+2, 'riding': '3D + 2'}),
    coordination=Coordination(2*D, {}),
    physique=Physique(3*D, {'running': 3*D+1}),
    intellect=Intellect(2*D, {}),
    acumen=Acumen(2*D, {'search': 3*D+2, 'survival': '3D +1'}),
    charisma=Charisma(3*D, {'mettle': '2D +2'}),
    move='10',
    strength_damage=2*D,
    fate_points='0',
    character_points='2',
    body=14,
    equipment='short sword (damage +1D+2); knife (damage +1D); padded leather armor (Armor Value +1D), with helmet'
)

cleric = Character(
    name='Cleric',
    agility=Agility(2*D+1, {'dodge': 2*D+2, 'fighting': 2*D+2, 'riding': 2*D+2}),
    coordination=Coordination(2*D, {}),
    physique=Physique(2*D, {}),
    intellect=Intellect(3*D+2, {'cultures': 3*D+2, 'healing': 3*D+2, 'reading/writing': 3*D+2, 'scholar': 3*D+2, 'speaking': 5*D}),
    acumen=Acumen(3*D, {'artist': 3*D+1, 'investigation': 3*D+1, 'search': 3*D+1, 'streetwise': 3*D+1}),
    charisma=Charisma(3*D, {'charm': 3*D+2, 'command': 4*D, 'mettle': 3*D, 'persuasion': 4*D}),
    extranormal=Miracles(2*D, {'divination': 2*D+2, 'favor': 2*D+1, 'strife': 2*D+2}),
    move='10',
    strength_damage='1D',
    fate_points='0',
    character_points='3',
    body=11,
    equipment='staff (damage +1D+2); fine garments with a heavy brocade vest (Armor Value +1); leather bag filled with a handful of small gold and silver coins and small jewels'
)

characters = [
    crafter, master_crafter, unskilled_laborer, merchant, guard, cleric, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

