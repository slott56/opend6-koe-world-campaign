"""
Generic Animals from Fantasy Rules
Used to populate *OpenD6 Fantasy* "Adventure Tips" chapter
"""
import sys
from opend6_tools.character import *

bird_of_prey = Creature(
    name='Bird of Prey (Falcon, Hawk )',
    agility=Agility(4*D, {'fighting': 5*D, 'flying': 5*D}),
    coordination=Coordination(1*D),
    physique=Physique(2*D),
    intellect=Intellect(1*D),
    acumen=Acumen(2*D, {'search': 3*D, 'tracking': 3*D}),
    charisma=Charisma(2*D, {'mettle': 3*D}),
    move='32 fly/15 glide',
    # strength_damage='1D',
    body=7,
    natural_abilities=[
        NaturalAbility('wings allow the bird to fly or glide for several hundred miles or as long as there are thermals to keep them aloft'),
        NaturalAbility('beak (damage +2)'),
        NaturalAbility('talons (damage +1D)'),
        NaturalAbility('small size (scale modifier 9)'),
    ]
)

cat_domestic = Creature(
    name='Cat, Domestic',
    agility=Agility(3*D, {'fighting': 4*D, 'climbing': 4*D, 'dodge': 4*D, 'jumping': 4*D, 'stealth': 4*D}),
    coordination=Coordination(1*D),
    physique=Physique(1*D, {'running': 3*D}),
    intellect=Intellect(1*D),
    acumen=Acumen(2*D, {'search': 3*D, 'tracking': 3*D}),
    charisma=Charisma(2*D, {'mettle': 3*D}),
    move='20',
    # strength_damage='1D',
    body=8,
    natural_abilities=[
        NaturalAbility('claws (damage +2)'),
        NaturalAbility('teeth (damage +2)'),
        NaturalAbility('small size (scale modifier 6)'),
    ],
)

cat_large = Creature(
    name='Cat, Large (Lion, Puma , Tiger)',
    agility=Agility(4*D, {'climbing': 5*D, 'dodge': 5*D, 'fighting': 5*D, 'jumping': 5*D, 'stealth': 5*D}),
    coordination=Coordination(2*D),
    physique=Physique(4*D, {'running': 5*D}),
    intellect=Intellect(1*D),
    acumen=Acumen(2*D, {'search': 3*D, 'tracking': 3*D}),
    charisma=Charisma(2*D, {'intimidation': 5*D, 'mettle': 4*D}),
    move='30',
    body=24,
    # strength_damage='20',
    natural_abilities=[
        NaturalAbility('thick fur (armor value +2)'),
        NaturalAbility('claws (damage +1D)'),
        NaturalAbility('teeth (damage +1D)'),
    ],
    note="Large cats can leap up to 10 meters horizontally or two meters vertically."
)

cobra = Creature(
    name='Cobra',
    agility=Agility(4*D, {'fighting': 5*D, 'stealth': 5*D}),
    coordination=Coordination(2*D, {'marksmanship:spitting': 4*D}),
    physique=Physique(1*D),
    intellect=Intellect(1*D),
    acumen=Acumen(2*D, {'search': 3*D, 'tracking': 3*D}),
    charisma=Charisma(2*D, {'intimidation': 4*D, 'mettle': 4*D}),
    body=5,
    move='15',
    # strength_damage='1D',
    natural_abilities=[
        NaturalAbility('fangs (damage +1D)'),
        NaturalAbility('venom injected when fighting success beats difficulty by 5 or more)'),
        NaturalAbility('venom spitting (with a called shot to the eyes or mouth, the cobra spits venom into this area)'),
        NaturalAbility('venom (causes 5 points of damage or 1 Wound level every 10 minutes until victim dies or is treated; Very Difficult stamina roll to resist)'),
        NaturalAbility('small size (scale modifier 9)'),
    ],
)

dog_domestic = Creature(
    name='Dog, Domestic',
    agility=Agility(3*D, {'dodge': 4*D, 'fighting': 4*D}),
    coordination=Coordination(1*D),
    physique=Physique(3*D, {'running': 4*D}),
    intellect=Intellect(1*D),
    acumen=Acumen(2*D, {'search': 3*D, 'tracking': 4*D}),
    charisma=Charisma(2*D, {'intimidation': 3*D, 'mettle': 2*D+1}),
    move='2S',
    # strength_damage='2D',
    body=9,
    natural_abilities=[
        NaturalAbility('teeth (damage +1D)'),
        NaturalAbility('small size (scale modifier 5)'),
    ],
)

dog_guard = Creature(
    name='Dog, Guard',
    agility=Agility(3*D, {'dodge': 6*D, 'fighting': 5*D}),
    coordination=Coordination(1*D),
    physique=Physique(4*D, {'running': 4*D+1}),
    intellect=Intellect(1*D),
    acumen=Acumen(2*D, {'search': 3*D, 'tracking': 4*D}),
    charisma=Charisma(2*D, {'intimidation': 5*D, 'mettle': 4*D}),
    move='25',
    # strength_damage='2D',
    body=12,
    natural_abilities=[
        NaturalAbility('teeth (damage +1D)'),
        NaturalAbility('small size (scale modifier 4)'),
    ],
)

horse = Creature(
    name='Horse',
    agility=Agility(3*D, {'fighting': 4*D, 'jumping': 4*D}),
    coordination=Coordination(1*D),
    physique=Physique(4*D, {'running': 5*D}),
    intellect=Intellect(1*D),
    acumen=Acumen(3*D),
    charisma=Charisma(2*D, {'intimidation': 3*D, 'mettle': 3*D}),
    move='25',
    # strength_damage='2D',
    body=15,
    natural_abilities=[
        NaturalAbility('hoof (damage +2)'),
        NaturalAbility('teeth (damage +2)'),
        NaturalAbility('large size (scale modifier 3)'),
    ],
    note='Horses can attack the same target twice in one round with their hooves (two front or two back) at no penalty, or they can bite once',
)

rats = Creature(
    name='Rats',
    agility=Agility(3*D, {'acrobatics': 3*D+1, 'climbing': 3*D+2, 'dodge': 3*D+1, 'fighting': 3*D+2, 'jumping': 4*D}),
    physique=Physique(1*D, {'running': 3*D, 'swimming': 1*D+2}),
    intellect=Intellect(1*D),
    acumen=Acumen(2*D, {'hide: self only': 4*D, 'search': 3*D}),
    charisma=Charisma(1*D, {'willpower': 2*D}),
    move='3',
    # strength_damage='1D',
    body=6,
    natural_abilities=[
        NaturalAbility('teeth (Strength Damage only)'),
        NaturalAbility('swarm attack (roll a single fighting total for entire group of rats, adding +5 to the total for every 10 creatures involved; if using the optional damage bonus, add the bonus for this roll to the Strength Damage of a single rat)'),
        NaturalAbility('small size (scale modifier 9 for single rat)'),
    ]
)

all_characters = {
    'Bird-of-Prey': bird_of_prey,
    'Cat, Domestic': cat_domestic,
    'Cat, Large': cat_large,
    'Cobra': cobra,
    'Dog, Domestic': dog_domestic,
    'Dog, Guard': dog_guard,
    'Horse': horse,
    'Rats': rats,
}

if __name__ == "__main__":
    app = build_app(all_characters)
    app()

__test__ = {
    "pass": ">>> pass\n"
}
