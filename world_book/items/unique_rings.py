"""
Extract Spells from ``unique_rings.ipynb``.
Created by V2025.6.27.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

With "test" argument, runs doctest, which uses the __test__ examples.

"""

from opend6_tools.magic import *



hurt_wearer = Item(
    name="Ring of Pain",
    notes="A plain looking ring made of lead, incompletely transmuted to gold, with an inscription of curing a specific disease or preventing a specific wound -- the inscribed disease or wound is *actually* a trigger for additional damage from the ring.",
    effect=DamageEffect("Damage to the wearer", 3*D, "physical", "ignores all armor"),
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
        GenericAspect(2,"Triggered by the disease or wound type in the inscription"),
        GenericAspect(0, "controller: Hælan"),
        ArcaneKnowledgeAspect("Controller: Baelu"),
        ArcaneKnowledgeAspect("Base Enchantment: Immediate Hurt"),
    ],
    price="D (20G)"
)

protect_from_poison = Item(
    name="Protection from Poisons",
    notes="A silver ring, set with a piece of bezoar cut in shape of a chalice, this reduces or eliminates the damage from poisons of any kind (ingested or infused.)",
    effect=ProtectionEffect("Protection", 3*D, "physical", "poisons only"),
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
        GenericAspect(0, "controller: Hælan"),
        ArcaneKnowledgeAspect("Controller: Hælan"),
        ArcaneKnowledgeAspect("Base Enchantment: Gradual Heal"),
    ],
    price="H (400G)"
)

summon_fire = Item(
    name="Ring of Fire",
    notes="An iron ring with a black onyx stone surrounding a sapphire, this will summon a small amount of fire from nearby sources.",
    effect=DamageEffect("Move small fire element", 4*D, "physical damage"),
    range=RangeAspect("20m"),
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
        GenericAspect(2,"Fire element must be found somewhere nearby"),
        ArcaneKnowledgeAspect("controller: Cyþan"),
        ArcaneKnowledgeAspect("Base Enchantment: Light Fire"),
    ],
    price="H (800G)"
)

invisibility = Item(
    name="Invisibility",
    notes="A ring of woven gold wires strung with tiny seed pearls; this provides invisibility from nearby observers",
    effect=DisadvantageEffect("Perception is ruined for anyone in range", 4),
    range=RangeAspect("10m"),
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
        ArcaneKnowledgeAspect("controller: Witan"),
        ArcaneKnowledgeAspect("Base Enchantment: Totally Invisible"),
    ],
    price="H (800G)"
)

protect_from_evil = Item(
    name="Protection from Evil",
    notes="A ring of gold (poorly transmuted from lead) with jade circle or crown, this ring will weaken and may break the will of opponents with evil intent",
    effect=AttributeEffect("Charisma", 4*D),
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
        GenericAspect(2, "Only opponents see this glamor"),
        ArcaneKnowledgeAspect("controller: Baelu"),
        ArcaneKnowledgeAspect("Base Invocation: Shield from Evil"),
    ],
    price="H (500G)"
)

resist_fire = Item(
    name="Fire Resistance",
    notes="Set with a cluster of diamonds, this reduces or eliminates the damage from fire",
    effect=ProtectionEffect("Protection", 3*D, "physical", "fire only"),
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
        ArcaneKnowledgeAspect("controller: Hælan"),
        ArcaneKnowledgeAspect("Base Enchantment: Pass Fire"),
    ],
    price="H (400G)"
)
items = [ 
    hurt_wearer, protect_from_poison, summon_fire, invisibility, protect_from_evil, resist_fire, 
]

__test__ = {
    
    'hurt_wearer': '>>> hurt_wearer.difficulty\n8\n',
    
    'protect_from_poison': '>>> protect_from_poison.difficulty\n4\n',
    
    'summon_fire': '>>> summon_fire.difficulty\n8\n',
    
    'invisibility': '>>> invisibility.difficulty\n8\n',
    
    'protect_from_evil': '>>> protect_from_evil.difficulty\n5\n',
    
    'resist_fire': '>>> resist_fire.difficulty\n4\n',
    
    
}


if __name__ == "__main__":
    app = build_app(items)
    app()

