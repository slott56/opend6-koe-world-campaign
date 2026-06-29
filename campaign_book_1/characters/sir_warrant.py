"""
Extract Characters from ``sir_warrant.ipynb``.
Created by V2026.5.7.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



sir_warrant = Character(
    name='Sir Warrant',
    description='Last of the full-blooded, old "Eastern Lords".  This heritage has no advantages, since the monarchy has moved to another city.',
    physique=Physique(4*D),
    agility=Agility(4*D, {'fighting': 1*D, 'combat': 1*D, 'riding': 1*D, 'melee combat': 1*D}),
    coordination=Coordination(4*D, ),
    intellect=Intellect(4*D, {'cultures': 1*D, 'speaking': 2*D}),
    acumen=Acumen(4*D, ),
    charisma=Charisma(4*D, {'intimidation': 6*D+2}),
    extranormal=Magic(3*D+1),
    body=20,
    move=10,
    advantages=[
        Patron(R2, "Earl Hillshire"),
        Authority(R2, "aristocracy"),
        Wealth(R2, "wealthy"),
    ],
    disadvantages=[
        Infamy(R1, "Reputation as loafing buffoon"),
        Quirk(R1, "Negotiates Everything"),
        Quirk(R3, "Insufferable superiority complex"),
    ],
    other_notes="Quote: <grunt>; 'I stand as my people's warrant'",
)
characters = [ 
    sir_warrant, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

