"""
Extract Spells from ``white_water_lightning_rod.ipynb``.
Created by V2025.6.27.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

With "test" argument, runs doctest, which uses the __test__ examples.

"""

from opend6_tools.magic import *



lightning_rod = Item(
    type="Rod", name="Lightning Rod",
    effect=DamageEffect(1*D, "range 90m", "ignores non-magical armor"),
    other_aspects={'charges': ChargesAspect(5)},
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen")]
)
items = [ 
    lightning_rod, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(items)
    app()

