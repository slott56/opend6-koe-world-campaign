"""
Extract Characters from ``variana``.
Created by V2026.3.10.dev1 opend6-tools, ``character_rewrite notebook`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *

R10 = 10
R14 = 14

variana_dragon = Character(
    name='Variana, Dragon',
    agility=Agility(2*D+2, {'acrobatics': 7*D, 'dodge': 7*D+1, 'fighting': 10*D, 'flying': 9*D+2}),
    coordination=Coordination(2*D, {'marksmanship fiery breath': '10D'}),
    physique=Physique(2*D, {'lifting': 5*D, 'running': 6*D, 'stamina': 5*D}),
    intellect=Intellect(3*D+1, {'cultures': 7*D, 'healing': 4*D+2, 'obscure cures': 5*D, 'navigation': 6*D, 'reading/writing': 6*D, 'scholar arcane lore': 10*D, 'speaking': 6*D+2, 'trading': 6*D}),
    acumen=Acumen(2*D+1, {'disguise': 5*D, 'investigation': 6*D, 'search': 6*D, 'streetwise': 3*D, 'survival': 4*D+2, 'tracking': 6*D}),
    charisma=Charisma(3*D+1, {'bluff': 6*D, 'charm': 5*D+2, 'command': 6*D, 'intimidation': 7*D, 'mettle': 6*D+1, 'persuasion': 5*D}),
    extranormal=Magic(2*D+1, {'alteration': 3*D+1, 'conjuration shapeshifting spells': 6*D+2, 'divination': 3*D+2}),
    strength_damage='+14',
    move='10',
    fate_points='3',
    character_points='20',
    body=26,
    disadvantages=[
        AchillesHeel(R3, 'Home Attunement : can only heal damage by resting within her cave , without the aid of medicine or magic'),
        Infamy(R3),
        Quirk(R3, 'mercurial'),
        Quirk(R3, 'territorial'),
        Quirk(R2, 'vain')],
    special_abilities=[
        Flight(R4, 'flying move 8D'),
        IncreasedAttribute(R10, '+10 to related totals'),
        IncreasedAttribute(R14, '+14 to related totals'),
        Longevity(R1),
        LuckGreat(R3, "with Restricted (R3), to Dragon's own cave"),
        NaturalArmor(R3, '+3D to damage resistance totals'),
        NaturalHandWeapon(R3, '+3D damage'),
        NaturalHandWeapon(R3, '+3D damage'),
        NaturalRangedWeapon(R2, 'damage 6D, range 10 / 20 / 40, with Ability Loss (R1), may only fire once every other round'),
        InfravisionUltravision(R6, '+12 to sight-based totals in darkness')],
    advantages=[
        Size(R4, 'scale value 12'),
        Wealth(R3)]
)
characters = [ 
    variana_dragon, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

