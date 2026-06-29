"""
Photomancy
----------

"""

from magic1 import Aspect, Spell, detail

spells = [
    Spell(
        effect=Aspect(
            format="negates up to 4D of darkness modifier", base_difficulty=12, count=1
        ),
        duration=Aspect(format="5 rounds ", base_difficulty=7, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="2.5 seconds ", base_difficulty=-2, count=1),
        name="Aura of Visibility",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Light", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="10", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Owl feather (common, destroyed)", base_difficulty=-6, count=1
            ),
            "Focused": Aspect(format="On target", base_difficulty=3, count=1),
            "Gestures": Aspect(
                format="Wave feather before his eyes while looking at intended target (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Lift the shroud of darkness that I might see my enemy” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes="With an intended target in sight and not more than 10\nmeters distant, the magic user waves an owl’s feather before\nhis eyes several times and utters an incantation. The feather\nis then consumed in a brilliant, momentary flash of fire. Now\nthe target creature is bathed in an aura of shimmering white\nlight that only the magic user can see. The aura is so bright\nthat it negates up to -4D of darkness modifier (including the\neffects of fog, smoke, and mist), allowing the mage to see\nand attack the creature without penalty in even the most\ncomplete darkness.\n\n",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(format="Blur (R2) Special Ability", base_difficulty=18, count=1),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="Self or 1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Blur",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Darkness, Folk", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="11", base_difficulty=0, count=1),
            "Focused": Aspect(format="On target", base_difficulty=5, count=1),
            "Gestures": Aspect(
                format="Wipe palm over eyes (simple)", base_difficulty=-1, count=1
            ),
            "Unreal Effect": Aspect(
                format="Disbelief difficulty of 13", base_difficulty=-5, count=1
            ),
        },
        notes="With a casual swipe of a hand over his eyes, the mage\n(or his chosen target) becomes indistinct to the naked eye\nby bending light over his form. For a period of one minute,\nthe mage adds 2 to his dodge, stealth/sneak, and hide totals,\nas +2 to all default search, tracking, investigation, and attack\ndifficulties against the mage. As this is an illusory spell,\ncharacters may disbelieve the effects with a mettle/willpower\nroll of 13. Those who succeed are thereafter able to see the\nmage distinctly.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="Infamy (R2), feared by most because of glowing eyes",
            base_difficulty=6,
            count=1,
        ),
        duration=Aspect(format="4 hours ", base_difficulty=21, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="2 round ", base_difficulty=-5, count=1),
        name="Glowing Eyes",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Light", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="16", base_difficulty=0, count=1),
            "Concentration": Aspect(
                format="1 round with willpower/mettle difficulty of 8",
                base_difficulty=-2,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=5, count=1),
            "Feedback": Aspect(
                format="-3 to damage resistance total", base_difficulty=-3, count=1
            ),
        },
        notes="With a minimal amount of pain to himself, the caster curses\na target with glowing eyes, thereby giving the creature the\nlook of that which is demon possessed or otherwise infernal\nin nature. This makes it extremely difficult for the afflicted\nto interact successfully with other beings, as people become\nill at ease by his unnatural appearance. The target has no\nmeans of knowing that he has been cursed except perhaps\nby looking in a mirror or other reflective surface.\nIn some cases, the spell may actually incur a bonus. If\nthe mage wanted to pass himself off as a demon or use it\nagainst extremely superstitous folk, for example, it might\nprovide some minor skill total bonuses (determined by the\ngamemaster).",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="Hindrance: Blindness (R15), +5 to difficulties of all sight-dependent actions",
            base_difficulty=45,
            count=1,
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="3.5 seconds ", base_difficulty=-3, count=1),
        name="Holy Light",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Light", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="35", base_difficulty=0, count=1),
            "Gestures": Aspect(
                format="With head titled back and eyes closed as if basking in the sun’s warmth, extend arms out to the sides (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“The sun abhors darkness, and evil cowers from the light that is goodness.” (sentence, loud)",
                base_difficulty=-3,
                count=1,
            ),
            "Multiple Targets": Aspect(
                format="Up to 5 targets", base_difficulty=15, count=1
            ),
        },
        other_conditions=[
            Aspect(
                format="Only affects evil or undead beings who can see the caster",
                base_difficulty=-2,
                count=1,
            )
        ],
        notes="When cast, the magic user creates a bright flare of light\nthat seems to emanate from his being. Up to five evil or\nundead targets within range and looking at the caster are\nblinded by this light. All sight-based actions for the affected\nincrease by +5 for one minute.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="Armor Value of 6D, physical only", base_difficulty=18, count=1
        ),
        duration=Aspect(format="1 week ", base_difficulty=29, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="3.5 minutes ", base_difficulty=-12, count=1),
        name="Light Chest",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Light, Dimension", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="20", base_difficulty=0, count=1),
            "Area of Effect": Aspect(
                format="Cuboid with height of 1 meter and sides of 2 meters",
                base_difficulty=5,
                count=1,
            ),
            "Components": Aspect(
                format="Crystal cube (very rare, destroyed); small glass disc (very common)",
                base_difficulty=-12,
                count=1,
            ),
            "Concentration": Aspect(
                format="5 seconds with a willpower/mettle difficulty of 8",
                base_difficulty=-2,
                count=1,
            ),
            "Focused": Aspect(format="On glass disc", base_difficulty=9, count=1),
            "Gestures": Aspect(
                format="Hold crystal cube and disk in outstretched hands to catch the light, then place it at feet (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Chest of light, secure what’s mine by right.” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
            "Variable Duration": Aspect(
                format="On/off switch with password set by mage",
                base_difficulty=8,
                count=1,
            ),
            "Other Alterants": Aspect(
                format="Can be carried; resistant to adverse environmental conditions (dust, rain, heat, etc.)",
                base_difficulty=2,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="A source of illumination is present",
                base_difficulty=-1,
                count=1,
            )
        ],
        notes="The magic user casts this spell on a glass disc and a finely\ncrafted cube of crystal, which is destroyed and replaced by a\nchest of radiant light. The chest had no weight, but its walls\nand lid are solid and it can be moved.\nWhen the spell is cast, the mage selects a password, and the\nchest cannot be opened by any creature, including the mage,\nunless the password is first spoken. Efforts at lockpicking are\nfutile. Any item, or combination of items, measuring less than\nfour cubic meters can be stored within the magical chest.\nThe chest lasts for one week and then disappears, leaving\nbehind the glass disk and any items that had been stored\nwithin.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="4D physical damage; Reduced Attribute: Agility/Reflexes (R7), -2D to the attribute",
            base_difficulty=33,
            count=1,
        ),
        duration=Aspect(format="1 round ", base_difficulty=4, count=1),
        range=Aspect(format="15 meters ", base_difficulty=6, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=6, count=1),
        casting_time=Aspect(format="1.5 seconds ", base_difficulty=-1, count=1),
        name="Light Ram",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Light, Inanimate Forces", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(
                format="17", base_difficulty=0, count=1
            ),  # Should be 18
            "Components": Aspect(
                format="Horn or tusk of a charging animal (common); tuff of wool (very common, destroyed)",
                base_difficulty=-7,
                count=1,
            ),
            "Countenance": Aspect(
                format="Mage appears drained and winded", base_difficulty=-1, count=1
            ),
            "Feedback": Aspect(
                format="-3 to damage resistance totals", base_difficulty=-3, count=1
            ),
            "Gestures": Aspect(
                format="Tuff of wool is released into the air and the horn violently shaken at the target (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Unleash the might of light.” (phrase)",
                base_difficulty=-1,
                count=1,
            ),
            "Other Alterant": Aspect(
                format="Effect appears as a powerful, charging animal",
                base_difficulty=1,
                count=1,
            ),
        },
        notes="To cast this spell, the mage releases a tuff of wool into the\nair (which is subsequently consumed by flame), shakes a ram’s\nhorn at an individual target, and utters a simple incantation.\nImmediately thereafter, a shimmering mass of glowing light\nappears, which vaguely discernible as a ram (or, in cultures\nwhere more appropriate, a bull, bison, elephant, or other\npowerful animal known for charging enemies). When this\nunleashed force strikes a target within 15 meters, it deals\n4D damage.\nThe force of the blow is overwhelming; targets hit by the\nspell feel as if they have indeed been impacted by a raging\nram and are staggered, if not thrown back. As a result, a\ncharacter struck by the spell is also subject to a 2D penality\nto Agility/Reflexes-related actions until the target’s turn in\nthe next round.\nIn addition to being used as a weapon, light ram can also\nbe used to batter down doors it strikes. This is particularly\nhandy during dungeon and building explorations.\nThe mage must succeed with a marksmanship/firearms or\napportation roll to hit the target.\n\n",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="lights with charm/persuasion of 5D+1", base_difficulty=16, count=1
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="60 meters ", base_difficulty=9, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=9, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Light Show",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Light", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="14", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Jar of fireflies or similar glowing insects (uncommon, destroyed)",
                base_difficulty=-8,
                count=1,
            ),
            "Gestures": Aspect(
                format="Point finger at target and release fireflies (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Watch and be amazed.” (phrase)", base_difficulty=-1, count=1
            ),
        },
        notes="To cast this spell, the mage must have a jar of living fireflies\nor similar insects. He simply says a few words of power, points\na finger at the target, and releases the fireflies (which die upon\nthe spell expiring). For a period of one minute, the fireflies\nbecome flashing, dancing orbs of glowing light, many times\ngreater in intensity than normal and far more enthralling.\nShould the target fail an opposed interaction roll against\nthe light’s charm/persuasion of 5D+1, the target of the spell\nis compelled to do nothing but watch them.\nIf the entranced creature is harmed, it recovers its senses\nand is no longer affected by the spell.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="lights with charm/persuasion of 5D", base_difficulty=15, count=1
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="100 meters ", base_difficulty=10, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=10, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Mass Light Show",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Light", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="24", base_difficulty=0, count=1),
            "Area of Effect": Aspect(
                format="10-meter radius circle", base_difficulty=20, count=1
            ),
            "Components": Aspect(
                format="Jar of fireflies or similar glowing insects (uncommon, destroyed)",
                base_difficulty=-8,
                count=1,
            ),
            "Gestures": Aspect(
                format="Point finger at target and release fireflies (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Watch and be amazed, one and all” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes="After saying a few words of power and pointing a finger at\nthe center of the intended 10-meter circle area of effect, she\nreleases the fireflies (which die upon the spell expiring). For\na period of one minute the fireflies become flashing, dancing\norbs of bright, enthralling light. All living creatures within\nthe area of effect must make an opposed interaction roll\nagainst the spell’s charm/persuasion of 5D or be compelled to\ndo nothing but watch them. Harming any entranced creature\nbreaks the spell.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="+4D to search", base_difficulty=18, count=1),
        duration=Aspect(format="4 hours ", base_difficulty=21, count=1),
        range=Aspect(
            format="Self or target within 1 meter ", base_difficulty=0, count=1
        ),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Night Vigilance",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Darkness", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="15", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Owl’s eye (uncommon, destroyed)", base_difficulty=-8, count=1
            ),
            "Focused": Aspect(format="On target", base_difficulty=7, count=1),
            "Gestures": Aspect(
                format="Pass the owl eye over the eyes of the target",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“See better.” (phrase)", base_difficulty=-1, count=1
            ),
        },
        other_conditions=[
            Aspect(format="Can only be cast at night", base_difficulty=-1, count=1)
        ],
        notes="This spell uses an owl’s eye to increase the nighttime\nvigilance and acuity of a single individual. The mage utters\na short phrase while passing the component over the eyes\nof the intended target. When the spell is cast, the owl’s eye\nturns to dust.\nThe subject of this spell becomes extremely attuned to the\nnight and unusually aware of his surroundings for a period\nof four-hours. During this time, the character gains a search\nbonus of +5D. However, this spell in no way reduces the need\nfor sleep or the negative effects resulting from lack of rest.\nThe target of the spell must still sleep 4+ hours or suffer the\neffects of fatigue.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="Quirk (R3), nyctophobia with Very Difficult will-power/mettle roll to overcome",
            base_difficulty=9,
            count=1,
        ),
        duration=Aspect(format="10 minutes ", base_difficulty=14, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="2 round ", base_difficulty=-5, count=1),
        name="Nyctophobia",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Darkness, Folk", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(
                format="19", base_difficulty=0, count=1
            ),  # Should be 13
            "Concentration": Aspect(
                format="1 round with willpower/mettle difficulty of 8",
                base_difficulty=-2,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=4, count=1),
            "Feedback": Aspect(
                format="-3 to damage resistance total", base_difficulty=-3, count=1
            ),
        },
        other_conditions=[
            Aspect(format="Limited to sentient beings", base_difficulty=-1, count=1)
        ],
        notes="Though the caster of this spell endures some pain to herself\n, she curses a person with a severe case of nyctophobia\n(fear of the dark or night) for 10 minutes. Characters that\nare overcome by their fright dissolve into quivering wrecks.\nThey can take no actions until the darkness is eliminated or\nthey’re removed from the darkened environment (at which\npoint they may make another attempt to overcome the\nfright using willpower/mettle or the default attribute). The\nexpiration of the spell’s duration immediately returns the\ntarget to normal.\n\n",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="difficulty to view hidden area or dispel darkness shrouding it",
            base_difficulty=20,
            count=1,
        ),
        duration=Aspect(format="1 year ", base_difficulty=38, count=1),
        range=Aspect(format="2.5 meters ", base_difficulty=2, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=2, count=1),
        casting_time=Aspect(format="1 hour ", base_difficulty=-18, count=1),
        name="Shadow Surface",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Darkness", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="27", base_difficulty=0, count=1),
            "Area of Effect": Aspect(
                format="Sphere with 3-meter radius and shape decided on at casting",
                base_difficulty=18,
                count=1,
            ),
            "Components": Aspect(
                format="Stick of charcoal (very common, destroyed)",
                base_difficulty=-4,
                count=1,
            ),
            "Countenance": Aspect(
                format="Caster develops dark rings under eyes during casting time",
                base_difficulty=-1,
                count=1,
            ),
            "Gestures": Aspect(
                format="Outline the area of effect with charcoal (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="Limited to areas continuously in darkness or shadow",
                base_difficulty=-2,
                count=1,
            )
        ],
        notes="Shadow surface allows a mage to create illusionary walls,\nfloors, ceilings, or other surfaces out of darkness. To cast\nit, the wizard outlines the illusionary surface’s dimensions\nwith a charcoal stick.\nThe surface appears absolutely real when viewed, but\nphysical objects may pass through it effortlessly. The spell\nis often used to mask doors, pits, or traps within tombs,\nfortresses, or other areas intended to be secure. Touch or\nprobing searches  always reveal the true nature of the surface,\nthough they do not cause the illusion to disappear. The only\nmeans by which the illusion might be removed, save for its\nduration expiring, is by exposure to a light source strong\nenough to negate it.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="Armor Value of 4D, physical only", base_difficulty=12, count=1
        ),
        duration=Aspect(format="2.5 hours ", base_difficulty=20, count=1),
        range=Aspect(
            format="Self or target within 1 meter ", base_difficulty=0, count=1
        ),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Shroud of Shade",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Darkness, light, entity", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="10", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Fragment of a funeral shroud from an occupied grave (uncommon, destroyed).",
                base_difficulty=-8,
                count=1,
            ),
            "Gestures": Aspect(
                format="Hold shroud fragment over the target’s head (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=6, count=1),
            "Incantations": Aspect(
                format="“Dark force rising, protect thee from the light.” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="Limited to those creatures physically harmed by exposure to sunlight or bright light; only protects against light",
                base_difficulty=-3,
                count=1,
            )
        ],
        notes="Typically, this spell is used on vampires and demons. By\nholding a fragment of a burial shroud over herself or another\nbeing within a meter range, the caster creates an ethereal\nshroud that protects the target from the damaging rays of\nthe sun. The shroud appears as a dark and filmy cape and\nhood that covers the target’s entire body. As a result, the\ntarget is nearly immune to the effects of normal sunlight\nfor a short time and might walk about unaffected, a valuable\nboon for vampires.\nAt the time of casting, the mage can convert the result\npoints from the casting into a bonus to protection or dura-\ntion. Convert the bonus points put into the effect into dice\nand pips of Armor Value (three points per die; one point\nper pip). Use the “Spell Measures” chart in the D6 Fantasy\nor D6 Adventure rulebooks to determine the addition to the\nduration in seconds.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="Infravision or Ultravision (R3), negates up to 6 points of modifiers for dim or dark conditions",
            base_difficulty=9,
            count=1,
        ),
        duration=Aspect(format="1 day ", base_difficulty=25, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Sight of Darkness",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Light, darkness", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="20", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Flint and tinder (common)", base_difficulty=-2, count=1
            ),
            "Feedback": Aspect(
                format="-3 to damage resistance total", base_difficulty=-3, count=1
            ),
            "Focused": Aspect(format="On target", base_difficulty=6, count=1),
            "Incantations": Aspect(
                format="“See.” (phrase)", base_difficulty=-1, count=1
            ),
        },
        notes="By the magic user sacrificing some of her life energy, she\ngrants a target with 24 hours of three ranks in Infravision\nor Ultravision (which the caster chooses before casting the\nspell). See the description of this Special Abilities in the\n“Character Options” chapter for more details.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="+4D to intimidation", base_difficulty=18, count=1),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Sinister Pall",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Darkness", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="11", base_difficulty=0, count=1),
            "Gestures": Aspect(
                format="Scowl darkly and clench fists menacingly (simple, offensive)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes="With a scowl and general menacing countenance, the\ncaster improves her intimidation skill for one minute. Her\nfeatures become shadowed and sinister, like the villain from\na horror movie. People are naturally unsettled by the cast -\ners appearance and therefore more prone to bending to the\nforce of his will.\n\n",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(format="+4D to one targeting skill", base_difficulty=18, count=1),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="3.5 seconds ", base_difficulty=-3, count=1),
        name="Sniper Light Beam",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Light", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="10", base_difficulty=0, count=1),
            "Gestures": Aspect(
                format="Run trigger finger down the length of weapon (fairly simple).",
                base_difficulty=-2,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="May only be used with a single direct-fire, self-powered projectile weapon, such as a crossbow or a gun",
                base_difficulty=-2,
                count=1,
            )
        ],
        notes="This spell creates a light beam that extends down the sights\nof a projectile weapon, effectively serving as a sniper’s laser\nsight. This improves the mage’s related ranged combat skill\nwhen using that weapon for a period of one minute. This\nbonus cannot be used with weapons that depend strength\nfor their power, such as bows or slings.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="reduce movement difficulty modifiery by up to -5",
            base_difficulty=5,
            count=1,
        ),
        duration=Aspect(format="3.5 minutes ", base_difficulty=12, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Stunt Plant",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Darkness, Plant", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="10", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="5-meter-radius circle", base_difficulty=10, count=1
            ),
            "Countenance": Aspect(
                format="Caster takes on a gray pallor", base_difficulty=-1, count=1
            ),
            "Focused": Aspect(format="On caster", base_difficulty=3, count=1),
            "Gestures": Aspect(
                format="Spread hands in intended direction and lower as if pressing down on something (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Diminish, plants! Shrivel and die!” (sentence, loud)",
                base_difficulty=-3,
                count=1,
            ),
        },
        notes="The caster literally presses back plant life before her,\ndiminishing or even killing them through the deprivation\nof light. All plants require light to grow. The effect lasts for\nthree and a half minutes. Vegetation (grasses, briars, shrubs,\ntrees) within five meters of the caster shrink a quarter of its\nnormal size each round, becoming less bushy and entangling.\nThis allows for freer movement within the area of effect.\nAssuming plants haven’t died completely, they begin to\nslowly rejuvenate as soon as the spell is complete, growing\nas per normal for the plant species in question. Trees may\ntake years or even decades to return to their previous state,\nwhile grass may require only a few weeks.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="Achilles’s Heel (R3), 5D damage and +20 to survival and stamina difficulties in desert environments each day the character is in the sun — values are not cumulative",
            base_difficulty=9,
            count=1,
        ),
        duration=Aspect(format="1 week ", base_difficulty=29, count=1),
        range=Aspect(format="Touch ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Sun Scourge",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Light, Fire", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="16", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Ashes of creature desiccated by the sun (uncommon)",
                base_difficulty=-4,
                count=1,
            ),
            "Feedback": Aspect(
                format="-2 to damage resistance totals", base_difficulty=-2, count=1
            ),
            "Focused": Aspect(format="On target", base_difficulty=7, count=1),
            "Gestures": Aspect(
                format="Raise arms toward the sun and sprinkle the ashes to the wind (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Like a scythe, O mighty sun; cut down thy enemies.” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes="Other Conditions (-2) Can only be cast when the sun is visible\nThe mage makes an offering of ashes to the sun and calls\nupon its power, which she channels through her body. Then,\nwith a minimal amount of pain to herself and a simple\ntouch, the caster inflicts pain to an opponent as if he were\nbeing burnt by the sun’s searing rays. It also makes him\nunusually susceptible to the harsh effects of the sun. If the\nvictim opposes the touch —as most aware and able-bodied\nbeings would — the mage must make a successful brawling/\nfighting attack.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="15 for resistance total of bars; negates up to 4D of darkness modifier",
            base_difficulty=37,
            count=1,
        ),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="25 meters ", base_difficulty=7, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=7, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        name="Sun Cage",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Light", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="31", base_difficulty=0, count=1),
            "Area of Effect": Aspect(
                format="Sphere with a radius of 3 meters", base_difficulty=15, count=1
            ),
            "Gestures": Aspect(
                format="Mime escaping from a cell with eyes squinted as if blinded by glaring light, then point at target (complex; acrobatics roll with difficulty of 11)",
                base_difficulty=-3,
                count=1,
            ),
            "Unreal Effect": Aspect(
                format="Disbelief difficulty of 13", base_difficulty=-10, count=1
            ),
        },
        notes="Light cage traps a target in a prison of magical sunlight.\nAfter miming escaping from a cell and indicating the intended\ntarget, the mage must make a marksmanship/firearms or ap-\nportation roll that beats the combat difficulty for the target.\nIf she succeeds, the target is trapped in a sphere with a radius\nof three meters. (Creatures larger than that cannot be con-\nfined by this spell.) The cage glows radiantly, bright enough\nto illuminate within one meter in all directions.\nThe result point bonus plus 15 serves as the damage resis-\ntance totals of the bars. The target can disbelieve and thus\nfree himself by generating a disbelief total of 13.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="Intangibility (R1), +3D to damage resistance total against physical attacks and movement is halved; Invisibil- ity (R3), +3 to dodge, sneak/stealth, and hide: self totals and +3 to search, tracking,  investigation, and attack difficulties against target",
            base_difficulty=33,
            count=1,
        ),
        duration=Aspect(format="5 rounds ", base_difficulty=7, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="3.5 minutes ", base_difficulty=-12, count=1),
        name="Turn to Shadow",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Darkness", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="16", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Dark clothes (very common)", base_difficulty=-2, count=1
            ),
            "Concentration": Aspect(
                format="3 seconds with willpower/mettle difficulty of 7",
                base_difficulty=-1,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=8, count=1),
        },
        other_conditions=[
            Aspect(
                format="Must be immersed in darkness or shadow during casting time",
                base_difficulty=-1,
                count=1,
            )
        ],
        notes="To cast this spell, the mage must be wearing dark clothes\nand devoid of any shiny objects that would catch and reflect\nlight. He must also be immersed in darkness or shadow at\nthe time of casting. The darkness need not be absolute; even\na shadowy corner of an inn’s common room is enough. When\nthe spell is cast, the mage transforms himself into a living\nshadow. He has no mass and therefore makes no noise and\nleaves no track of his passage, moves at half his normal rate,\nmay assume any general shape (though details are not pos-\nsible), and may flow through tiny openings.\nBecause he is insubstantial, most physical attacks pass\nright through the mage. However, he in turn cannot attack\nin this form, nor can he speak or uses spells that require\nbiological conditions (incantations, for example, or handling\nof material components).",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="+4D darkness modifier", base_difficulty=12, count=1),
        duration=Aspect(format="5 rounds ", base_difficulty=7, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="2.5 seconds ", base_difficulty=-2, count=1),
        name="Veil of Darkness",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Folk, Darkness", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="12", base_difficulty=0, count=1),
            "Countenance": Aspect(
                format="The mage looks drained, with dark rings around eyes",
                base_difficulty=-1,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=3, count=1),
            "Gestures": Aspect(
                format="Cover eyes with a hand, then a throwing mostion at a target (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“You see NOTHING!” (sentence, loud)",
                base_difficulty=-3,
                count=1,
            ),
        },
        notes="The mage covers his eyes with a hand, drawing energy from\nwithin himself, and then throws a ball of pure darkness at a\ntarget. He must make a marksmanship/firearms or apporta-\ntion roll to hit the target, and may throw the spell up to 10\nmeters distant. Hit targets find themselves blinded by a veil\nof darkness that covers their eyes, imposing a +4D darkness\ndifficulty modifier on all relevant actions performed by this\ncreature for a period of 25 seconds. The bolt of darkness must\nbe fired in the same round that the mage casts the spell.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="brawling/fighting of 4D; lifting/lift of 5D; 6D physical damage",
            base_difficulty=45,
            count=1,
        ),
        duration=Aspect(format="3 rounds ", base_difficulty=6, count=1),
        range=Aspect(format="5 meters ", base_difficulty=4, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=4, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Vengeful Void",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Darkness, Water", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="24", base_difficulty=0, count=1),
            "Gestures": Aspect(
                format="Point at an intensely dark area (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Rise, darkness, and avenge me. I command it.” (sentence, loud)",
                base_difficulty=-3,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="A void of darkness in an otherwise illuminated environment",
                base_difficulty=-3,
                count=1,
            )
        ],
        notes="To cast this spell, a void of darkness or dense shadow (such\nas a deep pit, a nonilluminated dungeon room, or a shadowy\nalley) must be present. The mage then shouts some words of\npower and points toward the black spot. Through this spell,\nthe mage animates the darkness of the void into a tidal-wave-\nlike mass that strikes down upon opponents with rage. The\ndarkness grabs an opponent within five meters brawling/fight-\ning of 4D and inflicts 6D damage. Once captured, the target\nis dragged back into the depths of the monster on the next\nround, though the opponent may attempt to escape the void’s\nlifting/lift of 5D. Those dragged into the void obviously must\ncontend with whatever dangers might lurk within (falling\ndamage from a pit, for example). Additionally, the darkness\ninflicts its normal damage on the trapped creature. Creatures\ntrapped within the darkness feel as if they are drowning and\nbeing crushed by the pressures of deep water.\n\n",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="negates up to -4D of darkness modifier; provides +2D cover modifier",
            base_difficulty=18,
            count=1,
        ),
        duration=Aspect(format="3.5 minutes ", base_difficulty=12, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Wall of Radiance",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Light", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="15", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Circle with radius of 3 meters", base_difficulty=6, count=1
            ),
            "Components": Aspect(
                format="A handful of crystal shards (uncommon, destroyed); lit candle (very common)",
                base_difficulty=-10,
                count=1,
            ),
            "Gestures": Aspect(
                format="Throw crystals into air and blow the flames of a candle toward them (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes="The magic user throws a handful of crystal fragments in\nthe direction in which he wishes to create the wall of radi -\nance. Then he blows the flames of a lit candle into the falling\nshards. A shield-like wall of shimmering white light measuring\nthree meters in diameter appears at a distance of up to 10\nmeters from the caster.\nThe wall is immobile and remains in that position for three\nand a half minutes. The light is so brilliant that it negates\nup to 4D of darkness modifier within one meter. Its bright-\nness provides a +2D cover modifier against anyone attacking\nfrom the other side of the barrier. The wall does not offer\nany physical barrier to attack or movement.\n\n",
        skill="Conjuration",
    ),
]

