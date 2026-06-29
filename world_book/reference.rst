##########################
  OpenD6 Reference Sheet
##########################

Generic Standard Difficulties
=============================

See :ref:`fantasy.game_basics`.

See Chapter 5 (or general task resolution information and other modifiers.

..  include:: ../shared/standard_difficulty_def.txt

Generic Difficulty Modifiers
----------------------------

See :ref:`fantasy.game_basics.difficulties` for samples.

..  csv-table::
    :header: "Situation Helps/ Hinders Character...", "Modifier"

    Slightly, ± 1-5
    Significantly, ± 6-10
    Decisively, ± 11-15
    Overwhelmingly, ± 16 or more

Interaction Difficulty Modifiers
----------------------------------

See :ref:`skill_difficulties.interaction` for additional information and modifiers.

Base Difficulty: 10 or target's Charisma or mettle

..  include:: ../shared/interaction_modifiers.txt

Information Difficulties
-------------------------

See :ref:`skill_difficulties.information` for additional information and modifiers.

..  include:: ../shared/information_difficulties.txt


Observation Difficulties
-------------------------

See :ref:`skill_difficulties.observation` for additional information and modifiers.

..  include:: ../shared/observation_difficulties.txt


Movement Difficulty Modifiers
------------------------------

See :ref:`fantasy.movement` for additional information and modifiers.

..  include:: ../shared/movement_difficulties.txt


Combat Summary
==============

See :ref:`fantasy.combat` and :ref:`fantasy.combat_options` for additional information and modifiers.

**Determining the Difficulty**

Base combat difficulty = defense total

-   Defense total = (passive defense value or active defense value) plus combat difficulty modifiers

    -   Passive defense value = 10

    -   Active defense value = full defense value or partial defense value

        -   Full defense value= any defense skill roll +10

        -   Partial defense value = any defense skill roll

**Determining Success**

If the attacker's combat skill total plus any modifiers equals or exceeds
the target's defense roll, the attack succeeds and may do damage.

**Determining Damage**

-   Damage total

    -   For attacks that do damage not modified by strength: damage total = roll of weapon damage die code plus damage modifiers

    -   For attacks that do damage modified by strength: damage total = roll of weapon damage die code plus character's Strength Damage die code plus damage modifiers

-   Damage resistance total

    -   Body Points: roll of Armor die code plus defense modifiers

    -   Wounds: roll of Physique plus Armor die code plus defense modifiers

-   If the damage total is greater than the damage resistance total, the target was injured.
    If the damage total is less than or equal to the damage resistance total, the target was not injured.

-   If the target was injured, subtract the damage resistance total from the damage total.
    Then either subtract this from the target's current Body Total or compare the value on the "Wound Level" chart.

Common Combat Difficulty Modifiers
-----------------------------------

..  include:: ../shared/combat_difficulties.txt

**Weapon is difficult to use** (character unfamiliar with technology, object is hard to throw or grasp, melee or thrown weapon is more
than 60 centimeters long, etc.): +5 or more to the combat difficulty.

The gamemaster may decide that such factors as experience, strength,
and features of the weapon (such as a well-balanced sword) lower this
modifier.

Strength Damage
---------------

..  note: almost duplicated in Character Basics chapter.

To figure the Strength Damage die code, drop the pips from the
character's *Physique* or *lifting* die code (but include any Disadvantages
or Special Abilities), divide the number by 2, and round up.

Wound Levels
--------------

See :ref:`fantasy.damage.wound` for additional damage information and modifiers.

..  include:: ../shared/wound_levels.txt

Abbreviated Healing Chart
==========================

See :ref:`fantasy.healing` for additional healing information and modifiers.

..  csv-table::
    :header: Healing Total, Body Points Recovered, Current Wound Level

    1-5, 2
    6-10, 1D,   "Stunned, unconscious"
    11-15, 2D,  "Wounded, Severely Wounded"
    16-20, 3D,  "Incapacitated"
    21-25, 4D,  "Mortally Wounded"
    26-30, 5D








