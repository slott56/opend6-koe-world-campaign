"""
FAVOR

When run as an app, generates .RST details of each Miracle.
"""

from magic1 import Aspect, Miracle, detail


invocations = [
    Miracle(
        effect=Aspect(
            format="+ 1D bonus to one non-Extranormal attribute",
            base_difficulty=6,
            count=1,
        ),
        duration=Aspect(format="5 rounds ", base_difficulty=7, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous", base_difficulty=5, count=1),
        casting_time=Aspect(format="2 seconds", base_difficulty=-1, count=1),
        name="Bless Person",
        other_aspects={
            "Difficulty": Aspect(format="11", base_difficulty=0.0, count=1),
        },
        other_conditions=[
            Aspect(
                format="Bonus may not be used to harm anything (-1); limited to humanoids (-2)",
                base_difficulty=-3,
                count=1,
            ),
        ],
        notes="A bless person surrounds and infuses the target character with\nspiritual energy, as long as the target remains within 10 meters of\nthe blessing cleric. The blessing enhances one attribute of the cleric's\nchoosing, which must be selected at the time he performs the bless\xad\ning. The blessed character receives the miracle success bonus to all\nrelated totals.\nA character may enjoy the effects of only one bless at any given\ntime. The cleric may use bless person on himself.\n",
        skill="Favor",
    ),
    Miracle(
        effect=Aspect(format="+2D Armor Value bonus", base_difficulty=9, count=1),
        duration=Aspect(format="8 rounds ", base_difficulty=8, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous", base_difficulty=5, count=1),
        casting_time=Aspect(format="2 seconds", base_difficulty=-1, count=1),
        name="Bless Armor",
        other_aspects={
            "Difficulty": Aspect(format="13", base_difficulty=0.0, count=1),
        },
        other_conditions=[],
        notes="Bless annorinfuses spiritual energy into any armor orgarmentthat\na single character is wearing. as long as the target remains within 10\nmeters of the blessing cleric. The blessed character adds the miracle\nsuccess bonus damage resistance totals.\nA character may enjoy the effects of only one bless at any given\ntime. The cleric may use bless armor on herself.\n",
        skill="Favor",
    ),
    Miracle(
        effect=Aspect(format="1.5 kilograms of food", base_difficulty=1, count=1),
        duration=Aspect(format="4hours ", base_difficulty=21, count=1),
        range=Aspect(format="1 meter or less ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Enhance Food",
        other_aspects={
            "Difficulty": Aspect(format="8", base_difficulty=0.0, count=1),
            "Components": Aspect(
                format="Any kind of food, in any condition (very common)",
                base_difficulty=-2,
                count=1,
            ),
        },
        other_conditions=[],
        notes="Food blessed by this miracle becomes better tasting, more nutri\xad\ntious, and possibly transforms into another food entirely. If not eaten\nwithin 10 minutes of its improvement, the food turns back to its\noriginal condition. (The four-hour duration is about how long it takes\nfor the body to break down the food, so the food needs to remain in\nexistence within the body for at least that long.)\nMinimal or average success turns spoiled meat, rotted vegetables,\nand the like into fresh food again. Good success can cleanse any food\nof any impurities or poisons. Superior success increases the quality\nof the food to the very best possible. Spectacular success actually\ntransforms the food into a different kind of food; changing from\na common fruit to an exotic one, from a cheap cut of pork to an\nexpensive cut of beef, water to wine, and so on.\n",
        skill="Favor",
    ),
    Miracle(
        effect=Aspect(format="healing skill of 5D+2", base_difficulty=17, count=1),
        duration=Aspect(format="1.5 seconds ", base_difficulty=1, count=1),
        range=Aspect(format="1 meter or less or touch ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round", base_difficulty=-4, count=1),
        name="Healing",
        other_aspects={
            "Difficulty": Aspect(format="7", base_difficulty=0.0, count=1),
        },
        other_conditions=[],
        notes="By channeling her spiritual energy to an injured person or creature,\nthe devotee can use this miracle to heal harm as if she had SD+2 in\nthe healing skill. Add the miracle success bonus to the healing total.\n",
        skill="Favor",
    ),
    Miracle(
        effect=Aspect(format="1.5 kilograms of food", base_difficulty=1, count=1),
        duration=Aspect(format="4hours ", base_difficulty=21, count=1),
        range=Aspect(format="1 meter or less ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round", base_difficulty=-4, count=1),
        name="Multiply Food",
        other_aspects={
            "Difficulty": Aspect(format="8", base_difficulty=0.0, count=1),
            "Components": Aspect(
                format="About a kilogram of any kind of edible food (very common)",
                base_difficulty=-2,
                count=1,
            ),
        },
        other_conditions=[],
        notes="The multiplying food invocation is performed on an amount of\nexisting food equal to a decent meal for one normal person. For\neach success level gained, double the amount of food. Any food not\neaten within 10 minutes of its production rots or turns to dust. (As\nwith enhance food, the food needs to be within the body for at least\nfour hours to give the body enough time to break it down and get\nnourishment from it.)\n",
        skill="Favor",
    ),
    Miracle(
        effect=Aspect(
            format="compare to miracle or curse difficulty", base_difficulty=20, count=1
        ),
        duration=Aspect(format="30 minutes ", base_difficulty=16, count=1),
        range=Aspect(format="2.5 meters ", base_difficulty=2, count=1),
        speed=Aspect(format="Instantaneous", base_difficulty=2, count=1),
        casting_time=Aspect(format="30 minutes ", base_difficulty=-16, count=1),
        name="Ritual Of Purification",
        other_aspects={"Difficulty": Aspect(format="12", base_difficulty=0.0, count=1)},
        other_conditions=[],
        notes="The purification ceremony heightens awareness\nof one's religion and removes the impurities of the\nmundane and the material from the spirit. With a\nminimal or average success, it allows the target to\ninvoke one miracle he failed or it removes one curse\n(either magical or miraculous). For any level above\naverage, the target either receives the miracle success\nbonus to any miracle he attempts within the duration\nof the ritual or may add the miracle success bonus\nto the effect's value to allow invocation of one failed\nmiracle or remove any one curse. The difficulty of the\ncurse or failed miracle must be equal to or less than\nthe effect's value (plus the miracle success bonus, if\napplicable) in order for the ritual to work.\n",
        skill="Favor",
    ),
    Miracle(
        effect=Aspect(format="Armor Value of SD+ 1", base_difficulty=16, count=1),
        duration=Aspect(format="5 rounds ", base_difficulty=7, count=1),
        range=Aspect(format="1.5m", base_difficulty=1, count=1),
        speed=Aspect(format="Instantaneous", base_difficulty=1, count=1),
        casting_time=Aspect(format="1.5 seconds ", base_difficulty=-1, count=1),
        name="Spiritual Shield",
        other_aspects={
            "Difficulty": Aspect(format="13", base_difficulty=0.0, count=1),
            "Area effect": Aspect(format="1-meter radius", base_difficulty=2, count=1),
        },
        other_conditions=[],
        notes="If successfully invoked, a shield of spiritual energy,\nabout two meters in diameter, appears up to 1.5\nmeters in frontofthecleric. It offers an Armor Value\nof SD+ 1 against all types of physical (not mental)\nattacks.",
        skill="Favor",
    ),
]


if __name__ == "__main__":
    detail(invocations)


__test__ = {
    "Bless Person": ">>> invocations[0].difficulty\n10",
    "Bless Armor": ">>> invocations[1].difficulty\n13",
    "Enhance Food": ">>> invocations[2].difficulty\n8",
    "Healing": ">>> invocations[3].difficulty\n7",
    "Multiply Food": ">>> invocations[4].difficulty\n8",
    "Ritual Of Purification": ">>> invocations[5].difficulty\n12",
    "Spiritual Shield": ">>> invocations[6].difficulty\n13",
}
