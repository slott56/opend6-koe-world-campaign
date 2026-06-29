"""
CONJURATION SPELLS

When run as an app, generates .RST details of each Spell.
"""

from magic1 import Aspect, Spell, detail


spells = [
    Spell(
        effect=Aspect(format="resistance total of bars", base_difficulty=25, count=1),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="25 meters ", base_difficulty=7, count=1),
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        casting_time=Aspect(format="1 min", base_difficulty=-9, count=1),
        name="Cage",
        other_aspects={
            "Difficulty": Aspect(format="27", base_difficulty=0.0, count=1),
            "Area Effect": Aspect(
                format="Sphere with a radius of 3 meters", base_difficulty=15, count=1
            ),
            "Gesture": Aspect(
                format="Mime escaping from a cell, then point to target (complex; acrobatics roll with difficulty of 11)",
                base_difficulty=-3,
                count=1,
            ),
            "Unreal Effect": Aspect(
                format="Disbelief difficulty of 13", base_difficulty=-7, count=1
            ),
        },
        other_conditions=[],
        notes="Cage traps a target in a prison of magical energy. To cast it, the\nwizard mimics trying to escape from a cell, then points at her target.\nIf a marksmanship total beats the combat difficulty for the target, the\nquarry is trapped. The cage is a sphere with a radius of three meters.\nCreatures larger than that can't be confined by this spell.\nThe effect's value plus the result points bonus serves as the damage\nresistance total of the bars. The target can disbelieve and thus free\nhimself by generating a Acumen or investigation total of 13.\n",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format='speaking skill with specialization in the animal\'s "language" at 5D',
            base_difficulty=15,
            count=1,
        ),
        duration=Aspect(format="6 minutes ", base_difficulty=13, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Communicate With Animals",
        other_aspects={
            "Difficulty": Aspect(format="10", base_difficulty=0.0, count=1),
            "Components": Aspect(
                format="Something from the type of animal with which she wants to communicate (very common)",
                base_difficulty=-2,
                count=1,
            ),
            "Gesture": Aspect(
                format="Draw a line on the ground (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
        },
        other_conditions=[],
        notes="To communicate with an animal, the caster places on the ground\nthe bit of something from that type of animal (lock of horse's hair,\nbird's feather, several strands of dog's hair). Then she draws a line\nfrom it to her and from it in the direction of the animal or animals\nshe wishes to speak to. For about six minutes, she receives the abil\xad\nity to communicate with any of that kind of animal as if she had a\nspecialization in its language at SD. She may add the result points\nbonus to her speaking roll total. The caster may not move more than\none meter from the casting location.\n",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="Bad Luck (R2) Disadvantage", base_difficulty=6, count=1),
        duration=Aspect(format="10 minutes ", base_difficulty=14, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous", base_difficulty=5, count=1),
        casting_time=Aspect(format="2 rounds ", base_difficulty=-5, count=1),
        name="Evil Eye Curse",
        other_aspects={
            "Difficulty": Aspect(format="11", base_difficulty=0.0, count=1),
            "Focused": Aspect(format="On target", base_difficulty=4, count=1),
            "Feedback": Aspect(
                format="-3 to damage resistance total", base_difficulty=-3, count=1
            ),
            "Concentration": Aspect(
                format="1 round with mettle difficulty of 8",
                base_difficulty=-2,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(format="Limited to Humans", base_difficulty=-3, count=1),
        ],
        notes='With a minimal amount of pain to himself, the caster curses a\nHuman target that she can see with 10 minutes of Bad Luck (R2).\nSee the description of this Disadnntage in the "Character Options"\nchapter for details.\n',
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="negates up to -4D of darkness modifier", base_difficulty=12, count=1
        ),
        duration=Aspect(format="10 minutes ", base_difficulty=14, count=1),
        range=Aspect(format="Touch ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="2 rounds", base_difficulty=-5, count=1),
        name="Glow Stone",
        other_aspects={
            "Difficulty": Aspect(
                format="12", base_difficulty=0.0, count=1
            ),  # Should be 10
            "Components": Aspect(
                format="white pebble (common, destroyed)", base_difficulty=-4
            ),
            "Focused": Aspect(format="On pebble", base_difficulty=5),
            "Gesture": Aspect(
                format="Hold pebble between thumb and forefinger (simple)",
                base_difficulty=-1,
            ),
            "Incantation": Aspect(
                format='"Stone of white, give us light." (sentence)', base_difficulty=-2
            ),
        },
        other_conditions=[],
        notes="The magic user casts this spell on a small, white stone, making it\nglow with a fierce radiance that extends for one meter in all direc\xad\ntions around the pebble. The effect lasts for 10 minutes. Once the\nduration wears off, the pebble turns to dust.\n",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="5 kilograms of food and water", base_difficulty=4, count=1
        ),
        duration=Aspect(format="4 hours ", base_difficulty=21, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1r", base_difficulty=-4, count=1),
        name="Feast",
        other_aspects={
            "Difficulty": Aspect(format="10", base_difficulty=0.0, count=1),
            "Components": Aspect(
                format="A plain, doth napkin (common), a small metal cup (common)",
                base_difficulty=-6,
                count=1,
            ),
            "Gesture": Aspect(
                format="Wave hand several times over napkin and cup (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Focused": Aspect(format="On people who eat food", base_difficulty=4),
            "Other Alterants": Aspect(
                format="clean water and hearty food", base_difficulty=3
            ),
        },
        other_conditions=[],
        notes="With this cantrip, the mage creates a meal for two of pure, dean\nwater; flavorful, hearty bread; fresh vegetables and fruits; and, if\ndesired, cheese wedges and smoked meat slices. The food must be\nconsumed within 10 minutes ofitsappearance, so that it has a chance\nto stay in the body long enough to be digested and actually provide\nnourishment. The result points bonus increases the amount of food\nappearing or (at the gamemaster's discretion) the quality of food.\n",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="4D in damage", base_difficulty=12, count=1),
        duration=Aspect(format="3.5 seconds", base_difficulty=3, count=1),
        range=Aspect(format="10m", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="1.5 seconds ", base_difficulty=-1, count=1),
        name="Mystic Bolt",
        other_aspects={
            "Difficulty": Aspect(format="10", base_difficulty=0.0, count=1),
            "Gesture": Aspect(
                format="Swirl hand in air as if gathering energy, then throw it at target (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantation": Aspect(
                format='"Ahl" (word, said loudly)', base_difficulty=-2, count=1
            ),
        },
        other_conditions=[],
        notes="The mage gathers energy from his surroundings and throws the ball\nat a target. It does 4D in damage at a range of up to 10 meters. He\nmust make a marksmanship roll to hit the target. The bolt must\nbe fired in the same round that the mage casts the spell.\n",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="Armor Value of 6D", base_difficulty=18, count=1),
        duration=Aspect(format="5 rounds ", base_difficulty=7, count=1),
        range=Aspect(format="1.5 meters ", base_difficulty=1, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=1, count=1),
        casting_time=Aspect(format="1.5 sec", base_difficulty=-1, count=1),
        name="Mystical Shield",
        other_aspects={
            "Difficulty": Aspect(format="10", base_difficulty=0.0, count=1),
            "Area effect": Aspect(
                format="One-meter radius",
                base_difficulty=2,
                count=1,
            ),
            "Components": Aspect(
                format="A simple ring(uncommon), handful of colored sand (com m on, destroyed)",
                base_difficulty=-10,
            ),
            "Focused": Aspect(format="On ring", base_difficulty=5, count=1),
            "Gesture": Aspect(
                format="Using colored und, scribe an oval shape in the air (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantation": Aspect(
                format='"Protection!" (word)', base_difficulty=-1, count=1
            ),
        },
        other_conditions=[],
        notes="By tossing some sand in a circle in front of her, the caster creates a\nsemi-transparent oval shield of the samecolor as the sand. The shield,\nabout two meters in diameter, appears up to 1.5 meters away. It is\nfocused on the ring, which the mage must wear. It offers an Armor\nValue of 6D against all types of physical (not ment.al) att.acks.\n",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="6D+2 stun damage", base_difficulty=15, count=1),
        duration=Aspect(format="3.5 seconds ", base_difficulty=3, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="1.5 sec", base_difficulty=-1, count=1),
        name="Stunned Senseless",
        other_aspects={
            "Difficulty": Aspect(format="12", base_difficulty=0.0, count=1),
            "Incantation": Aspect(format='"Stop!" (word)', base_difficulty=-1),
            "Gesture": Aspect(
                format="Point finger and then palm at intended t.arget (fairly simple)",
                base_difficulty=-2,
            ),
        },
        other_conditions=[],
        notes="With a gesture and a word, the magic user sends a bolt of mystical\nenergy toward his in tended t.arget. However , the bolt isn't intended\nto harm the target, instead only doing stun damage.",
        skill="Conjuration",
    ),
]


if __name__ == "__main__":
    detail(spells)


__test__ = {
    "Cage": ">>> spells[0].difficulty\n27",
    "Communicate With Animals": ">>> spells[1].difficulty\n10",
    "Evil Eye Curse": ">>> spells[2].difficulty\n11",
    "Glow Stone": ">>> spells[3].difficulty\n10",
    "Feast": ">>> spells[4].difficulty\n10",
    "Mystic Bolt": ">>> spells[5].difficulty\n10",
    "Mystical Shield": ">>> spells[6].difficulty\n10",
    "Stunned Senseless": ">>> spells[7].difficulty\n12",
}
