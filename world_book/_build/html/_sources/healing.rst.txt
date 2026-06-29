..  _healing:

###########
  Healing
###########

There are many different ways that characters can regain their health.
Characters may never get back more than their maximum number of Body Points or Wounds.
|mod_opend6| See the :external:ref:`OpenD6 Fantasy, "Healing"<fantasy.healing>` chapter.

It's important to note the additional form of healing that applies to characters in this world.

Body Points
===========

|use_opend6|
This is the suggested method for tracking damage.

Wound Levels
============

|use_opend6|
If desired, this can be used, instead of body points.


Magic Fatigue Points
====================

Magic fatigue points is a feature unique to this system.
Mages and clerics must track their magic fatigue points, which are similar to Body points.
Performing magic reduces the number fatigue points.
Healing and resting will recover fatigue points.

Any attempt at magic with zero fatigue points will result in Body damage.
See the :ref:`damage` section for details.

Natural Healing
---------------

To recover magic fatigue points, either use a Healing skill, or roll *Physique*.
Apply a modifier based on how much actual rest the mage (or cleric) has had for the previous four hours.

..  csv-table::
    :header: Activity Level, Modifier

    No activity, +1D
    Light activity, +0D
    Fighting or running, -1D

The result of the roll determines how many die of fatigue points can be recovered.

Make a second roll to determine the number of fatigue points recovered for each four-hour rest period.

..  admonition:: FATIGUE POINTS HEALING

    ..  csv-table::
        :header: Healing or Physique Roll, Body Points Recovered

        0, 0
        1-5, 2
        6-10, 1D
        11-15, 2D
        16-20, 3D
        21-25, 4D
        26-30, 5D
        30+, 6D

It's important that recuperation has a duration of four hours.
Players who want to try to "reset the mage" so they can continue a battle will find this approach results in severe injury to the mage.

If the rest period is interrupted, the fatigue point recovery is pro-rated by the amount of time spent.
Divide the dice result by 4 hours and multiply by the hours of actual rest. Round fractions down.

**Example**. Player's healing roll is 22. This lets them roll 4D for the fatigue points.
This roll results in a potential recovery of 15 points spread over four hours.
After an hour of rest, the party is surprised by an attack.
The character will have recovered :math:`\tfrac{1}{4} \times 15 = 4` points of fatigue.
Enough for a brief spell or two.

Healing Skill
-------------

The Healing skill can be used to recover fatigue points as well as body points (or wound levels.)
A character with this skill can roll Healing to help a fatigued mage, and find the
results on the "Fatigue Points Healing" chart.
A successful roll recovers the listed number of points.

Recuperation Skill
-------------------

A mage with the Recuperation skill can recover fatigue points using this skill.
Roll for healing using the *recuperation* skill.
Look up the results on the "Fatigue Points Healing" chart.
A successful roll recovers the listed number of points over a four-hour period.
It's important that any interruption will reduce the number of fatigue points actually recovered.
