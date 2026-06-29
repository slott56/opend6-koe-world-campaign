"""
Elemental
---------

This was significantly edited to correct parsing problems.
Avoid running parse_spells and overwriting it
"""

from textwrap import dedent
from magic1 import Aspect, Spell, detail

spells = [
    Spell(
        effect=Aspect(
            format="5D physical damage, ignores nonmagical armor",
            base_difficulty=23,
            count=1,
        ),
        duration=Aspect(format="5 rounds ", base_difficulty=7, count=1),
        range=Aspect(format="25 meters ", base_difficulty=7, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=7, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Acidic Attack",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Water", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="20", base_difficulty=0, count=1),
            "Component": Aspect(
                format="Small vile of acid (uncommon)", base_difficulty=-4, count=1
            ),
            "Focused": Aspect(format="On target", base_difficulty=6, count=1),
            "Gestures": Aspect(
                format="Shaking the vile at the target (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Burn!.” (phrase)", base_difficulty=-1, count=1
            ),
        },
        notes=dedent("""\
            When a mage casts acidic attack, the spell lasts for 5 rounds.
            Each round, damage continues, but is reduced by 1D. This
            represents the acid’s potency gradually decreasing.  Nonmagi-
            cal armor does not offer a defense against this spell, as the
            mystical corrosive promptly burns through metal, leather,
            clothing, and so on.
            
            As the attack is magical, there is no way to extinguish the
            acid except to dispel it.
        """),
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(format="moves up to 150 kilograms", base_difficulty=18, count=1),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="2.5 seconds ", base_difficulty=-2, count=1),
        name="Burrow",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Earth", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="18", base_difficulty=0, count=1),
            "Components": Aspect(
                format="A mole skull (common)", base_difficulty=-3, count=1
            ),
            "Focused": Aspect(format="On caster", base_difficulty=7, count=1),
            "Gestures": Aspect(
                format="Digging motions with hands (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Dig.” (phrase)", base_difficulty=-1, count=1
            ),
            "Variable Movement": Aspect(
                format="Movement of 5 meters per round", base_difficulty=1, count=1
            ),
        },
        notes=dedent("""\
            The burrow spell allows the caster to move through all types
            of soil at a rapid pace. When the spell is completed, the caster
            sinks into the earth in a fountain of dirt and sand. As he
            travels through the earth, the soil in front of him is pushed
            behind, collapsing the tunnel he creates. The mage using the
            spell will have a rudimentary idea of which way he is going,
            but he may need to poke his head back above the surface from
            time to time to make sure he is not going off track.
            
            The spell does not allow the caster to move through stone
            or any material harder than clay. He usually travels one meter
            under the surface, but if he encounters stone that he cannot
            penetrate, he may go up or down in the strata to avoid it.
            
            There is a small pocket of air that travels with the user,
            allowing him to breathe as he wriggles through the soil.
            Several trips to the surface during the duration are necessary
            to refresh this air pocket.
        """),
        skill="Apportation",
    ),
    Spell(
        effect=Aspect(format="brawling/fighting of 6D", base_difficulty=18, count=1),
        duration=Aspect(format="1 second ", base_difficulty=0, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="2.5 seconds ", base_difficulty=-2, count=1),
        name="Cone of Wind",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Air", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="11", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Cone 8 meters long and 4 meters at its wide end",
                base_difficulty=10,
                count=1,
            ),
            "Gestures": Aspect(
                format="Both hands make a pushing motion in the direction of the wind (simple)",
                base_difficulty=-1,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Mighty wind, drive my enemies before me!” (sentence, loud)",
                base_difficulty=-3,
                count=1,
            ),
        },
        notes=dedent("""\
            This spell is a favorite of mages who want to knock down
            opponents without doing any permanent injury. When the
            spell is cast a cone of powerful wind blasts from the caster’s
            hands out to a distance of eight meters. The cone is about
            30 centimeters wide at the casters hands and spreads out to
            four meters in diameter at its far end.
            
            The caster rolls the brawling/fighting score that the spell
            generates once; this total is used as a knockdown attempt
            against the combat difficulty for each target within one meter
            of the caster. (Those over one meter away get a +1 bonus to
            their defense totals per full meter distant.)  Anyone who fails
            to withstand the blast fall to the ground and must spend an
            action in the next round getting up.
            
            This attack affects opponents with a Physique/Strength
            die code of no more than the spell’s skill total divided by 3
            (ignore any remainder).
            
            This spell does not require a separate targeting roll.
        """),
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="command: elemental of 6D", base_difficulty=18, count=1),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="2.5 meters ", base_difficulty=3, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=3, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Control Elemental (Template)",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Entity, any one element: air, earth, fire, or water",
                base_difficulty=0,
                count=1,
            ),
            "Difficulty": Aspect(format="18", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Small figurine of elemental type, made of precious metals and jewels (very rare)",
                base_difficulty=-5,
                count=1,
            ),
            "Focused": Aspect(format="On caster", base_difficulty=7, count=1),
            "Gestures": Aspect(
                format="Make a circle with both arms (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“(Type of elemental), bow to my will!” (sentence, loud)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes=dedent("""\
            This spell bends the mind and will of an elemental, forcing
            it to do the caster’s bidding. An elemental under the effects
            of this spell becomes a slave to the caster, doing anything
            he compels it to.
            
            When the spell is cast, the caster generates a command:
            elemental skill total and compares it to the willpower/mettle
            total generated by the elemental. If the caster’s total is higher,
            the elemental is his to command for the duration of the spell.
            The caster will be aware that this spell is about to end just
            before the duration expires, giving him time to recast the
            spell if he wishes.
            
            If the elemental makes a higher total than the caster of the
            spell, the elemental may have a bad reaction to the caster, or
            it may flee the area, depending on its type, relative power,
            and temperament. Fire and water elemental will be more
            likely to attack, being more mercurial and hostile, while air
            and earth elementals will be more prone to flight.
        """),
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="changes based on result points", base_difficulty=0, count=1
        ),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 hour ", base_difficulty=-18, count=1),
        name="Control Local Weather",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Air, inanimate forces, water", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="19", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Sphere with radius of 11 meters", base_difficulty=55, count=1
            ),
            "Components": Aspect(
                format="A rainmaker, a statuette or tube made of wood and designed to sound like rain when shaken (common, destroyed)",
                base_difficulty=-6,
                count=1,
            ),
            "Concentration": Aspect(
                format="10 minutes with willpower/mettle difficulty of 11",
                base_difficulty=-5,
                count=1,
            ),
            "Gestures": Aspect(
                format="Broad sweeping hand motions toward the sky (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Powers of nature, make the weather my slave.” (litany; willpower/mettle diffiuclty of 15)",
                base_difficulty=-4,
                count=1,
            ),
        },
        notes=dedent("""\
            This spell gives the caster the ability to control the weather
            to a limited extent. To cast the spell, the mage concentrates
            for 10 minutes on what type of weather he wants, and then
            chants the incantation continuously for the remainder of
            an hour.
            
            The spell manipulates  the temperature, pressure, and
            humidity within 11 meters of the caster. How successful
            he is in making the change depends on the result points of
            the spell, as detailed below. When the duration expires, the
            weather gradually returns to its prespell conditions.
            
            The gamemaster decides on the local weather conditions
            using the charts herein. Each level of change from the cur -
            rent conditions requires one result point. Thus, if the day is
            fair with warm temperatures and a light breeze, to make it
            cold and foggy with a strong wind requires four result points.
            (A skill total equalling the difficulty may make one level of
            change in aspect of the weather.)
            
            The caster can also change the radius of the effect at a cost
            of three result points for each additional meter.
            
            As this is a magical change, the weather may not behave
            as it would under normal circumstances.
            It must always be remembered that changing the weather
            in one place may also change it in some way somewhere
            else. This can prompt revenge attacks from other mages
            or angry residents, so users of this spell must exercise the
            utmost care.
            
            ..  sidebar::             Control Local Weather Effects

                Round all fractions up. Modifiers are cumulative.
                
                Precipitation Levels
                
                - None (fair weather)
                - Fog (all sight-based actions have a difficulty modifier equal to the result points, with a minimum of +1)
                - Rain (or snow\\*)
                - Freezing rain\\* (all physical actions have a difficulty modifier equal to one-quarter of the result points, with a minimum of +1)
                - Sleet\\* (all physical actions have a difficulty modifier equal to one-half of the result points, with a minimum of +1)
                - Small hail\\*\\* (damage per round equals one-quarter of the result points, with a minimum of 1 point)
                - Large hail\\*\\* (damage per round equals one-half of the result points, with a minimum of 1 point)
                
                \\* Temperature must also be freezing.
                
                \\*\\* Hail can be in combination with rain/snow or no Precipitation, at the caster’s choice.
                
                Temperature Levels
                
                - Freezing (damage per round equals the result points, with a minimum of 1 point)
                - Cold
                - Warm
                - Hot (all physical actions have a difficulty modifier equal to one-quarter of the result points, with a minimum of +1)
                - Very hot (damage per round equals one-half of the result points, with a minimum of 1 point)
                
                Wind Levels
                
                - None
                - Light breeze
                - Moderate winds
                - Strong winds (all physical actions have a difficulty modifier equal to one-quarter of the result points, with a minimum of +1)
                - Gale (all physical actions have a difficulty modifier equal to one-half of the result points, with a minimum of +1)
                - Storm (all physical actions have a difficulty modifier equal to the result points, with a minimum of +1)
                - Hurricane/tornado (all physical actions have a difficulty modifier equal to 1.25 times the result points, with a minimum of +1; the gamemaster may also decide that small items are whipped about, causing injury)
                
                The caster can cause any combination of these changes,
                as long as the total point cost does not exceed 2 times the
                result points of the spell casting.
                
                - Expand the area affected by 1 meter: 5 points
                - Change the temperature: Look up the desired change in degrees Celsius under the Measures column of the “Spell Measures” table; the equivalent value is the number of points this changes costs
                - Change the pressure by 0.01 bars: 1 point
                - Change humidity by 1 degree C
                
                With a minimal success, the caster may only raise or lower
                the temperature within 2 degrees Celsius. A slight breeze
                could be created, and perhaps some wispy, clouds. Average
                success allows the caster to raise or lower the temperature
                by 5 degrees, conjure or dispel a moderate amount of cloud
                cover, and a stiff breeze of less than 10 kph could also be cre-
                ated or canceled. Good success on the casting roll will allow
                the mage to cause or cancel light rain or snow, change the
                temperature by up to 10 degrees, and change the wind speed
                by up to 20 kph. Truly powerful weather conditions can be
                created or stopped with a superior success. the temperature
                can be raised or lowered by 20 degrees, and wind speed can
                be modified by up to 40 kph. A thunderstorm or snowstorm
                can be conjured or canceled. Spectacular success allows the
                temperature to be raised or lowered by 30 degrees, wind
                changes of up to 80 kph, and the ability to create or cancel
                powerful storms of rain or snow.
                
        """),
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="100 liters or 0.1 cubic meters", base_difficulty=10, count=1
        ),
        duration=Aspect(format="10 minutes ", base_difficulty=14, count=1),
        range=Aspect(format="3.5 meters ", base_difficulty=3, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=3, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Create Element (Template)",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="any one element: air, earth, fire, or water",
                base_difficulty=0,
                count=1,
            ),
            "Difficulty": Aspect(format="11", base_difficulty=0, count=1),
            "Gestures": Aspect(
                format="Cup hands, whisper into them, then mime throwing toward target spot (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Elemental Powers, create (name of element)!” (sentence, loud)",
                base_difficulty=-3,
                count=1,
            ),
        },
        notes=dedent("""\
            This is one of the first spells learned by many elemental
            mages. By casting the spell, the mage conjures a small amount
            of the element in its raw form. Water appears as a puddle if
            there is no container to hold it; fire burns away merrily without
            fuel; air disperses into the space around it; and earth appears
            in a pile on the ground. None of these conjured elements can
            be used as a weapon by creating them on or inside a person;
            the effect of the spell makes the element only in a clear area
            unoccupied by another person or object.
            
            As this is magically crafted material, it doesn’t have all the
            physical characteristics as natural elements. For example,
            created water does not stay around long enough to be fully
            digested by the body, but it can be used for cleansing. The
            fire only can be used to shed illumination. Air might aid in
            respiration. Earth could be used to design a small enclosure.
            The specific game benefits of these are based on the result
            points and determined by the gamemaster.
        """),
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="15 attribute dice, arranged as the caster likes; Body Points/Wounds and movement based on result points",
            base_difficulty=68,
            count=1,
        ),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="10 minutes ", base_difficulty=-14, count=1),
        name="Create Elemental (Template)",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="any one element: air, earth, fire, or water",
                base_difficulty=0,
                count=1,
            ),
            "Difficulty": Aspect(format="34", base_difficulty=0, count=1),
            "Components": Aspect(
                format="1 carat gemstone, see below for type (very rare, destroyed)",
                base_difficulty=-10,
                count=1,
            ),
            "Concentration": Aspect(
                format="10 minutes with willpower/mettle difficulty of 11",
                base_difficulty=-5,
                count=1,
            ),
            "Focused": Aspect(
                format="On created elemental", base_difficulty=17, count=1
            ),
            "Gestures": Aspect(
                format="Circular hand motions with gemstone com- ponent (fairly simple)",
                base_difficulty=-2,
            ),
            "Incantations": Aspect(
                format="Long speech explaining exact details of the type of elemental desired (litany; persuasion roll with difficulty of 15)",
                base_difficulty=-4,
            ),
        },
        notes=dedent("""\
            In many elemental mage circles, the ability to cast this
            spell successfully is what differentiates the true masters of
            the art from the pretenders. Performing the spell successfully
            creates a powerful servant composed of the elemental type
            specified by the spell. The caster dictates the attributes of the
            final form that the elemental takes as part of the spell. Some
            samples are given below of the different type of elementals
            that can be created.
            
            The type of gemstone needed for the spell varies with what
            type of elemental the caster is creating: Air needs a diamond,
            earth requires an emerald, fire specifies a ruby, and water
            uses a blue sapphire.
            
            The elemental created is not necessarily under the control
            of the caster. A smart mage will be prepared to cast the con-
            trol elemental spell immediately. Alternately, some casters
            who have an intimate knowledge of elementals may try to
            use gifts or promises of future favors to bribe the elemental
            into serving them.
            
            The 15 attribute dice may be allocated as the caster sees
            fit, and with the gamemaster’s permission, she may use some
            of the dice to buy Special Abilities to reflect the natural abili-
            ties of the elemental. The elemental will have a number of
            Body Points equal to 10 plus the points by which the spell
            beat the difficulty; Wound levels equal to the points above
            the difficulty, divided by two, rounded up, minimum of one
            Wound level. Movement equals the result points in meters
            per round, with a minimum of one meter per round.
            
            **Sample Elementals**
            
            Here are some sample elementals that could be
            created with this spell. Special Abilities are given for
            point cost reference. The attribute names are from D6
            Adventure; gamemasters and players using other genres
            should convert the names.
            
            **Air Elemental**: Reflexes 2D, Coordination 2D,
            Physique 2D, Knowledge 1D, Perception 1D, Charisma
            1D. Move: 1+. Strength Damage: 1D. Body Points: 10+/
            Wound levels: 1+. Natural Abilities: Flight (R1, 6 points),
            flying rate equals 2 times Move.
            
            **Earth Elemental**: Reflexes 2D, Coordination 1D,
            Physique 6D, Knowledge 1D, Perception 1D, Charisma
            1D. Move: 1+.  Strength Damage: 3D. Body Points: 10+/
            Wound levels: 1+. Natural Abilities: Natural Armor (R1,
            3 points) +1D to damage resistance totals.
            
            **Fire Elemental**: Reflexes 4D, Coordination 3D,
            Physique 3D, Knowledge 1D, Perception 1D, Charisma
            1D. Move: 1+.  Strength Damage: 2D. Body Points: 10+/
            Wound levels: 1+ . Natural Abilities:  Natural Ranged
            Weapon: Flame (R1, 3 points), 3D damage.
            
            **Water Elemental**: Reflexes 3D, Coordination 3D,
            Physique 4D, Knowledge 1D, Perception 1D, Charisma
            1D. Move: 1+.  Strength Damage: 2D. Body Points: 10+/
            Wound levels: 1+. Natural Abilities: Natural Armor (R1,
            3 points) +1D to damage resistance totals.
        """),
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="3D physical damage, ignores all armor", base_difficulty=18, count=1
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="5 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="2.5 seconds ", base_difficulty=-2, count=1),
        name="Desiccate",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Water", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="16", base_difficulty=0, count=1),
            "Component": Aspect(
                format="Small strip of dried rawhide (very common, destroyed)",
                base_difficulty=-4,
                count=1,
            ),
            "Focused": Aspect(format="Target of the spell", base_difficulty=5, count=1),
            "Gestures": Aspect(
                format="Point at target (simple)", base_difficulty=-1, count=1
            ),
            "Incantations": Aspect(
                format="“Drought shall be your death!” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="Ineffective against those without fluid in their bodies",
                base_difficulty=-1,
                count=1,
            )
        ],
        notes=dedent("""\
            This is a particularly nasty spell, used by sorcerers with
            little regard for mercy. The spell is targeted with a marksman-
            ship/firearms or apportation roll. If the attack is successful,
            the target takes 3D of damage each round for the next 12
            rounds. This damage is caused by the rapid desiccation, or
            removal of fluid, from all of the target’s soft tissues. This is
            an extremely painful and unpleasant process to say the least,
            and if the spell does enough damage to kill the target, all that
            is left is a dried, mummy-like husk.
            
            Armor is ineffective against this damage, since the dam -
            age comes from inside the target’s body. Any creature that
            does not have fluid inside of it, like a golem or other creature
            made of stone, is unaffected.
        """),
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="6D physical damage, ignores all armor", base_difficulty=36, count=1
        ),
        duration=Aspect(format="2 rounds ", base_difficulty=5, count=1),
        range=Aspect(format="2.5 meters ", base_difficulty=2, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=2, count=1),
        casting_time=Aspect(format="3.5 seconds ", base_difficulty=-3, count=1),
        name="Drown",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Water", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="21", base_difficulty=0, count=1),
            "Components": Aspect(
                format="A mouthful of water (ordinary, destroyed)",
                base_difficulty=-2,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=5, count=1),
            "Gestures": Aspect(
                format="Spit mouthful of water at target (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“A sailor’s death shall take you!” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes=dedent("""\
            To cast this spell, the mage fills his mouth with water,
            spits it at the target, and speaks the incantation. The spell
            is aimed with a throwing (not apportation) roll. If it hits suc-
            cessfully, the target’s lungs fill with water and she begins to
            drown, taking 6D of damage for the next two rounds. Armor
            does not help absorb this damage, but the target can make
            a stamina roll with a difficulty equal to the caster’s spell skill
            total to expel the water from his lungs after the first round.
            If successful, he takes no damage from the second round of
            the spell effect.
        """),
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="2.5 months in the past", base_difficulty=34, count=1),
        duration=Aspect(format="5 minutes ", base_difficulty=13, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="40 minutes ", base_difficulty=-17, count=1),
        name="Earth Muse",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="earth, time", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="19", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Divination sphere with radius of 25 meters",
                base_difficulty=21,
                count=1,
            ),
            "Components": Aspect(
                format="A miniature sundial (uncommon); dirt or stone (ordinary)",
                base_difficulty=-5,
                count=1,
            ),
            "Concentration": Aspect(
                format="1 round with a willpower/mettle difficulty of 8",
                base_difficulty=-2,
                count=1,
            ),
            "Gestures": Aspect(
                format="As the incantation is spoken, place hands on the stone or ground in the center of the area of effect; slowly, draw in the arms and place the palms on closed eyes. After pausing for several seconds, throw hands out wide. (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="Utter the following after meditation: “Oh mighty spirits who have seen all, heed my plea and answer my call. The time grows nigh to share your thoughts; come to me now and show what time has wrought!” (litany; persuasion roll with difficulty of 15)",
                base_difficulty=-4,
                count=1,
            ),
        },
        notes=dedent("""\
            Although there are many who may choose to think otherwise, there are beings that dwell just beyond the realm of
            human perception. These spiritual elemental forces of nature
            often live far longer than the mere mortals who sometimes
            rudely intrude upon their realm. Theirs is the gift of knowl-
            edge, for these enigmatic souls have experienced much dur-
            ing their existence. The power of the earth muse spell allows
            the mage to communicate with elemental forces that dwell
            within the ground, untamed stone or stone structures. Such
            creatures are able to speak of things that have occurred in
            the spell’s area of effect. Persistent characters who repeat -
            edly question the earthen sages about items or events that
            are out of their range of caring (events that are more than
            2.5 months old) or beyond the area of effect cause the spell
            to abruptly end. The caster has worn out her welcome with
            the beings that she’s trying to gather information from. If
            this should happen, no spirits will answer the caster’s call
            for 24 hours should she attempts to recast earth muse  in
            the same area. A Critical Failure along with a failed skill roll
            when attempting to cast earth muse temporally blights the
            intended area of effect and no earth muse spells will function
            there for 24 hours.
        """),
        skill="Divination",
    ),
    Spell(
        effect=Aspect(format="5D physical damage", base_difficulty=15, count=1),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="1 kilometer ", base_difficulty=15, count=1),
        speed=Aspect(format="10 meters per second ", base_difficulty=5, count=1),
        casting_time=Aspect(format="1 hour ", base_difficulty=-18, count=1),
        name="Earthquake",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Earth", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="32", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Circle with radius of 15 meters", base_difficulty=30, count=1
            ),
            "Components": Aspect(
                format="A diamond of at least 1 carat (very rare, destroyed)",
                base_difficulty=-10,
                count=1,
            ),
            "Concentration": Aspect(
                format="10 minutes with willpower/mettle difficulty of 11",
                base_difficulty=-5,
                count=1,
            ),
            "Gestures": Aspect(
                format="A series of foot and hand gestures (complex; acrobatics roll with difficulty of 11)",
                base_difficulty=-3,
                count=1,
            ),
            "Incantations": Aspect(
                format="Complex litany of elemental names and formulas (litany; languages/speaking roll with difficulty of 15)",
                base_difficulty=-4,
                count=1,
            ),
            "Other Alterants": Aspect(
                format="+10D additional damage done to stationary targets",
                base_difficulty=30,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(format="Cannot affect anything flying", base_difficulty=-1, count=1)
        ],
        notes=dedent("""\
            Casting this spell causes the ground within the area of
            effect to be shaken by violent tremors. Anything or anyone
            touching the ground will take 5D of damage for each full
            round they spend inside the area of the quake. Stationary
            targets — such as trees and buildings — take an additional
            10D of damage per round. Any movement through the area
            of the quake decreases by a number of meters per round equal
            to the result points (minimum adjustment of zero), as the
            shaking throws about objects and heaves the ground.
            
            Because the area of the spell is so large, no targeting roll
            is necessary. The caster may simply center the quake on any
            point within the range.
            
            After the spell is cast, it takes the quake some time to begin.
            Use the “Spell Measures” chart in the rulebook to find the
            value of the range from the caster to the center of the quake,
            subtract the speed value of 5, and look up this number on the
            chart. Convert the related measure to minutes or seconds to
            see how long it takes the quake to begin.
        """),
        skill="Alteration",
    ),
    Spell(
        effect=Aspect(
            format="+2D physical damage; Armor Value of 2D", base_difficulty=15, count=1
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="Touch ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1.5 seconds ", base_difficulty=-1, count=1),
        name="Elemental Body (Template)",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="any one element: air, earth, fire, or water",
                base_difficulty=0,
                count=1,
            ),
            "Difficulty": Aspect(format="15", base_difficulty=0, count=1),
            "Focused": Aspect(format="On target", base_difficulty=4, count=1),
            "Gestures": Aspect(
                format="Touch subject (simple)", base_difficulty=-1, count=1
            ),
            "Incantations": Aspect(
                format="“(Name of element), protect me and harm my foe!” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
            "Other Alterant": Aspect(
                format="Effect doubled against one opposite element (specified at time of casting)",
                base_difficulty=6,
                count=1,
            ),
        },
        notes=dedent("""\
            When cast, this spell covers the body of the target (and
            anything she wears or holds) in a sheath of the element.
            This sheath provides armor and adds damage to any attacks
            made with appendages or hand-held weapons. The armor
            and damage effects are doubled if they are used against
            the opposite element. For example, a mage sheathed in fire
            would do double damage against water-based creatures, and
            his armor from the spell would protect him double from
            water-based attacks.
        """),
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="4D physical damage", base_difficulty=12, count=1),
        duration=Aspect(format="1 second ", base_difficulty=0, count=1),
        range=Aspect(format="40 meters ", base_difficulty=8, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=8, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        name="Elemental Burst (Template)",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="any one element: air, earth, fire, or water",
                base_difficulty=0,
                count=1,
            ),
            "Difficulty": Aspect(format="17", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Sphere with radius of 3 meters", base_difficulty=15, count=1
            ),
            "Components": Aspect(
                format="A tiny amount of the element used in the burst (ordinary)",
                base_difficulty=-1,
                count=1,
            ),
            "Gestures": Aspect(
                format="Move both hands inward, and then throw them out like an explosion (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“(Name of element), destroy my enemies with your power!” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes=dedent("""\
            A favorite of many combat mages, this spell conjures a
            powerful burst of the element, damaging all the targets within
            its area. The spell does not discern between friend and foe,
            so the caster must use care in aiming the blast.
            
            The form of the shot depends on the element used: Air is
            a concussive inward blast; earth, a hail of rocks; fire, a huge
            burst of flame; and water, a powerful drowning wave.
            
            The caster generates a throwing or apportation total against
            the combat difficulty of the main target. The total receives a
            +3, because the spell covers a large area, making it easier to
            hit the target. Those more than a meter away from the center
            with defense totals greater than the targeting roll (without
            the bonus) dodge out of the way. For everyone else, reduce the
            damgae done by 1 for each meter away from the center.
        """),
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="+3D physical damage", base_difficulty=14, count=1),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="3.5 seconds ", base_difficulty=-3, count=1),
        name="Elemental Edge (Template)",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="any one element: air, earth, fire, or water",
                base_difficulty=0,
                count=1,
            ),
            "Difficulty": Aspect(format="12", base_difficulty=0, count=1),
            "Focused": Aspect(format="On a weapon", base_difficulty=4, count=1),
        },
        notes=dedent("""\
            This simple spell covers the dangerous part of a weapon
            with a sheath of energy that causes extra damage. The type
            of energy varies depending on the elemental type of the
            spell: Air covers the weapon in electricity, earth is acid, the
            fire sheath is flames, and water is brutally cold ice. For the
            duration of the spell, the weapon inflicts an additional 3D of
            damage every time it successfully strikes a target.
        """),
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="up to 1 month into the future", base_difficulty=32, count=1
        ),
        duration=Aspect(format="5 minutes ", base_difficulty=13, count=1),
        range=Aspect(format="1 meter ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        name="Elemental Scrying",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Time, earth, air, fire, water", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="13", base_difficulty=0, count=1),
            "Components": Aspect(
                format="A small piece of the target of the spell, such as nail clippings, a few hairs, or a drop of blood (common); small amount of each of the four elements (very common, destroyed)",
                base_difficulty=-7,
                count=1,
            ),
            "Gestures": Aspect(
                format="Wave hands over components (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Elements of the universe, show me this person’s future.”(sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes=dedent("""\
            According to some philosophies, the entire universe is
            composed of the four elements. By drawing upon the con -
            nection of these elements to all things, the caster can pull
            back the veil of time and peer into the future. Because the
            future is not set, the visions that the caster sees of the future
            may or may not come true, and divination is far from an exact
            science. The act of seeing what will happen in the target’s
            future can often change the future as well, so anything seen
            with this spell should be taken with a grain of salt in the best
            of circumstances.
            
            To cast the spell, the mage spends one minute murmuring
            the incnatation over the elements and the bit of the target.
            At the end of that time, the caster receives a burst of insight,
            highlighting about five minutes’ worth of events for the next
            month of the target’s life. The result points of the casting roll
            determine how much information the caster can get about
            the target’s future.
            
            Zero points reveals small details and perhaps a few flashes of
            important facts. One to four points allows the most important
            or dangerous event to be revealed, without a great amount of
            detail. Five to eight points gives more information about the
            key event, and a much closer timeframe, along with minor
            details. Nine to 12 points allows even more details and vague
            information about the remainder of the day surrounding the
            key as well. More than 12 points reveals up to five minutes
            of the most important event like a movie, plus gives a decent
            recounting of the remainder of the month, even if that would
            make duration longer than five minutes.
            
            **Example**: Morgan the mage wants to see into her com -
            panion Bator’s future. She successfully casts the spell. If
            she achieved a minimal success, she would know that Bator
            will be in grave danger during the next month. On a solid
            success, she would know that the fighter was going to be
            ambushed some time in the afternoon of the following day.
            Good success would tell Morgan that Bator was going to be
            ambushed by a large group; sometime in the early afternoon.
            Superior success would tell the mage that the rest of Bator’s
            month will be uneventful, and that the ambush was going
            to be from a group of 15 goblins at 2:00 p.m. Finally, if the
            mage manages to achieve Spectacular success, she will see the
            ambush as if it were happening in front of her, with a good
            amount of exacting detail.
            
            Note that in the example above the mage was never told
            exactly where the ambush would happen, or how to avoid it.
            Even if Bator stays right where he is for a month, the ambush
            could still happen, but the details would change slightly from
            the vision seen by the scrying mage. The gamemaster should
            never let a good roll on a divination spell disrupt the game.
            """),
        skill="Divination",
    ),
    Spell(
        effect=Aspect(format="4D physical damage", base_difficulty=12, count=1),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="3 meters ", base_difficulty=3, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=3, count=1),
        casting_time=Aspect(format="2.5 seconds ", base_difficulty=-2, count=1),
        name="Flame Jet",
        other_aspects={
            "Arcane Knowledge": Aspect(format="Fire", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="17", base_difficulty=0, count=1),
            "Components": Aspect(
                format="A small open flame (ordinary, destroyed)",
                base_difficulty=-2,
                count=1,
            ),
            "Gestures": Aspect(
                format="Point finger (simple)", base_difficulty=-1, count=1
            ),
            "Focused": Aspect(format="On caster’s finger", base_difficulty=4, count=1),
            "Incantations": Aspect(
                format="“Burn!” (phrase)", base_difficulty=-1, count=1
            ),
            "Variable Duration": Aspect(
                format="On/off switch", base_difficulty=8, count=1
            ),
        },
        notes="This spell causes a roaring line of fire to erupt from the\ncaster’s fingertip. The jet is only a few centimeters across,\nbut it extends out to about three meters from the caster.\nThe caster can freely turn the effect on and off during the\none minute duration, to avoid accidentally burning things\nhe does not want to. Marksmanship/firearms or apportation is\nused to aim the jet if it is being used as an attack. The caster\ncan make one attack with it per round.",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(format="6D physical damage", base_difficulty=18, count=1),
        duration=Aspect(format="1 second ", base_difficulty=0, count=1),
        range=Aspect(format="100 meters ", base_difficulty=10, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=10, count=1),
        casting_time=Aspect(format="2.5 seconds ", base_difficulty=-2, count=1),
        name="Lightning Bolt",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Inanimate Forces", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="15", base_difficulty=0, count=1),
            "Components": Aspect(
                format="A small steel or iron rod (very common); a piece of wool (very common)",
                base_difficulty=-4,
                count=1,
            ),
            "Gestures": Aspect(
                format="Rub the wool on the steel rod, and then mimic flinging a bolt (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantation": Aspect(
                format="“Power of lightning, smite my foe!” (sentence, loud)",
                base_difficulty=-3,
                count=1,
            ),
            "Other Alterant": Aspect(
                format="Gain a bonus against targets wearing metal",
                base_difficulty=3,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="Targeting difficulty increased when used near large amounts of metal",
                base_difficulty=-1,
                count=1,
            )
        ],
        notes="This spell generates a powerful stroke of lightning. The\ncaster must aim the bolt using throwing or apportation. If\nthe target of spell is wearing large amounts of metal, (a suit\nof chain or plate armor, for example), she is much easier to\nhit, giving a modifier of +3 to the targeting total. If a large\npiece of metal is within a meter of the caster or the target,\na modifier of +3 should be added to the difficulty to hit the\ntarget, because the metal will tend to pull the lightning away\nfrom its intended path.\n\n",
        skill="Conjuration",
    ),
    Spell(
        effect=Aspect(
            format="5D inhaling damage, ignores all armor; Hindrance: Blindness (R12), +4 to difficulties of all sight-dependent actions",
            base_difficulty=66,
            count=1,
        ),
        duration=Aspect(format="3 rounds ", base_difficulty=6, count=1),
        range=Aspect(format="40 meters ", base_difficulty=8, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=8, count=1),
        casting_time=Aspect(format="2 rounds ", base_difficulty=-5, count=1),
        name="Miasma",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Air, darkness", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="54", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Sphere with radius of 3 meters", base_difficulty=15, count=1
            ),
            "Focused": Aspect(format="On targets", base_difficulty=14, count=1),
            "Components": Aspect(
                format="Rotten egg (common)", base_difficulty=-3, count=1
            ),
            "Gestures": Aspect(format="Point (simple)", base_difficulty=-1, count=1),
        },
        notes="A thick, black pall appears at the targeted location. Each\nround that a character is within the dense cloud, she suffers\n5D damage. The miasma also obscures sight, so all attacks\nare done blind. All damage comes from inhaling.\n\n",
        skill="Conjuration",
    ),
    # This is incomplete in the source PDF.
    # Spell(
    #     effect=Aspect(
    #         format="100 liters or 0.1 cubic meters or 3D+1 damage to an elemental",
    #         base_difficulty=10,
    #         count=1,
    #     ),
    #     duration=Aspect(format="template", base_difficulty=0, count=1),
    #     range=Aspect(format="2.5 meters ", base_difficulty=2, count=1),
    #     speed=Aspect(format="Instantaneous ", base_difficulty=2, count=1),
    #     casting_time=Aspect(format="template", base_difficulty=0, count=1),
    #     name="Shape Element (Template)",
    #     other_aspects={
    #         "Arcane Knowledge": Aspect(
    #             format="any one element: air, earth, fire, or water",
    #             base_difficulty=0,
    #             count=1,
    #         ),
    #         "Difficulty": Aspect(format="11", base_difficulty=0, count=1),
    #     },
    #     notes="",
    #     skill="Apportation",
    # ),
]

if __name__ == "__main__":
    detail(spells)


__test__ = {
    "Acidic Attack": ">>> spells[0].difficulty\n20",
    "Burrow": ">>> spells[1].difficulty\n18",
    "Cone of Wind": ">>> spells[2].difficulty\n11",
    "Control Elemental (Template)": ">>> spells[3].difficulty\n18",
    "Control Local Weather": ">>> spells[4].difficulty\n19",
    "Create Element (Template)": ">>> spells[5].difficulty\n11",
    "Create Elemental (Template)": ">>> spells[6].difficulty\n34",
    "Desiccate": ">>> spells[7].difficulty\n16",
    "Drown": ">>> spells[8].difficulty\n21",
    "Earth Muse": ">>> spells[9].difficulty\n19",
    "Earthquake": ">>> spells[10].difficulty\n32",
    "Elemental Body (Template)": ">>> spells[11].difficulty\n15",
    "Elemental Burst (Template)": ">>> spells[12].difficulty\n17",
    "Elemental Edge (Template)": ">>> spells[13].difficulty\n12",
    "Elemental Scrying": ">>> spells[14].difficulty\n13",
    "Flame Jet": ">>> spells[15].difficulty\n17",
    "Lightning Bolt": ">>> spells[16].difficulty\n15",
    "Miasma": ">>> spells[17].difficulty\n54",
    # This was incomplete in the source document.
    # "Shape Element (Template)": ">>> spells[18].difficulty\n11",
}
