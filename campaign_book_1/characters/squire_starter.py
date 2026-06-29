"""
Extract Characters from ``squire_starter.ipynb``.
Created by V2026.5.7.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



squire_starter = Character(
    name='Squire Starter (Son of Sir Warrant)',
    description='Official bride produced no children.  He is actually son of a concubine, and is of mixed heritage.',
    other_notes="""Quote: "I'll get you for that.""""",
    physique=Physique(4*D),
    agility=Agility(4*D, {'fighting': 2, 'riding': 1*D, 'melee combat': 2}),
    coordination=Coordination(4*D, {}),
    intellect=Intellect(3*D+2, {'cultures': 1, 'speaking': 1*D}),
    acumen=Acumen(3*D+2,),
    charisma=Charisma(3*D+2),
    body=20,
    move=10,
    advantages=[
        Patron(R1, "Sir Warrant"),
        Authority(R1, "aristocracy"),
        Wealth(R1, "wealthy"),
    ],
    disadvantages=[
        Infamy(R1, "Always in a fight"),
        Quirk(R1, "Hostile to every affront and slight"),
        Quirk(R1, "Insufferable superiority complex"),
    ],
)
characters = [ 
    squire_starter, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

