"""
Extract Characters from ``oven.ipynb``.
Created by V2026.5.7.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



oven = Character(
    name='Oven, daughter of Sir Bond',
    description="Daughter of Baron of White Water.  Her mother has been exiled.  She's very greedy.",
    other_notes="""Quote: "What's it worth -- in gold?" """,
    physique=Physique(3*D+2),
    agility=Agility(4*D, {'fighting': 1*D, 'riding': 2*D, 'melee combat': 2*D}),
    coordination=Coordination(4*D, ),
    intellect=Intellect(3*D+2, {'cultures': 1*D, 'trading': 2*D}),
    acumen=Acumen(3*D+2, {'hide': 1*D, 'streetwise': 1*D}),
    charisma=Charisma(3*D+2, {'intimidation': 5*D}),
    body=24,
    move=10.0,
    advantages=[
        Patron(R1, "Sir Bond"),
        Authority(R2, "aristocracy"),
        Wealth(R1, "wealthy"),
    ],
    disadvantages=[
        Infamy(R1, "Reputation as greedy"),
        Quirk(R1, "Greedy to the point of kleptomania"),
        Quirk(R3, "Hates politics"),
    ],
)
characters = [ 
    oven, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

