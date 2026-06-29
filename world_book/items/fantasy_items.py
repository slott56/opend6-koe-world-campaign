"""
Extract Spells from ``fantasy_items.ipynb``.
Created by V2025.6.27.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

With "test" argument, runs doctest, which uses the __test__ examples.

"""

from opend6_tools.magic import *



amulet_protection = Item(
    name = "Amulet of Protection",
    notes = "An oddly-shaped pendant on a thick leather cord envelopes the wearer in a defensive aura",
    effect = SpecialAbilityEffect(SpecialAbilityType.attack_resistance, 1, "non-enchanted weapons",
        modifications=[
            Limitation(LimitationType.burn_out, 1, "can be lost or stolen"),
        ]
    ),
    type="Jewelry: Amulet",
    price="H (200 G)"
)

enchanted_dagger = Item(
    name="Enchanted Dagger",
    notes="The weapon gives the user a greater chance of harming magical creatures",
    effect=SpecialAbilityEffect(SpecialAbilityType.natural_hand_to_hand_weapon, 1,
        modifications=[
            Enhancement(EnhancementType.magically_empowered, 2),
            Limitation(LimitationType.burn_out, 1, "can be lost or stolen")
        ]
    ),
    type="Weapon: Dagger",
    price="H (600 G)"
)

ring_of_power = Item(
    name="Ring of Power",
    notes="With this ring, the user can cast low-level magical spells",
    effect=CompositeEffect(
        "Ring",
        SpecialAbilityEffect(
            SpecialAbilityType.increased_attribute, 1, "magic",
            modifications=[
                Enhancement(EnhancementType.additional_effect, 4, "treat as if user uas 1D+1 in Magic regardless of actual Magic score"),
            ]
        ),
        SpecialAbilityEffect(
            SpecialAbilityType.skill_bonus, 1, "magic skills, alteration, apportation, and conjuration"
        ),
        modifications=[
            Limitation(LimitationType.burn_out, 1, "can be lost or stolen")
        ]
    ),
    type="Jewelry: ring",
    price="L (1200 G)"
)

dragons_kiss = Item(
    name="Dragon's Kiss",
    effect=SkillEffect(2*D, "bonus to healing skill"),
    other_conditions=[
        Limitation(DisadvantageType.burn_out, 1, note="can be lost or stolen")
    ],
    price="M (5 G)",
    notes=(
        "Rubbing this pungent concoction upon wounds hastens the healing process.\n"
        "The mixture must be kept dry at all times; otherwise, its healing properties are lost.\n"
        "There's enough in one packet for two uses."
    )
)

adrik_incense = Item(
    name="Adrik Incense",
    effect=AttributeEffect(2*D, "bonus to any Intellect skill"),
    other_conditions=[
        Limitation(DisadvantageType.burn_out, 1, note="can be lost or stolen")
    ],
    price="M (4 G)",
    notes=(
        "Burning this incense while performing any Intellect\n"
        "skill adds a +2 bonus to all related totals for one round\n"
        "Each stick of incense provides one use."
    )
)

dried_lion_flower_tea = Item(
    name="Dried Lion Flower Tea",
    effect=SkillEffect(2*D, "bonus to any stamina skills"),
    other_conditions=[
        Limitation(DisadvantageType.burn_out, 1, note="can be lost or stolen")
    ],
    notes=(
        "Brewing this tea and consuming adds 2 to stamina\n"
        "totals for two hours. The dry tea is sold in silk packs\n"
        "with enough for a single use."
    ),
    price="M (5 G)",
)

sun_mirror = Item(
    name="Mirror of the Highest Sun",
    effect=SpecialAbilityEffect(SpecialAbilityType.uncanny_aptitude, 4),
    other_aspects={
        "disdvantage": Limitation(DisadvantageType.burn_out, 1)
    },
    notes=(
        "These holy items are highly polished metal, made more\n"
        "reflective than any conventional means by the abbey's secret\n"
        "process. Although it does not seem to have any miraculous\n"
        "abilities of its own, it can augment other effects that rely on\n"
        "light or the sun. Thus vampires find light reflected by this\n"
        "mirror even more unbearable, illusions using it as a component\n"
        "are more effective, and so on."
    ),
    price="VD (100 G)"
)

charm = Item(
    name="Charm",
    effect=SkillEffect(4 * D, "bonus to charm skill"),
    other_conditions=[
        Limitation(DisadvantageType.burn_out, 1, note="can be lost or stolen"),
        OtherAlterant(-2, "acrid taste and a strong odor: Easy mettle or stamina to detect")
    ],
    price="M (5 G)",
    notes=(
        "This potion improves the attractiveness of a\n"
        "person for one day ( +4D to charm skill), but it requires that\n"
        "the user to ingest the liquid. Since the clear fluid has an\n"
        "acrid taste and a strong odor, imbibing it's a challenge (Easy\n"
        "mettle or stamina attempt). Mixing it with a substance that\n"
        "covers the flavor and smell reduces the difficulty."
    )
)

wretchedness = Item(
    name="Water of Wretchedness",
    effect=DisadvantageEffect(DisadvantageType.bad_luck, 3),
    other_conditions=[
        Limitation(DisadvantageType.burn_out, 1, note="can be lost or stolen"),
        OtherAlterant(-2, "offensive odor: Easy mettle or stamina to detect")
    ],
    price="M (5 G)",
    notes=(
        "A thick, syrupy substance that possesses an offensive\n"
        "odor. Once this potion has been consumed, the target\n"
        "suffers Bad Luck (R3). If the potion is mixed with another\n"
        "liquid or poured over food, the effect is reduced to Bad\n"
        "Luck (R2), as the potency is decreased. Coaxing or fooling a victim into consuming the liquid is at a +S to the\n"
        "interaction attempt."
    )
)

singing_sword = Item(
    name="Singing Sword",
    effect=CompositeEffect(
        "sword",
        DamageEffect(2*D, "ordinary sword damage"),
        DisadvantageEffect(DisadvantageType.hindrance, 2, note="Distracting whistle"),
        DamageEffect(2*D+1, "Sonic blast",),
        DamageEffect(1*D, "Sonic blast", "heats armor"),
        DamageEffect(2*D+2, "Destructive Vibration")# Destructive Vibration
    ),
    notes=(
        "The exquisite weapon is a long sword, with a engraved hilt"
        "depicting a beautiful woman singing with a lute. Its deadliness"
        "is based upon the wielder's skill."
        "\n\n"
        "-   A hero with a melee combat skill of 4D or less causes the unsheathed blade to emit a high-pitched whistle that can distract an opponent who fails" "an Easy mettle roll in the first round of hearing the sword."
        "\n\n"
        "-   Characters with a melee combat skill of at least 6D can cause the sword to send forth a sonic blast, causes 2D+1 damage to all within two meters." "Anyone wearing metal armor suffers an additional 1D of damage, as the sound sonic vibrations heat the metal."
        "\n\n"
        "-   Heroes with a melee combat skill of 8D can cause the sword to produce a low-pitched tone that can damage all solid objects. Anything composed of" "stone, glass, wood, or flesh within the two-meter area of effect suffers 2D+2 damage."
        "\n\n"
        "Each ability may only be used once per day, and the hero"
        "must have the appropriate skill level to use them. The wielder"
        "is not affected by any of the sword's abilities."
    )
)
items = [ 
    amulet_protection, enchanted_dagger, ring_of_power, dragons_kiss, adrik_incense, dried_lion_flower_tea, sun_mirror, charm, wretchedness, singing_sword, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(items)
    app()

