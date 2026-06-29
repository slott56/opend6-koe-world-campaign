"""
fantasy_DIVINATION

When run as an app, generates .RST details of each Spell.
"""

from magic2 import *


spells = [
    Spell(
        name="Detect the Living",
        skill="Divination",
        notes=[
            "Before throwing the spell, the caster should decide what sort of being she’s looking for, because she’ll need a piece of it for the spell to work (a lock of hair from a Human, fur or fangs from an animal, etc.).",
            "The caster sets the object on fire and inhales the smoke while concentrating. Once the casting is done, the mage can detect the presence of any such being within a 10-meter radius for two rounds. The higher the search skill total is above the difficulty, the more information the caster knows about the beings she seeks (such as location, number, gender, etc.). The difficulty starts at 10 for a Human-sized creature, and goes down for larger creatures, up for smaller ones, and up for the number of other types of creatures in the area.",
        ],
        effect=SkillEffect("search to locate a single type of creature", "8D"),
        duration=DurationAspect(measure="10 sec"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 min"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            'area_effect': AreaEffectAspect("10 meter radius circle"),
            "component": CompositeAspect(
                ComponentsAspect("Something from the type of creature being detected", "uncommon; destroyed"),
                ComponentsAspect("fire, such as a match or lit coal", "very common; destroyed"),
            ),
            "concentration": ConcentrationAspect("25 seconds", note="mettle difficulty of 9"),
            "gesture": GesturesAspect("Inhale smoke", "very simple"),
            "variable_movement": VariableMovementAspect("target invisible")
        },
        other_conditions=[],
    ),

    Spell(
        name="Scrying",
        skill="Divination",
        notes=[
            "By interpreting cards or runes, the diviner gains a sense of what the future holds for the person who the reading is about. The mage may choose to look for a condition that could occur up to two and a half months into the future. She can see one minute’s worth of the future. Use the result points of the divination roll to determine how much information she receives: Zero points reveals confusing images. One to four points allows one useful fact to be gleaned from the reading. Five to eight points tells the mage a few useful facts, including the time of the occurrence. Nine to 12 points allows the mage to note more details, including time and location. Thirteen or more points lets the mage see the scene as if she were present, though in shades of gray."
        ],
        effect=TimeEffect("view the past", "2.5 months"),
        duration=DurationAspect(measure="1 min"),
        range=RangeAspect("touch"),  # (difficulty=0, description="Scrying object"),
        casting_time=CastingTimeAspect(measure="2 rounds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "components": CompositeAspect(
                ComponentsAspect("Scrying tool with images or symbols (tarot cards, playing cards, runes, etc.)", "uncommon"),
                ComponentsAspect("item the person owned for at least a month or the person herself", "very rare"),
            ),
            "gesture": GesturesAspect(
                "Randomize the tool and place parts of the tool in a set pattern, then interpret the symbols.",
                "simple; challenging (scholar difficulty of 15)"
            ),
        },
        other_conditions=[GenericAspect(difficulty=-1, description="Physical contact with tool")],
    ),

    Spell(
        name="Sense Past",
        skill="Divination",
        notes=[
            "The mage can learn about the past of a single object he touches. He’ll see visions of events that occurred in a five-meter radius around the object in the past. The mage can view events that took place in a past period of time whose value (as read on the “Spell Measures” table) is less than or equal to the effect’s value plus the result points bonus. The mage can scan back to that period at a rate of one week’s worth of images per minute of the spell."
        ],
        effect=TimeEffect("view the past", "66 weeks"),
        duration=DurationAspect(measure="66 min"),
        range=RangeAspect(measure="touch"),
        casting_time=CastingTimeAspect(measure="25 min"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "area_effect": AreaEffectAspect("5 meter radius sphere"),
            "concentration": ConcentrationAspect("10 minutes", note="mettle difficulty of 11"),
            "components": CompositeAspect(
        ComponentsAspect("Magnifying glass", "uncommon"),
                ComponentsAspect("expensive pocket watch", "very rare"),
            ),
            "countenance": CountenanceAspect("Skin turns sickly gray color for duration of spell", "noticeable"),
        },
        other_conditions=[
            GenericAspect(difficulty=-1, description="Physical contact with object"),
        ],
    ),

]


if __name__ == "__main__":
    detail(spells)

__test__ = {
    "Detect the Living": ">>> spells[0].difficulty\n14",
    "Scrying": ">>> spells[1].difficulty\n10",  # Rules say 11
    "Sense Past": ">>> spells[2].difficulty\n25",
}
