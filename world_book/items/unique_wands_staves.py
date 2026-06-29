"""
Extract Spells from ``unique_wands_staves.ipynb``.
Created by V2025.6.27.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

With "test" argument, runs doctest, which uses the __test__ examples.

"""

from opend6_tools.magic import *



cancellation = Item(
    name="Rod of Disruption",
    notes="A thick rod of a willow trunk, with iron inlays running its length; it will disturb the enchantment of items up to 5 times before it must be recharged",
    effect=GenericEffect(
        description="compare to skill total of spell countering", difficulty=30
    ),
    other_aspects={
        'charges': ChargesAspect(5),
    },
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
        ArcaneKnowledgeAspect("Controller: Hælan -- Anti-Cyþan"),
        ArcaneKnowledgeAspect("Base Enchantment: Disrupt Spell")
    ],
    price="H (170G)"
)

curing = Item(
    name="Wand of Healing",
    notes="A slender wand of willow, with a white, silk ribbon wound around it, this will cure many injuries or diseases",
    effect=SkillEffect("Heal disease", "5D", "skill"),
    other_aspects={
        'charges': ChargesAspect(5),
    },
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
        ArcaneKnowledgeAspect("Controller: Hælan"),
        ArcaneKnowledgeAspect("Base Enchantment: Gradual Heal")
    ],
    price="VD (90G)"
)

serpent = Item(
    name="Serpent Staff",
    notes="A staff made from gnarled black locust, cut down, and carved with a repeating scaled pattern concealing the words to command it; on command becomes a large, deadly viper",
    effect=GenericEffect("Temperamental Conjuration of 10D viper.", 30, notes="some Earth elemental holding the viper in place will be discarded; some earth must be used to reverse the effect"),
    other_aspects={
        'charges': ChargesAspect(2),
    },
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
        ArcaneKnowledgeAspect("Controller: Baelu"),
        ArcaneKnowledgeAspect("Base Enchantment: Reanimation")
    ],
    price="H (160G)"
)

enemy_detection = Item(
    name="Scepter of Enemy Detection",
    notes="A scepter of oak, topped with a small bronze shield, this will find anyone within 30m who has activate animosty",
    effect=SkillEffect(
        "search of 8D to locate an enemy", 8*D
    ),
    other_aspects={
        'charges': ChargesAspect(10),
    },
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
        ArcaneKnowledgeAspect("Controller: Hildeþrymm"),
        ArcaneKnowledgeAspect("Base Invocation: Detect Enemies")
    ],
    price="H (140G)"
)

fear = Item(
    name="Wand of Fear",
    notes="A poplar rod, with 3 yellow bands",
    effect=SkillEffect("intimidation skill bonus", "+6D+2", "skill modifier"),
    other_aspects={
        'charges': ChargesAspect(5),
    },
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
        ArcaneKnowledgeAspect("Controller: Baelu"),
        ArcaneKnowledgeAspect("Base Enchantment: Fear")
    ],
    price="H (170G)"
)

fire = Item(
    name="Staff of Eternal Flame",
    notes="A staff of pine, still smelling faintly of resin, crowned with an iron starburst",
    effect=DamageEffect("move fire 2m/s, does damage on contact", "6D", "physical damage", "ignores nonmagical armor"),
    duration=DurationAspect(measure="5 m"),
    range=RangeAspect(measure="10 m"),
    other_aspects={
        'charges': ChargesAspect(5),
    },
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
        ArcaneKnowledgeAspect("Controller: Cyþan"),
        ArcaneKnowledgeAspect("Base Enchantment: Fire Ball")
    ],
    price="H (240G)"
)

lightning = Item(
    name="Lightning Rod",
    notes="A narrow rod of shining tin, wrapped with a thickly woven hemp handle",
    effect=DamageEffect("move air+fire 2m/s, does damage", "5D+1", "physical damage", "ignores all armor"),
    range=RangeAspect(measure="30 m"),
    other_aspects={
        'charges': ChargesAspect(5),
    },
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
        ArcaneKnowledgeAspect("Controller: Folme"),
        ArcaneKnowledgeAspect("Base Enchantment: Lightning")
    ],
    price="H (210G)"
)

missile = Item(
    name="Rod of Darts",
    notes="A hollow rod of heavy, dark tin, wrapped with a wooden handle at one end; the operation is fiddly with having to load the dart and fire by touching the obsidian to it",
    effect=DamageEffect("Dart", "+4D", "physical damage; damage modifier"),
    range=RangeAspect(measure="30 m"),
    other_aspects={
        'charges': ChargesAspect(20),
        'components': ComponentsAspect(
             ("Black obsidian", "uncommon; destroyed"), ("dart", "common"),
        ),
    },
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
        ArcaneKnowledgeAspect("Controller: Folme"),
        ArcaneKnowledgeAspect("Base Enchantment: Deadly Dart")
    ],
    price="VD (100G)"
)

treasure = Item(
    name="Gold Divining Rod",
    notes="Clumsy chestnut rod with four wavy carvings",
    effect=SkillEffect("boosts Acumen/search", "+3D", "skill modifier"),
    # duration=DurationAspect(measure="5 m"),
    range=RangeAspect(measure="10 m"),
    other_aspects={
        'charges': ChargesAspect(10),
    },
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
        ArcaneKnowledgeAspect("Controller: Witan"),
        ArcaneKnowledgeAspect("Base Enchantment: Find Path")
    ],
    price="H (120G)"
)

knock = Item(
    name="Knock Cudgel",
    notes="heavy poplar branch, topped with a knot, wrapped in tin",
    effect=DamageEffect("break latch or bar", "8D", "physical damage"),
    other_aspects={
        'charges': ChargesAspect(5),
    },
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
        ArcaneKnowledgeAspect("Controller: Folme"),
        ArcaneKnowledgeAspect("Base Enchantment: Knock")
    ],
    price="H (140G)"
)
items = [ 
    cancellation, curing, serpent, enemy_detection, fear, fire, lightning, missile, treasure, knock, 
]

__test__ = {
    
    'cancellation': '>>> cancellation.difficulty\n17\n',
    
    'curing': '>>> curing.difficulty\n9\n',
    
    'serpent': '>>> serpent.difficulty\n16\n',
    
    'enemy_detection': '>>> enemy_detection.difficulty\n14\n',
    
    'fear': '>>> fear.difficulty\n17\n',
    
    'fire': '>>> fire.difficulty\n24\n',
    
    'lightning': '>>> lightning.difficulty\n21\n',
    
    'missile': '>>> missile.difficulty\n10\n',
    
    'treasure': '>>> treasure.difficulty\n12\n',
    
    'knock': '>>> knock.difficulty\n14\n',
    
    
}


if __name__ == "__main__":
    app = build_app(items)
    app()

