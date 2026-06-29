"""
More Spells

When run as an app, generates .RST details of each Spell.

..  todo:: Cleanup

    -   Redo 3 Illusions to have Unreal Effect modifier!
    -   Restate duration, range, casting_time using time_aspect, weight_aspect, and distance_aspect

Difficulty Mapping.

Legacy definitions had 10 distinct degrees of difficulty, from 1 to 10.
This seem to belong to 6 distinct ranks from an OpenD6 view.

Rank 1, Cantrips. These have difficulty range from 2 to 10. Target, is 5 ±3.

-   [Protection from Magic-1]
-   [Halt-1]
-   [Illusion of Rat-2]
-   [Sleep-2]
-   [Shield-2]
-   [Communicate w/ Plant/Animal-2]

Remaining difficulties range from 10-30, with 5 obvious targets: 10, 15, 20, 25, 30.
Map legacy difficulties:

-   3-4 to 10 ±3
-   5-6 to 15 ±3
-   7-8 to 20 ±3
 -  9 to 25 ±3
-   and 10 to 30 ±3

Rank 2: 10-point.

-   [Light Fire-3]
-   [Move Fire-3]
-   [Wind Gust-3]
-   [ESP-3]
-   [Light-3]
-   [Shocking Grasp-3]
-   [Find Path-3]
-   [Telekinesis-3]
-   [Gradual Heal-4]
-   [Freeze-4]
-   [Passfire-4]
-   [Knock-4]
-   [Warp Wood-4]
-   [Infravision-4]
-   [Silence-4]

Rank 3: 15-point.

-   [Immediate Hurt-5]
-   [Illusion of Small Monster-5]
-   [Fire Ball-5]
-   [Wind Storm-5]
-   [Charm-5]
-   [Hold Portal-5]
-   [Impervious leather armor-5]

-   [Move Wall of Rock-6]
-   [Passwall-6]
-   [Lightning-6]
-   [Dirt to Mud-6]
-   [Levitate-6]
-   [Mend Iron-6]
-   [Pass Plant-6]
-   [Human Combustion-6]

Rank 4: 20-point.

-   [Conjure Wall of Rock-7]
-   [Totally Invisible-7]
-   [Durable Illusion of Small Monster-8]
-   [Flesh to Stone-8]

Rank 6: 30-point.

-   [Earth Quake-10]

"""

from magic1 import Aspect, Spell, detail, time_aspect, distance_aspect, weight_aspect


