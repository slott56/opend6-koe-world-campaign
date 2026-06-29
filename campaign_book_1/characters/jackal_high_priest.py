"""
Extract Characters from ``jackal_high_priest.ipynb``.
Created by V2026.5.7.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



senior_priest_internal = Character(
    name='Jackal Senior Priest -- Internal',
    other_notes="Quote: 'Cruelty is as Cruelty does, I always say'",
    physique=Physique(4*D),
    agility=Agility(4*D, {'fighting': 1*D+1, 'melee combat': 1*D}),
    coordination=Coordination(4*D),
    intellect=Intellect(3*D+2, {'reading/writing': 1*D,  'speaking': 1*D+1}),
    acumen=Acumen(3*D+2),
    charisma=Charisma(3*D+2, {'intimidation': 4*D+2}),
    body=22,
    move=10,
    special_abilities=[
        NaturalHandWeapon(2, "Martial arts skills: 1D+2 bare-hand attack"),
        NaturalArmor(2, "Martial Block"),
    ],
    disadvantages=[
        Infamy(2, "Known to be cruel"),
        Devotion(1, "Great Priest Xorn"),
        Employed(2, "By Xorn, wherever he is"),
        Quirk(2, "Cruel"),
    ]
)

senior_priest_external = Character(
    name='Jackal Senior Priest -- External',
    other_notes="Quote: 'Be lika a jackal: ruthless and relentless'",
    physique=Physique(3 * D),
    agility=Agility(3 * D, {'fighting': 1 * D , 'melee combat': 1 * D}),
    coordination=Coordination(3 * D),
    intellect=Intellect(3 * D,
                        {'reading/writing': 2 * D, 'speaking': 1 * D}),
    acumen=Acumen(3 * D),
    charisma=Charisma(3 * D, {'intimidation': 3 * D}),
    body=22,
    move=10.0,
    special_abilities=[
        NaturalHandWeapon(2, "Martial arts skills: 1D+2 bare-hand attack"),
        NaturalArmor(2, "Martial Block"),
    ],
    disadvantages=[
        Devotion(1, "Great Priest Xorn"),
        Employed(2, "By Xorn, wherever he is"),
        Quirk(1, "Officious"),
    ]
)
characters = [ 
    senior_priest_internal, senior_priest_external, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

