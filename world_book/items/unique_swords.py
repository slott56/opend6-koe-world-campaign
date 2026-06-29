"""
Extract Characters from ``unique_swords.ipynb``.
Created by V2025.6.27.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-format player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



justice = Sword(
    name='Sword of Justice',
    description="A well-made sword with runes of Strength and a ruby; the sword has the divination power to reveal the recent actions of a person, allowing the wielder to chose a just path forward.",

    intellect=Intellect(2*D, {"communication": 3*D}),
    physique=Physique(2*D, {"lifting": 2*D}),
    charisma=Charisma(2*D),
    acumen=Acumen(0*D),
    agility=Agility(0*D),
    coordination=Coordination(0*D),
    extranormal=Magic(4*D, {'divination': 2*D}),
    body=1*D,
    strength_damage=2*D,
    disadvantages=[
        Hindrance(R3, "A sword; immobile without a wielder"),
    ],
    natural_abilities=[
        NaturalHandWeapon(2*D+2, "damage"),
    ],
    special_abilities=[
        SkillBonus(R3, "Divination of actions of up to 2 weeks in the past for one target. Must be touching."),
        SpecialAbility(R3, "Psionic communication of divination to wielder."),
    ]
)

fire = Sword(
    name='Fire Sword',
    description="An oddly-shaped sword with runes of Fire and rings of iron woven into the hilt; part of the damage effect includes burns, it also protects the wielder from fire.",

    intellect=Intellect(2*D),
    physique=Physique(2*D, {"lifting": 1*D}),
    charisma=Charisma(2*D),
    acumen=Acumen(0*D),
    agility=Agility(0*D),
    coordination=Coordination(0*D),
    extranormal=Magic(4*D, {'conjuration': 3*D}),
    body=1*D,
    strength_damage=2*D,
    disadvantages=[
        Hindrance(R3, "A sword; immobile without a wielder"),
    ],
    natural_abilities=[
        NaturalHandWeapon(2*D+2, "damage"),
        NaturalHandWeapon(5*D, "damage from burns after a successful hit"),
    ],
    special_abilities=[
        Intangibility(R3, "+3D protection wielder from fire"),
    ]
)

survivor = Sword(
    name='Sword of Survival',
    description="A poorly-made old sword with the rune of Plenty inscribed prominently on the blade, it can help the wielder through afflicting an opponents with a sudden burst of bad luck",

    intellect=Intellect(2*D, {"speaking": 3*D, "traps": 1*D}),
    physique=Physique(1*D, {"lifting": 2*D}),
    charisma=Charisma(1*D),
    acumen=Acumen(0*D),
    agility=Agility(2*D),
    coordination=Coordination(0*D),
    extranormal=Magic(3*D, {'transformation': 3*D}),
    body=1*D,
    disadvantages=[
        Hindrance(R3, "A sword; immobile without a wielder"),
        Quirk(R2, "Taunts enemies"),
    ],
    natural_abilities=[
        NaturalHandWeapon(2*D+2, "damage"),
    ],
    special_abilities=[
        SpecialAbility(R5, "Pushes bad luck onto opponent with a hit that does damage; the opponent's next actions gets +15 and +10 difficulties."),
    ]
)

sealing = Sword(
    name='Sword of Escape',
    description="A short sword with a hammer molded into the hilt; this can try open a closed door and close an open door. It's also an awkward hammer.",

    intellect=Intellect(1*D, {"speaking": 2*D, "traps": 2*D}),
    physique=Physique(2*D, {"lifting": 3*D}),
    charisma=Charisma(3*D),
    acumen=Acumen(0*D),
    agility=Agility(0*D),
    coordination=Coordination(0*D),
    extranormal=Magic(2*D, {'transformation': 2*D}),
    body=1*D,
    disadvantages=[
        Hindrance(R3, "A sword; immobile without a wielder"),
    ],
    natural_abilities=[
        NaturalHandWeapon(2*D, "damage"),
    ],
    special_abilities=[
        SpecialAbility(R3, "Warp a wooden door to wedge it closed"),
        SpecialAbility(R3, "Warp a wooden door to smash it open"),
    ]
)

stalker = Sword(
    name="Stalker's Sword",
    description="A short, hefty hunting sword with a rider's spur welded onto the end of the pommel; this is awkward as a weapon, but it will help the wielder's healing skills, and can also help the wielder avoid injury by dodging and running away.",

    intellect=Intellect(2*D, {"healing": 3*D}),
    physique=Physique(2*D, {"lifting": 2*D}),
    charisma=Charisma(2*D),
    acumen=Acumen(2*D, {"survival": 2*D}),
    agility=Agility(0*D),
    coordination=Coordination(0*D),
    extranormal=Magic(2*D, {'transformation': 1*D, "divination": 1*D}),
    body=1*D,
    disadvantages=[
        Hindrance(R3, "A sword; immobile without a wielder"),
    ],
    natural_abilities=[
        NaturalHandWeapon(2*D+2, "damage"),
    ],
)

champions = Sword(
    name="Champion's Blade",
    description="A beautifully made, expensive-looking sword, with the rune of flame and a jade figure worked around into the pommel nut, this sword is cruel and will injure the wielder if it's used in combat and successfully hits someone.",

    intellect=Intellect(2*D, {"speaking": 1*D}),
    physique=Physique(2*D),
    charisma=Charisma(3*D, {"persuasion": 3*D}),
    acumen=Acumen(0*D),
    agility=Agility(0*D),
    coordination=Coordination(0*D),
    extranormal=Magic(2*D, {'transformation': 2*D}),
    body=1*D,
    disadvantages=[
        Hindrance(R3, "A sword; immobile without a wielder"),
        BadLuck(R3, "Something always seems to go wrong"),
    ],
    natural_abilities=[
        NaturalHandWeapon(2*D+2, "damage"),
    ],
    special_abilities=[
        NaturalMagick(R3, "Bolt of energy, stun only, to wielder only")
    ]
)
swords = [ 
    justice, fire, survivor, sealing, stalker, champions, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(swords)
    app()

