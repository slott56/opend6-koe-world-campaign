"""
Extract Characters from ``ch_7_goblin_guards.ipynb``.
Created by V2026.6.15.dev3 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



goblin_greater = Creature(
    name="Greater Goblin",
    description="Inhabitants of the realm of mountains and forests",
    agility=Agility(3 * D+2, {'acrobatics': 2, 'dodge': 2, 'fighting': 2, "melee combat": 2, 'stealth': 2}),
    coordination=Coordination(3 * D+2, {"marksmanship": 2, "throwing": 1}),
    physique=Physique(3 * D+2,
                      {'running': 2, 'stamina': 2}),
    intellect=Intellect(3 * D, {"healing": 2, "scholar": 2, "traps": 2}),
    acumen=Acumen(3 * D, {"crafting": 2, "survival": 2}),
    charisma=Charisma(3 * D, {'command': 2, "intimidation": 1*D}),
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
    armor=["bone and hide armor +1D", "buckler +2"],
    weapons=["sword +1D+2"],

)

goblin = Creature(
    name="Goblin",
    description="Inhabitants of the realm of mountains and forests",
    agility=Agility(3 * D, {'acrobatics': 2, 'dodge': 2, 'fighting': 2, "melee combat": 2, 'stealth': 2}),
    coordination=Coordination(3 * D, {"marksmanship": 2, "throwing": 1}),
    physique=Physique(3 * D,
                      {'running': 2, 'stamina': 2}),
    intellect=Intellect(3 * D, {"healing": 2, "scholar": 2, "traps": 2}),
    acumen=Acumen(3 * D, {"crafting": 2, "survival": 2}),
    charisma=Charisma(2 * D),
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
    armor=["bone and hide armor +1D"],
    weapons=["sword +1D"],
)

troll = Creature(
    name='Troll',
    agility=Agility(2*D, {'dodge': 2*D, 'fighting': 2*D, 'melee combat': 2*D}),
    coordination=Coordination(1*D),
    physique=Physique(4*D+2, {'running': 2, 'lifting': 2*D}),
    intellect=Intellect(1*D),
    acumen=Acumen(2*D, {'search': 2, 'tracking': 2}),
    charisma=Charisma(2*D, {'intimidation': 2, 'mettle': 2}),
    move='20',
    # strength_damage='2D+2',
    body=12,
    natural_abilities=[
        NaturalHandWeapon('teeth (damage +1D)'),
        NaturalHandWeapon('claws (damage +1D)'),
        NaturalAbility('large size (scale modifier 2)'),
        NaturalArmor(2, "-2 damage adjustment"),
    ],
    advantages=[
        Equipment(2, "Weapon or survival gear unknown to humans"),
        Hardiness(2, "Really tough"),
        AcceleratedHealing(2, "Heals quickly"),
    ],
    disadvantages=[
        AchillesHeel(4, "Fire does double damage")
    ],
)
characters = [ 
    goblin_greater, goblin, troll, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

