"""
Extract Characters from ``creatures.ipynb``.
Created by V2025.6.27.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-format player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



æsir = Character(
    name="Æs",
    description="Tall and pretty, these beings have powerful magic skills and often have wonderful equipment.",
    acumen=Acumen(4*D),
    charisma=Charisma(4*D, {"charm": 2*D, "intimidation": 3*D, "mettle": 3*D}),
    intellect=Intellect(4*D, {"speaking": 2*D}),
    agility=Agility(4*D, {"combat": 2*D, "fighting": 2*D, "melee combat": 2*D}),
    coordination=Coordination(4*D, {"throwing": 2*D}),
    physique=Physique(4*D, {"lifting": 2*D, "running": 2*D}),
    extranormal=Magic(4*D),
    advantages=[Fame(3, "widely-known and recognized"),],
    special_abilities=[
        Longevity(3, "Lives thousands of years"),
        NaturalArmor(2, "Very tough"),
        NaturalHandWeapon(2, "Throws a powerful punch"),
    ],
    realm="bright towers and cities",
)

djinn = Character(
    name='Djinn',
    description="In human-ish form, they are intimidating. In their column-of-sand form, they're able to travel quickly over the landscape.",
    agility=Agility(4*D, {'acrobatics': 2*D, 'flying': 2*D}),
    coordination=Coordination(4*D, {'sleight of hand': 2*D}),
    physique=Physique(5*D, {'lifting': 3*D+1, 'running': 2*D}),
    intellect=Intellect(4*D, {'devices': 1*D, 'healing': 1*D, 'traps': 1*D}),
    acumen=Acumen(4*D, {'crafting': 1*D, 'design': 1*D, 'hide': 1*D, 'know-how': 1*D}),
    charisma=Charisma(3*D, {'intimidation': 2*D, 'charm': 1*D}),
    extranormal=Magic(5*D),
    move=15,
    disadvantages=[
        Employed(1, "anyone who knows its true name can command it completely"),
        AchillesHeel(2, "talkative, can be charmed into revealing their name")
    ],
    special_abilities=[
        AttackResistance(1, "+1D to damage resistance total against weapons not blessed or enchanted"),
        Longevity(3, "Lives thousands of years"),
        Transmutation(1, "Becomes a column of blowing sand; grants 4 ranks of Hypermovement +8m/round"),
        Flight(1, "Flying at speed of 20m/round")
    ],
    realm="bright sand and wind",
)

afrit = Creature(
    name='Afrit',
    description="Unlike the Djinni, the Afriti can pass for human. In their column-of-sand form, they're able to travel quickly over the landscape. Enemies of the Djinni.",
    agility=Agility(4*D, {'acrobatics': 2*D, 'flying': 2*D, 'fighting': 2*D}),
    coordination=Coordination(4*D, {'throwing': 2*D}),
    physique=Physique(4*D, {'lifting': 5*D+2, 'stamina': 2*D}),
    intellect=Intellect(4*D, {'cultures': 1*D, 'speaking': 1*D, 'trading': 1*D}),
    acumen=Acumen(4*D, {'disguise': 1*D, 'gambling': 1*D, 'hide': 1*D, 'tracking': 1*D}),
    charisma=Charisma(3*D, {'intimidation': 2*D, 'charm': 1*D}),
    extranormal=Magic(5*D),
    move=15,
    disadvantages=[
        AchillesHeel(1, "anyone who knows its true name can summon it; whether or not it cooperates is another story"),
        AchillesHeel(2, "talkative, can be charmed into revealing their name"),
        Enemy(2, "hunted by Djinni"),
    ],
    special_abilities=[
        AttackResistance(1, "+1D to damage resistance total against weapons not blessed or enchanted"),
        Longevity(3, "Lives thousands of years"),
        Transmutation(1, "Becomes a column of blowing sand, which grants 2 ranks of Hypermovement +4m/round, and +2D to attack resistance"),
        Flight(1, "Flying at speed of 20m/round")
    ],
    realm="bright sand and wind",
)

air_elemental = Creature(
    name="Air Elemental",
    description="The air element freed from the æther",
    agility=Agility(3 * D, {'contortion': 2 * D, 'flying': 2 * D}),
    coordination=Coordination(1 * D),
    physique=Physique(5 * D,
                      {'running/flying': 2 * D, 'stamina': 2 * D}),
    intellect=Intellect(1 * D),
    acumen=Acumen(1 * D),
    charisma=Charisma(1 * D, {'intimidation': 6 * D}),
    advantages=[
    ],
    disadvantages=[
        AchillesHeel(3, "Vulnerability to earth-based attacks, takes double damage"),
    ],
    special_abilities=[
        ArmorDefeatingAttack(2, "+2D attacking, except for tightly-woven cloth armor"),
        AttackResistance(3, "+3D for non-enchanted weapons"),
        NaturalRangedWeapon(3, "+3D gusts of wind"),
    ],
    natural_abilities=[
        NaturalAbility("Flying from location to location, able to fit through the smallest opening.")
    ],
    realm="bright sand and wind",
)

air_dragon = Creature(
    name="Air Dragon",
    description="A dragon that rarely touches land, and has a bellow that can kill. If forced to land on level ground, it will never fly again."
                "Breeds on sheet cliffs. They can only take off by falling.",
    agility=Agility(3 * D, {'flying': 2 * D}),
    coordination=Coordination(2 * D),
    physique=Physique(5 * D,
                      {'stamina': 3 * D}),
    intellect=Intellect(3 * D, {"navigation": D, "speaking": D}),
    acumen=Acumen(3 * D, {"search": D, "tracking": D}),
    charisma=Charisma(3 * D, {'intimidation': 2 * D}),
    advantages=[
    ],
    disadvantages=[
        AchillesHeel(3, "Can't land: Barely able to waddle on near useless legs, can't take off."),
    ],
    special_abilities=[
        ArmorDefeatingAttack(2, "+2D attacking, except for tightly-woven cloth armor"),
        AttackResistance(3, "+3D for non-enchanted weapons"),
        NaturalRangedWeapon(3, "+3D a bellow so loud, it causes injury"),
    ],
    natural_abilities=[
        NaturalAbility("Flying more-or-less constantly.")
    ],
    realm="bright sand and wind",
)

giant_centipede = Creature(
    name="Giant Centipede",
    description="A 1-2 meter long centipede, with 20 pairs of long legs, a surprisingly tough hide, and a vicious poison in the huge forcipules (pincers) that surround the mouth",
    agility=Agility(2 * D),
    coordination=Coordination(2 * D),
    physique=Physique(5 * D,
                      {'stamina': 3 * D}),
    intellect=Intellect(2 * D),
    acumen=Acumen(3 * D, {"tracking": D}),
    charisma=Charisma(3 * D, {'intimidation': 2 * D}),
    advantages=[
    ],
    disadvantages=[
    ],
    special_abilities=[
        NaturalHandWeapon(3, "Poison in the forcipules (pincers)"),
        NaturalArmor(2, "tough chitonous hide")
    ],
    natural_abilities=[
        InfravisionUltravision(2),
    ],
    realm="bright sand and wind",
)

giant = Creature(
    name='Giant',
    description="These are huge creatures, often weighing over one thousand kg.",
    agility=Agility(3*D, {'fighting': 4*D, 'melee combat': 4*D}),
    coordination=Coordination(1*D, {'throwing': 4*D}),
    physique=Physique(5*D, {'lifting': 6*D, 'running': 6*D+2}),
    intellect=Intellect(3*D, {'navigation': 1*D}),
    acumen=Acumen(1*D, {'tracking': 2*D}),
    charisma=Charisma(1*D, {'intimidation': 6*D}),
    move=10,
    advantages=[Size(3, 'Huge, scale value 8')],
    # disadvantages=[],
    special_abilities=[
        Hypermovement(2, '+4 to Move'),
        IncreasedAttribute(3, 'Physique, +3 to all Physique totals'),
        Fear(2, "+2D to intimidation and +2D to combat defense"),
    ],
    equipment='Large club (damage +2D); armor (defense +2D)',
    realm="dark smoke and ash",
)

troll = Creature(
    name='Troll',
    description="These are large creatures, often weighing several hundred kg. They prefer to hide and tunnel and build traps.",
    agility=Agility(3*D, {'fighting': 2*D, 'melee combat': 2*D}),
    coordination=Coordination(3*D, {'throwing': 1*D}),
    physique=Physique(4*D, {'lifting': 4*D, 'stamina': 1*D}),
    intellect=Intellect(3*D, {'healing': 1*D, 'traps': 3*D}),
    acumen=Acumen(2*D, {'hide': 2*D, 'know-how': 2*D}),
    charisma=Charisma(1*D, {'intimidation': 6*D}),
    move=10,
    advantages=[Size(1, 'Large, scale value 3')],
    disadvantages=[AchillesHeel(3, "Vulnerability to Fire: does double damage"),],
    special_abilities=[
        AcceleratedHealing(3, "+3D to Physique for natural healing"),
        AttackResistance(2, "+1D for extranormal, and non-enchanted weapons"),
    ],
    equipment='Often armed with war hammer (+1D+2), bone and hide armor (+1D), small shield (+2D)',
    realm="dark smoke and ash",
)

ogre = Creature(
    name="Ogre",
    description="These are large creatures. They are clever and magic use, but terrified of water.",
    agility=Agility(3*D, {'fighting': 2*D, 'melee combat': 2*D}),
    coordination=Coordination(3*D, {'throwing': 1*D}),
    physique=Physique(2*D, {'lifting': 2*D, 'stamina': 2*D}),
    intellect=Intellect(3*D, {'healing': 1*D, 'scholar': 3*D}),
    acumen=Acumen(3*D, {'disguise': 2*D, 'know-how': 2*D}),
    charisma=Charisma(1*D, {'intimidation': 6*D}),
    extranormal=Magic(3*D, {'apportation': 2*D}),
    advantages=[Size(1, 'Large, scale value 3')],
    disadvantages=[AchillesHeel(3, "Vulnerability to Water, takes +1D damage from a bucket-full"),],
    special_abilities=[
        AttackResistance(2, "+1D for extranormal, and non-enchanted weapons"),
    ],
    realm="dark smoke and ash",
)

giant_spider = Creature(
    name="Giant Spider",
    description="A spider with a 1-2 meter long body and 2-3 meter legs, a surprisingly tough hide, and a vicious poison in the fangs inside the mouth",
    agility=Agility(3 * D),
    coordination=Coordination(3 * D),
    physique=Physique(2 * D,
                      {'stamina': 3 * D}),
    intellect=Intellect(2 * D),
    acumen=Acumen(3 * D, {"tracking": D}),
    charisma=Charisma(3 * D, {'intimidation': 2 * D}),
    advantages=[
    ],
    disadvantages=[
    ],
    special_abilities=[
        NaturalHandWeapon(3, "Poison in the mouth fangs"),
        NaturalArmor(2, "tough chitonous hide")
    ],
    natural_abilities=[
        InfravisionUltravision(2),
    ],
    realm="dark smoke and ash",
)

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

fire_elemental = Creature(
    name="Fire Elemental",
    description="The fire element freed from the æther",
    agility=Agility(3 * D, {'contortion': 2 * D, 'jumping': 2 * D}),
    coordination=Coordination(1 * D),
    physique=Physique(5 * D,
                      {'running': 2 * D, 'stamina': 2 * D}),
    intellect=Intellect(1 * D),
    acumen=Acumen(1 * D),
    charisma=Charisma(1 * D, {'intimidation': 6 * D}),
    advantages=[
        Contacts(1, "Can find (and free) fire elements"),
    ],
    disadvantages=[
        AchillesHeel(3, "Vulnerability to Water, takes double damage"),
    ],
    special_abilities=[
        ArmorDefeatingAttack(2, "+2D attacking, except for cloth armor soaking wet"),
        AttackResistance(3, "+3D for non-enchanted weapons"),
        NaturalRangedWeapon(3, "+3D Balls of fire"),
    ],
    natural_abilities=[
        NaturalAbility("Leaping from location to location, finding and freeing other fire elements.")
    ],
    realm="bright fire",
)

fire_dragon = Creature(
    name="Fire Dragon",
    description="A dragon that breathes fire, violently opposed to acid dragons. Lives near volcanoes, nests in caldera.",
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
        AchillesHeel(3, "Vulnerability to water and acid, takes double damage"),
    ],
    special_abilities=[
        ArmorDefeatingAttack(2, "+2D attacking, except for cloth armor soaking wet"),
        AttackResistance(3, "+3D for non-enchanted weapons"),
        NaturalRangedWeapon(3, "+3D for a plume of fire"),
    ],
    natural_abilities=[
        NaturalAbility("Flight")
    ],
    realm="bright fire",
)

elf = Creature(
    name="Elf, Gnome, Goblin, Kobold",
    description="Inhabitants of the realm of mountains and forests",
    agility=Agility(3 * D, {'acrobatics': 2, 'dodge': 2, 'fighting': 2, "melee combat": 2, 'stealth': 2}),
    coordination=Coordination(3 * D, {"marksmanship": 2, "throwing": 1}),
    physique=Physique(3 * D,
                      {'running': 2, 'stamina': 2}),
    intellect=Intellect(3 * D, {"healing": 2, "scholar": 2, "traps": 2}),
    acumen=Acumen(3 * D, {"crafting": 2, "survival": 2}),
    charisma=Charisma(3 * D, {'command': 1, "intimidation": 2}),
    extranormal=Magic(3*D),
    disadvantages=[
        CulturalUnfamiliarity(2, "Lost in human company"),
    ],
    advantages=[
        Equipment(2, "Weapon or survival gear unknown to humans"),
    ],
    special_abilities=[
        CombatSense(2, "Surprise reduced by 4"),
    ],
    realm="Ælvish, mountains and forests",
)

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

metal_man = Creature(
    name="Metal Man",
    description="Inhabitants of the unknown realm",
    agility=Agility(2 * D, {'fighting': 2, "melee combat": 2}),
    coordination=Coordination(2 * D),
    physique=Physique(4 * D,
                      {'lifting': 2*D, 'stamina': 2*D}),
    intellect=Intellect(2 * D),
    acumen=Acumen(2 * D),
    charisma=Charisma(1 * D, {"intimidation": 2*D}),
    disadvantages=[
        CulturalUnfamiliarity(2, "Lost in human company"),
        AchillesHeel(3, "Vulnerability to water and acid, takes double damage"),
    ],
    advantages=[
        Equipment(2, "Weapon or survival gear unknown to humans"),
    ],
    special_abilities=[
    ],
    realm="unknown realm",
)
characters = [ 
    æsir, djinn, afrit, air_elemental, air_dragon, giant_centipede, giant, troll, ogre, giant_spider, lizard_man, water_elemental, acid_dragon, poisonous_watersnake, fire_elemental, fire_dragon, elf, dwarf, earth_elemental, earth_dragon, metal_man, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

