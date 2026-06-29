"""
Extract Spells from ``unique_cups.ipynb``.
Created by V2025.6.27.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

With "test" argument, runs doctest, which uses the __test__ examples.

"""

from opend6_tools.magic import *



neutralize_poison = Item(
    name='Chalice of Purity',
    notes="More like a wide bowl than a cup, this will enhance any food eaten from it.",
    effect=CompositeEffect(
        "Enhancements",
        GenericEffect("purify 4D of impurity", (2*D).measure),
        MassEffect("mass of food that fits in the chalice", "1 kilogram"),
    ),
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
        ArcaneKnowledgeAspect("controller: Hælan"),
        ArcaneKnowledgeAspect("Base Enchantment: Enhance Food"),
    ],
    price="H (300G)"
)

endless_drink = Item(
    name='Jug of Plenty',
    notes='A pitcher, or ewer that will slowly fill with whatever liquid is in it. For water, it creates a liter in about an hour. For something more complex, like wine or beer, it will make two hours. For something very complicated, like a potion, the time depends on the base difficulty of the potion.',
    effect=CompositeEffect(
        "Multiplication",
        GenericEffect("proper balance of elements 4D", (4*D).measure),
        MassEffect("mass of liquid in jug", "1 kilograms"),
    ),
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
        ArcaneKnowledgeAspect("controller: Witan"),
        ArcaneKnowledgeAspect("Base Invocation: Multiply Food"),
    ],
    price="H (600G)"
)

sleep = Item(
    name='Mug of Sleep',
    notes='common ceramic mug; when someone drinks from this mug, the mug will have a successful link and will attempt the R4 Sleep Enchantment.',
    effect=DisadvantageEffect("Narcolepsy", 4, "-4D to mental and physical attributes"),
    duration=DurationAspect(measure="1 hr"),
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
        ArcaneKnowledgeAspect("controller: Hildeþrymm"),
        ArcaneKnowledgeAspect("Base Enchantment: Sleep"),
    ],
    price="H (1500G)"
)

obedience = Item(
    name='Cup of Docility',
    notes="Looks like a drinking gourd; when someone drinks from this mug, the mug will have a successful link and will attempt the R3 Charm Enchantment.",
    effect=SkillEffect("Favorable Feelings", "+4D"),
    duration=DurationAspect(measure="30 min"),
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
        ArcaneKnowledgeAspect("controller: Folme"),
        ArcaneKnowledgeAspect("Base Invocation: Charm"),
    ],
    price="H (1400G)"
)
items = [ 
    neutralize_poison, endless_drink, sleep, obedience, 
]

__test__ = {
    
    'neutralize_poison': '>>> neutralize_poison.difficulty\n3\n',
    
    'endless_drink': '>>> endless_drink.difficulty\n6\n',
    
    'sleep': '>>> sleep.difficulty\n15\n',
    
    'obedience': '>>> obedience.difficulty\n14\n',
    
    
}


if __name__ == "__main__":
    app = build_app(items)
    app()

