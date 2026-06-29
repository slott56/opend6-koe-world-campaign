"""
Extract Spells from ``fantasy_miracle_FAVOR.ipynb``.
Created by V2025.6.27.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

With "test" argument, runs doctest, which uses the __test__ examples.

"""

from opend6_tools.magic import *



bless_person = Miracle(
        name="Bless Person",
        skill="Favor",
        notes="A bless person surrounds and infuses the target character with\nspiritual energy, as long as the target remains within 10 meters of\nthe blessing cleric. The blessing enhances one attribute of the cleric's\nchoosing, which must be selected at the time he performs the bless\xad\ning. The blessed character receives the miracle success bonus to all\nrelated totals.\nA character may enjoy the effects of only one bless at any given\ntime. The cleric may use bless person on himself.\n",
        effect=SkillEffect("bonus to three non-Extranormal attributes", "+3D", "attribute modifier"),
        duration=DurationAspect("5 rounds"),
        range=RangeAspect("10 meters"),
        speed=SpeedAspect.based_on(("range",), ""),
        casting_time=CastingTimeAspect("2 seconds"),
        other_aspects={},
        other_conditions=[
            GenericAspect(
                -1,
                "Bonus may not be used to harm anything",
            ),
            GenericAspect(
                -2,
                "limited to humans",
            ),
            GenericAspect(0, "Difficulty: 11"),
        ],
    )

bless_armor = Miracle(
        name="Bless Armor",
        skill="Favor",
        notes="Bless annorinfuses spiritual energy into any armor orgarmentthat\na single character is wearing. as long as the target remains within 10\nmeters of the blessing cleric. The blessed character adds the miracle\nsuccess bonus damage resistance totals.\nA character may enjoy the effects of only one bless at any given\ntime. The cleric may use bless armor on herself.\n",
        effect=SkillEffect("Armor Value bonus", "+2D", "protection modifier"),
        duration=DurationAspect("8 rounds"),
        range=RangeAspect("10 meters"),
        speed=SpeedAspect.based_on(("range",), ""),
        casting_time=CastingTimeAspect("2 seconds"),
        other_aspects={},
        other_conditions=[GenericAspect(0, "Difficulty: 13")],
    )

enhance_food = Miracle(
        name="Enhance Food",
        skill="Favor",
        notes="Food blessed by this miracle becomes better tasting, more nutritious, and possibly transforms into another food entirely. If not eaten\nwithin 10 minutes of its improvement, the food turns back to its\noriginal condition. (The four-hour duration is about how long it takes\nfor the body to break down the food, so the food needs to remain in\nexistence within the body for at least that long.)\nMinimal or average success turns spoiled meat, rotted vegetables,\nand the like into fresh food again. Good success can cleanse any food\nof any impurities or poisons. Superior success increases the quality\nof the food to the very best possible. Spectacular success actually\ntransforms the food into a different kind of food; changing from\na common fruit to an exotic one, from a cheap cut of pork to an\nexpensive cut of beef, water to wine, and so on.\n",
        effect=CompositeEffect(
            "Enhancements",
            GenericEffect("restore 3D of rot", (3*D).measure),
            GenericEffect("purify 2D of impurity", (2*D).measure),
            MassEffect("mass of food", "2 kilograms"),
        ),
        duration=DurationAspect("4 hours"),
        range=RangeAspect("self"),
        speed=SpeedAspect.based_on(("range",), ""),
        casting_time=CastingTimeAspect("1 round"),
        other_aspects={
            "components": ComponentsAspect(
                "Any kind of food, in any condition", "very common"
            )
        },
        other_conditions=[GenericAspect(0, "Difficulty: 8")],
    )

healing = Miracle(
        name="Healing",
        skill="Favor",
        notes="By channeling her spiritual energy to an injured person or creature,\nthe devotee can use this miracle to heal harm as if she had 6D+1 in\nthe healing skill. Add the miracle success bonus to the healing total.\n",
        effect=SkillEffect("healing skill", "+6D+1", "skill modifier"),
        duration=DurationAspect("1.5 seconds"),
        range=RangeAspect("self"),
        speed=SpeedAspect.based_on(("range",), ""),
        casting_time=CastingTimeAspect("1 round"),
        other_aspects={},
        other_conditions=[GenericAspect(0, "Difficulty: 7")],
    )

