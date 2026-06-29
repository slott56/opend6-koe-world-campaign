"""
DIVINATION SPELLS

When run as an app, generates .RST details of each Spell.
"""

from magic1 import Aspect, Spell, detail


spells = [
    Spell(
        effect=Aspect(
            format="search of 8D to locate a single type of creature",
            base_difficulty=24,
            count=1,
        ),
        duration=Aspect(format="10 seconds ", base_difficulty=5, count=1),
        range=Aspect(format="Self", base_difficulty=0.0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        name="Detect the Living",
        other_aspects={
            "Difficulty": Aspect(format="14", base_difficulty=0.0, count=1),
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
                format="Bending (can't see t.arget)", base_difficulty=4, count=1
            ),
        },
        other_conditions=[],
        notes="Before throwing the spell, the caster should decide what sort of being\nshe's looking for, because she'll need a piece of it for the spell to work\n(a lock of hair from a Human, fur or fangs from an animal, etc.).\nThe caster sets the object on fire and inhales the smoke while cocentrating.\nOnce thecasting is done, the mage can detect the presence\nof any such being within a 10-meterradius for two rounds. The higher\nthe search skill total is above the difficulty, the more information the\ncaster knows about the beings she seeks (such as location, number,\ngender, etc.). The difficulty st.arts at 10 for a Human-sized creature,\nand goes down for larger creatures, up for smaller ones, and up for\nthe number of other types of creatures in the area.\n",
        skill="Divination",
    ),
    Spell(
        effect=Aspect(format="2.5 months", base_difficulty=34, count=1),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="Scrying object ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="2 rounds", base_difficulty=-5, count=1),
        name="Scrying",
        other_aspects={
            "Difficulty": Aspect(format="11", base_difficulty=0.0, count=1),
            "Components": Aspect(
                format="Scrying tool with images or symbols (tarot cards, playing cards, runes, etc.) (uncommon); item the person owned for at least a month or the person herself (very rare)",
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
            Aspect(format="Physical cont.act with tool", base_difficulty=-1, count=1),
        ],
        notes="By interpreting cards or runes, the diviner gains a sense of what\nthe future holds for the person who the reading is about. The mage\nmay choose to look for a condition that could occur up to two and\na half months into the future. She can see one minute's worth of\nthe future. Use the result points of the divination roll to determine\nhow much information she receives: Zero points reveals confusing\nimages. One to four points allows one useful fact to be gleaned from\nthe reading. Five to eight points tells the mage a few useful facts,\nincluding the time of the occurrence. Nine to 12 points allows the\nmage to note more details, including time and location. Thirteen\nor more points lets the mage see the scene as if she were present,\nthough in shades of gray.\n",
        skill="Divination",
    ),
    Spell(
        effect=Aspect(format="66 weeks in past", base_difficulty=38, count=1),
        duration=Aspect(format="66 minutes", base_difficulty=18, count=1),
        range=Aspect(format="Touch ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="25 minutes ", base_difficulty=-16, count=1),
        name="Sense Past",
        other_aspects={
            "Difficulty": Aspect(format="25", base_difficulty=0.0, count=1),
            "Area Effect": Aspect(
                format="Sphere with a radius of 5m", base_difficulty=25
            ),
            "Concentration": Aspect(
                format="10 minutes with a mettle difficulty of 11", base_difficulty=-5
            ),
            "Components": Aspect(
                format="Magnifying glass (uncommon), expensive pocket watch (very rare)",
                base_difficulty=-9,
            ),
            "Countenance": Aspect(
                format="Skin turns sickly gray color for duration of spell",
                base_difficulty=-1,
            ),
        },
        other_conditions=[
            Aspect(format="Physical contact with object", base_difficulty=-1),
        ],
        notes="The mage can learn about the past of a single object he touches.\nHe'll see visions of events that occurred in a five-meter radius around\nthe object in the past. The mage can view events that took place in\na past period of time whose value (as read on the \"Spell Measures\"\nt.able) is less than or equal to the effect's value plus the result points\nbonus. The mage can scan back to that period at a rate of one week's\nworth of images per minute of the spell.",
        skill="Divination",
    ),
]


if __name__ == "__main__":
    detail(spells)


__test__ = {
    "Detect the Living": ">>> spells[0].difficulty\n14",
    "Scrying": ">>> spells[1].difficulty\n11",
    "Sense Past": ">>> spells[2].difficulty\n25",
}
