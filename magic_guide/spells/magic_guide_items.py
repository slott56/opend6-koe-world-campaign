"""
Extract Spells from ``magic_guide_items.ipynb``.
Created by V2025.6.27.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

With "test" argument, runs doctest, which uses the __test__ examples.

"""

from opend6_tools.magic import *



enchant_weapon = Spell(
    name="Enchant Weapon",
    notes="""
The enchanting of even the weakest of magical weapons can be a daunting task for a mage. Draining mentally, emotionally, physically, and magically, it’s no wonder that there’s always a hesitancy to create such weapons. Nonetheless, such things are produced, and there are mages willing to sacrifice their lives for the creation of the prefect weapon, particularly when it is designed with a specific goal in mind.
    """,
    skill="Alteration",
    effect=DamageEffect(1*D, "damage", ),
    range=RangeAspect("touch"),
    speed=SpeedAspect.based_on('range', 'instantaneous'),
    duration=DurationAspect("60 years"),
    casting_time=CastingTimeAspect("1 hour"),
    other_aspects={
        "concentration": ConcentrationAspect("1 hour"),
        "feedback": FeedbackAspect(-2),
        "focused": FocusedAspect(10, "on weapon"),
        "incantations": IncantationsAspect("repeat phrase for duration of casting", "litany"),
        "arcane_knowledge": ArcaneKnowledgeAspect("metal, magic")
    }
)

magic_weapon = Spell(
    name="Magic Weapon",
    notes="""
A faint blue glow embodies the weapon being enchanted when this spell is cast. This transforms the normal into the enchanted, making it possible to do damage to those creatures that are invulnerable to normal weapons. Furthermore, the spell ignores nonmagical armor. When successfully cast, the target weapon gains a +3D damage bonus.
    """,
    skill="Alteration",
    effect=DamageEffect(3*D, "damage bonus", "ignore non magical armor"),
    range=RangeAspect("25 m"),
    speed=SpeedAspect.based_on('range', 'instantaneous'),
    duration=DurationAspect("1 day"),
    casting_time=CastingTimeAspect("1 round"),
    other_aspects={
        "components": ComponentsAspect("precious gem", "uncommon"),
        "countenance": CountenanceAspect("noticeable", "target has a faint glow"),
        "focused": FocusedAspect(10, "on weapon"),
        "gestures": GesturesAspect("swinging motion", "simple"),
        "arcane_knowledge": ArcaneKnowledgeAspect("metal, magic")
    }
)
spells = [ 
    enchant_weapon, magic_weapon, 
]

__test__ = {
    
    'enchant_weapon': '>>> enchant_weapon.difficulty\n15\n',
    
    'magic_weapon': '>>> magic_weapon.difficulty\n26\n',
    
    
}


if __name__ == "__main__":
    app = build_app(spells)
    app()

