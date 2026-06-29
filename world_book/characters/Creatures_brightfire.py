"""
Extract Characters from ``creatures.ipynb realm bright fire characters``.
Created by V2026.5.7.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



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
characters = [ 
    fire_elemental, fire_dragon, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

