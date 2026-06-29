"""
Items from OpenD6 Fantasy Locations
"""
from textwrap import dedent
from opend6_tools.magic2 import *

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
    notes=dedent("""\
        The exquisite weapon is a long sword, with a engraved hilt
        depicting a beautiful woman singing with a lute. Its deadliness
        is based upon the wielder's skill.
         
        -   A hero with a melee combat skill of 4D or less causes the unsheathed blade to emit a high-pitched whistle that can distract an opponent who fails an Easy mettle roll in the first round of hearing the sword.
        
        -   Characters with a melee combat skill of at least 6D can cause the sword to send forth a sonic blast, causes 2D+1 damage to all within two meters. Anyone wearing metal armor suffers an additional 1D of damage, as the sound sonic vibrations heat the metal. 
        
        -   Heroes with a melee combat skill of 8D can cause the sword to produce a low-pitched tone that can damage all solid objects. Anything composed of stone, glass, wood, or flesh within the two-meter area of effect suffers 2D+2 damage. 
        
        Each ability may only be used once per day, and the hero
        must have the appropriate skill level to use them. The wielder
        is not affected by any of the sword's abilities.
    """)
)

# The exquisite weapon is a long sword, with a engraved hilt
# depicting a beautiful woman singing with a lute. Its deadliness
# is based upon the wielder's skill. A hero with a melee combat
# skill of 4D or less causes the unsheathed blade to emit a
# high-pitched whistle that can distract an opponent who fails
# an Easy mettle roll in the first round of hearing the sword.
# Characters with a melee combat skill of at least 6D can cause
# the sword to send forth a sonic blast, causes 2D+1 damage to
# all within two meters. Anyone wearing metal armor suffers an
# additional 1D of damage, as the sound sonic vibrations heat
# the metal. Heroes with a melee combat skill of 8D can cause
# the sword to produce a low-pitched tone that can damage all
# solid objects. Anything composed of stone, glass, wood, or
# flesh within the two-meter area of effect suffers 2D+ 2 damage. Each ability may only be used once per day, and the hero
# must have the appropriate skill level to use them. The wielder
# is not affected by any of the sword's abilities.


items = [
    singing_sword,
]

__test__ = {
    "singing_sword": ">>> singing_sword.difficulty\n15",
}

if __name__ == "__main__":
    app = build_app(items)
    app()