spells = [
    Spell(
        effect=Aspect(format="Cure 5D of disease", base_difficulty=15, count=1),
        duration=Aspect(format="Instantaneous", base_difficulty=0, count=1),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=Aspect(format="1 s", base_difficulty=0, count=1),
        name="Gradual Heal",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
        },
        other_conditions=[
            Aspect(format="Heal only with Body <= 3/4", base_difficulty=-2, count=1),
            Aspect(format="limited to 3 body parts", base_difficulty=-1, count=1),
            Aspect(format="limited to disease cure", base_difficulty=-1, count=1),
            Aspect(format="Controller: Hælan Coordination"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Alteration: Physique",
        notes="Cures a disease or poison",
        # difficulty=4,
    ),
    Spell(
        effect=Aspect(format="+5D damage", base_difficulty=15, count=1),
        duration=Aspect(format="1 s", base_difficulty=0, count=1),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=Aspect(format="1 s", base_difficulty=0, count=1),
        name="Immediate Hurt",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
        },
        other_conditions=[
            Aspect(format="Damage only with Body <= 1/2", base_difficulty=-2, count=1),
            Aspect(format="Controller: Hælan Coordination"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Alteration: Physique",
        notes="Adds to previously received injuries",
        # difficulty=5,
    ),
    Spell(
        effect=Aspect(
            format="Illusion of small (60 kg) monster", base_difficulty=9, count=1
        ),
        duration=Aspect(format="5 m", base_difficulty=10, count=1),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=Aspect(format="1 s", base_difficulty=0, count=1),
        name="Illusion of Small Monster",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
            "other_alterant": Aspect(
                format="illusion is moving", base_difficulty=3, count=1
            ),
        },
        other_conditions=[
            Aspect(format="illusion limited to 3 colors", base_difficulty=3, count=1),
            Aspect(format="Controller: Baelu Charisma"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Psychic Communication",
        notes="An autonomous illusion of a small monster",
        # difficulty=5,
    ),
    Spell(
        effect=Aspect(format="Illusion of 1 kg rat", base_difficulty=1, count=1),
        duration=Aspect(format="5 m", base_difficulty=10, count=1),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=time_aspect("5 sec"),
        name="Illusion of Rat",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
            "concentration": time_aspect("5 sec"),
            "other_alterant": Aspect(
                format="illusion is moving", base_difficulty=3, count=1
            ),
        },
        other_conditions=[
            Aspect(format="illusion limited to 1 color", base_difficulty=-3, count=1),
            Aspect(format="Controller: Baelu Charisma"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Psychic Communication",
        notes="An autonomous illusion of a large rat",
        # difficulty=2,
    ),
    Spell(
        effect=Aspect(format="Illusion of 60 kg monster", base_difficulty=9, count=1),
        duration=Aspect(format="1 hr", base_difficulty=18, count=1),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=Aspect(format="1 s", base_difficulty=0, count=1),
        name="Durable Illusion of Small Monster",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
            "other_alterant": Aspect(
                format="illusion is moving", base_difficulty=5, count=1
            ),
        },
        other_conditions=[
            Aspect(format="illusion limited to 3 colors", base_difficulty=5, count=1),
            Aspect(format="Controller: Baelu Charisma"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Psychic Communication",
        notes="This illusion lasts one hour before starting to fade",
        # difficulty=8,
    ),
    Spell(
        effect=Aspect(format="-2D to effect (after link)", base_difficulty=10, count=1),
        duration=Aspect(format="1 s", base_difficulty=0, count=1),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=time_aspect("5s"),
        name="Protection from Magic",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
            "concentration": time_aspect("5s"),
        },
        other_conditions=[
            Aspect(format="opposed", base_difficulty=0, count=1),
            Aspect(format="Controller: None"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Alteration",
        notes="Distinct from Shield which prevents the link, this mitigates effects",
        # difficulty=1,
    ),
    Spell(
        effect=Aspect(
            format="Halt! with +2D to overcome mettle", base_difficulty=10, count=1
        ),
        duration=time_aspect("2 sec"),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=time_aspect("5 sec"),
        name="Halt",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
            "concentration": time_aspect("5 sec"),
        },
        other_conditions=[
            Aspect(format="Controller: Witan Acumen")  # vs. Charisma mettle
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Psychic Communication",
        notes="The halt duration is short; an agility check is required to keep from stumbling",
        # difficulty=1,
    ),
    Spell(
        effect=Aspect(format="Freeze: -4D to physique", base_difficulty=12, count=1),
        duration=time_aspect("2 min"),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=time_aspect("5 sec"),
        name="Freeze",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
            "concentration": time_aspect("5 sec"),
        },
        other_conditions=[Aspect(format="Controller: Folme Agility")],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Psychic Communication",
        notes="Physique is (temporarily) drained away, making movement difficult",
        # difficulty=4,
    ),
    Spell(
        # Related spells: Somniomancy Groggy is 22, Kiss of the Sandman is 21.
        # This is **not** a Rank-1 cantrip.
        effect=Aspect(
            format="Sleep: -4D to mental and physical attributes",
            base_difficulty=24,
            count=1,
        ),
        duration=time_aspect("5 min"),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=time_aspect("5 sec"),
        name="Sleep",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
            "concentration": time_aspect("5 sec"),
            "feedback": Aspect(
                format="-2 to damage resistance total", base_difficulty=-2, count=1
            ),
        },
        other_conditions=[Aspect(format="Controller: Folme Agility")],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Psychic Communication",
        notes="Physique, Coordination, Acumen, and Intellect are (temporarily) reduced, leading to fatique",
        # difficulty=2,  # far too low.
    ),
    Spell(
        effect=Aspect(
            format="Move 600kg earth element to a new position",
            base_difficulty=14,
            count=1,
        ),
        duration=time_aspect("1 min"),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=time_aspect("5 sec"),
        name="Move Wall of Rock",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
            "concentration": time_aspect("5 sec"),
            "area_of_effect": Aspect(
                format="27 cu m, 3m×3m×3m, 2m sphere", base_difficulty=10, count=1
            ),
        },
        other_conditions=[
            Aspect(format="elemental already present", base_difficulty=-4, count=1),
            Aspect(format="Controller: Hildeþrymm Physique"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Alteration: Earth",
        notes="See Conjure Wall of Rock for a complementary spell",
        # difficulty=6,
    ),
    Spell(
        effect=Aspect(
            format="Move 600kg earth element to a new position",
            base_difficulty=14,
            count=1,
        ),
        duration=time_aspect("5 min"),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=time_aspect("5 sec"),
        name="Conjure Wall of Rock",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
            "concentration": time_aspect("5 sec"),
            "area_of_effect": Aspect(
                format="27 cu m, 3m×3m×3m, 2m sphere", base_difficulty=10, count=1
            ),
        },
        other_conditions=[
            Aspect(format="Controller: Hildeþrymm Physique"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Conjuration: Earth",
        notes="Creates a wall from free earth elements",
        # difficulty=7,
    ),
    Spell(
        effect=Aspect(
            format="Move small (2D damage) fire element", base_difficulty=6, count=1
        ),
        duration=Aspect(format="1 s", base_difficulty=0, count=1),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=time_aspect("1 sec"),
        name="Light Fire",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
        },
        other_conditions=[
            Aspect(format="Controller: Cyþan Intelligence"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Alteration: Fire",
        notes="The fire must exist; this merely moves it to ignite something else",
        # difficulty=3,
    ),
    Spell(
        effect=Aspect(
            format="Move large (5D damage) fire element", base_difficulty=15, count=1
        ),
        duration=Aspect(format="1 s", base_difficulty=0, count=1),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=time_aspect("5 sec"),
        name="Move Fire",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
            "concentration": time_aspect("5 sec"),
        },
        other_conditions=[
            Aspect(format="Controller: Cyþan Intelligence"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Alteration: Fire",
        notes="The fire must exist; this merely moves it somewhere else",
        # difficulty=3,
    ),
    Spell(
        effect=Aspect(
            format="Remove 2m x 1m x 7m section of wall", base_difficulty=10, count=1
        ),
        duration=Aspect(format="10m", base_difficulty=14, count=1),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=Aspect(format="1 s", base_difficulty=0, count=1),
        name="Passwall",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
        },
        other_conditions=[
            Aspect(format="Controller: Hildeþrymm Physique"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Alteration: Earth",
        notes="The earth element doesn't vanish; it's moved out of the passage",
        # difficulty=6,
    ),
    Spell(
        effect=Aspect(
            format="Remove 2m x 1m x 7m section of fire", base_difficulty=10, count=1
        ),
        duration=time_aspect("2 min"),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=time_aspect("5 sec"),
        name="Passfire",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
            "concentration": time_aspect("5 sec"),
        },
        other_conditions=[
            Aspect(format="Controller: Cyþan Intelligence"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Alteration: Fire",
        notes="The fire element doesn't vanish; it's moved out of the passage",
        # difficulty=4,
    ),
    Spell(
        effect=Aspect(
            format="move fire 2m/s, does 7D damage", base_difficulty=21, count=1
        ),
        duration=Aspect(format="1 s", base_difficulty=0, count=1),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=time_aspect("5 sec"),
        name="Fire Ball",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
        },
        other_conditions=[
            Aspect(format="Controller: Cyþan Intelligence"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Alteration: Fire",
        notes="Charisma",
        # difficulty=5,
    ),
    Spell(
        effect=Aspect(
            format="move air+fire 2m/s, does 6D damage", base_difficulty=18, count=1
        ),
        duration=Aspect(format="1 s", base_difficulty=0, count=1),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=time_aspect("1 sec"),
        name="Lightning",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
        },
        other_conditions=[
            Aspect(format="Controller: Folme Agility"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Alteration: Air + Fire",
        notes="The balance of elements is mostly air with a touch of fire.",
        # difficulty=6,
    ),
    Spell(
        effect=Aspect(format="shake 1,000 kg earth", base_difficulty=15, count=1),
        duration=Aspect(format="5 s", base_difficulty=4, count=1),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=time_aspect("5 sec"),
        name="Earth Quake",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
            "concentration": time_aspect("5 sec"),
            "area_of_effect": Aspect(
                format="20m r circle", base_difficulty=40, count=1
            ),
        },
        other_conditions=[
            Aspect(format="Controller: Hildeþrymm Physique"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Alteration: Earth",
        notes="The area is large enough that the mage is barely able to avoid the effects; damage is incidental usually from falling objects",
        # difficulty=10,
    ),
    Spell(
        effect=Aspect(format="add water to earth", base_difficulty=5, count=1),
        duration=time_aspect("5 min"),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=time_aspect("5 sec"),
        name="Dirt to Mud",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
            "concentration": time_aspect("5 sec"),
            "area_of_effect": Aspect(
                format="10m radius circle", base_difficulty=20, count=1
            ),
        },
        other_conditions=[Aspect(format="Controller: Hælan Coordination")],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Alteration: Water",
        notes="The water must be located nearby; the mud starts to revert after 5 minutes, escape is difficult requiring patience and sometimes the help of a shovel or pry-bar",
        # difficulty=6,
    ),
    Spell(
        effect=Aspect(format="25 kg move 1m/s", base_difficulty=7, count=1),
        duration=Aspect(format="1 s", base_difficulty=0, count=1),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=Aspect(format="1 s", base_difficulty=0, count=1),
        name="Wind Gust",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
        },
        other_conditions=[
            Aspect(format="Controller: Folme Agility"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Alteration: Air",
        notes="A gust that will move 25 kg will unbalance a target unprepared for it",
        # difficulty=3,
    ),
    Spell(
        effect=Aspect(
            format="100 kg move 1m/s, +3D damage", base_difficulty=10 + 9, count=1
        ),
        duration=time_aspect("3 rounds"),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=time_aspect("5 sec"),
        name="Wind Storm",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
            "concentration": time_aspect("5 sec"),
        },
        other_conditions=[
            Aspect(format="Controller: Folme Agility"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Alteration: Air",
        notes="This generally knocks a person down (to stand is Very Difficult 21-25); it batters them for 3 rounds",
        # difficulty=5,
    ),
    Spell(
        effect=Aspect(
            format="move 10 kg door; 3D damage to latch", base_difficulty=5 + 9, count=1
        ),
        duration=Aspect(format="1 s", base_difficulty=0, count=1),
        range=Aspect(format="touch", base_difficulty=1, count=1),
        casting_time=Aspect(format="1 s", base_difficulty=0, count=1),
        name="Knock",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
        },
        other_conditions=[
            Aspect(format="limited to wood", base_difficulty=-1, count=1),
            Aspect(format="Controller: Depends on type of wood"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=1, count=1),
        skill="Alteration: [type of wood]",
        notes="This tends to destroy the door",
        # difficulty=4, # Much easier, actually.
    ),
    Spell(
        effect=Aspect(format="10 kg move 1m/s", base_difficulty=5, count=1),
        duration=Aspect(format="1 s", base_difficulty=0, count=1),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=Aspect(format="1 s", base_difficulty=0, count=1),
        name="Warp Wood",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
        },
        other_conditions=[
            Aspect(format="limited to wood", base_difficulty=0.0, count=1),
            Aspect(format="Controller: Depends on type of wood"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Alteration: wood",
        notes="The wood's shape is changed, any damage is incidental",
        # difficulty=4,
    ),
    Spell(
        effect=Aspect(
            format="Gather general thoughts from hostile target",
            base_difficulty=15,
            count=1,
        ),
        duration=Aspect(format="1 s", base_difficulty=0, count=1),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=time_aspect("5 sec"),
        name="ESP",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
            "concentration": time_aspect("5 sec"),
        },
        other_conditions=[
            Aspect(format="Controller: Witan Acumen"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Divination",
        notes="This provides very general background information",
        # difficulty=3,
    ),
    Spell(
        effect=Aspect(
            format="Drain away water, air, fire, replace with earth, 100kg",
            base_difficulty=30,
            count=1,
        ),
        duration=time_aspect("1 min"),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=time_aspect("5 sec"),
        name="Flesh to Stone",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
            "concentration": time_aspect("5 sec"),
        },
        other_conditions=[
            Aspect(format="limited to living animal", base_difficulty=-1, count=1),
            Aspect(format="Controller: Hildeþrymm Physique"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Alteration: Earth",
        notes="Displaces 3 elements to surrounding area; replaces with the earth, which must be present",
        # difficulty=8,
    ),
    Spell(
        effect=Aspect(format="Favorable Feelings +4D", base_difficulty=12, count=1),
        duration=time_aspect("5 min"),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=Aspect(format="1 s", base_difficulty=0, count=1),
        name="Charm",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
        },
        other_conditions=[
            Aspect(format="Controller: Baelu Charisma"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Psychic Communication",
        notes="Creates favorable feelings; acting as a supplement to common Charisma-based skills",
        # difficulty=5,
    ),
    Spell(
        effect=Aspect(format="10 kg", base_difficulty=5, count=1),
        duration=Aspect(format="40 min", base_difficulty=12, count=1),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=Aspect(format="1 s", base_difficulty=0, count=1),
        name="Hold Portal",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
        },
        other_conditions=[
            Aspect(format="limited to wood", base_difficulty=0.0, count=1),
            Aspect(format="Controller: Depends on type of wood"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Alteration: wood",
        notes="The door is stuck closed, but -- of course -- can be battered down",
        # difficulty=5,
    ),
    Spell(
        effect=Aspect(
            format="A small cold fire (0D Damage at most), +1D to searching",
            base_difficulty=3,
            count=1,
        ),
        duration=Aspect(format="40m", base_difficulty=12, count=1),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=time_aspect("5 sec"),
        name="Light",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
            "concentration": time_aspect("5 sec"),
        },
        other_conditions=[
            Aspect(format="Controller: Witan Acumen"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Alteration: Fire",
        notes="This requires the fire from a torch or large lantern; it stays where the mage puts it. It doesn't consume any fuel",
        # difficulty=3,
    ),
    Spell(
        effect=Aspect(
            format="adds +2D to link difficulty", base_difficulty=10, count=1
        ),
        duration=time_aspect("2 min"),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=time_aspect("5 sec"),
        name="Shield",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
            "concentration": time_aspect("5 sec"),
        },
        other_conditions=[
            Aspect(format="Controller: None"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Psychic Communication",
        notes="This prevents a link from being formed. See Protection from Magic for a complementary spell to block effects after a link has been formed",
        # difficulty=2,  # Too low. Should be larger.
    ),
    Spell(
        effect=Aspect(format="-8D to perception", base_difficulty=24, count=1),
        duration=time_aspect("5 min"),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=time_aspect("5 sec"),
        name="Totally Invisible",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
            "concentration": time_aspect("5 sec"),
        },
        other_conditions=[
            Aspect(format="Controller: Witan Acumen"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Alteration",
        notes="The thing is almost impossible to see",
        # difficulty=7,
    ),
    Spell(
        effect=Aspect(
            format="10 kg, +2D damage resistance", base_difficulty=5 + 6, count=1
        ),
        duration=time_aspect("5 min"),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=Aspect(format="1 s", base_difficulty=0, count=1),
        name="Impervious leather armor",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
        },
        other_conditions=[
            Aspect(format="limited to leather", base_difficulty=-1, count=1),
            Aspect(format="Controller: Hildeþrymm Physique"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Alteration",
        notes="This is a temporary boost in the defensive value of leather armor",
        # difficulty=5,
    ),
    Spell(
        effect=Aspect(format="100 kg move 1m/s", base_difficulty=10, count=1),
        duration=Aspect(format="10 min", base_difficulty=14, count=1),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=Aspect(format="1 s", base_difficulty=0, count=1),
        name="Levitate",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
        },
        other_conditions=[
            Aspect(format="Controller: Depends on substance being levitated"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Apportation: Depends on elements being levitated",
        notes="Levitation is not flight; this is very risky when used out doors; 10 min of rising at 1m/s will be followed by a 600' fall",
        # difficulty=6,
    ),
    Spell(
        effect=Aspect(
            format="Enhanced Senses +2D to see heat", base_difficulty=6, count=1
        ),
        duration=time_aspect("1 min"),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=time_aspect("5 sec"),
        name="Infravision",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
            "concentration": time_aspect("5 sec"),
        },
        other_conditions=[
            Aspect(format="Controller: Witan Acumen"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Alteration",
        notes="Heat from passing footsteps are difficult (but not impossible) to see",
        # difficulty=4,
    ),
    Spell(
        effect=Aspect(format="Reshape 15 kg of iron", base_difficulty=6, count=1),
        duration=Aspect(format="1 hr", base_difficulty=18, count=1),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=Aspect(format="1 s", base_difficulty=0, count=1),
        name="Mend Iron",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
        },
        other_conditions=[
            Aspect(format="Controller: Cyþan Intelligence corresponds with Iron"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Alteration: Earth + Fire",
        notes="This is a slow process and requires a source of fire and earth",
        # difficulty=6,
    ),
    Spell(
        effect=Aspect(format="Does %{count}D Damage", base_difficulty=3, count=6),
        duration=Aspect(format="1 s", base_difficulty=0, count=1),
        range=Aspect(format="Touch", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 s", base_difficulty=0, count=1),
        name="Shocking Grasp",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
        },
        other_conditions=[Aspect(format="Controller: Hælan Coordination")],
        speed=Aspect(format="Instantaneous", base_difficulty=0, count=1),
        skill="Alteration: Air + Fire",
        notes="A touch that does 6D damage",
        # difficulty=3,
    ),
    Spell(
        effect=Aspect(
            format="Remove 2m x 1m x 7m section of plant", base_difficulty=15, count=1
        ),
        duration=Aspect(format="5m", base_difficulty=12, count=1),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=time_aspect("5 sec"),
        name="Pass Plant",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
            "concentration": time_aspect("5 sec"),
        },
        other_conditions=[
            Aspect(format="limited to plants", base_difficulty=-1, count=1),
            Aspect(format="Controller: Depends on type of plant"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Alteration: plants",
        notes="Plant matter decomposed to earth, water, air and displaced",
        # difficulty=6,
    ),
    Spell(
        effect=Aspect(format="+3D to find path", base_difficulty=9, count=1),
        duration=Aspect(format="5m", base_difficulty=12, count=1),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=time_aspect("5 sec"),
        name="Find Path",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
            "concentration": time_aspect("5 sec"),
        },
        other_conditions=[
            Aspect(format="Controller: Witan Acumen"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Divination",
        notes="A big boost in locating a path through obstacles",
        # difficulty=3,
    ),
    Spell(
        effect=Aspect(format="+6D damage from fire", base_difficulty=18, count=1),
        duration=Aspect(format="3 r", base_difficulty=6, count=1),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=time_aspect("5 sec"),
        name="Human Combustion",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
            "concentration": time_aspect("5 sec"),
        },
        other_conditions=[
            Aspect(format="Controller: Cyþan Intelligence"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Alteration: Fire",
        notes="This is simply nasty -- up to three rounds of damage",
        # difficulty=6,
    ),
    Spell(
        effect=Aspect(format="25 kg move 1m/s", base_difficulty=7, count=1),
        duration=Aspect(format="10 sec", base_difficulty=5, count=1),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=Aspect(format="1 s", base_difficulty=0, count=1),
        name="Telekinesis",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
        },
        other_conditions=[Aspect(format="Controller: [substance target is made of]")],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Apportation: Depends on elements being moved",
        notes="Movement is a slow walk",
        # difficulty=3,  # Up to 6 for more mass,
    ),
    Spell(
        effect=Aspect(format="Perception -4D", base_difficulty=12, count=1),
        duration=time_aspect("5 min"),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=time_aspect("5 sec"),
        name="Silence",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
            "concentration": time_aspect("5 sec"),
            "area_of_effect": Aspect(format="2m r circle", base_difficulty=4, count=1),
        },
        other_conditions=[
            Aspect(format="Controller: Witan Acumen"),
        ],
        speed=Aspect(format="1 sec", base_difficulty=0, count=1),
        skill="Alteration: Air",
        notes="This will silence most noises in a small circle around the target",
        # difficulty=4,
    ),
    Spell(
        effect=Aspect(
            format="+1D to gather common info; potentially hostile",
            base_difficulty=10,
            count=1,
        ),
        duration=Aspect(format="1 s", base_difficulty=0, count=1),
        range=Aspect(format="20 m", base_difficulty=7, count=1),
        casting_time=time_aspect("5s"),
        name="Communicate w/ Plant/Animal",
        other_aspects={
            "incantation": Aspect(format="Litany", base_difficulty=-4),
            "concentration": time_aspect("5s"),
        },
        other_conditions=[
            Aspect(format="Controller: Witan Acumen"),
        ],
        speed=Aspect(format="Instantaneous", base_difficulty=7, count=1),
        skill="Divination",
        notes="This will gather a bit of common information",
        # difficulty=3,
    ),
]


if __name__ == "__main__":
    detail(spells, spell_heading="-")

__test__ = {"placeholder": ">>> pass"}

import logging
import pytest

# Scenario Outline: Converted spells fall into bands approximating target degrees of difficulty
# Given <spell name>
#  And <target difficulty>
#  When spell difficulty is computed for <spell name>
#  Then computed difficulty is within -2 +3 of <target difficulty>
#  Examples:
_SPELL_DIFFICULTIES = sorted(
    [
        # Cantrip-like (Rank 1), 5 pt (was 1-2)
        ("Protection from Magic", 5),
        ("Halt", 5),
        ("Illusion of Rat", 5),
        ("Communicate w/ Plant/Animal", 5),
        ("Knock", 5),
        ("Shocking Grasp", 5),
        # Rank 2: 10 pt (was 3-4)
        ("Shield", 10),
        ("Light Fire", 10),
        ("Move Fire", 10),
        ("Wind Gust", 10),
        ("ESP", 10),
        ("Light", 10),
        ("Find Path", 10),
        ("Telekinesis", 10),
        ("Gradual Heal", 10),
        ("Freeze", 10),
        ("Passfire", 10),
        ("Warp Wood", 10),
        ("Infravision", 10),
        ("Silence", 10),
        ("Immediate Hurt", 10),
        # Rank 3: 15 pt (was 5-6)
        ("Illusion of Small Monster", 15),
        ("Fire Ball", 15),
        ("Wind Storm", 15),
        ("Charm", 15),
        ("Hold Portal", 15),
        ("Impervious leather armor", 15),
        ("Move Wall of Rock", 15),
        ("Passwall", 15),
        ("Lightning", 15),
        ("Levitate", 15),
        ("Mend Iron", 15),
        ("Pass Plant", 15),
        ("Human Combustion", 15),
        # Rank 4 and 6: 20 pt and 30 pt (was 7-10)
        ("Dirt to Mud", 20),
        ("Sleep", 20),
        ("Conjure Wall of Rock", 20),
        ("Totally Invisible", 20),
        ("Durable Illusion of Small Monster", 20),
        ("Flesh to Stone", 20),
        ("Earth Quake", 30),
    ],
    key=lambda nm_d: nm_d[1],
)
_SPELL_MAP = {s.name: s for s in spells}


@pytest.mark.parametrize("spell_name,difficulty", _SPELL_DIFFICULTIES)
def test_spell_approx_difficulty(spell_name, difficulty, caplog):
    caplog.set_level(logging.DEBUG, logger="Spell")
    force_recomputation_for_the_log = _SPELL_MAP[spell_name]._difficulty()
    assert difficulty - 2 <= _SPELL_MAP[spell_name].difficulty < difficulty + 3
