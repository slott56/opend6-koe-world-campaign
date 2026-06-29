"""
Extract Spells from ``bandit_spells.ipynb``.
Created by V2025.6.27.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

With "test" argument, runs doctest, which uses the __test__ examples.

"""

from opend6_tools.magic import *



war_blast = Spell(
    name="War Blast",
    effect=DamageEffect(2*D, "fire-based", "ignore all armor"),
    duration=DurationAspect("1 sec"),
    range=RangeAspect("20m"),
    speed=SpeedAspect.based_on('range'),
    casting_time=CastingTimeAspect("1 round"),
    other_aspects={
        "incantation": IncantationsAspect("Demon Blast", "litany"),
        "concentration": ConcentrationAspect(measure="1 rounds"),
    },
)

war_bolt = Spell(
    name="War Bolt",
    effect=DamageEffect(3*D, "earth-based"),
    duration=DurationAspect("1 sec"),
    range=RangeAspect("20m"),
    speed=SpeedAspect.based_on('range'),
    casting_time=CastingTimeAspect("1 round"),
    other_aspects={
        "incantation": IncantationsAspect("War Blast", "litany"),
        "concentration": ConcentrationAspect(measure="1 rounds"),
    },
)

battle_shield = Spell(
    name="Battle Shield",
    effect=ProtectionEffect(2*D, "protection_modifier", "A wall of fire-like shimmer"),
    duration=DurationAspect("1 min"),
    range=RangeAspect("8m"),
    speed=SpeedAspect.based_on('range'),
    casting_time=CastingTimeAspect("1 round"),
    other_aspects={
        'area_effect': AreaEffectAspect('2m radius sphere'),
        "incantation": IncantationsAspect("Demon Shield Chant", "litany"),
        "concentration": ConcentrationAspect(measure="1 rounds"),
    }
)

dispel = Spell(
    name="Demonic Cleansing",
    effect=SkillEffect("Boost Charisma/intimidation", 4*D, "break concentration"),
    duration=DurationAspect("2 rounds"),
    range=RangeAspect("8m"),
    speed=SpeedAspect.based_on('range'),
    casting_time=CastingTimeAspect("1 round"),
    other_aspects={
        'area_effect': AreaEffectAspect('2m radius sphere'),
        "incantation": IncantationsAspect("Mage Intimidation Chant", "litany"),
        "concentration": ConcentrationAspect(measure="1 round"),
    }
)

bravery = Spell(
    name="Demonic Inspiration",
    effect=SkillEffect("Boost combat skill", 4*D),
    duration=DurationAspect("2 minutes"),
    range=RangeAspect("8m"),
    speed=SpeedAspect.based_on('range'),
    casting_time=CastingTimeAspect("1 round"),
    other_aspects={
        'area_effect': AreaEffectAspect('2m radius sphere'),
        "incantation": IncantationsAspect("Mage Inspiration Chant", "litany"),
        "concentration": ConcentrationAspect(measure="1 round"),
    }
)
spells = [ 
    war_blast, war_bolt, battle_shield, dispel, bravery, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(spells)
    app()

