"""
OpenD6 Project Spells

See *The OpenD6 Project*, https://opend6project.wordpress.com.

When run as an app, generates .RST details of each Spell.
"""

from magic1 import Aspect, Spell, detail


cantrips = [
    Spell(
        effect=Aspect(format="medicine skill of 5D+2", base_difficulty=16, count=1),
        duration=Aspect(format="1.5 seconds", base_difficulty=1, count=1),
        range=Aspect(format="Touch", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round", base_difficulty=-4, count=1),
        name="Aid",
        other_aspects={},
        other_conditions=[
            Aspect(
                format="Physical contact with creature; may only be used on living creatures",
                base_difficulty=-3,
                count=1,
            )
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=0, count=1),
        notes=[
            "By touching an injured being, the magic user can use this cantrip to heal harm as if he had 5D+2 in the medicine skill."
        ],
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="charm skill bonus of +4D", base_difficulty=18, count=1),
        duration=Aspect(format="1 minute", base_difficulty=9, count=1),
        range=Aspect(format="Self", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round", base_difficulty=-4, count=1),
        name="Charm",
        other_aspects={
            "Gesture": Aspect(
                format="Smile and make a gesture of welcome or admiration",
                base_difficulty=-2,
                count=1,
            ),
            "Unreal Effect": Aspect(
                format="Difficulty to disbelieve is 13", base_difficulty=-9, count=1
            ),
        },
        other_conditions=[
            Aspect(
                format="May only be used on humanoids who understand the caster’s language and can hear the caster",
                base_difficulty=-2,
                count=1,
            ),
        ],
        speed=Aspect(format="0D", base_difficulty=0, count=1),
        notes=[
            "With a smile and a friendly gesture, the caster improves his charm skill by for one minute. (If he no charm skill, add the bonus to the character’s Charisma attribute.) As this is an illusory spell, if the intended target of the charm disbelieves it, any effect the charm attempt had wears off immediately."
        ],
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="+1D bonus to one non-Extranormal attribute",
            base_difficulty=6,
            count=1,
        ),
        duration=Aspect(format="5 rounds", base_difficulty=7, count=1),
        range=Aspect(format="1 meter", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round", base_difficulty=-4, count=1),
        name="Heighten Attribute (Template)",
        other_aspects={
            "Gesture": Aspect(
                format="Mime an activity using a skill that falls under the attribute to be heightened (complex, action difficulty of 11; examples: sleight of hand for Coordination, lifting for Physique)",
                base_difficulty=-3,
                count=1,
            )
        },
        other_conditions=[],
        speed=Aspect(format="0D", base_difficulty=0, count=1),
        notes=[
            "This cantrip gives the target a bonus of +1D to one of his attributes for 25 seconds, or five rounds — as long as he doesn’t move more than a meter from the spot on which he received the bonus.",
            "Note that this is only a template for a spell and not an actual spell, because it does not indicate in the description which attribute is affected. The caster must specify which attribute and skill to mime before learning the spell (which takes one round).",
        ],
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="1 kilogram of bread and water", base_difficulty=1, count=1
        ),
        duration=Aspect(format="4 hours", base_difficulty=21, count=1),
        range=Aspect(format="Touch", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round", base_difficulty=-4, count=1),
        name="Meal",
        other_aspects={
            "Components": Aspect(
                format="A plain, cloth napkin (common), a small metal cup (common)",
                base_difficulty=-6,
                count=1,
            ),
            "Gestures": Aspect(
                format="Wave hands several times over napkin and cup (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantation": Aspect(
                format="“Fill these with food and drink.” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        other_conditions=[],
        speed=Aspect(format="0D", base_difficulty=0, count=1),
        notes=[
            "With this cantrip, the mage creates a simple meal of bread and water, which sticks around in the system long enough to be digested and actually provide nourishment."
        ],
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="compare to difficulty to open lock", base_difficulty=18, count=1
        ),
        duration=Aspect(format="1 round", base_difficulty=4, count=1),
        range=Aspect(format="Touch", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round", base_difficulty=-4, count=1),
        name="Open Lock",
        other_aspects={
            "Components": Aspect(
                format="Large metal key (common)", base_difficulty=-3, count=1
            ),
            "Gesture": Aspect(
                format="Mime opening the lock with the key (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantation": Aspect(
                format="“Open, Lock, and reveal your secrets.” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(format="Physical contact with lock", base_difficulty=-1, count=1),
        ],
        speed=Aspect(format="0D", base_difficulty=0, count=1),
        notes=[
            "To cast this cantrip, the mage touches the lock with one hand while, with the key held in it, miming opening the lock with the other hand. After reciting the incantation, he touches the lock with the key and turns the key. If the spell effect’s value is equal to or greater than the difficulty of the lock, it opens. If there are any traps or wards on the lock, they are not circumvented by this spell! Note that this spell works on any kind of mechanical lock."
        ],
        skill="Apportation",
    ),
]

alteration_spells = [
    Spell(
        effect=Aspect(
            format="compare to skill total of spell countering",
            base_difficulty=29,
            count=1,
        ),
        duration=Aspect(format="1 round", base_difficulty=4, count=1),
        range=Aspect(format="60m", base_difficulty=9, count=1),
        speed=Aspect(format="Instant", base_difficulty=9, count=1),
        casting_time=Aspect(format="1 round", base_difficulty=-4, count=1),
        name="Countermagic",
        other_aspects={
            "Concentration": Aspect(
                format="3 seconds with mettle difficulty of 7",
                base_difficulty=-1,
                count=1,
            ),
            "Gesture": Aspect(
                format="Wave hand through air as if wiping away something (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Incantation": Aspect(
                format="“Your hold is broken!” (sentence, said loudly)",
                base_difficulty=-3,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="One spell, which the caster must specify when casting this spell",
                base_difficulty=-4,
                count=1,
            ),
        ],
        notes=[
            "The caster concentrates on the spell he wishes to counter, waving his hand and shouting the required incantation. The effect’s value plus the result points bonus are compared to the skill total used to create the targeted spell. If the countermagic number is equal to or higher than the target spell’s skill total, the spell is broken."
        ],
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="compare to skill total of spell countering",
            base_difficulty=29,
            count=1,
        ),
        duration=Aspect(format="1r", base_difficulty=4, count=1),
        range=Aspect(
            format="Self or a target within 1 meter", base_difficulty=0, count=1
        ),
        speed=Aspect(format="Instant", base_difficulty=0, count=1),
        casting_time=Aspect(format="25 minutes", base_difficulty=-16, count=1),
        name="Countermagic Ward",
        other_aspects={
            "Charges": Aspect(
                format="6 charges, with a ward to go off when a spell “hits” the target",
                base_difficulty=6,
                count=1,
            ),
            "Concentration": Aspect(
                format="10 minutes with mettle difficulty of 10",
                base_difficulty=-4,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=6, count=1),
            "Gesture": Aspect(
                format="Wave hand through air as if wiping away something (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Incantation": Aspect(
                format="“Let no spell touch me!” (sentence, said loudly)",
                base_difficulty=-3,
                count=1,
            ),
        },
        other_conditions=[],
        notes=[
            "Similar to the countermagic spell, this spell gives the target a general protection against spells. It is triggered by a spell “hitting” the target. Up to six spells can be countered in this fashion. The effect’s value plus result points bonus are compared to the skill total used to create the targeted spell. If the countermagic ward number is equal to or higher than the target spell’s skill total, the spell is broken. Regardless of the success of the ward, one charge is lost."
        ],
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(format="+4D in damage", base_difficulty=18, count=1),
        duration=Aspect(format="5 rounds", base_difficulty=7, count=1),
        range=Aspect(format="100 m", base_difficulty=10, count=1),
        speed=Aspect(format="Instant", base_difficulty=10, count=1),
        casting_time=Aspect(format="1 hr", base_difficulty=-18, count=1),
        name="Deadly Bullet",
        other_aspects={
            "Component": Aspect(
                format="Black obsidian (uncommon, destroyed), dart (common)",
                base_difficulty=-11,
                count=1,
            ),
            "Feedback": Aspect(
                format="-3 to damage resistance total", base_difficulty=-3, count=1
            ),
            "Focused": Aspect(format="", base_difficulty=5, count=1),
            "Gesture": Aspect(
                format="Rub the tip of the bullet on the stone (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Incantation": Aspect(
                format="“Darkness of death.” (a few words)", base_difficulty=-1, count=1
            ),
            "Variable Movement": Aspect(
                format="+2 accuracy bonus", base_difficulty=4, count=1
            ),
        },
        other_conditions=[],
        notes=[
            "This spell uses a piece of black obsidian to increase the deadliness of a bullet. The mage utters a short, dark phrase while gently stroking the tip of the bullet across the stone. The darkness travels into the bullet, draining the stone of its pigment.",
            "To release the spell, the caster inserts it into an appropriate gun within five rounds of casting the spell. The gun’s user must generate an marksmanship total, adding a +2 bonus for the increased accuracy of the spell, against the combat difficulty for the target. The target must be within range of the spell, or the bullet merely does its normal effect. The target takes an additional 4D in damage in the round the bullet hits and for the next four rounds. The spell ends if the target moves beyond the spell’s range.",
        ],
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(format="+4D in damage", base_difficulty=18, count=1),
        duration=Aspect(format="5 rounds", base_difficulty=7, count=1),
        range=Aspect(format="100m", base_difficulty=10, count=1),
        speed=Aspect(format="Instant", base_difficulty=10, count=1),
        casting_time=Aspect(format="40 min", base_difficulty=-17, count=1),
        name="Deadly Dart",
        other_aspects={
            "Charges": Aspect(format="1 charge", base_difficulty=1, count=1),
            "Components": Aspect(
                format="Black obsidian (uncommon, destroyed), dart (common)",
                base_difficulty=-11,
                count=1,
            ),
            "Feedback": Aspect(
                format="-3 to damage resistance total", base_difficulty=-3, count=1
            ),
            "Focused": Aspect(format="", base_difficulty=5, count=1),
            "Gesture": Aspect(
                format="Rub the tip of the bullet on the stone (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Incantation": Aspect(
                format="“Darkness of death.” (a few words)", base_difficulty=-1, count=1
            ),
            "Variable Movement": Aspect(
                format="+2 accuracy bonus", base_difficulty=4, count=1
            ),
        },
        other_conditions=[],
        notes=[
            "This spell uses a piece of black obsidian to increase the deadliness of a dart. The mage utters a short, dark phrase while gently stroking the tip of the dart across the stone. The darkness travels into the dart, draining the stone of its pigment.",
            "To release the spell, the caster throws the dart within five rounds of casting the spell. He generate an marksmanship total, adding a +2 bonus for the increased accuracy of the spell, against the combat difficulty for the target. The target must be within range of the spell, or the dart merely does its normal effect. The target takes an additional 4D in damage in the round the dart hits and for the next four rounds. The spell ends if the target moves beyond the spell’s range.",
        ],
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(format="8D drain", base_difficulty=24, count=1),
        duration=Aspect(format="1 min", base_difficulty=9, count=1),
        range=Aspect(format="40m", base_difficulty=8, count=1),
        speed=Aspect(format="Instant", base_difficulty=8, count=1),
        casting_time=Aspect(format="15 sec", base_difficulty=-6, count=1),
        name="Drain Toughness",
        other_aspects={
            "Components": Aspect(
                format="Blood of a great cat (very rare, destroyed), funnel (common, destroyed)",
                base_difficulty=-16,
                count=1,
            ),
            "Gesture": Aspect(
                format="Pick up an item and pull it closer (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Incantation": Aspect(
                format="“Weaken and perish before my hand.” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        other_conditions=[],
        notes=[
            "Caster focuses magical energies into a funnel, with the large end facing the target. When activated, the funnel pulls energy from the target, and sends it to the source of the spell. The spell itself is not visible, but it can be felt. It requires a marksmanship roll to focus on a target.",
            "Compare the spell effect’s value to a roll of the target’s Physique. Multiply the difference by 3. This is the target’s negative damage resistance total modifier. If this number is greater than 3 times the die code in the target’s Physique (ignore the pips), the target is unconscious for eight hours. The negative modifier vanishes after one minute.",
            "The caster receives one-half (rounded up) of the negative damage resistance total modifier as a positive modifier to her damage resistance. When the spell wears off after one minute, the resistance total bonus goes with it.",
        ],
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="intimidation skill bonus at +6D+2", base_difficulty=30, count=1
        ),
        duration=Aspect(format="2.5 min", base_difficulty=11, count=1),
        range=Aspect(format="100m", base_difficulty=10, count=1),
        speed=Aspect(format="Instant", base_difficulty=10, count=1),
        casting_time=Aspect(format="1 min", base_difficulty=-9, count=1),
        name="Fear",
        other_aspects={
            "Components": Aspect(
                format="An item owned for at least a month by the target (very rare)",
                base_difficulty=-5,
                count=1,
            ),
            "Gesture": Aspect(
                format="Point item at target (simple)", base_difficulty=-1, count=1
            ),
            "Incantation": Aspect(
                format="Frightening words (a few words)", base_difficulty=-1, count=1
            ),
            "Unreal Effect": Aspect(
                format="Difficulty to disbelieve is 13", base_difficulty=-8, count=1
            ),
        },
        other_conditions=[],
        notes=[
            "To cast the spell, the mage first needs something belonging to her target — his comb, his watch, a lock of his hair. Mutter a few words of power, point the item at the target, and watch the fun. This spell gives the caster an intimidation skill bonus of +6D+2, but only towards that target. The target may disbelieve it with a Charisma or mettle roll of 13."
        ],
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(format="4D damage", base_difficulty=12, count=1),
        duration=Aspect(format="3 rounds", base_difficulty=6, count=1),
        range=Aspect(format="15m", base_difficulty=6, count=1),
        speed=Aspect(format="Instant", base_difficulty=6, count=1),
        casting_time=Aspect(format="1 round", base_difficulty=-4, count=1),
        name="Water Spray",
        other_aspects={
            "Components": Aspect(
                format="Liter of water (ordinary, destroyed), squeezable container (uncommon)",
                base_difficulty=-6,
                count=1,
            )
        },
        other_conditions=[],
        notes=[
            "The mage needs a liter of water in a container that she can squeeze to produce a spray. As she casts the spell, the mage squirts the water onto her hand, letting it run off in the direction of her target. The volume and force behind the water spray increases dramatically. The spray lasts for three rounds of combat. The spell does 4D in damage per round and requires a marksmanship roll each round to hit the target. The caster may only select one target per spell duration."
        ],
        skill="Alteration",
    ),
]

apportation_spells = [
    Spell(
        effect=Aspect(format="1 meter per round", base_difficulty=4, count=1),
        duration=Aspect(format="4 min", base_difficulty=12, count=1),
        range=Aspect(format="25m", base_difficulty=7, count=1),
        speed=Aspect(format="Instant", base_difficulty=7, count=1),
        casting_time=Aspect(format="1 round", base_difficulty=-4, count=1),
        name="Alter Movement",
        other_aspects={
            "Focused": Aspect(format="On target", base_difficulty=2, count=1),
            "Gesture": Aspect(
                format="Point at target, then make running motion with fingers (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantation": Aspect(
                format="First say, “I command your speed,” followed by whether the target should slow or quicken (sentence)",
                base_difficulty=-2,
                count=1,
            ),
            "Variable Effect": Aspect(
                format="Caster may increase effect’s value by up to 5 points on the “Spell Measures” chart",
                base_difficulty=5,
                count=1,
            ),
            "Other Alterant": Aspect(
                format="At time of casting, mage may choose to speed up or slow down target (small)",
                base_difficulty=1,
                count=1,
            ),
        },
        other_conditions=[],
        notes=[
            "The caster makes her target either hurry up or slow down, depending on how she words her command. The target’s movement is altered by the measure of the spell effect’s value plus any result points bonus (as read on the “Spell Measures” chart).",
            "**Example**",
            "A magic user casts the alter movement spell to slow down a charging bull. At casting time, he decided to use the spell effect’s value plus the full variable amount, for a minimum change value of 9, or 60 meters per second (12 meters per round). If his skill total was one point over the difficulty, the new change value would be 10, or 100 meters per second (10 meters per round). This rate would then be subtracted from the bull’s current movement rate, causing the raging animal to come to a complete and shockingly sudden stop.",
        ],
        skill="Apportation",
    ),
    Spell(
        effect=Aspect(format="wind with a lifting of 5D", base_difficulty=15, count=1),
        duration=Aspect(format="1hr", base_difficulty=18, count=1),
        range=Aspect(format="Self", base_difficulty=0, count=1),
        speed=Aspect(format="Instant", base_difficulty=0, count=1),
        casting_time=Aspect(format="1hr", base_difficulty=-18, count=1),
        name="Carrying Wind",
        other_aspects={
            "Area Effect": Aspect(format="3-meter sphere", base_difficulty=15, count=1),
            "Charges": Aspect(format="6 charges", base_difficulty=4, count=1),
            "Component": Aspect(
                format="May only be cast outdoors, in a clear area (ordinary), mage wears loose clothes (common)",
                base_difficulty=-4,
                count=1,
            ),
            "Feedback": Aspect(format="points of damage", base_difficulty=-8, count=1),
            "Gesture": Aspect(
                format="Mimic a fight (fairly simple)", base_difficulty=-2, count=1
            ),
            "Incantation": Aspect(
                format="“I subdue you and I command you, O wind!” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
            "Variable Movement": Aspect(
                format="25 meters per second", base_difficulty=7, count=1
            ),
        },
        other_conditions=[],
        notes=[
            "This is a charged spell. To cast it, the mage goes outside and starts running, jumping, and mimicking flight. The mage should be wearing something loose that can catch the wind. One cast garners the mage six charges of the spell.",
            "When released, the spell causes a wind to rise and lifts the mage into the air. The mage can control the direction of the wind and its speed (up to 25 meters a round). The spell can carry as if it had a lifting of 5D.",
            "The wind forms a three-meter sphere around the mage’s body, and nothing can be carried that won’t fit in that sphere.",
        ],
        skill="Apportation",
    ),
    Spell(
        effect=Aspect(
            format="passage can handle up to 150 kg.", base_difficulty=11, count=1
        ),
        duration=Aspect(format="2 rounds", base_difficulty=5, count=1),
        range=Aspect(format="100 km", base_difficulty=25, count=1),
        speed=Aspect(format="Instant", base_difficulty=25, count=1),
        casting_time=Aspect(format="2.75 hr", base_difficulty=-20, count=1),
        name="Doorway Home",
        other_aspects={
            "Charges": Aspect(format="3 charges", base_difficulty=2, count=1),
            "Components": Aspect(
                format="Something from the location (ordinary, destroyed)",
                base_difficulty=-2,
                count=1,
            ),
            "Concentration": Aspect(
                format="40 minutes with willpower difficulty of 12",
                base_difficulty=-6,
                count=1,
            ),
            "Incantations": Aspect(
                "A statement describing the place (sentence)", base_difficulty=-2
            ),
            "Gestures": Aspect(
                format="Pantomime building a doorway (complex; artist roll with difficulty of 11)",
                base_difficulty=-3,
                count=1,
            ),
        },
        other_conditions=[],
        notes=[
            "After the mage casts the spell, she has firmly fixed in her mind three uses of it. When she releases the spell, she opens a doorway in front of her through which she may step through and instantly be transported somewhere else. The points the skill total is above the difficulty may be added to the effect’s value (thus increasing the amount that can travel through the doorway). An unbreakable barrier over the doorway resists weight of a greater amount than what the spell can handle to go through the doorway. The doorway remains open for two rounds, allowing up to two passages of material weighing no more than 150 kilograms."
        ],
        skill="Apportation",
    ),
    Spell(
        effect=Aspect(
            format="teleport up to 150 kilograms", base_difficulty=11, count=1
        ),
        duration=Aspect(format="1.5r", base_difficulty=1, count=1),
        range=Aspect(format="100 m", base_difficulty=10, count=1),
        speed=Aspect(format="Instant", base_difficulty=10, count=1),
        casting_time=Aspect(format="1r", base_difficulty=-4, count=1),
        name="Relocate Person",
        other_aspects={
            "Charges": Aspect(format="3 charges", base_difficulty=2, count=1),
            "Gesture": Aspect(
                format="Point to target then point in direction of new location (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantation": Aspect(
                format="“Go there.” (one or two words)", base_difficulty=-1, count=1
            ),
        },
        other_conditions=[],
        notes=[
            "After the mage casts the spell, she has firmly fixed in her mind three uses of it. When she releases the spell, she points at her intended target, which will be instantly teleported to the range of the spell. The result points bonus may be added either to the value of the weight transported or the distance traveled; read the new value on the “Spell Measures” chart. The spell will not allow anything to appear inside a solid object. Remember that a target who is aware of the potential relocation may roll her Physique or lifting and add it to her weight. The caster’s spell roll must then beat that difficulty as well as the spell’s difficulty.",
            "**Note**",
            "A similar spell, Relocate Item, is identical in every way except that the effect is to carry an item weighing no more than 10 kilograms, with a value of 5, and thus the difficulty is 11.",
        ],
        skill="Apportation",
    ),
    Spell(
        effect=Aspect(
            format="move an object of up to 10 kilograms", base_difficulty=5, count=1
        ),
        duration=Aspect(format="2.5sec", base_difficulty=2, count=1),
        range=Aspect(format="1 km", base_difficulty=15, count=1),
        speed=Aspect(format="Instant", base_difficulty=15, count=1),
        casting_time=Aspect(format="1 round", base_difficulty=-4, count=1),
        name="Retrieve",
        other_aspects={
            "Gesture": Aspect(
                format="Stand on tiptoes, point out to imaginary objects and then reach to pick them up. (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantation": Aspect(
                format="“I want to reach out beyond the boundaries of the time and space. I want that object to return with me.” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="May only be cast in conjunction with view (spell described herein)",
                base_difficulty=-5,
                count=1,
            ),
        ],
        notes=[
            "Through the use of this spell, the caster can target something he’s seen through a view spell and bring it to his current location (assuming he’s no more than one kilometer from the object). The object can weigh no more than the effect’s value (including bonuses) as read on the “Spell Measures” table."
        ],
        skill="Apportation",
    ),
]

conjuration_spells = [
    Spell(
        effect=Aspect(format="Bad Luck (R2) Disadvantage", base_difficulty=6, count=1),
        duration=Aspect(format="10 min", base_difficulty=14, count=1),
        range=Aspect(format="10m", base_difficulty=5, count=1),
        speed=Aspect(format="Instant", base_difficulty=5, count=1),
        casting_time=Aspect(format="2 rounds", base_difficulty=-5, count=1),
        name="Bad Luck Curse",
        other_aspects={
            "Focused": Aspect(format="On target", base_difficulty=4, count=1),
            "Feedback": Aspect(
                format="-3 to damage resistance total", base_difficulty=-3, count=1
            ),
            "Concentration": Aspect(
                format="1 round with willpower difficulty of 8",
                base_difficulty=-2,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(format="Limited to Humans", base_difficulty=-3, count=1),
        ],
        notes=[
            "With a minimal amount of pain to himself, the caster curses a Human target with 10 minutes of Bad Luck (R2). See the description of this Disadvantage in the “Character Options” chapter for details."
        ],
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="resistance total of bars", base_difficulty=25, count=1),
        duration=Aspect(format="1 hr", base_difficulty=18, count=1),
        range=Aspect(format="25m", base_difficulty=7, count=1),
        speed=Aspect(format="Instant", base_difficulty=7, count=1),
        casting_time=Aspect(format="1 min", base_difficulty=-9, count=1),
        name="Cage",
        other_aspects={
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
        notes=[
            "Cage traps a target in a prison of magical energy. To cast it, the wizard mimics trying to escape from a cell, then points at her target. If a marksmanship total beats the combat difficulty for the target, the quarry is trapped. The cage is a sphere with a radius of three meters. Creatures larger than that can’t be confined by this spell.",
            "The effect’s value plus the result points bonus serves as the damage resistance total of the bars. The target can disbelieve and thus free himself by generating a Acumen or investigation total of 13.",
        ],
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="speaking skill with specialization in the animal’s “language” at 5D",
            base_difficulty=15,
            count=1,
        ),
        duration=Aspect(format="6 min", base_difficulty=13, count=1),
        range=Aspect(format="1 m", base_difficulty=0, count=1),
        speed=Aspect(format="Instant", base_difficulty=0, count=1),
        casting_time=Aspect(format="1r", base_difficulty=-4, count=1),
        name="Communicate with Animals",
        other_aspects={
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
        notes=[
            "To communicate with an animal, the caster places on the ground the bit of something from that type of animal (lock of horse’s hair, bird’s feather, several strands of dog’s hair). Then she draws a line from it to her and from it in the direction of the animal or animals she wishes to speak to. For about six minutes, she receives the ability to communicate with any of that kind of animal as if she had a specialization in its language at 5D. She may add the result points bonus to her speaking roll total. The caster may not move more than one meter from the casting location."
        ],
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="search difficulty of 20 and image transfer of 2.5 meters",
            base_difficulty=22,
            count=1,
        ),
        duration=Aspect(format="100 sec", base_difficulty=10, count=1),
        range=Aspect(format="Self or touch", base_difficulty=0, count=1),
        speed=Aspect(format="Instant", base_difficulty=0, count=1),
        casting_time=Aspect(format="1r", base_difficulty=-4, count=1),
        name="Displacement",
        other_aspects={
            "Gesture": Aspect(
                format="Turn around and then start hopping from one location to another, while looking back at previous spot before jumping again (complex; acrobatics roll with difficulty of 11)",
                base_difficulty=-3,
                count=1,
            ),
            "Incantation": Aspect(
                format="“Hide my true location from sight.” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        other_conditions=[],
        notes=[
            "By bending the light around the target, an image of the person or thing is transferred up to 2.5 meters away from his actual location. He becomes invisible to normal sight at his true location, and his image appears and copies all of his movements and actions until the end of the duration. A character must beat a difficulty of 20 with a Perception or search roll or a location spell to find the displaced target.",
            "Anyone touching the image recognizes it for what it really is. This does not give them the ability to see where the target is standing. Any area effect attacks and spells will hit the target should he be in the radius. Otherwise, only using items or other spells discloses the true location of the target.",
        ],
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="Bad Luck (R2) Disadvantage", base_difficulty=6, count=1),
        duration=Aspect(format="10 min", base_difficulty=14, count=1),
        range=Aspect(format="10 m", base_difficulty=5, count=1),
        speed=Aspect(format="Instant", base_difficulty=5, count=1),
        casting_time=Aspect(format="2 rounds", base_difficulty=-5, count=1),
        name="Evil Eye Curse",
        other_aspects={
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
        notes=[
            "With a minimal amount of pain to himself, the caster curses a Human target that she can see with 10 minutes of Bad Luck (R2). See the description of this Disadvantage in the “Character Options” chapter for details."
        ],
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="5 kilograms of food and water", base_difficulty=4, count=1
        ),
        duration=Aspect(format="4 hr", base_difficulty=21, count=1),
        range=Aspect(format="1 m", base_difficulty=0, count=1),
        speed=Aspect(format="Instant", base_difficulty=0, count=1),
        casting_time=Aspect(format="1r", base_difficulty=-4, count=1),
        name="Feast",
        other_aspects={
            "Focused": Aspect(
                format="On people who eat food", base_difficulty=4, count=1
            ),
            "Components": Aspect(
                format="A plain, cloth napkin (common), a small metal cup (common)",
                base_difficulty=-6,
                count=1,
            ),
            "Gesture": Aspect(
                format="Wave hand several times over napkin and cup (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Other Alterants": Aspect(
                format="clean water and hearty food", base_difficulty=3
            ),
        },
        other_conditions=[],
        notes=[
            "With this cantrip, the mage creates a meal for two of pure, clean water; flavorful, hearty bread; fresh vegetables and fruits; and, if desired, cheese wedges and smoked meat slices. The food must be consumed within 10 minutes of its appearance, so that it has a chance to stay in the body long enough to be digested and actually provide nourishment. The result points bonus increases the amount of food appearing or (at the gamemaster’s discretion) the quality of food.",
        ],
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="Flight (R1) Special Ability plus the flying skill at +1D",
            base_difficulty=23,
            count=1,
        ),
        duration=Aspect(format="10 min", base_difficulty=14, count=1),
        range=Aspect(format="Touch", base_difficulty=0, count=1),
        speed=Aspect(format="Immediate", base_difficulty=0, count=1),
        casting_time=Aspect(format="3r", base_difficulty=-6, count=1),
        name="Flight",
        other_aspects={
            "Concentration": Aspect(
                format="One round with willpower difficulty of 8",
                base_difficulty=-2,
                count=1,
            ),
            "Component": Aspect(
                format="Bird’s feather (very common)", base_difficulty=-2, count=1
            ),
            "Focused": Aspect(format="On target", base_difficulty=7, count=1),
            "Gesture": Aspect(
                format="Point at target (simple)", base_difficulty=-1, count=1
            ),
            "Incantation": Aspect(
                format="“Fly!” (a few words)", base_difficulty=-1, count=1
            ),
        },
        other_conditions=[],
        notes=[
            "This spell provides the target, who must be within one meter of the caster, the ability to fly and the knowledge to use it for 10 minutes. There is no visible means of convenience; the target can simply move through the air by force of will. The rate equals twice the target’s normal movement rate."
        ],
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="negates up to -4D of darkness modifier", base_difficulty=12, count=1
        ),
        duration=Aspect(format="10 min", base_difficulty=14, count=1),
        range=Aspect(format="Touch", base_difficulty=0, count=1),
        speed=Aspect(format="Instant", base_difficulty=0, count=1),
        casting_time=Aspect(format="2r", base_difficulty=-5, count=1),
        name="Glow Stone",
        other_aspects={
            "Area Effect": Aspect(
                format="Sphere with radius of one meter", base_difficulty=5, count=1
            ),
            "Components": Aspect(
                format="white pebble (common, destroyed)", base_difficulty=-4, count=1
            ),
            "Focused": Aspect(format="On pebble", base_difficulty=5, count=1),
            "Gesture": Aspect(
                format="Hold pebble between thumb and forefinger (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Incantation": Aspect(
                format="“Stone of white, give us light.” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        other_conditions=[],
        notes=[
            "The magic user casts this spell on a small, white stone, making it glow with a fierce radiance that extends for one meter in all directions around the pebble. The effect lasts for 10 minutes. Once the duration wears off, the pebble turns to dust."
        ],
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="telekinesis skill at 4D+1", base_difficulty=13, count=1),
        duration=Aspect(format="5 rounds", base_difficulty=7, count=1),
        range=Aspect(format="1m", base_difficulty=0, count=1),
        speed=Aspect(format="Instant", base_difficulty=0, count=1),
        casting_time=Aspect(format="1r", base_difficulty=-4, count=1),
        name="Helping Hand",
        other_aspects={
            "Focused": Aspect(format="On the caster", base_difficulty=4, count=1)
        },
        other_conditions=[],
        notes=[
            "The caster can move items without touching them, as if he had the Psionics telekinesis skill at 4D+1. See the description of the telekinesis skill in the “Psionics” chapter for difficulties and ranges."
        ],
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="negates up to 4D of darkness modifier", base_difficulty=12, count=1
        ),
        duration=Aspect(format="10 min", base_difficulty=14, count=1),
        range=Aspect(format="Touch", base_difficulty=0, count=1),
        speed=Aspect(format="Instant", base_difficulty=0, count=1),
        casting_time=Aspect(format="2 rounds", base_difficulty=-5, count=1),
        name="Light",
        other_aspects={
            "Area Effect": Aspect(
                format="Sphere with radius of one meter", base_difficulty=5, count=1
            ),
            "Components": Aspect(
                format="white pebble (common, destroyed)", base_difficulty=-4, count=1
            ),
            "Focused": Aspect(format="On pebble", base_difficulty=5, count=1),
            "Gestures": Aspect(
                format="Hold pebble between thumb and forefinger (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Stone of white, give us light.” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        other_conditions=[],
        notes=[
            "The magic user casts this spell on a small, white stone, making it glow with a fierce radiance that extends for one meter in all directions around the pebble. The effect lasts for 10 minutes. Once the duration wears off, the pebble turns to dust."
        ],
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="4D in damage", base_difficulty=12, count=1),
        duration=Aspect(format="1D", base_difficulty=3, count=1),
        range=Aspect(format="10 m", base_difficulty=5, count=1),
        speed=Aspect(format="Instant", base_difficulty=5, count=1),
        casting_time=Aspect(format="1.5s", base_difficulty=-1, count=1),
        name="Mystic Bolt",
        other_aspects={
            "Gesture": Aspect(
                format="Swirl hand in air as if gathering energy, then throw it at target (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantation": Aspect(
                format="“Ah!” (word, said loudly)", base_difficulty=-2, count=1
            ),
        },
        other_conditions=[],
        notes=[
            "The mage gathers energy from his surroundings and throws the ball at a target. It does 4D in damage at a range of up to 10 meters. He must make a marksmanship roll to hit the target. The bolt must be fired in the same round that the mage casts the spell."
        ],
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="Armor Value of 6D", base_difficulty=18, count=1),
        duration=Aspect(format="5r", base_difficulty=7, count=1),
        range=Aspect(format="1.5m", base_difficulty=1, count=1),
        speed=Aspect(format="Instant", base_difficulty=1, count=1),
        casting_time=Aspect(format="1.5sec", base_difficulty=-1, count=1),
        name="Mystical Shield",
        other_aspects={
            "Area effect": Aspect(
                format="One-meter radius", base_difficulty=2, count=1
            ),
            "Components": Aspect(
                format="A simple ring (uncommon), handful of colored sand (common, destroyed)",
                base_difficulty=-10,
                count=1,
            ),
            "Focused": Aspect(format="On ring", base_difficulty=5, count=1),
            "Gesture": Aspect(
                format="Using colored sand, scribe an oval shape in the air (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantation": Aspect(
                format="“Protection!” (word)", base_difficulty=-1, count=1
            ),
        },
        other_conditions=[],
        notes=[
            "By tossing some sand in a circle in front of her, the caster creates a semi-transparent oval shield of the same color as the sand. The shield, about two meters in diameter, appears up to 1.5 meters away. It is focused on the ring, which the mage must wear. It offers an Armor Value of 6D against all types of physical (not mental) attacks."
        ],
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="6D+2 stun damage", base_difficulty=15, count=1),
        duration=Aspect(format="1.5sec", base_difficulty=3, count=1),
        range=Aspect(format="10m", base_difficulty=5, count=1),
        speed=Aspect(format="Instant", base_difficulty=5, count=1),
        casting_time=Aspect(format="1.5sec", base_difficulty=-1, count=1),
        name="Stunned Senseless",
        other_aspects={
            "Gesture": Aspect(
                format="Point finger and then palm at intended target (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantation": Aspect(format="“Stop!” (word)", base_difficulty=-1, count=1),
        },
        other_conditions=[],
        notes=[
            "With a gesture and a word, the magic user sends a bolt of mystical energy toward his intended target. However, the bolt isn’t intended to harm the target, instead only doing stun damage."
        ],
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="Hindrance (R2) Disadvantage", base_difficulty=6, count=1),
        duration=Aspect(format="10 min", base_difficulty=14, count=1),
        range=Aspect(format="1km", base_difficulty=10, count=1),
        speed=Aspect(format="Instant", base_difficulty=10, count=1),
        casting_time=Aspect(format="2r", base_difficulty=-5, count=1),
        name="Voodoo Curse",
        other_aspects={
            "Components": Aspect(
                format="Scrap from clothing target wore recently or lock of hair (very rare); doll in the shape of Human (common); several large, thick pins (common)",
                base_difficulty=-11,
                count=1,
            ),
            "Concentration": Aspect(
                format="1 round with willpower difficulty of 8",
                base_difficulty=-2,
                count=1,
            ),
            "Incantation": Aspect(
                format="Description of what caster wants the target to feel (complete sentence)",
                base_difficulty=-2,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=4, count=1),
        },
        other_conditions=[],
        notes=[
            "With a few simple items and a spell inspired by the rites of the vodun religion, the caster can cause great pain to his target. First the caster attaches the scrap of clothing or the lock of hair to the doll. Then, while placing pins in appropriate places, the caster describes the kind of pain he desires his target to feel. For 10 minutes after the completion of the spell, the target receives a +2 difficulty modifier to the caster’s choice of any three skills."
        ],
        skill="Conjuration",
    ),
]

divination_spells = [
    Spell(
        effect=Aspect(
            format="search of 8D to locate a single type of creature",
            base_difficulty=24,
            count=1,
        ),
        duration=Aspect(format="10 sec", base_difficulty=5, count=1),
        range=Aspect(format="Self", base_difficulty=0, count=1),
        speed=Aspect(format="Instant", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 min", base_difficulty=-9, count=1),
        name="Detect the Living",
        other_aspects={
            "Area effect": Aspect(
                format="10-meter radius circle", base_difficulty=20, count=1
            ),
            "Component": Aspect(
                format="Something from the type of creature being detected (uncommon, destroyed); fire, such as a match or lit coal (very common, destroyed)",
                base_difficulty=-12,
                count=1,
            ),
            "Concentration": Aspect(
                format="25 seconds with a mettle difficulty of 9",
                base_difficulty=-3,
                count=1,
            ),
            "Gesture": Aspect(
                format="Inhale smoke (simple)", base_difficulty=-1, count=1
            ),
            "Variable Movement": Aspect(
                format="Bending (can’t see target)", base_difficulty=4, count=1
            ),
        },
        other_conditions=[],
        notes=[
            "Before throwing the spell, the caster should decide what sort of being she’s looking for, because she’ll need a piece of it for the spell to work (a lock of hair from a Human, fur or fangs from an animal, etc.).",
            "The caster sets the object on fire and inhales the smoke while concentrating. Once the casting is done, the mage can detect the presence of any such being within a 10-meter radius for two rounds. The higher the search skill total is above the difficulty, the more information the caster knows about the beings she seeks (such as location, number, gender, etc.). The difficulty starts at 10 for a Human-sized creature, and goes down for larger creatures, up for smaller ones, and up for the number of other types of creatures in the area.",
        ],
        skill="Divination",
    ),
    Spell(
        effect=Aspect(format="2.5 months", base_difficulty=34, count=1),
        duration=Aspect(format="1 min", base_difficulty=9, count=1),
        range=Aspect(format="Scrying object", base_difficulty=0, count=1),
        speed=Aspect(format="Instant", base_difficulty=0, count=1),
        casting_time=Aspect(format="2 rounds", base_difficulty=-5, count=1),
        name="Scrying",
        other_aspects={
            "Components": Aspect(
                format="Scrying tool with images or symbols (tarot cards, playing cards, runes, etc. ) (uncommon); item the person owned for at least a month or the person herself (very rare)",
                base_difficulty=-9,
                count=1,
            ),
            "Gesture": Aspect(
                format="Randomize the tool and place parts of the tool in a set pattern (fairly simple); interpret the symbols (very complex, scholar difficulty of 15)",
                base_difficulty=-6,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(format="Physical contact with tool", base_difficulty=-1, count=1),
        ],
        notes=[
            "By interpreting cards or runes, the diviner gains a sense of what the future holds for the person who the reading is about. The mage may choose to look for a condition that could occur up to two and a half months into the future. She can see one minute’s worth of the future. Use the result points of the divination roll to determine how much information she receives: Zero points reveals confusing images. One to four points allows one useful fact to be gleaned from the reading. Five to eight points tells the mage a few useful facts, including the time of the occurrence. Nine to 12 points allows the mage to note more details, including time and location. Thirteen or more points lets the mage see the scene as if she were present, though in shades of gray.",
        ],
        skill="Divination",
    ),
    Spell(
        effect=Aspect(format="66 weeks in past", base_difficulty=38, count=1),
        duration=Aspect(format="66 min", base_difficulty=18, count=1),
        range=Aspect(format="Touch", base_difficulty=0, count=1),
        speed=Aspect(format="Instant", base_difficulty=0, count=1),
        casting_time=Aspect(format="25 min", base_difficulty=-16, count=1),
        name="Sense Past",
        other_aspects={
            "Area effect": Aspect(
                format="Sphere with radius of 5 meters", base_difficulty=25, count=1
            ),
            "Concentration": Aspect(
                format="10 minutes with a mettle difficulty of 11",
                base_difficulty=-5,
                count=1,
            ),
            "Components": Aspect(
                format="Magnifying glass (uncommon), expensive pocket watch (very rare)",
                base_difficulty=-9,
                count=1,
            ),
            "Countenance": Aspect(
                format="Skin turns sickly gray color for duration of spell",
                base_difficulty=-1,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(format="Physical contact with object", base_difficulty=-1, count=1),
        ],
        notes=[
            "The mage can learn about the past of a single object he touches. He’ll see visions of events that occurred in a five-meter radius around the object in the past. The mage can view events that took place in a past period of time whose value (as read on the “Spell Measures” table) is less than or equal to the effect’s value plus the result points bonus. The mage can scan back to that period at a rate of one week’s worth of images per minute of the spell."
        ],
        skill="Divination",
    ),
    Spell(
        effect=Aspect(format="search skill of 3D", base_difficulty=9, count=1),
        duration=Aspect(format="10 min", base_difficulty=14, count=1),
        range=Aspect(format="1 km", base_difficulty=15, count=1),
        speed=Aspect(format="Instant", base_difficulty=15, count=1),
        casting_time=Aspect(format="1 min", base_difficulty=-9, count=1),
        name="View",
        other_aspects={
            "Feedback": Aspect(
                format="-3 to damage resistance total", base_difficulty=-3, count=1
            ),
            "Gesture": Aspect(
                format="Make swimming gestures with hands (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantation": Aspect(
                format="“Let me see beyond what I know to be.” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        other_conditions=[],
        notes=[
            "The caster opens a tunnel of sorts in space. Nothing may pass through it, but the caster may look through it to the other end. The tunnel starts with a range of one kilometer. This range is determined by the range value of the spell, and can be much longer, depending on the success the caster has throwing the spell. Any bonus from casting goes to both range and speed, being split evenly between them. (To determine the bonus, subtract the skill total from the spell difficulty. Divide by 2, and round up. Add this number to the range and look up the new value on the “Spell Measures” table.)",
            "The effect of the spell takes the place of the character’s search while using the spell, as it is hard to make out minute details.",
        ],
        skill="Divination",
    ),
]
#
# def main():
#     writer = SpellWriter()
#
#     print("Cantrips")
#     print("========")
#     print()
#
#     for spell in cantrips:
#         print(writer.report(spell))
#
#     print("Alteration Spells")
#     print("=================")
#     print()
#
#     for spell in alteration_spells:
#         print(writer.report(spell))
#
#     print("Apportation Spells")
#     print("==================")
#     print()
#
#     for spell in apportation_spells:
#         print(writer.report(spell))
#
#     print("Conjuration Spells")
#     print("==================")
#     print()
#
#     for spell in conjuration_spells:
#         print(writer.report(spell))
#
#     print("Divination Spells")
#     print("=================")
#     print()
#
#     for spell in divination_spells:
#         print(writer.report(spell))

if __name__ == "__main__":
    books = {
        "Cantrips": cantrips,
        "Alteration Spells": alteration_spells,
        "Apportation Spells": apportation_spells,
        "Conjuration Spells": conjuration_spells,
        "Divination Spells": divination_spells,
    }
    detail(books, section_heading="-", spell_heading="~")

__test__ = {
    "Aid": ">>> cantrips[0].difficulty\n5",
    "Charm": ">>> cantrips[1].difficulty\n5",
    "Heighten Attribute (Template)": ">>> cantrips[2].difficulty\n3",
    "Meal": ">>> cantrips[3].difficulty\n4",
    "Open Lock": ">>> cantrips[4].difficulty\n5",
    "Countermagic": ">>> alteration_spells[0].difficulty\n19",
    "Countermagic Ward": ">>> alteration_spells[1].difficulty\n11",
    "Deadly Bullet": ">>> alteration_spells[2].difficulty\n10",
    "Deadly Dart": ">>> alteration_spells[3].difficulty\n11",
    "Drain Toughness": ">>> alteration_spells[4].difficulty\n12",
    "Fear": ">>> alteration_spells[5].difficulty\n19",
    "Water Spray": ">>> alteration_spells[6].difficulty\n10",
    "Alter Movement": ">>> apportation_spells[0].difficulty\n15",
    "Carrying Wind": ">>> apportation_spells[1].difficulty\n13",
    "Doorway Home": ">>> apportation_spells[2].difficulty\n18",
    "Relocate Person": ">>> apportation_spells[3].difficulty\n14",
    "Retrieve": ">>> apportation_spells[4].difficulty\n12",
    "Bad Luck Curse": ">>> conjuration_spells[0].difficulty\n11",
    "Cage": ">>> conjuration_spells[1].difficulty\n27",
    "Communicate with Animals": ">>> conjuration_spells[2].difficulty\n10",
    "Displacement": ">>> conjuration_spells[3].difficulty\n12",
    "Evil Eye Curse": ">>> conjuration_spells[4].difficulty\n11",
    "Feast": ">>> conjuration_spells[5].difficulty\n10",
    "Flight": ">>> conjuration_spells[6].difficulty\n16",
    "Glow Stone": ">>> conjuration_spells[7].difficulty\n12",
    "Helping Hand": ">>> conjuration_spells[8].difficulty\n10",  # Given as 18 in source site
    "Light": ">>> conjuration_spells[9].difficulty\n12",
    "Mystic Bolt": ">>> conjuration_spells[10].difficulty\n10",
    "Mystical Shield": ">>> conjuration_spells[11].difficulty\n10",
    "Stunned Senseless": ">>> conjuration_spells[12].difficulty\n12",
    "Voodoo Curse": ">>> conjuration_spells[13].difficulty\n12",
    "Detect the Living": ">>> divination_spells[0].difficulty\n14",
    "Scrying": ">>> divination_spells[1].difficulty\n11",
    "Sense Past": ">>> divination_spells[2].difficulty\n25",
    "View": ">>> divination_spells[3].difficulty\n19",
}
