"""
Extract Spells from ``new_keep_items.ipynb``.
Created by V2025.6.27.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

With "test" argument, runs doctest, which uses the __test__ examples.

"""

from opend6_tools.magic import *



rod_of_missiles = Item(
    type="Rod/Wand/Staff", name="Rod of Missiles",
    notes="A short, heavy rod with a stored attack.",
    effect=DamageEffect("energy blast", 2*D, "ignores normal armor"),
    other_aspects={'charges': ChargesAspect(5)},
    other_conditions=[Limitation(LimitationType.burn_out, 1, "can be lost or stolen")])

helm_bravery = Item(
    type="Armor", name="Helm of Bravery",
    effect=SkillEffect("Intimidation", 3*D),
    other_conditions=[Limitation(LimitationType.burn_out, 1, "can be lost or stolen")]
)

power_shield = Item(
    type="Armor", name="Power Shield",
    effect=CompositeEffect(
        "Gain power",
        ProtectionEffect(3*D, "physical attacks"),
        SkillEffect(3*D, "boost physique by amount of damage protection"),
    ),
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
    ]
)

bottled_wind = Item(
    type="Artifact", name="Bottled Wind",
    notes="It's a large urn with straps so you can hold it",
    effect=SpecialAbilityEffect(SpecialAbilityType.flight, 3),
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
    ]
)

precognition_crystal = Item(
    type="Artifact", name="Forge Crystal",
    notes="an irregular lump of amber-like material, it grants obscure, oracular views of a possible future",
    effect=SpecialAbilityEffect(SpecialAbilityType.extra_sense, 1, "Precognition", modifications=Limitation(LimitationType.flaw, 1, "Vague visions")),
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
    ]
)

linked_mirrors = Item(
    type="Artifact", name="Linked Mirrors",
    notes="two identical mirrors; they can be viewed by a mage as one mirror in two places, and each mirror shows what's visible to the other",
    effect=SpecialAbilityEffect(SpecialAbilityType.extra_sense, 2, "Remote Sensing", modifications=Limitation(LimitationType.flaw, 1, "Can be hard to interpret")),
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
    ]
)

cats_eye_ring = Item(
    type="Artifact", name="Cat's Eye Ring",
    notes="a ring too large for a human, carved from a block of Chrysoberyl and polished to perfection",
    effect=SpecialAbilityEffect(
        SpecialAbilityType.infravision_ultravision, 3, "See in the dark",
        modifications=[
            Limitation(LimitationType.flaw, 1, "Can be hard to interpret"),
            Limitation(LimitationType.flaw, 1, "Too large to wear comfortably"),
        ]),
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
    ]
)

cup_of_visions = Item(
    type="Artifact", name="Cup of Visions",
    notes="a cup made from fine clay white on the inside and dark on the outside. It's supposed to be used to read tea leaves, that's not something any of the mages in the Jackal Temple have every tried.",
    effect=SkillEffect("Divination", 3*D, "Read the tea-drinker's past"),
    other_conditions=[
        Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
        Limitation(LimitationType.flaw, 1, "Can be hard to interpret"),
    ]
)
items = [ 
    rod_of_missiles, helm_bravery, power_shield, bottled_wind, precognition_crystal, linked_mirrors, cats_eye_ring, cup_of_visions, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(items)
    app()

