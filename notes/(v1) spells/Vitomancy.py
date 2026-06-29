"""
Vitomancy
---------

"""

from magic1 import Aspect, Spell, Cantrip, detail

spells = [
    Spell(
        effect=Aspect(
            format="+2D to caster’s animal handling  or persuasion: animals [D6 Space only]; +2D to target’s willpower/mettle",
            base_difficulty=18,
            count=1,
        ),
        duration=Aspect(format="1 day ", base_difficulty=25, count=1),
        range=Aspect(format="Self or touch ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="2 rounds ", base_difficulty=-5, count=1),
        name="Animal Loyalty",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Animal", base_difficulty=0, count=1),
            "Difficulty": Aspect(
                format="20", base_difficulty=0, count=1
            ),  # Should be 21
            "Focused": Aspect(
                format="On caster and target", base_difficulty=8, count=1
            ),
            "Gestures": Aspect(
                format="Gently stroke the target animal (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="Make soothing sounds (phrase)", base_difficulty=-1, count=1
            ),
        },
        other_conditions=[
            Aspect(
                format="Limited to animals that are friendly to the caster; target and caster must remain within 10 meters of each other to get bonuses",
                base_difficulty=-2,
                count=1,
            )
        ],
        notes="To inspire unnatural loyalty in a pet, animal companion,\nor mount, the caster simply strokes the creature and makes\nreassuring, soothing sounds. For a full day thereafter, the\nanimal will be especially loyal to the caster, which translates\ninto an animal handling  (or persuasion: animals in D6 Space)\nbonus of +2D for the caster toward the target creature. In\naddition, because the animal is so trusting of the caster,\nwhenever it’s within 10 meters of the caster, it gains a will-\npower/mettle bonus of +2D to resist attempts, magical or\notherwise, by others to alter its behavior.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="+2D to lifting/lift to recover fallen comrades; +2D to willpower/mettle  to resist attempts to dissuade recovery",
            base_difficulty=18,
            count=1,
        ),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Animal Savior",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Animal", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="16", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Something from the type of animal targeted (very common); something from the individual to be protected by the target animal (very common)",
                base_difficulty=-4,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=7, count=1),
            "Gestures": Aspect(
                format="Draw a line on the ground (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(format="Limited to animals", base_difficulty=-1, count=1)
        ],
        notes="To cast this spell, the mage places on the ground something\nfrom that type of animal to be targeted (strands of dog’s fur\nor locks of horse’s hair, for example) and something from the\nindividual the animal is intended to watch over. She then\ndraws a line from these items toward the animal, and then\ntoward the individual to be protected.\nFor a period of one hour, the targeted animal keeps a watch-\nful eye over its ward. Should  the ward ever fall (rendered\nunconscious, incapacitated, paralyzed, dead, or otherwise\nunmoving), the animal will quickly descend upon the body\nand pull it to a location out of harm’s way. This spell grants\nthe animal a +2D lifting/lift bonus for this purpose, allowing\neven a small dog the ability to pull a human to safety, and\na +2D willpower/mettle bonus to resist efforts to dissuade\nintervention.\nWhile there is no range limitation on how far the animal\nwill theoretically pull the character, the location to which\nthe immobilized character is moved is always the nearest\n“safe” place. This might mean dragging the body out of a\nroom, behind a tree, into a defile, or any other such sheltered\nlocale. In an environment where there is no readily avail -\nable protection, such as barren and flat desert or plains, the\nanimal pulls the body far enough away to be removed from\nthe melee and out of range of whatever missile weapons the\nenemy possesses (if any).",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="4D damage, ignores nonmagical armor", base_difficulty=18, count=1
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Asp Arrow",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Animal", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="16", base_difficulty=0, count=1),
            "Component": Aspect(
                format="A live asp or other poisonous snake (uncommon)",
                base_difficulty=-4,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=5, count=1),
            "Gestures": Aspect(
                format="Crouch as if coiled like a snake, shape hand into a fist with two fingers extended like asp fangs, then spring and throw the gathered energy at target (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="Make a snake-like sound (phrase)", base_difficulty=-1, count=1
            ),
        },
        notes="To cast this spell, the mage must have a live asp or other\npoisonous snake on his person. Usually, mages keep them in\nsmall earthenware pots or reed baskets. By coiling himself as\na snake would, not only is he drawing upon energy to propel\nthe mystical arrow but is also tapping into the essence of the\nsnake itself. Once the mystical energy is released, an arrow\nappears and flies toward the intended target, to a range of\n10 meters. The mage must make a marksmanship/firearms or\napportation roll to hit the target. If the arrow flies true and\nhits, it immediately transforms into a large asp and delivers\na poisonous bite., which causes 4D of damage each round\nfor one minute. The asp arrow must be fired in the round\nafter the mage casts the spell. The mage may add the result\npoint bonus of the spell to either the targeting total or the\nfirst damage total.\n\n",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="Natural Hand-to-Hand Weapon: Fists (R2), +2D damage",
            base_difficulty=12,
            count=1,
        ),
        duration=Aspect(format="5 rounds ", base_difficulty=7, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="3.5 seconds ", base_difficulty=-3, count=1),
        name="Bashing Fists",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Folk", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="10", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Pair of black leather gloves (common)",
                base_difficulty=-3,
                count=1,
            ),
            "Gestures": Aspect(
                format="Put on gloves (fairly simple); punch each fist into the other open hand (simple)",
                base_difficulty=-3,
                count=1,
            ),
            "Incantations": Aspect(
                format="Let out an ear-splitting roar of rage (phrase, loud)",
                base_difficulty=-2,
                count=1,
            ),
            "Other Alterant": Aspect(
                format="Opponent receives increased difficulties with each landed punch",
                base_difficulty=12,
                count=1,
            ),
        },
        notes="To cast the spell, the mage must first put on a pair of black\nleather gloves. The mage then lets out a roar as mighty as he\ncan muster and punches each of his fists into an open hand,\nall the while feeling himself become overwhelmed with a\nsense of pent-up rage. This violent urge must be released\nwithin the next five rounds or it dissipates, and can only be\nreleased in unarmed combat. The spell provides the Natural\nHand-to-Hand Weapons: Fists Special Ability, which gives the\nattacker +2D to his unarmed Strength Damage. In addition\nto damage inflicted, each blow landed by the mage pushes\nhis foe. This causes the victim to stumble, reducing all Agil-\nity/Reflexes or related totals by 3 until the mage’s turn in\nthe next round.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="+4D to intimidation", base_difficulty=18, count=1),
        duration=Aspect(format="10 minutes ", base_difficulty=14, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Beast Warden",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Animal", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="20", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Sphere with radius of 3 meters", base_difficulty=15, count=1
            ),
            "Components": Aspect(
                format="Rowan berries (uncommon, destroyed)",
                base_difficulty=-8,
                count=1,
            ),
            "Countenance": Aspect(
                format="Animal appears menancing", base_difficulty=-2, count=1
            ),
            "Gestures": Aspect(
                format="Point from target to those to be guarded, bear teeth and snarl (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Guard.” (phrase)", base_difficulty=-1, count=1
            ),
            "Unreal Effect": Aspect(
                format="Disbelief difficulty of 13", base_difficulty=-8, count=1
            ),
            "Other Alterants": Aspect(
                format="Animal will fight to the death to keep captives in area of effect",
                base_difficulty=10,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="May only be used on animals who are friendly to the caster",
                base_difficulty=-2,
                count=1,
            )
        ],
        notes="To cast this spell, the mage must have a small supply ber-\nries harvested from a rowan tree. The mage points at the\nanimal he wishes to target, then at a creature or creature he\nwishes the animal to guard, snarling and bearing his teeth\nto get the point across. After uttering a simple command\nword, the spell is cast. The target animal devotedly keeps\nthe specified beings in a confined area measuring three\nmeters in diameter by circling. In the eyes of its captives, the\nanimal’s countenance changes completely, become far more\nfrightening and imposing. As a result, the animal gains an\nintimidation skill bonus of +4D.\nMost captives are too frightened to attempt escape, save\nfor those who make a willpower/mettle roll of 13 to disbelieve\nthe spell’s effect. Captives attempting to escape find them -\nselves harrassed immediately upon trying to leave the area\nof effect. The animal attacks until either it or the prisoner\nis dead or subdued.\nWhile predators are most often targeted, this spell is by\nno means limited to them. Herbivores, such as boars, deer,\nand bulls, can be equally effective.\nBlades of Flesh",
        skill="Alteration",
    ),
    Cantrip(
        effect=Aspect(
            format="Natural Hand-to-Hand Weapon: Blades of Flesh (R1), +1D damage",
            base_difficulty=6,
            count=1,
        ),
        duration=Aspect(format="5 rounds ", base_difficulty=7, count=1),
        range=Aspect(
            format="Self or target within 1 meter ", base_difficulty=0, count=1
        ),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Blades of Flesh",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Folk", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="3", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Any bladed weapon (common)", base_difficulty=-3, count=1
            ),
            "Focused": Aspect(format="On target", base_difficulty=2, count=1),
            "Gestures": Aspect(
                format="Draw weapon across hand (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes="This spell gives the target a bonus of +1D to Strength\nDamage for 25 seconds, or five rounds. With the simple slash\nof a blade, the spell transforms the target’s hands, elbows,\nand feet into lethal blades of flesh that can slash or pierce\nas well as bludgeon.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="Hindrance: Club Feet (R12): +4 to the difficulty of any foot-related skill use and -4 to initiative rolls",
            base_difficulty=36,
            count=1,
        ),
        duration=Aspect(format="10 minutes ", base_difficulty=14, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Club Feet",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Animal, Folk", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="31", base_difficulty=0, count=1),
            "Focused": Aspect(format="On target", base_difficulty=10, count=1),
            "Gestures": Aspect(
                format="Mime tripping and falling, eyes focused on target (complex; acrobatics roll with difficulty of 11)",
                base_difficulty=-3,
                count=1,
            ),
            "Incantations": Aspect(
                format="“I’m such a clumsy oaf.” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes="While willingly causing himself to trip and fall (acrobatics\nroll of 11 or fail the spell due to ineptitude), and casually\nexcusing himself for his clumsiness, the mage casts this\npotent spell and curses a target not more than 10 meters\naway. The curse twists the victim’s feet until they are hor -\nribly misshapen, rendering his legs so uncoordinated that\nhe can literally trip over himself. This is reflected by a +4\nto the difficulties of various foot-related tasks and a -4 to\ninitiative totals. When the spell wears off 10 minutes later,\nthe character is restored immediately to normal.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="3D damage, ignores all armor", base_difficulty=18, count=1
        ),
        duration=Aspect(format="5 rounds ", base_difficulty=7, count=1),
        range=Aspect(format="Touch ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Cobra Strike",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Folk, Animal", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="14", base_difficulty=0, count=1),
            "Charges": Aspect(
                format="2 improved charges released only with successful attack",
                base_difficulty=11,
                count=1,
            ),
            "Components": Aspect(
                format="Cobra skin gloves (very rare); flute (very common)",
                base_difficulty=-6,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=5, count=1),
            "Gestures": Aspect(
                format="Play tune on a flute (complex; artist roll with difficulty of 11)",
                base_difficulty=-3,
                count=1,
            ),
        },
        notes="This spell requires the caster to wear cobra skin gloves\nand have a flute. The mage casts the spell by playing a short\ntune on her flute, the kind that snake-charmers use to lure\ncobras from their wicker pots. On the next round, as the mage\nattemtps to land an open-handed strike, her hand spreads out\nlike a hood, and the head of a cobra momentarily appears in\nthe palm to strike the target. On a successful attack, the blow\ninflicts normal unarmed damage and for five rounds (starting\nwith the one in which the blow landed), the victim is poisoned\nand takes 3D damge per round until duration ends.\n\n",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="+6D+2 to willpower/mettle", base_difficulty=30, count=1),
        duration=Aspect(format="2.5 minutes ", base_difficulty=11, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Courage",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Folk", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="23", base_difficulty=0, count=1),
            "Area of Effect": Aspect(
                format="Sphere with radius of 5 meters", base_difficulty=25, count=1
            ),
            "Components": Aspect(
                format="Braided lion’s mane rope (very rare)",
                base_difficulty=-4,
                count=1,
            ),
            "Concentration": Aspect(
                format="3 seconds with willpower/mettle difficulty of 7",
                base_difficulty=-1,
                count=1,
            ),
            "Feedback": Aspect(
                format="-3 to damage resistance totals", base_difficulty=-3, count=1
            ),
            "Gestures": Aspect(
                format="Hold the lion’s mane rope above the head and shake it while turning in a circle (complex; acrobatics roll with difficulty of 11)",
                base_difficulty=-3,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Fight by me, my friends, and together we’ll taste victory or achieve immortality” (sentence, loud)",
                base_difficulty=-3,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="Limited to sentient beings and those who are neutral or trusting of the mage",
                base_difficulty=-2,
                count=1,
            )
        ],
        notes="Casting this spell requires the mage to have a rope braided\nfrom lion’s mane. He holds the rope aloft as a symbol of cour-\nage and shakes it mightily as he turns in a complete circle,\ndemonstrating its importance to all around him.\nFor a period of more than two minutes thereafter, his mere\npresence steadies his allies when terror would otherwise fill\ntheir hearts and shake their resolve. All allies with a 5-meter\nradius gain a willpower/mettle skill bonus of +6D+2 for resist-\ning fear, intimidation, or even pain and torture.\nUnder the influence of this spell, only the most weak\nhearted of characters will break rather than present a stoic\nface to their enemies. If a character affected by fear is ral -\nlied by her companions, she may roll again to shake off the\neffect. This spell can only be used on sentient beings, and it\nonly affects individuals who are neutral toward or trusting\nof the mage.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(format="+4D to search", base_difficulty=18, count=1),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="5 rounds ", base_difficulty=-7, count=1),
        name="Eagle-Eye",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Folk, Avian", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="20", base_difficulty=0, count=1),
            "Area of Effect": Aspect(
                format="Divination sphere with radius of 10 meters",
                base_difficulty=15,
                count=1,
            ),
            "Component": Aspect(
                format="Eye of an eagle (uncommon, destroyed)",
                base_difficulty=-8,
                count=1,
            ),
            "Concentration": Aspect(
                format="25 seconds with a willpower/mettle difficulty of 9",
                base_difficulty=-3,
                count=1,
            ),
            "Focused": Aspect(format="On caster", base_difficulty=5, count=1),
            "Gestures": Aspect(
                format="Ingest the eagle’s eye (simple)", base_difficulty=-1, count=1
            ),
            "Variable Duration": Aspect(
                format="On/off switch", base_difficulty=8, count=1
            ),
        },
        other_conditions=[
            Aspect(
                format="-6 to Agility/Reflexes and related totals while spell is active",
                base_difficulty=-6,
                count=1,
            )
        ],
        notes="The caster ingests an eye of an eagle, closes his eyes, and\nconcentrates. When he opens his eyes after 25 seconds, the\nmage perceives a bird’s eye view of his surrounding area, as\nthough he was looking down from the vantage point of a\nsoaring eagle. The mage gains awareness of all objects within\n10 meters of his person that are large enough to normally\nbe seen with his eye. However, the mage cannot see under\nor through solid objects.\nThe area of effect moves with the caster until the spell\ndissolves after one minute.\nCreatures may attempt to hide from the mage, but he gains\na search bonus of +4D to see them because of his vantage\npoint. This may have the unintended and happy side effect\nof preventing surprise — assuming the mage notices his\nattackers before they strike.\nThe mage may target spells at anything he sees through\nthis spell as if he had line of sight. However, he must still\naccount for cover. For example, a character hiding behind\nan overturned table still enjoys such cover as it provides,\neven though he is clearly seen through the mage’s bird’s eye\nview; remember, the spell still originates from the mage’s\nphysical form.\nThe unusual perspective can be disorienting for the mage,\nand during the spell’s duration, he suffers -6 to all Agility/\nReflexes and related totals while spell is active.",
        skill="Divination",
    ),
    Spell(
        effect=Aspect(
            format="Quirk (R3), envy requiring a Very Difficult willpower/mettle roll to overcome Disadvantage",
            base_difficulty=9,
            count=1,
        ),
        duration=Aspect(format="4 hours ", base_difficulty=21, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="2 rounds ", base_difficulty=-5, count=1),
        name="Envy",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Folk", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="18", base_difficulty=0, count=1),
            "Concentration": Aspect(
                format="1 round with willpower/mettle difficulty of 8",
                base_difficulty=-2,
                count=1,
            ),
            "Feedback": Aspect(
                format="-3 to damage resistance totals", base_difficulty=-3, count=1
            ),
            "Focused": Aspect(format="On target", base_difficulty=6, count=1),
        },
        notes="While casting this spell is moderately painful to the mage,\nit might well be the death of the target. The caster curses a\nhumanoid target that she can see with four hours of extreme\nenvy. Envy is the desire to possess what others have. Those\nafflicted with envy covet what others have —personality\ntraits, personal good fortune, and material goods. The need\nto prove themselves, to obtain a perceived glory or possess\na valuable item, often places the individuals in potentially\ndangerous situations — they might rush to disarm a trap,\npush other characters aside to be the first to fight a foe, or race\nto secure a treasure headless of potential risks. A character\ntargeted by this spell must make a Very Difficult  willpower/\nmettle roll to overcome his envious impulses.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="+2D to brawling/fighting and melee combat; +2D to intimidation",
            base_difficulty=27,
            count=1,
        ),
        duration=Aspect(format="5 rounds ", base_difficulty=7, count=1),
        range=Aspect(format="5 meters ", base_difficulty=4, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=4, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Gang Fight",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Folk", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="27", base_difficulty=0, count=1),
            "Focused": Aspect(format="On targets", base_difficulty=6, count=1),
            "Gestures": Aspect(
                format="Frown menacingly and point with authority at allies (complex; intimidation roll with difficulty of 11)",
                base_difficulty=-3,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Rip ’em apart, boys” (sentence, loud)",
                base_difficulty=-3,
                count=1,
            ),
            "Multiple Targets": Aspect(
                format="Up to 6 targets", base_difficulty=18, count=1
            ),
        },
        other_conditions=[
            Aspect(
                format="Targets must be allies of the caster and either outnumber the oppoents or have them at a decisive disadvantage",
                base_difficulty=-2,
                count=1,
            )
        ],
        notes="When the mage attempts to cast this spell, he must pres-\nent a commanding and frightful image by succeeding an\nintimidation roll with a difficulty of 11. If she fails this, she\nsimply doesn’t present herself with enough menacing author-\nity and the spell doesn’t work. If successful, however, mage\nmakes up to six allies fight with ruthless vigor, employing all\nmanner of dirty tricks and providing them a bonus to their\nclose combat skills of +2D. It also lends them a menacing air,\nresulting in an intimidation bonus of 2D.\nThe targets must outnumber their opponents or have a\nmarked disadvantage, because the thuglike tactics the caster\nwishes her allies to employ depend to a large degree upon\nintimidation and ganging-up on victims.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="4D damage, ignores all armor; Achilles’ Heel (R4), metabolic difference — must eat a meal every two hours or all mental and physical attributes decrease by 1 pip, with penalty increasing by 1 pip for each hour without food and disappearing with consumption of food",
            base_difficulty=36,
            count=1,
        ),
        duration=Aspect(format="1 day ", base_difficulty=25, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Gnawing Hunger",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Animal, Folk", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="35", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Any food item that might be eaten by the intended target (ordinary, destroyed)",
                base_difficulty=-2,
                count=1,
            ),
            "Countenance": Aspect(
                format="The caster’s  skin tightens around the cheeks in a sickly fashion",
                base_difficulty=-2,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=12, count=1),
            "Gestures": Aspect(
                format="Double over in direction of the target as if suffering severe abdominal pain (fairly simiple)",
                base_difficulty=-3,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Hunger gnaws like a ravenous beast!” (sentence, loud)",
                base_difficulty=-3,
                count=1,
            ),
        },
        notes="To cast this spell, the mage must have in an item of food\nthat the target might reasonably be expected to eat (meat for\na carnivore, plants for an herbivore). She holds this item in\nher hand while pointing a finger at the target, and when she\ndoubles over mimicking stomach pains as the food crumbles\nto dust. While performing these actions, she utters a simple\nbut malicious phrase, after which the target suffers 4D damage\nfrom intense stomach pains. The target literally begins starv-\ning to death and at an accelerated pace. ll mental and physical\nattributes decrease by 1 pip (with the penalty increasing by\n1 pip for each hour without food) due to weakness. These\npenalties are negated once the target has eaten.\n\n",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="+1D+1 to acrobatics, dodge, and sneak/stealth",
            base_difficulty=18,
            count=1,
        ),
        duration=Aspect(format="5 rounds ", base_difficulty=7, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Graceful Step",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Animal, Folk", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="12", base_difficulty=0, count=1),
            "Focused": Aspect(format="On target", base_difficulty=5, count=1),
            "Gestures": Aspect(
                format="Shake one leg, then the next (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes="This spell makes the target graceful for a period of five\nrounds, which affects her acrobatics, dodge, and sneak/stealth\nattempts and increases them by 1D+1.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(format="2D of cover modifier", base_difficulty=6, count=1),
        duration=Aspect(format="5 rounds ", base_difficulty=7, count=1),
        range=Aspect(format="3 meters ", base_difficulty=3, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=3, count=1),
        casting_time=Aspect(format="1.5 seconds ", base_difficulty=-1, count=1),
        name="Pollen Cloud",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Plant", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="14", base_difficulty=0, count=1),
            "Area of Effect": Aspect(
                format="Sphere with radius of 3 meters", base_difficulty=15, count=1
            ),
            "Components": Aspect(
                format="Fresh flower bloom (very common, destroyed)",
                base_difficulty=-2,
                count=1,
            ),
            "Feedback": Aspect(
                format="-3 to damage resistance total", base_difficulty=-3, count=1
            ),
            "Focused": Aspect(format="On target", base_difficulty=2, count=1),
            "Gestures": Aspect(
                format="Bring bloom to lips and gently blow (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Belladonna’s breath.” (phrase)", base_difficulty=-1, count=1
            ),
        },
        other_conditions=[
            Aspect(format="Spell negated by strong winds", base_difficulty=-1, count=1)
        ],
        notes="With some minor pain to herself, the mage creates a cloud\nof pollen. To cast this spell, she must have a fresh flower,\nwhich she brings to her lips and then blows in the intended\ndirection. After uttering a simple incantation, a dense cloud of\npollen emerges from the bloom and quickly fills a six-meter-\nwide sphere. The pollen cloud is as thick as fog, providing\n2D of cover modifier. Under normal conditions, the cloud\ndissipates after five rounds. However, in moderately windy\nconditions it blows away after two rounds, and heavy winds\nprevent the spell from working entirely.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="Fast Reactions (R1), +1D to initiative roll and one additional free action in each of 3 rounds, with Ability Loss (R1), only useful with throwing; +2D to throwing",
            base_difficulty=12,
            count=1,
        ),
        duration=Aspect(format="5 minutes ", base_difficulty=13, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="3.5 seconds ", base_difficulty=-3, count=1),
        name="Quick Release",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Folk", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="10", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Spearhead (common, destroyed)", base_difficulty=-6, count=1
            ),
            "Focused": Aspect(format="On caster", base_difficulty=5, count=1),
            "Gestures": Aspect(
                format="Squeeze palms together with spearhead between (simple)",
                base_difficulty=-1,
                count=1,
            ),
        },
        notes="The caster places a spearhead in his hands and crushes\nit between his palms, leaving his hands bloodied and the\nspearhead mere dust. Until the blood dries (a period of about\n10 minutes), the mage becomes extremely fast at releasing\nthrown weapons. This results in +1D bonus to his initiative\nroll when wielding thrown weapons. In addition, because\nhe can release weapons with such amazing speed, he can\nmake an additional throwing attack in up to three rounds.\nThis spell provides no benefit when using missile weapons\nor firearms.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="willpower/mettle of 8D", base_difficulty=24, count=1),
        duration=Aspect(format="10 minutes ", base_difficulty=14, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="2 rounds ", base_difficulty=-5, count=1),
        name="Reveal Disposition",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Folk", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="16", base_difficulty=0, count=1),
            "Concentration": Aspect(
                format="10 seconds with willpower/mettle difficulty of 8",
                base_difficulty=-2,
                count=1,
            ),
            "Feedback": Aspect(
                format="-3 to damage resistance totals", base_difficulty=-3, count=1
            ),
            "Focused": Aspect(format="On target", base_difficulty=7, count=1),
            "Gestures": Aspect(
                format="Make a gesture of friendship (simple)",
                base_difficulty=-1,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="Target must interact with the target; may only be used on a single sentient being who understand the caster’s language",
                base_difficulty=-3,
                count=1,
            )
        ],
        notes="This spell is particularly useful by individuals involved in\ndelicate diplomacy. After meditating in silence for 10 seconds,\nthe mage warmly introduces herself to the individual that she\nwants to influence. The person must be a sentient being who\nunderstands her language. If the target doesn’t comprehend\nher, the spell and her time are wasted. Interpreters aren’t\nsufficient, as the spell relies upon personal interaction and\ncommon ground.\nWhen the spell is successfully cast, the mage rolls the will-\npower/mettle from the spell against the opponent’s willpower/\nmettle. By beating this difficulty, the caster senses the target’s\ndisposition toward her by seeing a glowing aura around it.\nThe aura is visible only to the mage. A white light suggests\nthe target is friendly or trusting; a gray-shaded aura indicates\nthat he is neutral or ambivalent. A shadow falling over the\ntarget indicates he is hostile or has superior standing.\nSince this spell lasts for 10 minutes, the mage may track how\nthe target’s disposition changes over the course of negotia-\ntions, allowing her to know the effectiveness of her diplomacy\nand attempts to change the target’s disposition. Because the\nmage can sense the nature of the target’s intentions (positive,\nambivalent, or harmful), she enjoys a willpower/mettle of 8D\nwhen resisting his interaction attempts.",
        skill="Divination",
    ),
    Spell(
        effect=Aspect(format="medicine/healing of 5D+2", base_difficulty=17, count=1),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="2 rounds ", base_difficulty=-5, count=1),
        name="Sense Ailment",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Animal, Folk", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(
                format="11", base_difficulty=0, count=1
            ),  # SHould be 6
            "Component": Aspect(
                format="An egg (very common, destroyed); bowl of water (ordinary)",
                base_difficulty=-5,
                count=1,
            ),
            "Concentration": Aspect(
                format="10 seconds with willpower/mettle difficulty of 8",
                base_difficulty=-2,
                count=1,
            ),
            "Gestures": Aspect(
                format="Run egg over patient and then crack it open into the bowl (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes="This spell allows a mage to tell if a creature suffers from the\neffects of poison, disease, or illness. Before casting this spell,\nshe enters a trance-like state while she runs an egg repeat -\nedly over the body of the patient. She then cracks it open\ninto a bowl of water. Using the skill provided by the spell,\nthe mage can interpret the egg’s appearance to determine\npresence and type of disease, toxin, or injury.\nIf the egg yoke floats to the surface, the patient is free of\nailments. If the yoke sinks, on the other hand, the creature\nis ill and the mage may figure out the cause.\nThe difficulty to detect the presence of an ailment is 7.\nWith five to eight result points, the mage understands the\nnature of the ailment. With nine to 16 result points, the\ncaster knows the cure. With 17 or more result points, the\nhealer figures out the cause.\nThis spell does not heal a patient of his ailment, nor does\nit provide any bonus to healing wounds or injuries.\n\n",
        skill="Divination",
    ),
    Spell(
        effect=Aspect(
            format="brawling/fighting of 5D; running of 2D; 5D physical damage; movement equal to result points in meters round with minimum of 1 meter per round",
            base_difficulty=40,
            count=1,
        ),
        duration=Aspect(format="5 minutes ", base_difficulty=13, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        name="Stick to Snake",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Plant, Animal", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="23", base_difficulty=0, count=1),
            "Component": Aspect(
                format="A long, thin dried stick (ordinary); rattlesnake tail rattle (uncommon)",
                base_difficulty=-5,
                count=1,
            ),
            "Focused": Aspect(format="On stick", base_difficulty=10, count=1),
            "Gestures": Aspect(
                format="Shake rattlesnake rattle while holding stick (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Wood to flesh and stick to snake.” (sentence).",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes="This spell turns a dead branch or other long pieces of thin,\ndried wood (arrow shafts, broomsticks, and so on) into a\nlarge and aggressive snake. To cast this spell, the mage must\nhave one hand on the wood while he shakes a rattlesnake tail\nrattle. After reciting the incantation, he drops the stick and\nwatches as it comes to life as a flesh-and-blood snake.\nIf provoked, the snake attacks whomever or whatever is\nnear it. When killed or the spell expires, the snake reverts\nback to its original form.\n\n\nSticky Fingers",
        skill="Conjuration",
    ),
    Cantrip(
        effect=Aspect(format="+2D to sleight of hand", base_difficulty=9, count=1),
        duration=Aspect(format="5 rounds ", base_difficulty=7, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Sticky Fingers",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Folk", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="5", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Ball of wax (very common, destroyed)",
                base_difficulty=-4,
                count=1,
            ),
            "Focused": Aspect(format="On caster", base_difficulty=3, count=1),
            "Gestures": Aspect(
                format="Rub fingers together (simple)", base_difficulty=-1, count=1
            ),
        },
        notes="(Cantrip) The caster places a small ball of wax in each hand and rubs\nhis fingers tips together, spreading the wax evenly over his\nfingertips. His fingers then become sticky and more nimble,\nallowing him to pick pockets, palm objects, and perform\nsimilar actions that require deft motor control with unnatural\nease. As a result, the character gains a sleight of hand bonus\nof +2D.\nThe sticky substance secreted by the character’s fingers is\nnot strong enough to have any direct application to climbing,\ngrappling, or any other related action that requires the use\nof strength as opposed to mere deftness of hand.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(format="+6D+2 to bluff/con", base_difficulty=30, count=1),
        duration=Aspect(format="4 hours ", base_difficulty=21, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        name="Taken Alive",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Death, Folk", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="15", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Garment made of valuable fabric (uncommon, destroyed); fire, such as match or lit coal (very common, destroyed)",
                base_difficulty=-12,
                count=1,
            ),
            "Concentration": Aspect(
                format="25 seconds with a willpower/mettle difficulty of 9",
                base_difficulty=-3,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=10, count=1),
            "Gestures": Aspect(
                format="Inhale smoke (simple)", base_difficulty=-1, count=1
            ),
            "Unreal Effect": Aspect(
                format="Disbelief difficulty of 13", base_difficulty=-8, count=1
            ),
            "Other Alterants": Aspect(
                format="Also works unconsciously", base_difficulty=2, count=1
            ),
        },
        other_conditions=[
            Aspect(
                format="May only be used on those that understand the concepts of wealth and ransom",
                base_difficulty=-1,
                count=1,
            )
        ],
        notes="While casting the spell, the mage sets on fire a garment\nmade of valuable fabric, such as a foreign cloth or silk. She\nthen inhales the smoke while concentrating for almost half\na minute.\nOnce the casting is complete, the mage (or her desired tar-\nget) exudes an aura that makes her enemies believe she is less\nvaluable dead than she is alive as ransom. When surrender-\ning, the caster gains a bluff/con bonus of +6D+2 to convince\nopponents of her worth and to spare her life by taking her\nprisoner, rather killing her. She also may bluff opponents\ninto believing her inflated worth even when unconscious or\notherwise incapacitated, as the enemy perceives noble stand-\ning or cultured bearing even in her motionless form.\nOf course, the enemy will expect that a ransom is forthcom-\ning, and after the spell’s duration expires the captive mage\nloses her bluff/con skill bonus and is no longer necessarily\nviewed as a valuable commodity.\nThis spell only affects those that understand the concepts\nof wealth and ransom.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(format="+4D to intimidation", base_difficulty=18, count=1),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Taunt",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Folk", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="11", base_difficulty=0, count=1),
            "Focused": Aspect(format="On caster", base_difficulty=5, count=1),
            "Gestures": Aspect(
                format="Make a contemptous gesture at opponent (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Is that the best you got?”, followed by piteous laughter (sentence, offensive)",
                base_difficulty=-3,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="May only be used attackers who understand the caster’s language and can hear the caster",
                base_difficulty=-2,
                count=1,
            )
        ],
        notes="This spell is cast with a smile that conveys contempt for\nan opponent’s abilities, a taunting gesture that urges him to\nattack the mage, and an insulting incantation that suggests\nnothing but disdain. For a period of a minute thereafter, the\nmage improves his initimidation skill by +5D when taunt -\ning his opponents in combat, goading them into anger and\ncareless action. He adds one-half of the difference between\nthe difficulty and the initimidation roll to any one attack or\ndefense attempt (not both) made at Point Blank or Short\nrange. This bonus works only if the opponent is actively\nattacking the mage; the spell provides no bonus to a mage\nfighting a creature that is purely defensive and doesn’t want\nto fight. In addition, the spell only works against those who\ncan hear the mage speaking.",
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="Hindrance: Hoarse (R7), +3 to  difficulties of actions requiring a voice, such bargain, charm, con, command, intimidation, languages/speaking, and persuasion",
            base_difficulty=21,
            count=1,
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Voice Wrack",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Folk", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="19", base_difficulty=0, count=1),
            "Focused": Aspect(format="On target", base_difficulty=6, count=1),
            "Gestures": Aspect(
                format="Rub throat as if sore and then point at target (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="Cough and whisper “steal voice.” (phrase)",
                base_difficulty=-1,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="Limited to those who can speak; spell has no effect at 1 meter or less from target",
                base_difficulty=-2,
                count=1,
            )
        ],
        notes="The mage rubs his throat as if it’s irritated, then points at\na target and, coughing, whispers a simple incantation. The\nspell mutes the subject’s words so that his voice projects as\na mere whisper. Those within a meter of the target can hear\nhis words as normal, but those beyond that range are hard\npressed to make out a sound. Interactions with those further\nthan one meter distant are challenging (+3 to related difficul-\nties), because his voice carries no weight or inflection.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="+2D to brawling/fighting", base_difficulty=9, count=1),
        duration=Aspect(format="5 rounds ", base_difficulty=7, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Wolfpack",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Animal", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="17", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Something from the type of animal with which she wants to communicate (very common); tuff of wolf fur (uncommon, destroyed)",
                base_difficulty=-10,
                count=1,
            ),
            "Focused": Aspect(format="On targets", base_difficulty=3, count=1),
            "Gestures": Aspect(
                format="Toss wolf fur at target creatures while holding the component of the animals to be affected (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Fight like the wolf!” followed by a wolf-like howl (phrase, loudly)",
                base_difficulty=-2,
                count=1,
            ),
            "Multiple targets": Aspect(format="8 targets", base_difficulty=24, count=1),
        },
        other_conditions=[
            Aspect(
                format="Animals affected must outnumber their opponents",
                base_difficulty=-1,
                count=1,
            )
        ],
        notes="To cast the spell, the caster must have something from the\ntype of animal to be affected (feathers from a bird, shed snake\nskin, hairs from a horse’s mane), as well as a tuff of wolf fur.\nUpon uttering the incantation, the wolf fur is released and\nis instantly consumed by magical fire.\nThis spell can be used on any animal or monster, but\nsentient beings are unaffected. The target creatures must\nalso outnumber their opponents, because the rabid wolf-\nlike tactics induced by this spell depend upon the ability\nto outflank and overwhelm their enemies. For five rounds,\nall affected creatures fight with a ferocity and cunning that\nprovides them a brawling/fighting bonus of +2D.\n\n",
        skill="Alteration",
    ),
]

