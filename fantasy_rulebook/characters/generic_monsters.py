"""
Generic Monsters from Fantasy Rules
Used to populate *OpenD6 Fantasy* "Adventure Tips" chapter
"""
import sys
from opend6_tools.character import *

demon_minor_destructive = Creature(
    name='Demon, Minor Destructive',
    agility=Agility(3*D, {'fighting': 4*D, 'stealth': 4*D}),
    coordination=Coordination(2*D, {'throwing': 4*D}),
    physique=Physique(5*D, {'lifting': 5*D+1, 'running': 6*D}),
    intellect=Intellect(2*D),
    acumen=Acumen(2*D),
    charisma=Charisma(2*D, {'intimidation': 6*D, 'mettle': 4*D}),
    move='10',
    strength_damage=2*D,
    body=24,
    disadvantages=[
        Employed(1, 'anyone who knows its true name can command it completely'),
        Devotion(3, 'totally committed to wreaking havoc'),
    ],
    special_abilities=[
        AttackResistance(1, '+1D to damage resistance total against weapons not blessed or enchanted'),
        Immortality(1, 'a holy symbol and proper ritual returns it to its realm'),
    ],
)

dragon_young = Creature(
    name='Dragon, Young',
    agility=Agility(3*D, {'fighting': 4*D, 'flying': 3*D+1}),
    coordination=Coordination(2*D, {'marksmanship': 3*D}),
    physique=Physique(5*D, {'lifting': 5*D+1}),
    intellect=Intellect(3*D),
    acumen=Acumen(2*D),
    charisma=Charisma(3*D, {'intimidation': 6*D, 'mettle': 3*D+2}),
    move='10',
    strength_damage='3D',
    body=32,
    advantages=[Size(4, 'large, scale value 12')],
    disadvantages=[
        AchillesHeel(3, "Metabolic Difference, requires large quantities of fresh meat"),
        Infamy(3, "species feared and hunted because of destructive tendencies"),
        Quirk(3, "easily angered"),
        Quirk(3, "greedy"),
    ],
    special_abilities=[
        NaturalArmor(2, 'Scales, +1D to damage resistance total'),
        NaturalHandWeapon(3, 'Claws, damage +3D'),
        NaturalRangedWeapon(2, 'Fiery Breath, damage 6D')
    ],
)

humanoid_evil = Creature(
    name='Evil Humanoid (Goblin, etc.)',
    agility=Agility(3*D, {'climbing': 3*D+2, 'fighting': 4*D, 'jumping': 3*D+1, 'stealth': 4*D}),
    coordination=Coordination(3*D, {'marksmanship': 4*D, 'throwing': 4*D}),
    physique=Physique(3*D, {'lifting': 3*D+1, 'running': 4*D}),
    intellect=Intellect(1*D),
    acumen=Acumen(2*D, {'hide': 2*D+2, 'survival': 3*D, 'tracking': 3*D}),
    charisma=Charisma(1*D, {'intimidation': 2*D}),
    move='10',
    strength_damage='2D',
    body=12,
    disadvantages=[Devotion(3, 'killing and looting')],
    # special_abilities='None',
)

giant = Creature(
    name='Giant',
    agility=Agility(3*D, {'fighting': 4*D, 'melee combat': 4*D}),
    coordination=Coordination(1*D, {'throwing': 4*D}),
    physique=Physique(5*D, {'lifting': 6*D, 'running': 6*D+2}),
    intellect=Intellect(2*D),
    acumen=Acumen(1*D, {'tracking': 2*D}),
    charisma=Charisma(1*D, {'intimidation': 6*D}),
    move='10',
    strength_damage='3D',
    body=26,
    advantages=[Size(2, 'Large, scale value 6')],
    # disadvantages=[],
    special_abilities=[
        Hypermovement(2, '+4 to Move'),
        IncreasedAttribute(3, 'Physique, +3 to all Physique totals'),
    ],
    equipment='Large club (damage +2D)',
)

walking_dead = Creature(
    name='Walking Dead (Skeleton, etc.)',
    agility=Agility(2*D, {'fighting': 3*D}),
    coordination=Coordination(1*D, {'Physiquev': 2*D, 'vlifting': 3*D}),
    intellect=Intellect(1*D),
    acumen=Acumen(1*D, {'search': 3*D, 'tracking': 3*D}),
    charisma=Charisma(1*D, {'intimidation': 6*D}),
    move='10',
    strength_damage=2*D,
    body=15,
    disadvantages=[
        Employed(3, 'slave to the one who raised them'),
    ],
    special_abilities=[
        Hardiness(2, '+2 to damage resistance totals'),
        Immortality(1, 'cease functioning when smashed to pieces or head is cut off'),
    ]
)

all_characters = {
    'Demon, Minor Destuctive': demon_minor_destructive,
    'Dragon, Young': dragon_young,
    'Humanoid, Evil': humanoid_evil,
    'Giant': giant,
    'Walking Dead': walking_dead,
}

if __name__ == "__main__":
    app = build_app(all_characters)
    app()

__test__ = {
    "pass": ">>> pass\n"
}