multiply_food = Miracle(
        name="Multiply Food",
        skill="Favor",
        notes="The multiplying food invocation is performed on an amount of\nexisting food equal to a decent meal for one normal person. For\neach success level gained, double the amount of food. Any food not\neaten within 10 minutes of its production rots or turns to dust. \n(As with enhance food, the food needs to be within the body for at least\nfour hours to give the body enough time to break it down and get\nnourishment from it.)\n",
        effect=CompositeEffect(
            "Multiplication",
            GenericEffect("proper balance of elements 4D", (4*D).measure),
            MassEffect("mass of food", "2 kilograms"),
        ),
        duration=DurationAspect("4 hours"),
        range=RangeAspect("self"),
        speed=SpeedAspect.based_on(("range",), ""),
        casting_time=CastingTimeAspect("1 round"),
        other_aspects={
            "components": ComponentsAspect(
                "About a kilogram of any kind of edible food", "very common"
            )
        },
        other_conditions=[GenericAspect(0, "Difficulty: 8")],
    )

purification = Miracle(
        name="Ritual Of Purification",
        skill="Favor",
        notes="The purification ceremony heightens awareness\nof one's religion and removes the impurities of the\nmundane and the material from the spirit. With a\nminimal or average success, it allows the target to\ninvoke one miracle he failed or it removes one curse\n(either magical or miraculous). For any level above\naverage, the target either receives the miracle success\nbonus to any miracle he attempts within the duration\nof the ritual or may add the miracle success bonus\nto the effect's value to allow invocation of one failed\nmiracle or remove any one curse. The difficulty of the\ncurse or failed miracle must be equal to or less than\nthe effect's value (plus the miracle success bonus, if\napplicable) in order for the ritual to work.\n",
        effect=GenericEffect(description="compare to miracle or curse difficulty", difficulty=20),
        duration=DurationAspect("30 minutes"),
        range=RangeAspect("2.5 meters"),
        speed=SpeedAspect.based_on(("range",), ""),
        casting_time=CastingTimeAspect("30 minutes"),
        other_aspects={},
        other_conditions=[GenericAspect(0, "Difficulty: 12")],
    )

spiritual_shield = Miracle(
        name="Spiritual Shield",
        skill="Favor",
        notes="If successfully invoked, a shield of spiritual energy,\nabout two meters in diameter, appears up to 1.5\nmeters in front of the cleric. It offers an Armor Value\nof 5D+ 1 against all types of physical (not mental)\nattacks.",
        effect=GenericEffect(description="Armor Value of 5D+ 1", difficulty=16),
        duration=DurationAspect("5 rounds"),
        range=RangeAspect("1.5 m"),
        speed=SpeedAspect.based_on(("range",), ""),
        casting_time=CastingTimeAspect("1.5 seconds"),
        other_aspects={"area_effect": AreaEffectAspect("1 meter radius circle")},
        other_conditions=[GenericAspect(0, "Difficulty: 13")],
    )

shield_from_evil = Miracle(
        name="Shield from Evil",
        skill="Favor",
        notes="If successfully invoked, a glamor around the cleric boosts their apparent charisma to those with malicious intent; this can often thwart them",
        effect=AttributeEffect("Charima boost", 5*D),
        duration=DurationAspect("5 minutes"),
        range=RangeAspect("self"),
        speed=SpeedAspect.based_on(("range",), ""),
        casting_time=CastingTimeAspect("3 seconds"),
        other_aspects={},
        other_conditions=[
            GenericAspect(2, "Only agaist those with malicious intent"),
            GenericAspect(0, "Difficulty: 7"),
        ],
    )
spells = [ 
    bless_person, bless_armor, enhance_food, healing, multiply_food, purification, spiritual_shield, shield_from_evil, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(spells)
    app()

