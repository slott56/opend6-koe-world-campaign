"""
Extract Spells from ``new_keep_spells.ipynb``.
Created by V2025.6.27.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

With "test" argument, runs doctest, which uses the __test__ examples.

"""

from opend6_tools.magic import *



fresh_air = Spell(
    name="Fresh Air",
    effect=SpecialAbilityEffect(SpecialAbilityType.accelerated_healing, 2, "Immediate help to the target"),
    duration=DurationAspect("1 sec"),
    range=RangeAspect("touch"),
    speed=SpeedAspect.based_on('range'),
    casting_time=CastingTimeAspect("1 round"),
    other_aspects={
        "incantation": IncantationsAspect("Air Summoning", "litany"),
    },
)

gust = Spell(
    name="Gust",
    effect=DamageEffect("Attack with powerful blast of air", 2*D, "physical damage"),
    duration=DurationAspect("1 sec"),
    range=RangeAspect("self"),
    speed=SpeedAspect.based_on('range'),
    casting_time=CastingTimeAspect("1 round"),
    other_aspects={
        "area_effect": AreaEffectAspect("20m height 4m radius cone"),
        "incantation": IncantationsAspect("Air Summoning", "litany"),
        "concentration": ConcentrationAspect(measure="1 rounds"),
    },
)

gale_of_wind = Spell(
    name="Gale of Wind",
    effect=DamageEffect("Attack with a relentless blast", 2*D, "physical damage", "ignores all armor"),
    duration=DurationAspect("1 sec"),
    range=RangeAspect("self"),
    speed=SpeedAspect.based_on('range'),
    casting_time=CastingTimeAspect("1 round"),
    other_aspects={
        "area_effect": AreaEffectAspect("20m height 8m radius cone"),
        "incantation": IncantationsAspect("Air Summoning", "litany"),
        "concentration": ConcentrationAspect(measure="1 rounds"),
    },
)

glide = Spell(
    name="Glide",
    effect=SpecialAbilityEffect(SpecialAbilityType.glider_wings, 3, "can glide from a high place or lift off into a very strong wind"),
    notes="The 'wings' are a hazy outline around the target of the spell; speed is typical movement, 10m per round",
    duration=DurationAspect("2 rounds"),
    range=RangeAspect("touch"),
    speed=SpeedAspect.based_on('range'),
    casting_time=CastingTimeAspect("1 round"),
    other_aspects={
        "incantation": IncantationsAspect("Air Summoning", "litany"),
    }
)

cleansing_breeze = Spell(
    name="Cleansing Breeze",
    effect=SpecialAbilityEffect(SpecialAbilityType.environmental_resistance, 4, "survive smoke or air-born poisons"),
    notes="There's little sense of a breeze, but smoke and poison are much less harmful.",
    duration=DurationAspect("2 minutes"),
    range=RangeAspect("touch"),
    speed=SpeedAspect.based_on('range'),
    casting_time=CastingTimeAspect("1 round"),
    other_aspects={
        'area_effect': AreaEffectAspect('4m radius sphere'),
        "incantation": IncantationsAspect("Air Summoning", "litany"),
        "concentration": ConcentrationAspect(measure="1 round"),
    }
)

sense_air = Spell(
    name="Sense Air",
    skill="Acumen",
    effect=SpecialAbilityEffect(SpecialAbilityType.enhanced_sense, 2, "feel movement"),
    duration=DurationAspect("2 minutes"),
    range=RangeAspect("10 m"),
    speed=SpeedAspect.based_on('range'),
    casting_time=CastingTimeAspect("2 rounds"),
    other_aspects={
        "incantation": IncantationsAspect("Air Summoning", "litany"),
        "concentration": ConcentrationAspect(measure="2 minutes"),
    }

)

body_of_mist = Spell(
    name="Body of Mist",
    skill="Physique",
    effect=SpecialAbilityEffect(SpecialAbilityType.intangibility, 2),
    duration=DurationAspect("4 minutes"),
    range=RangeAspect("self"),
    speed=SpeedAspect.based_on('range'),
    casting_time=CastingTimeAspect("2 rounds"),
    other_aspects={
        "incantation": IncantationsAspect("Air Summoning", "litany"),
        "concentration": ConcentrationAspect(measure="2 minutes"),
    },
    other_conditions=[Limitation(LimitationType.side_effect, 2, "double damage from air-based enchantments")]
)

tornado = Spell(
    name="Tornado",
    effect=DamageEffect("Crushing blast of wind", 6 * D, "physical damage", "ignores all armor"),
    duration=DurationAspect("1 sec"),
    range=RangeAspect("self"),
    speed=SpeedAspect.based_on('range'),
    casting_time=CastingTimeAspect("3 rounds"),
    other_aspects={
        "area_effect": AreaEffectAspect("20m height 8m radius cone"),
        "incantation": IncantationsAspect("Air Summoning", "litany"),
        "concentration": ConcentrationAspect.based_on('casting_time'),
        "feedback": FeedbackAspect(10),
    },
)
spells = [ 
    fresh_air, gust, gale_of_wind, glide, cleansing_breeze, sense_air, body_of_mist, tornado, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(spells)
    app()

