"""
Extract Characters from ``temple_clerics``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



typical_fa_ayn_temple_elder = Character(
    name="Typical Fa'ayn temple elder",
    agility=Agility(2*D+1, {}),
    coordination=Coordination(2*D+1, {}),
    physique=Physique(2*D, {'stamina': 2*D+2}),
    intellect=Intellect(4*D, {'healing': 4*D+1, 'reading/writing': 5*D, 'scholar': 5*D}),
    acumen=Acumen(3*D+1, {'artist': 3*D+2, 'crafting': 4*D}),
    charisma=Charisma(4*D, {'charm': 4*D+2, 'command': '4D +2', 'mettle': 4*D+2, 'persuasion': 5*D}),
    strength_damage=1*D,
    move='10',
    fate_points='0',
    character_points='4',
    body=16,
    disadvantages=[
        Devotion(R3, 'to the holy order (including a vow of poverty)'),
        Employed(R3, 'by the holy order')],
    advantages=[
        Authority(R2, "over Fa'ayn followers"),
        Contacts(R2, "within the Fa'ayn order")],
    special_abilities=[
        SkillBonus(R2, '+1 to charm, persuasion, and command totals')]
)

typical_fa_ayn_temple_neonate = Character(
    name="Typical Fa'ayn temple neonate",
    agility=Agility(2*D+1, {'dodge': 3*D+1, 'melee combat': 3*D+1}),
    coordination=Coordination(2*D+2, {}),
    physique=Physique(2*D+1, {'lifting': 3*D, 'stamina': 2*D+2}),
    intellect=Intellect(2*D+2, {'cultures': 3*D, 'healing': 4*D+2, 'reading/writing': 4*D, 'scholar': 4*D, 'trading': 3*D}),
    acumen=Acumen(2*D+1, {'artist': 2*D+2, 'crafting': 3*D}),
    charisma=Charisma(2*D+2, {}),
    strength_damage=1*D,
    move='10',
    fate_points='0',
    character_points='2',
    body=12,
    disadvantages=[
        Devotion(R2, 'to the holy order (including a vow of poverty)'),
        Employed(R2, 'by the holy order')],
    advantages=[
        Contacts(R1, "within the Fa'ayn order")]
)

typical_fa_ayn_traveling_cleric = Character(
    name="Typical Fa'ayn traveling cleric",
    agility=Agility(3*D, {'dodge': 4*D, 'melee combat': 4*D}),
    coordination=Coordination(2*D, {}),
    physique=Physique(2*D, {'stamina': 2*D+1}),
    intellect=Intellect(3*D, {'cultures': 3*D+2, 'healing': 4*D, 'reading/ writing': 3*D+1, 'scholar': 4*D, 'speaking': 3*D+1, 'trading': 3*D+1}),
    acumen=Acumen(3*D, {'crafting': 3*D+1, 'investigation': 3*D+1, 'search': 3*D+1}),
    charisma=Charisma(3*D, {'charm': 3*D+1, 'command': '3D + 1', 'intimidation': 3*D+2, 'mettle': 4*D, 'persuasion': 3*D+1}),
    extranormal=Miracles(2*D, {'favor': 3*D, 'strife': 3*D}),
    strength_damage=1*D,
    move='10',
    fate_points='0',
    character_points='2',
    body=11,
    disadvantages=[
        Devotion(R3, 'to the holy order (including a vow of poverty)'),
        Employed(R2, 'by the holy order')],
    advantages=[
        Contacts(R1, "within the Fa'ayn order")],
    equipment='various seeds; pouch; blanket '
)
characters = [ 
    typical_fa_ayn_temple_elder, typical_fa_ayn_temple_neonate, typical_fa_ayn_traveling_cleric,
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

