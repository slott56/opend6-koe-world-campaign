"""
Extract Characters from ``creatures.ipynb realm dark cold and mist characters``.
Created by V2026.5.7.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



lizard_man = Creature(
    name="Lizard Man",
    description="Intelligent, bipedal lizard, with bright plumage and surprisingly long fingers (or very short wings). They fight with a wickedly curved beak and massive foot claws.",
    agility=Agility(3*D, {'flying': 1, 'jumping': 1*D, 'fighting': 3*D}),
    coordination=Coordination(3*D),
    physique=Physique(3*D, {'running': 2*D, 'stamina': 2*D, 'swimming': 2}),
    intellect=Intellect(3*D, {'cultures': 1*D, 'navigation': 2*D, 'scholar': 1*D}),
    acumen=Acumen(3*D, {'investigation': 2*D, 'crafting': 1*D}),
    charisma=Charisma(3*D, {'persusion': 1*D}),
    advantages=[],
    disadvantages=[AchillesHeel(3, "Vulnerability to Fire, takes double damage"),],
    special_abilities=[
        NaturalHandWeapon(3, "+2D beak"),
        NaturalHandWeapon(3, "+1D+2 claws on feet"),
    ],
    natural_abilities=[],
    realm="dark cold and mist",
)

water_elemental = Creature(
    name="Water Elemental",
    description="The water element freed from the æther",
    agility=Agility(3*D, {'contortion': 2*D, 'stealth': 2*D}),
    coordination=Coordination(1*D),
    physique=Physique(5*D, {'lifting': 2*D, 'stamina': 2*D, 'swimming': 4*D}),
    intellect=Intellect(1*D),
    acumen=Acumen(1*D),
    charisma=Charisma(1*D, {'intimidation': 6*D}),
    advantages=[],
    disadvantages=[AchillesHeel(3, "Vulnerability to Fire, takes double damage"),],
    special_abilities=[
        ArmorDefeatingAttack(2, "+2D attacking, except for rain gear"),
        AttackResistance(3, "+3D for non-enchanted weapons"),
        NaturalHandWeapon(3, "+3D waves that hit hard"),
    ],
    natural_abilities=[
        NaturalAbility("Flowing, filling a space of any shape, fitting through small openings.")
    ],
    realm="dark cold and mist",
)

acid_dragon = Creature(
    name="Acid Dragon",
    description="A dragon that swims and spits acid as well as flies. Violently opposed to fire dragons. Breeds on small islands in the sea somewhere.",
    agility=Agility(3 * D, {'flying': 2 * D}),
    coordination=Coordination(2 * D),
    physique=Physique(5 * D,
                      {'stamina': 3 * D, 'swimming': 3*D}),
    intellect=Intellect(3 * D, {"navigation": D, "speaking": D}),
    acumen=Acumen(3 * D, {"search": D, "survival": D}),
    charisma=Charisma(3 * D, {'intimidation': 2 * D}),
    advantages=[
    ],
    disadvantages=[
        AchillesHeel(3, "Vulnerability to Fire, takes double damage"),
    ],
    special_abilities=[
        ArmorDefeatingAttack(2, "+2D attacking, except for tightly-woven, water-proof rain gear"),
        AttackResistance(3, "+3D for non-enchanted weapons"),
        NaturalRangedWeapon(3, "+3D for a gout of acid"),
    ],
    natural_abilities=[
        NaturalAbility("Flight"),
        NaturalAbility("Swimming"),
    ],
    realm="dark cold and mist",
)

poisonous_watersnake = Creature(
    name="Watersnake",
    description="A large -- 3-5m long -- snake with a terrifying venom in it's fangs.",
    agility=Agility(3 * D),
    coordination=Coordination(2 * D),
    physique=Physique(2 * D,
                      {'stamina': 3 * D, 'swimming': 3*D}),
    intellect=Intellect(2 * D),
    acumen=Acumen(3 * D, {"search": D, "survival": D}),
    charisma=Charisma(3 * D, {'intimidation': 2 * D}),
    advantages=[
    ],
    disadvantages=[
        AchillesHeel(3, "Vulnerability to Fire, takes double damage"),
    ],
    special_abilities=[
        NaturalHandWeapon(3, "Poison in the mouth fangs"),
    ],
    natural_abilities=[
        NaturalAbility("Swimming"),
    ],
    realm="dark cold and mist",
)
characters = [ 
    lizard_man, water_elemental, acid_dragon, poisonous_watersnake, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

