"""
Extract Characters from ``creatures.ipynb realm Ælvish, caves and earth characters``.
Created by V2026.5.7.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



dwarf = Creature(
    name="Dwarf",
    description="Inhabitants of the realm of caves and earth",
    agility=Agility(3 * D, {'fighting': 2, "melee combat": 2, 'stealth': 2}),
    coordination=Coordination(3 * D, {"sleight of hand": 1}),
    physique=Physique(3 * D,
                      {'lifting': 2, 'stamina': 1*D}),
    intellect=Intellect(3 * D, {"trading": 2, "scholar": 2, "traps": 2}),
    acumen=Acumen(3 * D, {"crafting": 2, "hide": 2}),
    charisma=Charisma(3 * D, {'charm': 1, "intimidation": 2}),
    extranormal=Magic(3*D),
    disadvantages=[
        CulturalUnfamiliarity(2, "Lost in human company"),
    ],
    advantages=[
        Equipment(2, "Weapon or survival gear unknown to humans"),
        Size(2, "Smaller than humans"),
    ],
    special_abilities=[
        InfravisionUltravision(2, "+4 in dark places"),
    ],
    realm="Ælvish, caves and earth",
)

earth_elemental = Creature(
    name="Earth Elemental",
    description="The earth element freed from the æther",
    agility=Agility(3*D, {'fighting': 2*D, 'melee combat': 2*D}),
    coordination=Coordination(1*D),
    physique=Physique(5*D, {'lifting': 2*D, 'stamina': 2*D, 'swimming': 4*D}),
    intellect=Intellect(1*D),
    acumen=Acumen(1*D),
    charisma=Charisma(1*D, {'intimidation': 6*D}),
    advantages=[],
    disadvantages=[Hindrance(3, "Slow"),],
    special_abilities=[
        ArmorDefeatingAttack(2, "+2D attacking, except for leather armor"),
        AttackResistance(3, "+3D for non-enchanted weapons"),
        NaturalHandWeapon(3, "+3D earth-shaking that knocks opponents down and beats them on the ground."),
    ],
    natural_abilities=[
        NaturalAbility("Transmutes from rock to sand; sand can pass through openings.")
    ],
    realm="Ælvish, caves and earth",
)

earth_dragon = Creature(
    name="Earth Dragon",
    description="A slow-moving dragon that with a hide like stone. They have small wings and are sometimes called Wyvern.",
    agility=Agility(3 * D, {'flying': 2 * D}),
    coordination=Coordination(2 * D),
    physique=Physique(5 * D,
                      {'stamina': 3 * D, 'running/flying': 3*D}),
    intellect=Intellect(3 * D, {"navigation": D, "speaking": D}),
    acumen=Acumen(3 * D, {"search": D, "survival": D}),
    charisma=Charisma(3 * D, {'intimidation': 2 * D}),
    advantages=[
    ],
    disadvantages=[
        AchillesHeel(3, "Vulnerability to air, wind, and loud noises, damage +1D, any intimidation attempt with a loud noise gets +3D"),
    ],
    special_abilities=[
        ArmorDefeatingAttack(2, "+2D attacking, except for heavily padded armor"),
        AttackResistance(3, "+3D for non-enchanted weapons"),
        NaturalHandWeapon(3, "+3D for a rock-like buffet with the tail"),
        NaturalHandWeapon(3, "+1D poisonous bite"),
    ],
    natural_abilities=[
        NaturalAbility("Flight"),
        NaturalAbility("Tunneling")
    ],
    realm="Ælvish, caves and earth",
)
characters = [ 
    dwarf, earth_elemental, earth_dragon, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

