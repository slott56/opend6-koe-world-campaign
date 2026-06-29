"""
Vitomancy

When run as an app, generates .RST-formatted details of each Spell.
"""

from decimal import Decimal
from typing import Annotated, Any
import typer
from opend6_tools.magic2 import *


spells = [
    Spell(
        name="Animal Loyalty",
        skill="Alteration",
        notes="To inspire unnatural loyalty in a pet, animal companion,\nor mount, the caster simply strokes the creature and makes\nreassuring, soothing sounds. For a full day thereafter, the\nanimal will be especially loyal to the caster, which translates\ninto an animal handling  (or persuasion: animals in D6 Space)\nbonus of +2D for the caster toward the target creature. In\naddition, because the animal is so trusting of the caster,\nwhenever it’s within 10 meters of the caster, it gains a will-\npower/mettle bonus of +2D to resist attempts, magical or\notherwise, by others to alter its behavior.",
        effect=CompositeEffect(
            "Animal Handling",
            SkillEffect(
            "boost caster’s animal handling", "+2D", "skill modifier"),
            SkillEffect("boost target’s willpower/mettle", "+2D", "skill modifier"),
        ),
        duration=DurationAspect("1 day"),
        range=RangeAspect("self"),
        casting_time=CastingTimeAspect("2 rounds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Animal", ""),
            "gestures": GesturesAspect("Gently stroke the target animal", "simple"),
            "incantations": IncantationsAspect("Make soothing sounds", "phrase"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On caster and target"
            ),
        },
        other_conditions=[
            GenericAspect(
                -2,
                "Limited to animals that are friendly to the caster; target and caster must remain within 10 meters of each other to get bonuses",
            ),
            GenericAspect(0, "Difficulty: 20"),
        ],
    ),
    Spell(
        name="Animal Savior",
        skill="Alteration",
        notes="To cast this spell, the mage places on the ground something\nfrom that type of animal to be targeted (strands of dog’s fur\nor locks of horse’s hair, for example) and something from the\nindividual the animal is intended to watch over. She then\ndraws a line from these items toward the animal, and then\ntoward the individual to be protected.\nFor a period of one hour, the targeted animal keeps a watch-\nful eye over its ward. Should  the ward ever fall (rendered\nunconscious, incapacitated, paralyzed, dead, or otherwise\nunmoving), the animal will quickly descend upon the body\nand pull it to a location out of harm’s way. This spell grants\nthe animal a +2D lifting/lift bonus for this purpose, allowing\neven a small dog the ability to pull a human to safety, and\na +2D willpower/mettle bonus to resist efforts to dissuade\nintervention.\nWhile there is no range limitation on how far the animal\nwill theoretically pull the character, the location to which\nthe immobilized character is moved is always the nearest\n“safe” place. This might mean dragging the body out of a\nroom, behind a tree, into a defile, or any other such sheltered\nlocale. In an environment where there is no readily avail -\nable protection, such as barren and flat desert or plains, the\nanimal pulls the body far enough away to be removed from\nthe melee and out of range of whatever missile weapons the\nenemy possesses (if any).",
        effect=CompositeEffect(
            "Save Animal",
            SkillEffect("boost lifting/lift to recover fallen comrades", "+2D", "skill modifier"),
            SkillEffect("boost willpower/mettle  to resist attempts to dissuade recovery", "+2D", "skill modifier"),
        ),
        duration=DurationAspect("1 hour"),
        range=RangeAspect("self"),
        casting_time=CastingTimeAspect("1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Animal", ""),
            "components": ComponentsAspect(
                ("Something from the type of animal targeted", "very common"),
                ("something from the individual to be protected by the target animal", "very common"),
            ),
            "gestures": GesturesAspect("Draw a line on the ground", "simple"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[
            GenericAspect(-1, "Limited to animals"),
            GenericAspect(0, "Difficulty: 16"),
        ],
    ),
    Spell(
        name="Asp Arrow",
        skill="Conjuration",
        notes="To cast this spell, the mage must have a live asp or other\npoisonous snake on his person. Usually, mages keep them in\nsmall earthenware pots or reed baskets. By coiling himself as\na snake would, not only is he drawing upon energy to propel\nthe mystical arrow but is also tapping into the essence of the\nsnake itself. Once the mystical energy is released, an arrow\nappears and flies toward the intended target, to a range of\n10 meters. The mage must make a marksmanship/firearms or\napportation roll to hit the target. If the arrow flies true and\nhits, it immediately transforms into a large asp and delivers\na poisonous bite., which causes 4D of damage each round\nfor one minute. The asp arrow must be fired in the round\nafter the mage casts the spell. The mage may add the result\npoint bonus of the spell to either the targeting total or the\nfirst damage total.\n\n",
        effect=SkillEffect("Arrow", "+4D",  "pysical damage", "ignores nonmagical armor"),
        duration=DurationAspect("1 minute"),
        range=RangeAspect("10 meters"),
        casting_time=CastingTimeAspect("1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Animal", ""),
            "component": ComponentsAspect(
                "A live asp or other poisonous snake", "uncommon"
            ),
            "gestures": GesturesAspect(
                "Crouch as if coiled like a snake, shape hand into a fist with two fingers extended like asp fangs, then spring and throw the gathered energy at target",
                "simple",
            ),
            "incantations": IncantationsAspect("Make a snake-like sound", "phrase"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 16")],
    ),
    Spell(
        name="Bashing Fists",
        skill="Conjuration",
        notes="To cast the spell, the mage must first put on a pair of black\nleather gloves. The mage then lets out a roar as mighty as he\ncan muster and punches each of his fists into an open hand,\nall the while feeling himself become overwhelmed with a\nsense of pent-up rage. This violent urge must be released\nwithin the next five rounds or it dissipates, and can only be\nreleased in unarmed combat. The spell provides the Natural\nHand-to-Hand Weapons: Fists Special Ability, which gives the\nattacker +2D to his unarmed Strength Damage. In addition\nto damage inflicted, each blow landed by the mage pushes\nhis foe. This causes the victim to stumble, reducing all Agil-\nity/Reflexes or related totals by 3 until the mage’s turn in\nthe next round.",
        effect=SpecialAbilityEffect("Natural Hand-to-Hand Weapon: Fists", 2, "+2D  damage"),
        duration=DurationAspect("5 rounds"),
        range=RangeAspect("self"),
        casting_time=CastingTimeAspect("3.5 seconds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Folk", ""),
            "components": ComponentsAspect("Pair of black leather gloves", "common"),
            "gestures": GesturesAspect("Put on gloves", "simple"),
            "incantations": IncantationsAspect(
                "Let out an ear-splitting roar of rage", "phrase", "loud"
            ),
            "other_alterant": OtherAlterant(12, "Opponent receives increased difficulties with each landed punch")
        },
        other_conditions=[
            GenericAspect(0, "Difficulty: 10"),
        ],
    ),
    Spell(
        name="Beast Warden",
        skill="Alteration",
        notes="To cast this spell, the mage must have a small supply ber-\nries harvested from a rowan tree. The mage points at the\nanimal he wishes to target, then at a creature or creature he\nwishes the animal to guard, snarling and bearing his teeth\nto get the point across. After uttering a simple command\nword, the spell is cast. The target animal devotedly keeps\nthe specified beings in a confined area measuring three\nmeters in diameter by circling. In the eyes of its captives, the\nanimal’s countenance changes completely, become far more\nfrightening and imposing. As a result, the animal gains an\nintimidation skill bonus of +4D.\nMost captives are too frightened to attempt escape, save\nfor those who make a willpower/mettle roll of 13 to disbelieve\nthe spell’s effect. Captives attempting to escape find them -\nselves harrassed immediately upon trying to leave the area\nof effect. The animal attacks until either it or the prisoner\nis dead or subdued.\nWhile predators are most often targeted, this spell is by\nno means limited to them. Herbivores, such as boars, deer,\nand bulls, can be equally effective.\nBlades of Flesh",
        effect=SkillEffect("intimidation", "+4D", "skill modifier"),
        duration=DurationAspect("10 minutes"),
        range=RangeAspect("10 meters"),
        casting_time=CastingTimeAspect("1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Animal", ""),
            "area_effect": AreaEffectAspect("3m radius sphere"),
            "components": ComponentsAspect("Rowan berries", "uncommon", "destroyed"),
            "countenance": CountenanceAspect("Animal appears menancing", "noticeable"),
            "gestures": GesturesAspect(
                "Point from target to those to be guarded, bear teeth and snarl",
                "simple",
            ),
            "incantations": IncantationsAspect("“Guard.”", "phrase"),
            "unreal_effect": UnrealEffectAspect.based_on("effect", "difficulty 13"),
            "other_alterant": OtherAlterant(10, "Animal will fight to the death to keep captives in area of effect"),
        },
        other_conditions=[
            GenericAspect(
                -2, "May only be used on animals who are friendly to the caster"
            ),
            GenericAspect(0, "Difficulty: 20"),
        ],
    ),
    Spell(
        name="Blades of Flesh",
        skill="Conjuration",
        notes="This spell gives the target a bonus of +1D to Strength\nDamage for 25 seconds, or five rounds. With the simple slash\nof a blade, the spell transforms the target’s hands, elbows,\nand feet into lethal blades of flesh that can slash or pierce\nas well as bludgeon.",
        effect=SpecialAbilityEffect(
            "Natural Hand-to-Hand Weapon: Blades of Flesh", 1, "+1D  damage"
        ),
        duration=DurationAspect("5 rounds"),
        range=RangeAspect("self"),
        casting_time=CastingTimeAspect("1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Folk", ""),
            "components": ComponentsAspect("Any bladed weapon", "common"),
            "gestures": GesturesAspect("Draw weapon across hand", "simple"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 3")],
    ),
    Spell(
        name="Club Feet",
        skill="Conjuration",
        notes="While willingly causing himself to trip and fall (acrobatics\nroll of 11 or fail the spell due to ineptitude), and casually\nexcusing himself for his clumsiness, the mage casts this\npotent spell and curses a target not more than 10 meters\naway. The curse twists the victim’s feet until they are hor -\nribly misshapen, rendering his legs so uncoordinated that\nhe can literally trip over himself. This is reflected by a +4\nto the difficulties of various foot-related tasks and a -4 to\ninitiative totals. When the spell wears off 10 minutes later,\nthe character is restored immediately to normal.",
        effect=DisadvantageEffect(
            "Hindrance: Club Feet",
            12,
            note=": +4 to the difficulty of any foot-related skill use and -4 to initiative rolls",
        ),
        duration=DurationAspect("10 minutes"),
        range=RangeAspect("10 meters"),
        casting_time=CastingTimeAspect("1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Animal, Folk", ""),
            "gestures": GesturesAspect(
                "Mime tripping and falling, eyes focused on target",
                "complex (acrobatics roll with difficulty of 11)",
            ),
            "incantations": IncantationsAspect("“I’m such a clumsy oaf.”", "sentence"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 31")],
    ),
    Spell(
        name="Cobra Strike",
        skill="Conjuration",
        notes="This spell requires the caster to wear cobra skin gloves\nand have a flute. The mage casts the spell by playing a short\ntune on her flute, the kind that snake-charmers use to lure\ncobras from their wicker pots. On the next round, as the mage\nattemtps to land an open-handed strike, her hand spreads out\nlike a hood, and the head of a cobra momentarily appears in\nthe palm to strike the target. On a successful attack, the blow\ninflicts normal unarmed damage and for five rounds (starting\nwith the one in which the blow landed), the victim is poisoned\nand takes 3D damge per round until duration ends.\n\n",
        effect=SkillEffect("Cobra damage", "+3D", "physical damage", "ignores all armor"),
        duration=DurationAspect("5 rounds"),
        range=RangeAspect("touch"),
        casting_time=CastingTimeAspect("1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Folk, Animal", ""),
            "charges": ChargesAspect(
                "2 improved charges", "released only with successful attack"
            ),
            "components": ComponentsAspect(
                ("Cobra skin gloves", "very rare"),
                ("flute", "very common"),
            ),
            "gestures": GesturesAspect(
                "Play tune on a flute", "complex (artist roll with difficulty of 11)"
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 14")],
    ),
    Spell(
        name="Courage",
        skill="Alteration",
        notes="Casting this spell requires the mage to have a rope braided\nfrom lion’s mane. He holds the rope aloft as a symbol of cour-\nage and shakes it mightily as he turns in a complete circle,\ndemonstrating its importance to all around him.\nFor a period of more than two minutes thereafter, his mere\npresence steadies his allies when terror would otherwise fill\ntheir hearts and shake their resolve. All allies with a 5-meter\nradius gain a willpower/mettle skill bonus of +6D+2 for resist-\ning fear, intimidation, or even pain and torture.\nUnder the influence of this spell, only the most weak\nhearted of characters will break rather than present a stoic\nface to their enemies. If a character affected by fear is ral -\nlied by her companions, she may roll again to shake off the\neffect. This spell can only be used on sentient beings, and it\nonly affects individuals who are neutral toward or trusting\nof the mage.",
        effect=SkillEffect("willpower/mettle", "+6D+2", "skill modifier"),
        duration=DurationAspect("2.5 minutes"),
        range=RangeAspect("self"),
        casting_time=CastingTimeAspect("1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Folk", ""),
            "area_effect": AreaEffectAspect("5 m radius sphere"),
            "components": ComponentsAspect("Braided lion’s mane rope", "very rare"),
            "concentration": ConcentrationAspect("3 seconds"),
            "feedback": FeedbackAspect(3),
            "gestures": GesturesAspect(
                "Hold the lion’s mane rope above the head and shake it while turning in a circle",
                "complex (acrobatics roll with difficulty of 11)",
            ),
            "incantations": IncantationsAspect(
                "“Fight by me, my friends, and together we’ll taste victory or achieve immortality”",
                "sentence",
                "loud",
            ),
        },
        other_conditions=[
            GenericAspect(
                -2,
                "Limited to sentient beings and those who are neutral or trusting of the mage",
            ),
            GenericAspect(0, "Difficulty: 23"),
        ],
    ),
    Spell(
        name="Eagle-Eye",
        skill="Divination",
        notes="The caster ingests an eye of an eagle, closes his eyes, and\nconcentrates. When he opens his eyes after 25 seconds, the\nmage perceives a bird’s eye view of his surrounding area, as\nthough he was looking down from the vantage point of a\nsoaring eagle. The mage gains awareness of all objects within\n10 meters of his person that are large enough to normally\nbe seen with his eye. However, the mage cannot see under\nor through solid objects.\nThe area of effect moves with the caster until the spell\ndissolves after one minute.\nCreatures may attempt to hide from the mage, but he gains\na search bonus of +4D to see them because of his vantage\npoint. This may have the unintended and happy side effect\nof preventing surprise — assuming the mage notices his\nattackers before they strike.\nThe mage may target spells at anything he sees through\nthis spell as if he had line of sight. However, he must still\naccount for cover. For example, a character hiding behind\nan overturned table still enjoys such cover as it provides,\neven though he is clearly seen through the mage’s bird’s eye\nview; remember, the spell still originates from the mage’s\nphysical form.\nThe unusual perspective can be disorienting for the mage,\nand during the spell’s duration, he suffers -6 to all Agility/\nReflexes and related totals while spell is active.",
        effect=SkillEffect("search skill", "+4D", "skill modifier"),
        duration=DurationAspect("1 minute"),
        range=RangeAspect("10 meters"),
        casting_time=CastingTimeAspect("5 rounds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Folk, Avian", ""),
            "area_effect": AreaEffectAspect("10 m radius divination sphere"),
            "component": ComponentsAspect("Eye of an eagle", "uncommon", "destroyed"),
            "concentration": ConcentrationAspect("25 seconds"),
            "gestures": GesturesAspect("Ingest the eagle’s eye", "simple"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On caster"
            ),
            "variable_duration": VariableDurationAspect("on/off switch")
        },
        other_conditions=[
            GenericAspect(
                -6, "-6 to Agility/Reflexes and related totals while spell is active"
            ),
            GenericAspect(0, "Difficulty: 20"),
        ],
    ),
    Spell(
        name="Envy",
        skill="Conjuration",
        notes="While casting this spell is moderately painful to the mage,\nit might well be the death of the target. The caster curses a\nhumanoid target that she can see with four hours of extreme\nenvy. Envy is the desire to possess what others have. Those\nafflicted with envy covet what others have —personality\ntraits, personal good fortune, and material goods. The need\nto prove themselves, to obtain a perceived glory or possess\na valuable item, often places the individuals in potentially\ndangerous situations — they might rush to disarm a trap,\npush other characters aside to be the first to fight a foe, or race\nto secure a treasure headless of potential risks. A character\ntargeted by this spell must make a Very Difficult  willpower/\nmettle roll to overcome his envious impulses.",
        effect=DisadvantageEffect(
            "Quirk ",
            3,
            note=", envy requiring a Very Difficult willpower/mettle roll to overcome Disadvantage",
        ),
        duration=DurationAspect("4 hours"),
        range=RangeAspect("10 meters"),
        casting_time=CastingTimeAspect("2 rounds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Folk", ""),
            "concentration": ConcentrationAspect("1 round"),
            "feedback": FeedbackAspect(3),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 18")],
    ),
    Spell(
        name="Gang Fight",
        skill="Alteration",
        notes="When the mage attempts to cast this spell, he must pres-\nent a commanding and frightful image by succeeding an\nintimidation roll with a difficulty of 11. If she fails this, she\nsimply doesn’t present herself with enough menacing author-\nity and the spell doesn’t work. If successful, however, mage\nmakes up to six allies fight with ruthless vigor, employing all\nmanner of dirty tricks and providing them a bonus to their\nclose combat skills of +2D. It also lends them a menacing air,\nresulting in an intimidation bonus of 2D.\nThe targets must outnumber their opponents or have a\nmarked disadvantage, because the thuglike tactics the caster\nwishes her allies to employ depend to a large degree upon\nintimidation and ganging-up on victims.",
        effect=CompositeEffect(
            "Fighting",
            SkillEffect(
            "brawling/fighting", "+2D", "skill modifier"),
            SkillEffect("melee combat", "+2D", "skill modifier"),
            SkillEffect("intimidation", "+2D", "skill modifier"),
        ),
        duration=DurationAspect("5 rounds"),
        range=RangeAspect("5 meters"),
        casting_time=CastingTimeAspect("1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Folk", ""),
            "gestures": GesturesAspect(
                "Frown menacingly and point with authority at allies",
                "complex (intimidation roll with difficulty of 11)",
            ),
            "incantations": IncantationsAspect(
                "“Rip ’em apart, boys”", "sentence", "loud"
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On targets"
            ),
            "multi_target": MultipleTargetAspect("6 targets"),
        },
        other_conditions=[
            GenericAspect(
                -2,
                "Targets must be allies of the caster and either outnumber the oppoents or have them at a decisive disadvantage",
            ),
            GenericAspect(0, "Difficulty: 27"),
        ],
    ),
    Spell(
        name="Gnawing Hunger",
        skill="Conjuration",
        notes="To cast this spell, the mage must have in an item of food\nthat the target might reasonably be expected to eat (meat for\na carnivore, plants for an herbivore). She holds this item in\nher hand while pointing a finger at the target, and when she\ndoubles over mimicking stomach pains as the food crumbles\nto dust. While performing these actions, she utters a simple\nbut malicious phrase, after which the target suffers 4D damage\nfrom intense stomach pains. The target literally begins starv-\ning to death and at an accelerated pace. ll mental and physical\nattributes decrease by 1 pip (with the penalty increasing by\n1 pip for each hour without food) due to weakness. These\npenalties are negated once the target has eaten.\n\n",
        effect=CompositeEffect(
            "Hunger",
            DamageEffect(
            "damage, ignores all armor", "4D", "physical damage", "ignores all armor"),
            DisadvantageEffect("Achilles’ Heel", 4, "metabolic difference — must eat a meal every two hours or all mental and physical attributes decrease by 1 pip, with penalty increasing by 1 pip for each hour without food and disappearing with consumption of food"),
        ),
        duration=DurationAspect("1 day"),
        range=RangeAspect("10 meters"),
        casting_time=CastingTimeAspect("1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Animal, Folk", ""),
            "components": ComponentsAspect(
                "Any food item that might be eaten by the intended target", "ordinary", "destroyed"
            ),
            "countenance": CountenanceAspect(
                "The caster’s  skin tightens around the cheeks in a sickly fashion",
                "noticeable",
            ),
            "gestures": GesturesAspect(
                "Double over in direction of the target as if suffering severe abdominal pain",
                "simple",
            ),
            "incantations": IncantationsAspect(
                "“Hunger gnaws like a ravenous beast!”", "sentence", "loud"
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 35")],
    ),
    Spell(
        name="Graceful Step",
        skill="Alteration",
        notes="This spell makes the target graceful for a period of five\nrounds, which affects her acrobatics, dodge, and sneak/stealth\nattempts and increases them by 1D+1.",
        effect=CompositeEffect(
            "Grace",
            SkillEffect("acrobatics", "1D+1", "skill modifier"),
            SkillEffect("dodge", "1D+1", "skill modifier"),
            SkillEffect("sneak/stealth", "+1D+1", "skill modifier"),
        ),
        duration=DurationAspect("5 rounds"),
        range=RangeAspect("self"),
        casting_time=CastingTimeAspect("1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Animal, Folk", ""),
            "gestures": GesturesAspect("Shake one leg, then the next", "simple"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 12")],
    ),
    Spell(
        name="Pollen Cloud",
        skill="Conjuration",
        notes="With some minor pain to herself, the mage creates a cloud\nof pollen. To cast this spell, she must have a fresh flower,\nwhich she brings to her lips and then blows in the intended\ndirection. After uttering a simple incantation, a dense cloud of\npollen emerges from the bloom and quickly fills a six-meter-\nwide sphere. The pollen cloud is as thick as fog, providing\n2D of cover modifier. Under normal conditions, the cloud\ndissipates after five rounds. However, in moderately windy\nconditions it blows away after two rounds, and heavy winds\nprevent the spell from working entirely.",
        effect=SkillEffect("cover modifier", "+2D"),
        duration=DurationAspect("5 rounds"),
        range=RangeAspect("3 meters"),
        casting_time=CastingTimeAspect("1.5 seconds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Plant", ""),
            "area_effect": AreaEffectAspect(
                "3m radius sphere"),
            "components": ComponentsAspect(
                "Fresh flower bloom", "very common", "destroyed"
            ),
            "feedback": FeedbackAspect(3),
            "gestures": GesturesAspect("Bring bloom to lips and gently blow", "simple"),
            "incantations": IncantationsAspect("“Belladonna’s breath.”", "phrase"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[
            GenericAspect(-1, "Spell negated by strong winds"),
            GenericAspect(0, "Difficulty: 14"),
        ],
    ),
    Spell(
        name="Quick Release",
        skill="Conjuration",
        notes="The caster places a spearhead in his hands and crushes\nit between his palms, leaving his hands bloodied and the\nspearhead mere dust. Until the blood dries (a period of about\n10 minutes), the mage becomes extremely fast at releasing\nthrown weapons. This results in +1D bonus to his initiative\nroll when wielding thrown weapons. In addition, because\nhe can release weapons with such amazing speed, he can\nmake an additional throwing attack in up to three rounds.\nThis spell provides no benefit when using missile weapons\nor firearms.",
        effect=CompositeEffect(
            "Move fast",
            SpecialAbilityEffect(
            "Fast Reactions", 1, "add to initiative roll and one additional free action in each of 3 rounds"),
            DisadvantageEffect("Ability Loss", 1, "only useful with throwing; +2D to throwing"),
        ),
        duration=DurationAspect("5 minutes"),
        range=RangeAspect("self"),
        casting_time=CastingTimeAspect("3.5 seconds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Folk", ""),
            "components": ComponentsAspect("Spearhead", "common", "destroyed"),
            "gestures": GesturesAspect(
                "Squeeze palms together with spearhead between", "simple"
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On caster"
            ),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 10")],
    ),
    Spell(
        name="Reveal Disposition",
        skill="Divination",
        notes="This spell is particularly useful by individuals involved in\ndelicate diplomacy. After meditating in silence for 10 seconds,\nthe mage warmly introduces herself to the individual that she\nwants to influence. The person must be a sentient being who\nunderstands her language. If the target doesn’t comprehend\nher, the spell and her time are wasted. Interpreters aren’t\nsufficient, as the spell relies upon personal interaction and\ncommon ground.\nWhen the spell is successfully cast, the mage rolls the will-\npower/mettle from the spell against the opponent’s willpower/\nmettle. By beating this difficulty, the caster senses the target’s\ndisposition toward her by seeing a glowing aura around it.\nThe aura is visible only to the mage. A white light suggests\nthe target is friendly or trusting; a gray-shaded aura indicates\nthat he is neutral or ambivalent. A shadow falling over the\ntarget indicates he is hostile or has superior standing.\nSince this spell lasts for 10 minutes, the mage may track how\nthe target’s disposition changes over the course of negotia-\ntions, allowing her to know the effectiveness of her diplomacy\nand attempts to change the target’s disposition. Because the\nmage can sense the nature of the target’s intentions (positive,\nambivalent, or harmful), she enjoys a willpower/mettle of 8D\nwhen resisting his interaction attempts.",
        effect=SkillEffect("willpower/mettle of  ", "+8D"),
        duration=DurationAspect("10 minutes"),
        range=RangeAspect("self"),
        casting_time=CastingTimeAspect("2 rounds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Folk", ""),
            "concentration": ConcentrationAspect("10 seconds"),
            "feedback": FeedbackAspect(3),
            "gestures": GesturesAspect("Make a gesture of friendship", "simple"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[
            GenericAspect(
                -3,
                "Target must interact with the target; may only be used on a single sentient being who understand the caster’s language",
            ),
            GenericAspect(0, "Difficulty: 16"),
        ],
    ),
    Spell(
        name="Sense Ailment",
        skill="Divination",
        notes="This spell allows a mage to tell if a creature suffers from the\neffects of poison, disease, or illness. Before casting this spell,\nshe enters a trance-like state while she runs an egg repeat -\nedly over the body of the patient. She then cracks it open\ninto a bowl of water. Using the skill provided by the spell,\nthe mage can interpret the egg’s appearance to determine\npresence and type of disease, toxin, or injury.\nIf the egg yoke floats to the surface, the patient is free of\nailments. If the yoke sinks, on the other hand, the creature\nis ill and the mage may figure out the cause.\nThe difficulty to detect the presence of an ailment is 7.\nWith five to eight result points, the mage understands the\nnature of the ailment. With nine to 16 result points, the\ncaster knows the cure. With 17 or more result points, the\nhealer figures out the cause.\nThis spell does not heal a patient of his ailment, nor does\nit provide any bonus to healing wounds or injuries.\n\n",
        effect=SkillEffect("medicine/healing of  2", "+5D+2", ),
        duration=DurationAspect("1 minute"),
        range=RangeAspect("self"),
        casting_time=CastingTimeAspect("2 rounds"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Animal, Folk", ""),
            "component": ComponentsAspect(
                ("An egg", "very common", "destroyed"),
                ("bowl of water", "ordinary"),
            ),
            "concentration": ConcentrationAspect("10 seconds"),
            "gestures": GesturesAspect(
                "Run egg over patient and then crack it open into the bowl", "simple"
            ),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 11")],
    ),
    Spell(
        name="Stick to Snake",
        skill="Conjuration",
        notes="This spell turns a dead branch or other long pieces of thin,\ndried wood (arrow shafts, broomsticks, and so on) into a\nlarge and aggressive snake. To cast this spell, the mage must\nhave one hand on the wood while he shakes a rattlesnake tail\nrattle. After reciting the incantation, he drops the stick and\nwatches as it comes to life as a flesh-and-blood snake.\nIf provoked, the snake attacks whomever or whatever is\nnear it. When killed or the spell expires, the snake reverts\nback to its original form.\n\n\nSticky Fingers",
        effect=CompositeEffect(
            "Snake",
            SkillEffect("brawling/fighting", "+5D", "skill"),
            AttributeEffect("running (movement equal to result points in meters round with minimum of 1 meter per round)", "2D", "attribute"),
            SkillEffect("physical damage", "5D"),
        ),
        duration=DurationAspect("5 minutes"),
        range=RangeAspect("self"),
        casting_time=CastingTimeAspect("1 minute"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Plant, Animal", ""),
            "component": ComponentsAspect(
                ("A long, thin dried stick", "ordinary"),
                ("rattlesnake tail rattle", "uncommon"),
            ),
            "gestures": GesturesAspect(
                "Shake rattlesnake rattle while holding stick", "simple"
            ),
            "incantations": IncantationsAspect(
                "“Wood to flesh and stick to snake.”", "sentence"
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On stick"
            ),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 23")],
    ),
    Spell(
        name="Sticky Fingers",
        skill="Alteration",
        notes="(Cantrip) The caster places a small ball of wax in each hand and rubs\nhis fingers tips together, spreading the wax evenly over his\nfingertips. His fingers then become sticky and more nimble,\nallowing him to pick pockets, palm objects, and perform\nsimilar actions that require deft motor control with unnatural\nease. As a result, the character gains a sleight of hand bonus\nof +2D.\nThe sticky substance secreted by the character’s fingers is\nnot strong enough to have any direct application to climbing,\ngrappling, or any other related action that requires the use\nof strength as opposed to mere deftness of hand.",
        effect=SkillEffect("boost sleight of hand", "+2D"),
        duration=DurationAspect("5 rounds"),
        range=RangeAspect("self"),
        casting_time=CastingTimeAspect("1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Folk", ""),
            "components": ComponentsAspect("Ball of wax", "very common", "destroyed"),
            "gestures": GesturesAspect("Rub fingers together", "simple"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On caster"
            ),
        },
        other_conditions=[GenericAspect(0, "Difficulty: 5")],
    ),
    Spell(
        name="Taken Alive",
        skill="Alteration",
        notes="While casting the spell, the mage sets on fire a garment\nmade of valuable fabric, such as a foreign cloth or silk. She\nthen inhales the smoke while concentrating for almost half\na minute.\nOnce the casting is complete, the mage (or her desired tar-\nget) exudes an aura that makes her enemies believe she is less\nvaluable dead than she is alive as ransom. When surrender-\ning, the caster gains a bluff/con bonus of +6D+2 to convince\nopponents of her worth and to spare her life by taking her\nprisoner, rather killing her. She also may bluff opponents\ninto believing her inflated worth even when unconscious or\notherwise incapacitated, as the enemy perceives noble stand-\ning or cultured bearing even in her motionless form.\nOf course, the enemy will expect that a ransom is forthcom-\ning, and after the spell’s duration expires the captive mage\nloses her bluff/con skill bonus and is no longer necessarily\nviewed as a valuable commodity.\nThis spell only affects those that understand the concepts\nof wealth and ransom.",
        effect=SkillEffect("bluff/con", "+6D+2", "skill modifier"),
        duration=DurationAspect("4 hours"),
        range=RangeAspect("self"),
        casting_time=CastingTimeAspect("1 minute"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Death, Folk", ""),
            "components": ComponentsAspect(
                ("Garment made of valuable fabric", "uncommon", "destroyed"),
                ("fire, such as match or lit coal", "very common", "destroyed"),
            ),
            "concentration": ConcentrationAspect("25 seconds"),
            "gestures": GesturesAspect("Inhale smoke", "simple"),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
            "other_alterants": OtherAlterant(2, "Also works unconsciously"),
            "unreal_effect": UnrealEffectAspect.based_on("effect", "difficulty 13")
        },
        other_conditions=[
            GenericAspect(
                -1,
                "May only be used on those that understand the concepts of wealth and ransom",
            ),
            GenericAspect(0, "Difficulty: 15"),
        ],
    ),
    Spell(
        name="Taunt",
        skill="Alteration",
        notes="This spell is cast with a smile that conveys contempt for\nan opponent’s abilities, a taunting gesture that urges him to\nattack the mage, and an insulting incantation that suggests\nnothing but disdain. For a period of a minute thereafter, the\nmage improves his initimidation skill by +5D when taunt -\ning his opponents in combat, goading them into anger and\ncareless action. He adds one-half of the difference between\nthe difficulty and the initimidation roll to any one attack or\ndefense attempt (not both) made at Point Blank or Short\nrange. This bonus works only if the opponent is actively\nattacking the mage; the spell provides no bonus to a mage\nfighting a creature that is purely defensive and doesn’t want\nto fight. In addition, the spell only works against those who\ncan hear the mage speaking.",
        effect=SkillEffect("Boost intimidation", "+4D", "skill modifier"),
        duration=DurationAspect("1 minute"),
        range=RangeAspect("self"),
        casting_time=CastingTimeAspect("1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Folk", ""),
            "gestures": GesturesAspect(
                "Make a contemptous gesture at opponent", "simple"
            ),
            "incantations": IncantationsAspect(
                "“Is that the best you got?”, followed by piteous laughter",
                "sentence",
                "offensive",
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On caster"
            ),
        },
        other_conditions=[
            GenericAspect(
                -2,
                "May only be used attackers who understand the caster’s language and can hear the caster",
            ),
            GenericAspect(0, "Difficulty: 11"),
        ],
    ),
    Spell(
        name="Voice Wrack",
        skill="Conjuration",
        notes="The mage rubs his throat as if it’s irritated, then points at\na target and, coughing, whispers a simple incantation. The\nspell mutes the subject’s words so that his voice projects as\na mere whisper. Those within a meter of the target can hear\nhis words as normal, but those beyond that range are hard\npressed to make out a sound. Interactions with those further\nthan one meter distant are challenging (+3 to related difficul-\nties), because his voice carries no weight or inflection.",
        effect=DisadvantageEffect(
            "Hindrance: Hoarse ",
            7,
            note="+3 to  difficulties of actions requiring a voice, such bargain, charm, con, command, intimidation, languages/speaking, and persuasion",
        ),
        duration=DurationAspect("1 minute"),
        range=RangeAspect("10 meters"),
        casting_time=CastingTimeAspect("1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Folk", ""),
            "gestures": GesturesAspect(
                "Rub throat as if sore and then point at target", "simple"
            ),
            "incantations": IncantationsAspect(
                "Cough and whisper “steal voice.”", "phrase"
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On target"
            ),
        },
        other_conditions=[
            GenericAspect(
                -2,
                "Limited to those who can speak; spell has no effect at 1 meter or less from target",
            ),
            GenericAspect(0, "Difficulty: 19"),
        ],
    ),
    Spell(
        name="Wolfpack",
        skill="Alteration",
        notes="To cast the spell, the caster must have something from the\ntype of animal to be affected (feathers from a bird, shed snake\nskin, hairs from a horse’s mane), as well as a tuff of wolf fur.\nUpon uttering the incantation, the wolf fur is released and\nis instantly consumed by magical fire.\nThis spell can be used on any animal or monster, but\nsentient beings are unaffected. The target creatures must\nalso outnumber their opponents, because the rabid wolf-\nlike tactics induced by this spell depend upon the ability\nto outflank and overwhelm their enemies. For five rounds,\nall affected creatures fight with a ferocity and cunning that\nprovides them a brawling/fighting bonus of +2D.\n\n",
        effect=SkillEffect("Boost brawling/fighting", "+2D", "skill modifier"),
        duration=DurationAspect("5 rounds"),
        range=RangeAspect("10 meters"),
        casting_time=CastingTimeAspect("1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "arcane_knowledge": ArcaneKnowledgeAspect("Animal", ""),
            "components": ComponentsAspect(
                ("Something from the type of animal with which she wants to communicate", "very common"),
                ("tuft of wolf fur", "uncommon", "destroyed"),
            ),
            "gestures": GesturesAspect(
                "Toss wolf fur at target creatures while holding the component of the animals to be affected",
                "simple",
            ),
            "incantations": IncantationsAspect(
                "“Fight like the wolf!” followed by a wolf-like howl", "phrase", "loud"
            ),
            "focused": FocusedAspect.based_on(
                ("effect", "duration"), target="Focused on On targets"
            ),
            "multiple_targets": MultipleTargetAspect("8 targets")
        },
        other_conditions=[
            GenericAspect(-1, "Animals affected must outnumber their opponents"),
            GenericAspect(0, "Difficulty: 17"),
        ],
    ),
]

__test__ = {
    "Animal Loyalty": ">>> spells[0].difficulty\n21",  # Rules say 20
    "Animal Savior": ">>> spells[1].difficulty\n16",
    "Asp Arrow": ">>> spells[2].difficulty\n16",
    "Bashing Fists": ">>> spells[3].difficulty\n11",  # Rules say 10
    "Beast Warden": ">>> spells[4].difficulty\n23",  # Rules say 20; unreal aspect seems wrong
    "Blades of Flesh": ">>> spells[5].difficulty\n4", # Rules say 3
    "Club Feet": ">>> spells[6].difficulty\n31",
    "Cobra Strike": ">>> spells[7].difficulty\n11",  # Rules say 14, but improved charges are wrong
    "Courage": ">>> spells[8].difficulty\n23",
    "Eagle-Eye": ">>> spells[9].difficulty\n20",
    "Envy": ">>> spells[10].difficulty\n18",
    "Gang Fight": ">>> spells[11].difficulty\n28",  # Rules say 27
    "Gnawing Hunger": ">>> spells[12].difficulty\n36",  # Rules say 35
    "Graceful Step": ">>> spells[13].difficulty\n12",
    "Pollen Cloud": ">>> spells[14].difficulty\n13",  # Rules say 14, Components looks wrong
    "Quick Release": ">>> spells[15].difficulty\n9",  # Rules say 10
    "Reveal Disposition": ">>> spells[16].difficulty\n16",
    "Sense Ailment": ">>> spells[17].difficulty\n6",  # Rules say 11 -- Don't know why
    "Stick to Snake": ">>> spells[18].difficulty\n22",  # Rules say 23 -- can't figure out effect of 40.
    "Sticky Fingers": ">>> spells[19].difficulty\n3",  # Rules say 5
    "Taken Alive": ">>> spells[20].difficulty\n14",  # Rules say 15
    "Taunt": ">>> spells[21].difficulty\n11",
    "Voice Wrack": ">>> spells[22].difficulty\n19",
    "Wolfpack": ">>> spells[23].difficulty\n17",
}


if __name__ == "__main__":
    app = build_app(spells)
    app()

