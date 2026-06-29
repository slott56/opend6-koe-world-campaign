"""
Extract Spells from ``system_spells.ipynb``.
Created by V2025.6.27.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "display" argument, generates .RST-formatted details of all the Spells.

With "debug" argument, prints debugging details for selected Spells.

With "test" argument, runs doctest, which uses the __test__ examples.

"""

from opend6_tools.magic import *



cast_chaos = Spell(
        name="Cast Chaos",
        skill="Conjuration",
        notes="The caster can unleash pure chaotic energy  in an attempt\nto simulate a spell. The incantation is cast at a\ndifficulty of 10 plus the simulated spell's difficulty,\nand automatically triggers a chaotic backlash (the GM\nrolls on the Unleashed Chaos Table). If the caster fails\nthe difficulty roll, the GM rolls a second time on the\nUnleashed Chaos Table. The simulated spell is treated\njust as if it had been cast normally (using it's speed,\nrange, area of effect, and duration.)\n",
        effect=GenericEffect(description="Spell being copied plus backlash", difficulty=30),
        duration=DurationAspect.based_on_spell("duration"),
        range=RangeAspect.based_on_spell("range"),
        casting_time=CastingTimeAspect("instant"),
        speed=SpeedAspect.based_on("range", "Instantaneous"),
        other_aspects={
            "area_effect": AreaEffectAspect.based_on_spell("area_effect"),
            "feedback": FeedbackAspect(10),
        },
        other_conditions=[GenericAspect(0, "can unleash chaos effect on failure")],
    )

chaos_burst = Spell(
        name="Chaos Burst",
        skill="Conjuration",
        notes="At the casting of this spell, three bolts of swirling energy\nerupt from the caster's fingertips and streak toward\none target. The spell user must make an attack\nroll for each bolt, but it is treated as a single action.\nEach bolt causes 4D damage. The caster then rolls\nonce on the Unleashed Chaos Table, regardless of his\nsuccess in hitting the target.\n",
        effect=DamageEffect("Bolts of swirling energy", "+4D", "physical damage", "ignores all armor"),
        duration=DurationAspect("instant"),
        range=RangeAspect("30 m"),
        casting_time=CastingTimeAspect("5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "concentration": ConcentrationAspect.based_on("casting_time", "On Target"),
            "gestures": GesturesAspect("Gestures", "complex"),
            "incantation": IncantationsAspect("Incantation", "complex"),
            "charges": ChargesAspect("3 charges"),
            "feedback": FeedbackAspect(10),
            "other_alterant": OtherAlterant(12, "roll once on the Unleashed Chaos Table regardless of success hitting the target"),
        },
        other_conditions=[
            GenericAspect(0, "can unleash chaos effect on failure"),
        ],
    )

chaos_web = Spell(
        name="Chaos Web",
        skill="Conjuration",
        notes="This chaos binding creates hundreds of strands of\nchaotic fiber that interweave themselves into a web\nof magical energy. The spell user must anchor the web\nbetween at least two objects. Anyone touching the\nweb with bare flesh automatically takes 3D damage\n(once per contact) and causes a chaotic backlash (roll\nonce on the Unleashed Chaos Table). Any attack on\nthe web results in an additional chaotic backlash\nWhen the spell ends, the fibers quickly break down\nand fade away, their innate chaos expunged. Note that\nthe caster is not immune to the effects of the web.\n",
        effect=DamageEffect("From touch", "3D", "physical damage"),
        duration=DurationAspect("30 min"),
        range=RangeAspect("20 m"),
        casting_time=CastingTimeAspect("5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "area_effect": GenericAspect(3, "Between two anchors, limit 3m"),
            "concentration": ConcentrationAspect.based_on("casting_time", "On Target"),
            "gestures": GesturesAspect("Gestures", "complex"),
            "incantation": IncantationsAspect("Incantation", "complex"),
            "other_alterant": OtherAlterant(12,
                                            "roll once on the Unleashed Chaos Table regardless of success hitting the target"),
        },
        other_conditions=[GenericAspect(0, "can unleash chaos effect on failure")],
    )

