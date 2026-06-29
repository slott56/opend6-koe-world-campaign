"""
Extract Characters from ``shadohowl``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



shadohowl = Character(
    name='Shadohowl',
    agility=Agility(3*D, {'acrobatics': 7*D, 'dodge': 7*D+1, 'fighting': 9*D+1, 'melee combat': 8*D+1, 'stealth': 8*D}),
    coordination=Coordination(3*D+1, {'lockpicking': 4*D, 'marksmanship': 3*D+2, 'sleight of hand': 3*D+2, 'throwing': 4*D+1}),
    physique=Physique(2*D+2, {'lifting': 7*D, 'running': 4*D+2, 'stamina': 4*D}),
    intellect=Intellect(3*D, {'cultures': 4*D, 'speaking': 4*D+1}),
    acumen=Acumen(3*D, {'artist origami': 5*D, 'disguise': 5*D+2, 'hide': 3*D+1, 'tracking': 4*D}),
    charisma=Charisma(3*D, {'intimidation': 5*D+1, 'mettle': 4*D}),
    strength_damage='+6',
    move='10',
    fate_points='1',
    character_points='4',
    body=28,
    disadvantages=[
        Debt(R2, 'to dark master(s)'),
        Infamy(R2, 'cruel and fearsome opponent'),
        Devotion(R1, 'to causing pain and injury'),
        Quirk(R1, 'provokable to blind rage')],
    advantages=[
        Fame(R3, 'dangerous and highly skilled opponent'),
        Size(R1, 'scale value 3')],
    special_abilities=[
        AcceleratedHealing(R1, '+1D to natural healing rate'),
        Ambidextrous(R1, '+1 to select skill totals when using two hands'),
        CombatSense(R1, 'combat modifier from surprise is at -2'),
        IncreasedAttribute(R6, '+6 to each related total'),
        NaturalArmor(R1, '+1D to damage resistance totals')]
)
characters = [ 
    shadohowl, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

