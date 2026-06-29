"""
Extract Characters from ``creatures.ipynb realm bright sand and wind characters``.
Created by V2026.5.7.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



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
characters = [ 
    djinn, afrit, air_elemental, air_dragon, giant_centipede, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