contain_chaos = Spell(
        name="Contain Chaos",
        skill="Alteration",
        notes="If cast within 10 seconds after a chaotic backlash, the\nspell user may capture the energy created by the temporary\nflux in the chaos stream. The spellcaster may\nthen recast the enchantment that caused the backlash\neven if he could not originally cast it.\n",
        effect=GenericEffect(description="Other spell's effect", difficulty=40),
        duration=DurationAspect("instant"),
        range=RangeAspect("40 m"),
        casting_time=CastingTimeAspect("10 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "concentration": ConcentrationAspect.based_on("casting_time", "On Target"),
            "gestures": GesturesAspect("Gestures", "complex"),
            "incantation": IncantationsAspect("Incantation", "complex"),
        },
        other_conditions=[
            GenericAspect(0, "can unleash chaos effect on failure"),
            GenericAspect(0, "within 2 rounds of chaotic backlash"),
        ],
    )

drain = Spell(
        name="Drain",
        skill="Alteration",
        notes="The caster may steal a Character Point from her target\nand use the power to temporarily increase her\nability to cast her next spell (receiving a 2D bonus to\nher spell skill roll against it's difficulty.) Note that the\nbonus applies only to the next spell cast by the spell\nuser. The victim of the incantation feels a dull pain in\nhis chest when the Character Point is sucked away. If\nthe target has no Character Points, he still feels the ache,\nbut the caster does not gain any benefit.\n",
        effect=CompositeEffect(
            "Drain and Use",
            DisadvantageEffect("Drain 1 character point", 6),
            SkillEffect("Increase spell-casting ability", "+2D", "skill modifier"),
        ),
        duration=DurationAspect("30 min"),
        range=RangeAspect("touch"),
        casting_time=CastingTimeAspect("25 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            # "concentration": ConcentrationAspect.based_on("casting_time", "On Target"),
            # "gestures": GesturesAspect("Gestures", "simple"),
            # "incantation": IncantationsAspect("Incantations", "short"),
        },
        other_conditions=[GenericAspect(0, "can unleash chaos effect on failure")],
    )

flash = Spell(
        name="Flash",
        skill="Conjuration",
        notes='This quick enchantment creates a painful burst of light\nthat affects all creatures within the spell\'s area of effect.\nThose affected (i.e., looking in the direction of\nthe light) go blind for 10 seconds (thereby suffering a\n-2D penalty to all actions during that time; see Chapter eight "Combat,"\nfor more information on blindness penalties.)\n',
        effect=DisadvantageEffect("Blindness", 3),
        duration=DurationAspect("10 seconds"),
        range=RangeAspect("1 m"),
        casting_time=CastingTimeAspect("5 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "area_effect": AreaEffectAspect("6m radius sphere"),
            "concentration": ConcentrationAspect.based_on("casting_time", "On Target"),
            "gestures": GesturesAspect("Gestures", "complex"),
            "incantation": IncantationsAspect("Incantations", "complex"),
        },
        other_conditions=[
            GenericAspect(5, "must be facing the caster"),
            GenericAspect(0, "can unleash chaos effect on failure"),
        ],
    )

hesitate = Spell(
        name="Hesitate",
        skill="Alteration",
        notes="Through this incantation, the caster injects a tiny\namount of chaos energy into his victim's body, causing\nthe target's muscles to spasm momentarily. As a\nresult, the target suffers a -3D penalty on his next Agility roll for initiative.\n",
        effect=DisadvantageEffect("Penalty on next Agility roll", 5),
        duration=DurationAspect("1 min"),
        range=RangeAspect("touch"),
        casting_time=CastingTimeAspect("10 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "concentration": ConcentrationAspect.based_on("casting_time", "On Target"),
            "gestures": GesturesAspect("Gestures", "complex"),
            "incantation": IncantationsAspect("Incantations", "phrase"),
        },
        other_conditions=[GenericAspect(0, "can unleash chaos effect on failure")],
    )

