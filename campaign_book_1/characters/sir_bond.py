"""
Extract Characters from ``sir_bond.ipynb``.
Created by V2026.5.7.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



sir_bond = Character(
    name='Sir Bond, Defender of White Water',
    description='Half-blooded.  Eastern Lord mother and conventional father.  Not a good administrator.  Very loud and ill-mannered.',
    other_notes="""Quote: "Just let me say that I don't like this at all." """,
    physique=Physique(3*D+2),
    agility=Agility(4*D, {'fighting': 1*D, 'riding': 2*D, 'melee combat': 1*D}),
    coordination=Coordination(4*D),
    intellect=Intellect(4*D, {'cultures': 1*D, 'speaking': 2*D, 'trading': 1*D}),
    acumen=Acumen(4*D, {'artist': 1*D, 'investigation': 1*D}),
    charisma=Charisma(4*D, {'intimidation': 6*D+2}),
    body=20,
    move=10.0,
    advantages=[
        Patron(R2, "Earl Southlands"),
        Authority(R2, "aristocracy"),
        Wealth(R2, "wealthy"),
    ],
    disadvantages=[
        Infamy(R1, "Reputation as womanizer"),
        Quirk(R1, "Argues Everything, even when he agrees"),
        Quirk(R3, "Afraid of assassination"),
    ],
)
characters = [ 
    sir_bond, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