if __name__ == "__main__":
    # import logging, sys
    # logging.basicConfig(level=logging.DEBUG, stream=sys.stderr)
    # for spell in spells:
    #     spell._difficulty()

    detail(spells)


__test__ = {
    "Animal Loyalty": ">>> spells[0].difficulty\n21",
    "Animal Savior": ">>> spells[1].difficulty\n16",
    "Asp Arrow": ">>> spells[2].difficulty\n16",
    "Bashing Fists": ">>> spells[3].difficulty\n10",
    "Beast Warden": ">>> spells[4].difficulty\n20",
    "Cantrip": ">>> spells[5].difficulty\n3",
    "Club Feet": ">>> spells[6].difficulty\n31",
    "Cobra Strike": ">>> spells[7].difficulty\n14",
    "Courage": ">>> spells[8].difficulty\n23",
    "Eagle-Eye": ">>> spells[9].difficulty\n20",
    "Envy": ">>> spells[10].difficulty\n18",
    "Gang Fight": ">>> spells[11].difficulty\n27",
    "Gnawing Hunger": ">>> spells[12].difficulty\n35",
    "Graceful Step": ">>> spells[13].difficulty\n12",
    "Pollen Cloud": ">>> spells[14].difficulty\n14",
    "Quick Release": ">>> spells[15].difficulty\n10",
    "Reveal Disposition": ">>> spells[16].difficulty\n16",
    "Sense Ailment": ">>> spells[17].difficulty\n6",
    "Stick to Snake": ">>> spells[18].difficulty\n23",
    "Cantrip": ">>> spells[19].difficulty\n5",
    "Taken Alive": ">>> spells[20].difficulty\n15",
    "Taunt": ">>> spells[21].difficulty\n11",
    "Voice Wrack": ">>> spells[22].difficulty\n19",
    "Wolfpack": ">>> spells[23].difficulty\n17",
}