netherdart = Spell(
        name="Netherdart",
        skill="Conjuration",
        notes="Upon the casting of this spell, five dark motes of energy\ncoalesce in the caster's hand. The chaos binder\nmay hurl the deadly magic one mote at a time (speed of +1)\nat the same or separate targets (each attack is\ntreated as a separate action.) The caster may choose\nto throw them all at once (incurring the applicable\nmulti-action penalties) or one at a time. A successful\nattack causes 3D in the victim as the black mote burrows\ninto the target's body. Once within, the dark energy\nbegins to suck away the victim's will (subtract one pip\nof a mental attribute one on pip of Endurance for every\n10 seconds the spell remains in effect; the lost pips return\nat the same rate they were lost.)\n",
        effect=DisadvantageEffect(
            "1 pip mental and 1 pip physique each 10 sec.", 9,
        ),
        duration=DurationAspect("1 minute"),
        range=RangeAspect("20 m"),
        casting_time=CastingTimeAspect("15 sec"),
        speed=SpeedAspect.based_on("range"),
        other_aspects={
            "concentration": ConcentrationAspect.based_on("casting_time", "On Target"),
            "gestures": GesturesAspect("Gestures", "complex"),
            "incantation": IncantationsAspect("Incantation", "Litany"),
            "charges": ChargesAspect("5 charges"),
        },
        other_conditions=[GenericAspect(0, "can unleash chaos effect on failure")],
    )

propel = Spell(
        name="Propel",
        skill="Apportation",
        notes="This spell builds up a wave of chaotic energy which\nthe caster feels as an invisible, pulsing force close\nby. At the completion of the incantation, the chaos\nbinder commands the wave to push objects or creatures in any direction.\nThe wave of force can manipulate\na target no less than 1 kilogram and no more\nthan 100 kilograms at a movement rate of up to 10\n(twice as fast as a walking human.) While directing\nthe wave, the caster may not undertake other activities,\nbut must concentrate on the energy to keep it\nfrom dispersing.\n",
        effect=MassEffect("Move", "100 kg"),
        duration=DurationAspect("10 minute"),
        range=RangeAspect("25 m"),
        casting_time=CastingTimeAspect("1 min"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "concentration": ConcentrationAspect.based_on("casting_time", "On Target"),
            "gestures": GesturesAspect("Gestures", "complex"),
            "incantation": IncantationsAspect("Incantation", "Litany"),
        },
        other_conditions=[GenericAspect(0, "can unleash chaos effect on failure")],
    )

sense_magic = Spell(
        name="Sense Residual Magic",
        skill="Divination",
        notes="Magic leaves telltale signs of its use in the form of\nshimmering paths of residual chaos invisible to the\nnaked eye. With this spell, the user attunes her sight\nto the range of chaos waves, enabling her to see these\nstringy paths and follow them to their source. The\ncaster may trail a particular path up to the spell's\narea of effect at which point it gradually fades. If the\noriginal caster has left the area, the trail ends in mid-air.\nThe spellcaster may then cast *Sense Residual Magic* again\nand pick up the trail where it left off, following up the\nlimit of it's area, and so on.\n",
        effect=SkillEffect("Follow magical trail up to 1km away", "+2D"),
        duration=DurationAspect("3 hr"),
        range=RangeAspect("1 km"),
        casting_time=CastingTimeAspect("5 min"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "concentration": ConcentrationAspect.based_on("casting_time", "On Target"),
            "gestures": GesturesAspect("Gestures", "complex"),
            "incantation": IncantationsAspect("Incantations", "litany"),
        },
        other_conditions=[
            GenericAspect(5, "original caster still in the area"),
            GenericAspect(0, "can unleash chaos effect on failure"),
        ],
    )

