"""
Extract Characters from ``ch_1_allies.ipynb``.
Created by V2026.6.15.dev3 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



butcher = Character(
    name='Butcher: Bounty Hunter',
    physique=Physique(4*D+1),
    agility=Agility(4*D, {'fighting': 1*D, 'melee combat': 2}),
    coordination=Coordination(4*D, {'marksmanship': 1*D,  'throwing': 1*D}),
    intellect=Intellect(3*D+2, {'healing': 2, 'trading': 2, 'traps': 2}),
    acumen=Acumen(3*D, {'disguise': 2, 'gambling': 1, 'hide': 1, 'investigation': 2, 'know-how': 2, 'search': 2, 'streetwise': 2, 'survival': 2, 'tracking': 2, 'speaking': 2}),
    charisma=Charisma(3*D+2, {'intimidation': 6*D}),
    body=22,
    move=10,
    advantages=[
        Contacts(2, "Squire Angler"),
    ],
    disadvantages=[
        Quirk(2, "Hates cult of the Jackal"),
        Quirk(2, "Secretive to the point of being annoying"),
        Quirk(2, "Tends to brag pointlessly"),
        Enemy(2, "Cult of the Jackal is after him"),
    ],
    weapons=["Ugly daggers 1D+1", "Mace 1D+1"],
    armor=["Padded leather armor +1D"],
)

stitcher = Character(
    name='Stitcher, Anti-Jackal Priest',
    physique=Physique(4*D),
    agility=Agility(4*D, {'fighting': 1*D}),
    coordination=Coordination(4*D, {'sleight of hand': 1}),
    intellect=Intellect(3*D+2, {'healing': 2*D,  'reading/writing': 1*D}),
    acumen=Acumen(3*D+2, {'gambling': 1*D}),
    charisma=Charisma(2*D+2,),
    extranormal=Miracles(3*D),
    body=22,
    move=10,
    advantages=[
        Contacts(1, "Butcher"),
    ],
    disadvantages=[
        Quirk(2, "Hates cult of the Jackal"),
        Quirk(2, "Drunk"),
        Quirk(2, "Gambler"),
        Enemy(2, "Cult of the Jackal"),
    ],
    weapons=[
        "Small daggers 1D"
    ],
)
characters = [ 
    butcher, stitcher, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