if __name__ == "__main__":
    detail(spells)


__test__ = {
    "Aura of Visibility": ">>> spells[0].difficulty\n10",
    "Blur": ">>> spells[1].difficulty\n11",
    "Glowing Eyes": ">>> spells[2].difficulty\n16",
    "Holy Light": ">>> spells[3].difficulty\n35",
    "Light Chest": ">>> spells[4].difficulty\n20",
    "Light Ram": ">>> spells[5].difficulty\n18",
    "Light Show": ">>> spells[6].difficulty\n14",
    "Mass Light Show": ">>> spells[7].difficulty\n24",
    "Night Vigilance": ">>> spells[8].difficulty\n15",
    "Nyctophobia": ">>> spells[9].difficulty\n13",
    "Shadow Surface": ">>> spells[10].difficulty\n27",
    "Shroud of Shade": ">>> spells[11].difficulty\n10",
    "Sight of Darkness": ">>> spells[12].difficulty\n20",
    "Sinister Pall": ">>> spells[13].difficulty\n11",
    "Sniper Light Beam": ">>> spells[14].difficulty\n10",
    "Stunt Plant": ">>> spells[15].difficulty\n10",
    "Sun Scourge": ">>> spells[16].difficulty\n16",
    "Sun Cage": ">>> spells[17].difficulty\n31",
    "Turn to Shadow": ">>> spells[18].difficulty\n16",
    "Veil of Darkness": ">>> spells[19].difficulty\n12",
    "Vengeful Void": ">>> spells[20].difficulty\n24",
    "Wall of Radiance": ">>> spells[21].difficulty\n15",
}