shroud = Spell(
        name="Shroud",
        skill="Conjuration",
        notes="When the enchantment is cast, a swirling, blotchy\ngray-and-black film encases the spellcaster's body,\ncompletely concealing her features.\n",
        effect=SkillEffect("Concealed: reduces Acumen", "+5D"),
        duration=DurationAspect( "4 hrs"),
        range=RangeAspect("self"),
        casting_time=CastingTimeAspect("5 min"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "concentration": ConcentrationAspect.based_on("casting_time", "On Target"),
            "gestures": GesturesAspect("Gestures", "simple"),
            "incantation": IncantationsAspect("Incantation", "phrase"),
        },
        other_conditions=[GenericAspect(0, "can unleash chaos effect on failure")],
    )

warp_magic = Spell(
        name="Warp Magic",
        skill="Alteration",
        notes="The caster may prevent a spell form occurring (just\nas another spellcaster unleashes an incantation), or\nmay eradicate a spell that has already been cast.\n",
        effect=SkillEffect("Prevent of spell effects", "+5D"),
        duration=DurationAspect("5 min"),
        range=RangeAspect("35 m"),
        casting_time=CastingTimeAspect("1 sec"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "concentration": ConcentrationAspect.based_on("casting_time", "On Target"),
            "gestures": GesturesAspect("Gestures", "complex"),
            "incantation": IncantationsAspect("Incantation", "litany"),
        },
        other_conditions=[
            GenericAspect(0, "can unleash chaos effect on failure"),
            GenericAspect(5, "Other Alterant: Timed to coincide"),
        ],
    )

zeodorics_defense = Spell(
        name="Zed'oric's Defense",
        skill="Alteration",
        notes="Using this incantation, the caster weaves chaos energy\ninto his body. The chaos field absorbs any physical damage\ninflicted upon the character (including magical attacks\nthat physically harm the target), giving a bonus of 1D\nto an Endurance or mental attribute roll to resist damage.\n",
        effect=CompositeEffect(
            "Defend against magic",
            ProtectionEffect("Absorb damage", "5D", "physical damage", "protection modifier"),
            ProtectionEffect("Resist magical effects", "1D", "protection modifier"),
        ),
        duration=DurationAspect("8 hr"),
        range=RangeAspect("self"),
        casting_time=CastingTimeAspect("5 min"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "concentration": ConcentrationAspect.based_on("casting_time", "On Target"),
            "gestures": GesturesAspect("Gestures", "complex"),
            "incantation": IncantationsAspect("Incantations", "litany"),
        },
        other_conditions=[GenericAspect(0, "can unleash chaos effect on failure")],
    )
spells = [ 
    cast_chaos, chaos_burst, chaos_web, contain_chaos, drain, flash, hesitate, netherdart, propel, sense_magic, shroud, warp_magic, zeodorics_defense, 
]

__test__ = {
    
    'chaos_burst': '>>> chaos_burst.difficulty\n16\n',
    
    'chaos_web': '>>> chaos_web.difficulty\n18\n',
    
    'contain_chaos': '>>> contain_chaos.difficulty\n22\n',
    
    'drain': '>>> drain.difficulty\n18\n',
    
    'flash': '>>> flash.difficulty\n14\n',
    
    'hesitate': '>>> hesitate.difficulty\n7\n',
    
    'netherdart': '>>> netherdart.difficulty\n20\n',
    
    'propel': '>>> propel.difficulty\n10\n',
    
    'sense_magic': '>>> sense_magic.difficulty\n14\n',
    
    'shroud': '>>> shroud.difficulty\n9\n',
    
    'warp_magic': '>>> warp_magic.difficulty\n16\n',
    
    'zeodorics_defense': '>>> zeodorics_defense.difficulty\n14\n',
    
    
}


if __name__ == "__main__":
    app = build_app(spells)
    app()

