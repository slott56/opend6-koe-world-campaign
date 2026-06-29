..  _`location.cave`:

############################
  The Jackal's Secret Cave
############################

Concealed in a narrow canyon between two steep hillsides, there's a hot spring.
Locals who wander these forests know it steams in winter, and avoid it.
Above this spring, high on the hillside, there's a wall of ancient limestone with a low opening.

The location of the hot spring and cave are revealed only in notes found in the the :ref:`location.keep`.
Look, specifically, in :ref:`location.keep.central_tower`.

Without the map, it is still possible to use divination to locate Xorn's final hideout.
The difficulty is Heroic, and a great deal of helpers and preparation is required.

General
=======

..  figure::  ../figures/salamander_cave.png

    The Secret Cave

    Scale: Square = 2m (6').


..  Worldographer Config:

    Use 50x50

    Entrance=5,4,8,5,GuardL,GuardR,Hall1
    GuardL=3,3,4,4
    GuardR=3,3,4,4
    Hall1=3,3,8,8,Hall2
    Hall2=4,4,5,5,Guard2,Shrine1,Hall3
    Guard2=3,3,4,4
    Shrine1=5,6,6,7
    Hall3=2,2,8,8,Shrine2
    Shrine2=5,6,6,7

Characters
=================

Goblins
~~~~~~~

..  include:: ../../characters/ch_7_goblin_guards.txt

Xorn
~~~~

Xorn is a beaten man, but will fight like hell anyway.
He will summon as many Hordlings as he can.

..  include:: ../../characters/xorn.txt
..  include:: ../../spells/xorn_spells.txt


See :ref:`character.xorn` additional notes.

The Salamander
~~~~~~~~~~~~~~

The "Jackal God" that Xorn communes with is actually a demon from the universe of fire.  A kind of fire elemental.  Immensely powerful and dangerous.

..  include:: ../../characters/salamander.txt


..  only:: hero

        ::

            Name: Salamander
            Characteristics:
            25	STR	15
            20	DEX	30
            18	CON	16
            20	BODY	20
            14	INT	4
            10	EGO	0
            15	PRE	5
            10	COM	0
            8	PD	3
            12	ED	8
            4	SPD	10
            10	REC	2
            50	END	7
            45	STUN	3
            6	Running	0
            2	Swimming	0
            Cost: 123
            Skills & Abilities:
            20	Combat	+4
            7	Stealth	15-
            7	Survival	13-
            1	Weapons Familiarity	Group
                4 levels with the red-hot crystal spear with which it fights.
            12	Armor: 8rPD Armor DEF (12), 0 END,

            20	Flare-up: 1d6 Flash Disable (BODY of) (10), 100 Range, 2 per Phase END,

            30	Firey Breath: 6d6 EB (30), 150 Range, 3 per Phase END,

            15	Huge: 800 Kg Mass (15), +15 Str, -3 Knockback, +3 BODY, +3 STUN, +3 PD, +3 ED, -2 DCV, +2 PER against, 4m Height, 2m Width, 2 Reach, 1.5 per Phase END,

            6	Superleap: +6 hex Leap (6), 2.5+1/5hexes END,

            100+ Disadvantage
            -20	Vulnerable: Common Situation, 2x Damage X,
                Cold or Water-based attacks do double damage!
            -15	Near Lava Pit: Uncommon Circumstances,
                Must be near a heat source
            -25	Monster Bonus: Constantly Occurs, Fully Impairs,

            Costs: char skills total disadv base
            123 + 118 = 160 = 60 + 100
            Background:
            Creature of fire, much like a fire elemental.  Cannot be killed by fire.
            Visuals:
            A big ol' lizard, 10-14 ft. tall capable of walking upright and using weapons.  Weapons are crystals that can withstand the heat of its lair.
            Rolls & Effects:
            Base OCV	7
            Base DCV	7
            Base ECV	3
            Phases	3/6/9/12
            Lift	800 Kg
            Jump	5 Hexes
            CON Roll	13-
            DEX Roll	13-
            INT Roll	12-
            EGO Roll	11-

Rooms
========

- **Entrance**.

- **GuardL**.

    The sunset horde.
    12 goblins and 2 great goblins.
    The go out maurauding sunset to midnight and sleep during the day.

    See `Goblins`_.

- **GuardR**.

    The midnight horde.
    12 goblins and 2 great goblins.
    The go out maurauding midnight to dawn and during the day.

    See `Goblins`_.

- **Guard2**.

    3 trolls. Trapped here controlled by the goblins.
    Not happy with anything.

    Fight or Flight tends toward Flight.

    ..  admonition:: Fight or Flight

        ..  csv-table::
            :header-rows: 1

            Roll, "Strategy"
            1-4, "Flee"
            5-6, "Fight"

    They tend to try and push through the doorway.

    See `Goblins`_.

-   **Hall2**.

    Door between 17.12 and 18.12 is concealed.
    Requires careful search, difficulty of Difficult 16.

- **Shrine1**.

    Xorn.  See `Xorn`_.

- **Shrine2**.

    The Salamander. See `The Salamander`_

