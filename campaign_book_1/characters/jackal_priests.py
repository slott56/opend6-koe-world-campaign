"""
Extract Characters from ``jackal_priests.ipynb``.
Created by V2026.5.7.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



priest = Character(
    name='Devoted Xorn Priests',
    physique=Physique(3*D+2),
    agility=Agility(4*D, {'fighting': 1*D, 'melee combat': 2}),
    coordination=Coordination(4*D),
    intellect=Intellect(3*D+2),
    acumen=Acumen(3*D+2),
    charisma=Charisma(3*D+2, {'intimidation': 3*D+1}),
    body=22,
    move=10.0,
    special_abilities=[
        NaturalHandWeapon(2, "Martial arts skills: 1D+2 bare-hand attack"),
        NaturalArmor(2, "Martial Block"),
    ],
    disadvantages=[
        Devotion(1, "Great Priest Xorn"),
        Employed(2, "Following Xorn"),
    ]
)

novice = Character(
    name='Devoted Xorn Novices',
    physique=Physique(3*D, {'stamina': 1*D}),
    agility=Agility(3*D, {'fighting': 1*D}),
    coordination=Coordination(3*D),
    intellect=Intellect(3*D),
    acumen=Acumen(3*D),
    charisma=Charisma(3*D),
    body=22,
    move=10.0,
    special_abilities=[
        NaturalHandWeapon(1, "Martial arts skills: 1D bare-hand attack"),
        NaturalArmor(1, "Martial Block"),
    ],
    disadvantages=[
        Devotion(1, "Great Priest Xorn"),
        Employed(2, "Following Xorn"),
    ]
)

pilgrim = Character(
    name='Temple of the Jackal Pilgrims',
    physique=Physique(2*D+2),
    agility=Agility(2*D+2, {'fighting': 0*D+2}),
    coordination=Coordination(2*D+2),
    intellect=Intellect(2*D+2),
    acumen=Acumen(2*D+2),
    charisma=Charisma(2*D+2, {'intimidation': 1*D}),
    body=22,
    move=10.0,
)
characters = [ 
    priest, novice, pilgrim, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

