"""
OpenD6 System Book Spells

When run as an app, generates .RST details of each Spell.
"""

import textwrap
from magic1 import Aspect, Spell, summary, detail

spells = [
    Spell(
        name="Cast Chaos",
        effect=Aspect(format="Spell being copied plus backlash", base_difficulty=30),
        speed=Aspect(format="Spell being copied"),
        range=Aspect(format="Spell being copied"),
        duration=Aspect(format="Spell being copied"),
        casting_time=Aspect(format="Instant", base_difficulty=0, count=1),
        other_aspects={
            "Area Effect": Aspect(format="Spell being copied"),
            "Feedback": Aspect(format="Backlash", base_difficulty=-10, count=1),
        },
        other_conditions=[
            Aspect(format="can unleash chaos effect on failure"),
        ],
        notes=textwrap.dedent("""\
            The caster can unleash pure chaotic energy  in an attempt
            to simulate a spell. The incantation is cast at a
            difficulty of 10 plus the simulated spell's difficulty,
            and automatically triggers a chaotic backlash (the GM
            rolls on the Unleashed Chaos Table). If the caster fails
            the difficulty roll, the GM rolls a second time on the
            Unleashed Chaos Table. The simulated spell is treated
            just as if it had been cast normally (using it's speed,
            range, area of effect, and duration.)
        """),
        skill="Conjuration",
    ),
    Spell(
        name="Chaos Burst",
        # Difficulty 15
        effect=Aspect(format="4D Damage, 3 charges", base_difficulty=12),
        speed=Aspect(format="2.5 sec", base_difficulty=-5),
        range=Aspect(format="30m", base_difficulty=7),
        duration=Aspect(format="Instant", base_difficulty=0),
        casting_time=Aspect(format="5 sec", base_difficulty=4, count=1),
        other_aspects={
            "Concentration": Aspect(format="On Target", base_difficulty=-4),
            "Gestures": Aspect(format="Complex", base_difficulty=-3),
            "Incantation": Aspect(format="Complex", base_difficulty=-3),
            "Charges": Aspect(format="3 charges", base_difficulty=-3),
            "Feedback": Aspect(format="Backlash", base_difficulty=-10, count=1),
        },
        other_conditions=[
            Aspect(format="can unleash chaos effect on failure"),
        ],
        notes=textwrap.dedent("""\
            At the casting of this spell, three bolts of swirling energy
            erupt from the caster's fingertips and streak toward
            one target. The spell user must make an attack
            roll for each bolt, but it is treated as a single action.
            Each bolt causes 4D damage. The caster then rolls
            once on the Unleashed Chaos Table, regardless of his
            success in hitting the target.
        """),
        skill="Conjuration",
    ),
    Spell(
        name="Chaos Web",
        # Difficulty 17
        effect=Aspect(
            format="touch: 3D Damage + backlash, attack: backlash",
            base_difficulty=29,
            count=1,
        ),
        speed=Aspect(format="Instant", base_difficulty=-7),
        range=Aspect(format="20m", base_difficulty=7),
        duration=Aspect(format="30 min", base_difficulty=8),
        casting_time=Aspect(format="5 sec", base_difficulty=4, count=1),
        other_aspects={
            "Area Effect": Aspect(format="Between two anchors", base_difficulty=3),
            "Concentration": Aspect(format="On Target", base_difficulty=-4),
            "Gestures": Aspect(format="Complex", base_difficulty=-3),
            "Incantation": Aspect(format="Complex", base_difficulty=-3),
        },
        other_conditions=[
            Aspect(format="can unleash chaos effect on failure"),
        ],
        notes=textwrap.dedent("""\
            This chaos binding creates hundreds of strands of
            chaotic fiber that interweave themselves into a web
            of magical energy. The spell user must anchor the web
            between at least two objects. Anyone touching the
            web with bare flesh automatically takes 3D damage
            (once per contact) and causes a chaotic backlash (roll
            once on the Unleashed Chaos Table). Any attack on
            the web results in an additional chaotic backlash
            When the spell ends, the fibers quickly break down
            and fade away, their innate chaos expunged. Note that
            the caster is not immune to the effects of the web.
        """),
        skill="Conjuration",
    ),
    Spell(
        name="Contain Chaos",
        # Difficulty 20
        effect=Aspect(format="Other spell's effect", base_difficulty=40, count=1),
        speed=Aspect(format="Instant", base_difficulty=-8),
        range=Aspect(format="40m", base_difficulty=8),
        duration=Aspect(format="Instant", base_difficulty=0),
        casting_time=Aspect(format="10 sec", base_difficulty=5, count=1),
        other_aspects={
            "Concentration": Aspect(format="On Target", base_difficulty=-4),
            "Gestures": Aspect(format="Complex", base_difficulty=-3),
            "Incantation": Aspect(format="Complex", base_difficulty=-3),
        },
        other_conditions=[
            Aspect(format="can unleash chaos effect on failure"),
            Aspect(format="within 2 rounds of chaotic backlash"),
        ],
        notes=textwrap.dedent("""\
            If cast within 10 seconds after a chaotic backlash, the
            spell user may capture the energy created by the temporary
            flux in the chaos stream. The spellcaster may
            then recast the enchantment that caused the backlash
            even if he could not originally cast it.
        """),
        skill="Alteration",
    ),
    Spell(
        name="Drain",
        # Difficulty 18
        # 1 character point == 1D == difficulty 3, multiplier of 3 for extranormal
        effect=Aspect(
            format="Drain 1 character point; 2D increase",
            base_difficulty=(3 * 3 + 2 * 3 * 3),
            count=1,
        ),
        speed=Aspect(format="Instant", base_difficulty=0),
        range=Aspect(format="Touch", base_difficulty=0),
        duration=Aspect(format="5 min", base_difficulty=12),
        casting_time=Aspect(format="25 sec", base_difficulty=-7, count=1),
        other_aspects={
            "Concentration": Aspect(format="On Target", base_difficulty=-4),
            "Gestures": Aspect(format="Complex", base_difficulty=-3),
            "Incantation": Aspect(format="Complex", base_difficulty=-3),
        },
        other_conditions=[
            Aspect(format="can unleash chaos effect on failure"),
        ],
        notes=textwrap.dedent("""\
            The caster may steal a Character Point from her target
            and use the power to temporarily increase her
            ability to cast her next spell (receiving a 2D bonus to
            her spell skill roll against it's difficulty.) Note that the
            bonus applies only to the next spell cast by the spell
            user. The victim of the incantation feels a dull pain in
            his chest when the Character Point is sucked away. If
            the target has no Character Points, he still feels the ache,
            but the caster does not gain any benefit.
        """),
        skill="Alteration",
    ),
    Spell(
        name="Flash",
        # Difficulty 10
        effect=Aspect(format="Blindness, -2D to vision", base_difficulty=6, count=1),
        speed=Aspect(format="Instant", base_difficulty=0),
        range=Aspect(format="1m", base_difficulty=0),
        duration=Aspect(format="10 seconds", base_difficulty=5),
        casting_time=Aspect(format="5 sec", base_difficulty=4, count=1),
        other_aspects={
            "Area Effect": Aspect(format="6m sphere", base_difficulty=5, count=6),
            "Concentration": Aspect(format="On Target", base_difficulty=-4),
            "Gestures": Aspect(format="Complex", base_difficulty=-3),
            "Incantation": Aspect(format="Complex", base_difficulty=-3),
        },
        other_conditions=[
            Aspect(format="must be facing the caster", base_difficulty=5),
            Aspect(format="can unleash chaos effect on failure"),
        ],
        notes=textwrap.dedent("""\
            This quick enchantment creates a painful burst of light
            that affects all creatures within the spell's area of effect.
            Those affected (i.e., looking in the direction of
            the light) go blind for 10 seconds (thereby suffering a
            -2D penalty to all actions during that time; see Chapter eight "Combat,"
            for more information on blindness penalties.)
        """),
        skill="Conjuration",
    ),
    Spell(
        name="Hesitate",
        # Difficulty 5
        effect=Aspect(
            format="-3D penalty on next Agility roll", base_difficulty=(9 * 2), count=1
        ),
        speed=Aspect(format="Instant", base_difficulty=0),
        range=Aspect(format="Touch", base_difficulty=0),
        duration=Aspect(format="1 min", base_difficulty=9),
        casting_time=Aspect(format="10 sec", base_difficulty=5, count=1),
        other_aspects={
            "Concentration": Aspect(format="On Target", base_difficulty=-4),
            "Gestures": Aspect(format="Complex", base_difficulty=-3),
            "Incantation": Aspect(format="Complex", base_difficulty=-3),
        },
        other_conditions=[
            Aspect(format="can unleash chaos effect on failure"),
        ],
        notes=textwrap.dedent("""\
            Through this incantation, the caster injects a tiny
            amount of chaos energy into his victim's body, causing
            the target's muscles to spasm momentarily. As a
            result, the target suffers a -3D penalty on his next Agility roll for initiative.
        """),
        skill="Alteration",
    ),
    Spell(
        name="Netherdart",
        # Difficulty 20
        effect=Aspect(
            format="3D Damage; 1 pip mental and 1 pip physique each 10 sec.",
            base_difficulty=(9 + 6 + 6),
        ),
        speed=Aspect(format="1 sec to arrive", base_difficulty=-6),
        range=Aspect(format="20 m", base_difficulty=7),
        duration=Aspect(format="1 minute", base_difficulty=9),
        casting_time=Aspect(format="15 sec", base_difficulty=6, count=1),
        other_aspects={
            "Concentration": Aspect(format="On Target", base_difficulty=-4),
            "Gestures": Aspect(format="Complex", base_difficulty=-3),
            "Incantation": Aspect(format="Litany", base_difficulty=-4),
            "Charges": Aspect(format="5 charges", base_difficulty=4),
        },
        other_conditions=[
            Aspect(format="can unleash chaos effect on failure"),
        ],
        notes=textwrap.dedent("""\
            Upon the casting of this spell, five dark motes of energy
            coalesce in the caster's hand. The chaos binder
            may hurl the deadly magic one mote at a time (speed of +1)
            at the same or separate targets (each attack is
            treated as a separate action.) The caster may choose
            to throw them all at once (incurring the applicable
            multi-action penalties) or one at a time. A successful
            attack causes 3D in the victim as the black mote burrows
            into the target's body. Once within, the dark energy
            begins to suck away the victim's will (subtract one pip
            of a mental attribute one on pip of Endurance for every
            10 seconds the spell remains in effect; the lost pips return
            at the same rate they were lost.)
        """),
        skill="Conjuration",
    ),
    Spell(
        name="Propel",
        # Difficulty 10
        effect=Aspect(
            format="Move up to 100 kg, 10 m/sec", base_difficulty=15, count=1
        ),
        speed=Aspect(format="Instant", base_difficulty=-7),
        range=Aspect(format="25 m", base_difficulty=7),
        duration=Aspect(format="10 minute", base_difficulty=14),
        casting_time=Aspect(format="1 min", base_difficulty=9, count=1),
        other_aspects={
            "Concentration": Aspect(format="On Target", base_difficulty=-4),
            "Gestures": Aspect(format="Complex", base_difficulty=-3),
            "Incantation": Aspect(format="Litany", base_difficulty=-4),
        },
        other_conditions=[
            Aspect(format="can unleash chaos effect on failure"),
        ],
        notes=textwrap.dedent("""\
            This spell builds up a wave of chaotic energy which
            the caster feels as an invisible, pulsing force close
            by. At the completion of the incantation, the chaos
            binder commands the wave to push objects or creatures in any direction.
            The wave of force can manipulate
            a target no less than 1 kilogram and no more
            than 100 kilograms at a movement rate of up to 10
            (twice as fast as a walking human.) While directing
            the wave, the caster may not undertake other activities,
            but must concentrate on the energy to keep it
            from dispersing.
        """),
        skill="Apportation",
    ),
    Spell(
        name="Sense Residual Magic",
        # Difficulty 10
        effect=Aspect(
            format="Follow magical trail up to 1km away up to 3hr old",
            base_difficulty=20,
            count=1,
        ),
        speed=Aspect(format="Instant", base_difficulty=-15),
        range=Aspect(format="1 km", base_difficulty=15),
        # Assumes move of 10 == 10m in 5sec round, 1km = 500sec = 8.3 min.
        duration=Aspect(format="10 min", base_difficulty=14),
        casting_time=Aspect(format="5 min", base_difficulty=12, count=1),
        other_aspects={
            "Concentration": Aspect(format="On Target", base_difficulty=-4),
            "Gestures": Aspect(format="Complex", base_difficulty=-3),
            "Incantation": Aspect(format="Litany", base_difficulty=-4),
        },
        other_conditions=[
            Aspect(format="original caster still in the area", base_difficulty=10),
            Aspect(format="can unleash chaos effect on failure"),
        ],
        notes=textwrap.dedent("""\
            Magic leaves telltale signs of its use in the form of
            shimmering paths of residual chaos invisible to the
            naked eye. With this spell, the user attunes her sight
            to the range of chaos waves, enabling her to see these
            stringy paths and follow them to their source. The
            caster may trail a particular path up to the spell's
            area of effect at which point it gradually fades. If the
            original caster has left the area, the trail ends in mid-air.
            The spellcaster may then cast *Sense Residual Magic* again
            and pick up the trail where it left off, following up the
            limit of it's area, and so on.
        """),
        skill="Divination",
    ),
    Spell(
        name="Shroud",
        # Difficulty 5
        effect=Aspect(format="Concealed -5D to Acumen", base_difficulty=15, count=1),
        speed=Aspect(format="Instant", base_difficulty=0),
        range=Aspect(format="Self", base_difficulty=0),
        duration=Aspect(format="4 hrs", base_difficulty=21),
        casting_time=Aspect(format="5 min", base_difficulty=12, count=1),
        other_aspects={
            "Concentration": Aspect(format="On Target", base_difficulty=-4),
            "Gestures": Aspect(format="Complex", base_difficulty=-3),
            "Incantation": Aspect(format="Litany", base_difficulty=-4),
        },
        other_conditions=[
            Aspect(format="can unleash chaos effect on failure"),
        ],
        notes=textwrap.dedent("""\
            When the enchantment is cast, a swirling, blotchy
            gray-and-black film encases the spellcaster's body,
            completely concealing her features.
        """),
        skill="Conjuration",
    ),
    Spell(
        name="Warp Magic",
        # Difficulty 15
        effect=Aspect(
            format="Prevent -5D of spell effects", base_difficulty=15, count=1
        ),
        speed=Aspect(format="Instant", base_difficulty=8),
        range=Aspect(format="35m", base_difficulty=8),
        duration=Aspect(format="5 min", base_difficulty=4),
        casting_time=Aspect(format="1 sec", base_difficulty=0, count=1),
        other_aspects={
            "Concentration": Aspect(format="On Target", base_difficulty=-4),
            "Gestures": Aspect(format="Complex", base_difficulty=-3),
            "Incantation": Aspect(format="Litany", base_difficulty=-4),
            "Other Alterant": Aspect(format="Timed to coincide", base_difficulty=5),
        },
        other_conditions=[
            Aspect(format="can unleash chaos effect on failure"),
        ],
        notes=textwrap.dedent("""\
            The caster may prevent a spell form occurring (just
            as another spellcaster unleashes an incantation), or
            may eradicate a spell that has already been cast.
        """),
        skill="Alteration",
    ),
    Spell(
        name="Zed'oric's Defense",
        # Difficulty 12
        effect=Aspect(
            format="Absorb 5D of damage; 1D bonus to resist magical effects",
            base_difficulty=(15 + 3 * 2.5),
            count=1,
        ),
        speed=Aspect(format="Instant", base_difficulty=0),
        range=Aspect(format="Self", base_difficulty=0),
        duration=Aspect(format="8 hr", base_difficulty=22),
        casting_time=Aspect(format="5 min", base_difficulty=12, count=1),
        other_aspects={
            "Concentration": Aspect(format="On Target", base_difficulty=-4),
            "Gestures": Aspect(format="Complex", base_difficulty=-3),
            "Incantation": Aspect(format="Litany", base_difficulty=-4),
        },
        other_conditions=[
            Aspect(format="can unleash chaos effect on failure"),
        ],
        notes=textwrap.dedent("""\
            Using this incantation, the caster weaves chaos energy
            into his body. The chaos field absorbs any physical damage
            inflicted upon the character (including magical attacks
            that physically harm the target), giving a bonus of 1D
            to an Endurance or mental attribute roll to resist damage.
        """),
        skill="Alteration",
    ),
]


if __name__ == "__main__":
    detail(spells, spell_heading="-")
    # summary(spells)


__test__ = {}
