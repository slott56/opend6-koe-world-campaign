"""
Extract Characters from ``squire_neck.ipynb``.
Created by V2026.5.7.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



squire_neck = Character(
    name='Squire Neck of White Water',
    description='Captain of the Guard in White Water.  Religious and a heavy drinker.  Has two lackeys who follow him everywhere, through whom he gives orders.  Heavy user of spies and assassins, justifiably worried about spies and assassins.',
    other_notes="Quote: 'Who is this person?'",
    physique=Physique(3*D+2),
    agility=Agility(4*D, {'fighting': 1*D, 'riding': 1*D, 'melee combat': 2}),
    coordination=Coordination(4*D, {'lockpicking': 1*D}),
    intellect=Intellect(4*D, {'cultures': 2, 'devices': 0*D, 'healing': 0*D, 'navigation': 0*D, 'reading/writing': 0*D, 'scholar': 0*D, 'speaking': 0*D, 'trading': 0*D, 'traps': 0*D}),
    acumen=Acumen(3*D+2, {'disguise': 2, 'hide': 2, 'investigation': 2, 'streetwise': 2}),
    charisma=Charisma(3*D+2, {'intimidation': 5*D}),
    body=24,
    move=10.0,
    advantages=[
        Patron(R1, "Sir Bond"),
        Authority(R1, "aristocracy"),
        Debt(R1, "wastrel"),
        Contacts(R1, "Spies"),
    ],
    disadvantages=[
        Infamy(R1, "Reputation as cruel"),
        Quirk(R2, "Afraid of assassination"),
        Hindrance(R3, "Alcoholic"),
        Quirk(R2, "Afraid of swords"),
    ],
)
characters = [ 
    squire_neck, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

