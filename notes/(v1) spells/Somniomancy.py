"""
Somniomancy
-----------

This was significantly edited to correct parsing problems.
Avoid running parse_spells and overwriting it
"""

from textwrap import dedent
from magic1 import Aspect, Spell, detail

spells = [
    Spell(
        name="Cleansing Sleep",
        effect=Aspect(format="medicine/healing of 9D", base_difficulty=27, count=1),
        duration=Aspect(format="10 hours ", base_difficulty=23, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="25 minutes ", base_difficulty=-16, count=1),
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Death, folk", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="10", base_difficulty=0, count=1),
            "Components": Aspect(
                format="Large amount of water (ordinary)", base_difficulty=-1, count=1
            ),
            "Gestures": Aspect(
                format="Washing with and drinking water (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="Effect may be used once per hour; spell is broken if caster is awakened during the duration",
                base_difficulty=-11,
                count=1,
            )
        ],
        notes=dedent("""\
            The mage casts this spell, spending 25 minutes washing
            herself thoroughly with water and drinking plenty of fluids,
            then she goes to sleep. While she sleeps, her body rids itself
            of toxins and diseases. This spell courses through her veins
            and organs, destroying harmful bacteria, viruses, and natural
            and synthetic toxins, rendering her healthy and fit once again.
            Each hour, the caster can attempt to eliminate a single poison
            or illness within her body by making a medicine/healing roll
            as if she had 9D in the skill. The gamemaster determines the
            difficulty to eliminate a specific poison or disease; 15 to 20
            is generally a good range.
            
            The caster may apply her result point bonus to the first
            *medicine/healing* roll she makes with this spell.
            """),
        skill="Conjuration",
    ),
    Spell(
        name="Concentration Lapse",
        effect=Aspect(
            format="difficult to attack target is at -5", base_difficulty=5, count=1
        ),
        duration=Aspect(format="1 round ", base_difficulty=4, count=1),
        range=Aspect(format="5 meters ", base_difficulty=4, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=4, count=1),
        casting_time=Aspect(format="1 second ", base_difficulty=0, count=1),
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="8", base_difficulty=0, count=1),
            "Gestures": Aspect(
                format="Waves hand in a hypnotic pattern (sim - ple)",
                base_difficulty=-1,
                count=1,
            ),
        },
        notes=dedent("""\
            The mage waves her hand in a sinuous motion or wiggles
            her fingers slowly.  The target must make a willpower/mettle
            roll with a difficulty of 10. If he fails, his eyelids droop briefly,
            and he experiences a momentary lapse of concentration,
            of the sort he might have if he were very tired. This lapse
            makes him fumble his defenses: He is too slow on the parry
            or notices the incoming punch half a second too late; the
            difficulty to hit him is decreased by  until the caster’s turn
            in the next round.
            
            The caster may apply her result point bonus to the difficulty
            of the target’s willpower/mettle roll to avoid the effect.
            """),
        skill="Alteraion",
    ),
    Spell(
        name="Detect Slumber",
        effect=Aspect(
            format="value to determine state of slumber", base_difficulty=5, count=1
        ),
        duration=Aspect(format="1 round ", base_difficulty=4, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 second ", base_difficulty=0, count=1),
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="12", base_difficulty=0, count=1),
            "Area of Effect": Aspect(
                format="Divination sphere sphere with radius of 10 meters",
                base_difficulty=15,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="Only works on sleeping creatures", base_difficulty=-1, count=1
            )
        ],
        notes=dedent("""\
            The caster’s vision takes on an added quality, providing her
            with additional information about certain creatures within
            the area of effect. Simply by looking at a creature within
            the area of effect, she instantly knows whether or not it is
            asleep. If it is not asleep, the caster has no additional means
            of discerning if it is resting, about to fall asleep, feigning
            sleep, dead, or in any other state; this spell simply reveals
            that the creature is sleeping or that it is not. Generally, the
            caster can determine the sleeping condition of all the crea -
            tures within the area of effect unless they are hidden from
            view or there are a great many of them (and thus some are
            concealing others).
        """),
        skill="Divination",
    ),
    Spell(
        name="Dream Travel",
        effect=Aspect(format="moves up to 150 kilograms", base_difficulty=11, count=1),
        duration=Aspect(format="40 seconds ", base_difficulty=8, count=1),
        range=Aspect(format="1 kilometer ", base_difficulty=15, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=15, count=1),
        casting_time=Aspect(format="25 seconds ", base_difficulty=-7, count=1),
        other_aspects={
            "Arcane Knowledge": Aspect(format="Dreams", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="19", base_difficulty=0, count=1),
            "Concentration": Aspect(
                format="25 seconds with willpower/mettle difficulty of 9",
                base_difficulty=-3,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(format="Pass only between dreamers", base_difficulty=-2, count=1)
        ],
        notes=dedent("""\
            The caster uses this spell to transport herself great distances
            via the dreams of other creatures. She moves from dream to
            dream in the time it takes to blink, seeing strange landscapes
            and briefly passing by the hopes and fears of myriad creatures
            before arriving at her destination.
            
            When she casts this spell, the caster targets a sleeping
            creature within one kilometer; she must see or otherwise
            be aware of the sleeper’s location (perhaps by sleep sense, for
            instance) and it must be the size of a cat or larger. Over the
            course of 30 seconds, her physical form fades into translucence
            and disappears entirely as she enters the sleeping creature’s
            dreams. During these 30 seconds, the caster  cannot influence
            events around her, nor can she move from her position; her
            mind and body are becoming part of the creature’s dreams.
            
            Though she enters the sleeping creature’s dreams, the
            dreamer does not detect her and she cannot deliver mes -
            sages or otherwise influence his dreams, as she could with
            step into sleep; she is merely along for the ride, using the
            creature’s sleeping consciousness as a vehicle for her unique
            brand of magic.
            
            Once at the new host, the caster’s physical form slowly
            manifests, fading into translucence and then becoming solid
            in the latest dreamer’s presence. As she was when she first
            entered the dreams, she is not physically present in the area
            until her form solidifies over the course of 30 seconds.
            
            Note that the caster has no knowledge of the surroundings
            of her destination dreamer, and she could appear in the midst
            of enemies or in an inhospitable environment — though
            as people do not usually sleep in these sorts of conditions,
            the odds are slim. The caster usually ends up in a bedroom
            somewhere and tiptoes out.
            
            Note that though the process of the caster’s physical self
            discorporating takes time, the dream travel itself is virtually
            instantaneous.
        """),
        skill="Apportation",
    ),
    Spell(
        name="Dream Visions",
        effect=Aspect(format="search of 4D", base_difficulty=12, count=1),
        duration=Aspect(format="10 minutes ", base_difficulty=14, count=1),
        range=Aspect(format="2.5 kilometers ", base_difficulty=17, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=17, count=1),
        casting_time=Aspect(format="5 hours ", base_difficulty=-22, count=1),
        other_aspects={
            "Arcane Knowledge": Aspect(format="Dreams", base_difficulty=0, count=1),
            "Difficulty": Aspect(
                format="22", base_difficulty=0, count=1
            ),  # Should be 20
            "Area of Effect": Aspect(
                format="Divination sphere with radius of 5 meters",
                base_difficulty=12,
                count=1,
            ),
            "Components": Aspect(
                format="Photographs or paintings of exotic locales (uncommon)",
                base_difficulty=-4,
                count=1,
            ),
            "Concentration": Aspect(
                format="1 hour with willpower/mettle difficulty of 12",
                base_difficulty=-6,
                count=1,
            ),
        },
        notes=dedent("""\
            This spell allows the caster to view distant places in her
            dreams, though those places are not exactly as they appear
            in the real world.
            
            The caster spends one hour in preparation, gazing at the
            photographs or paintings and envisioning the place she
            would like to see (which does not have to be the place of
            the paintings). Then, she goes to sleep. Four hours into her
            sleep (which are part of the casting time), her dreams take
            on more meaningful forms. She can observe any one area
            within 2.5 kilometers as if she were there herself, using a
            search skill of 4D. She can view an area with which she is
            familiar or she can specify a direction and distance, such
            as “southwest, 1.22 kilometers,” and view the area at that
            distance. If the specified location is within the ground, a
            wall, or other obstruction, she sees nothing but darkness.
            Her point of view can appear close to the ground, viewing
            it as she would if she were standing there, or it can appear
            floating in the air, at ground level, and so on.
            
            The caster does not see the areas exactly as normal, for
            she is within the dreamscape. Areas and people within the
            dreamscape appear as they do in the real world, but the
            lighting is indistinct and gray mists hover at the edges of
            vision. Forms are muted and blurred. Most importantly, the
            subconscious images that people associate with individuals,
            places, and things walk the dreamscape. Though these images
            may have no physical existence in the real world, they are the
            things people dream about when they visit these areas and
            creatures in their sleep. For example, a graveyard dreamscape
            may be haunted by ghosts and the cries of the dead, because
            these fears lurk in humanity’s subconscious and when people
            dream of graveyards, these images often appear. A sports star
            in the dreamscape may have trophies, women, and dollar bills
            floating around him, as these are the ideas that other people
            associate with such a celebrity.
            
            The ancillary images in the dreamscape can serve both
            to enhance and obscure the caster’s understanding and are
            tools for the gamemaster to use.
        """),
        skill="Divination",
    ),
    Spell(
        name="Dreams in Hand",
        effect=Aspect(
            format="creates 1 kilogram of inanimate material",
            base_difficulty=0,
            count=1,
        ),
        duration=Aspect(format="40 minutes ", base_difficulty=17, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 hour ", base_difficulty=-18, count=1),
        other_aspects={
            "Arcane Knowledge": Aspect(format="Dreams", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="10", base_difficulty=0, count=1),
            "Component": Aspect(
                format="A few grains of sand (ordinary)", base_difficulty=-1, count=1
            ),
            "Concentration": Aspect(
                format="1 hour with willpower/mettle difficulty of 12",
                base_difficulty=-6,
                count=1,
            ),
            "Focused": Aspect(format="On sand", base_difficulty=3, count=1),
            "Other Alterant": Aspect(
                format="Item can be of any complexity or value, but the greater the complexity or value, the greater the secondary skill roll required",
                base_difficulty=25,
                count=1,
            ),
        },
        notes=dedent("""\
        This spell allows the caster to enter her dreams, envision
        an item, and return to the waking world with that item in
        her possession.
        
        For one hour, the caster meditates on the spell and the
        item she wishes to create with her dreams. She can imagine
        anything she likes, though complicated or artistic objects
        require skill rolls as determined by the gamemaster. (Failure
        on the secondary skill roll indicates that some obvious flaw
        exists in the item; success has no effect beyond the item’s
        satisfactory creation.)
        
        Aftershe awakes from the meditation, the object is in
        her hand, a physical reality. It remains substantial for 40
        minutes; after this time, it grows translucent before it dis -
        appears entirely.
        
        The caster can use this spell to create items of great intrinsic
        worth, like currency, precious metals, or jewelry, but they
        vanish when the duration expires, which is bound to anger
        shopkeepers.
        
        The caster can add her result point bonus to the spell’s
        duration value and refigure the measure in seconds.
        """),
        skill="Conjuration",
    ),
    Spell(
        name="Dreamtime",
        effect=Aspect(
            format="up to 1 year in the past or future — specified at spell casting; search of 4D",
            base_difficulty=50,
            count=1,
        ),
        duration=Aspect(format="25 minutes ", base_difficulty=16, count=1),
        range=Aspect(format="20 kilometers ", base_difficulty=19, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=19, count=1),
        casting_time=Aspect(format="5 hours ", base_difficulty=-22, count=1),
        other_aspects={
            "Arcane Knowledge": Aspect(format="Dreams", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="43", base_difficulty=0, count=1),
            "Area of Effect": Aspect(
                format="Divination sphere with radius of 5 meters",
                base_difficulty=12,
                count=1,
            ),
            "Components": Aspect(
                format="A 4-hour hourglass (uncommon)", base_difficulty=-4, count=1
            ),
            "Concentration": Aspect(
                format="1 hour with willpower/mettle difficulty of 12",
                base_difficulty=-6,
                count=1,
            ),
            "Other Alterant": Aspect(
                format="May select time period viewed", base_difficulty=2, count=1
            ),
        },
        notes=dedent("""\
            This spell allows the caster to use her dreams to view places
            as they appeared in the past or will appear in the future.
            
            The caster spends one hour in preparation, meditating and
            focusing, at the end of which she turns the hourglass and
            goes to sleep. Four hours later (which are part of the casting
            time), as the sand in the hourglass trickles out, the caster’s
            dreams take on meaning.
            
            In addition to the ability to view a distant location (up to
            20 kilometers away), the caster can also look up to a year
            into the past or the future. She makes the decision as to the
            area and the time when she casts the spell. (For example,
            “The playground at Washington Heights Elementary School,
            January 2, 3:31 p.m.”)
            
            If the caster looks into the past, she sees the area as it
            appeared back then. The dreamscape images, however, are
            those that modern-day people feel for the area. For example,
            if a terrible murder was committed in a certain house last
            week, and the caster observes the house as it was one month
            ago, before the murder, the dreamscape still shows her shad-
            owy images of death and fear, for that is what people in the
            current time associate with the house.
            
            If the caster looks into the future, she sees the area as it is
            most likely to appear. The future is uncertain and many factors
            can change it, but she sees the area as it will most probably
            appear — assuming that no one does anything significant
            to alter it. Like looking into the past, the dreamscape reveals
            images that modern-day people associate with the area. For
            example, the caster may view a coastline as it will appear five
            months from now and see the remains of a terrorist attack
            — broken piers, dead bodies, ravaged beaches. Even though
            five months from now people will associate the coastline with
            horror and violence, currently they see it as a simple beach,
            and the dreamscape images are people in swimsuits, beach
            balls, and the like (and maybe the odd shark, as a nod to the
            neurotic mothers of the world).
        """),
        skill="Divination",
    ),
    Spell(
        name="Groggy",
        effect=Aspect(
            format="-1D to two mental and two physical attributes",
            base_difficulty=24,
            count=1,
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="1.5 seconds ", base_difficulty=-1, count=1),
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(
                format="22", base_difficulty=0, count=1
            ),  # Should be 21
            "Gestures": Aspect(
                format="The caster yawns widely (simple)", base_difficulty=-1, count=1
            ),
        },
        notes=dedent("""\
            The caster yawns hugely and, as all know, yawning is
            contagious. The target follows suit. This spell magnifies the
            target’s feeling of sleepiness, making him momentarily groggy
            and unable to think straight, as if badly in need of rest. His
            reflexes are slowed, his hand-eye coordination decreased,
            and his mind easily distracted. He suffers a -1D penalty on
            two mental and two physical attributes (such as Reflexes,
            Knowledge, Co ordination, and Perception in D6 Adventure )
            for 12 rounds.
        """),
        skill="Alteration",
    ),
    Spell(
        name="Insomnia",
        effect=Aspect(
            format="Achilles’ Heel (R3), insomnia — -1 pip to all mental and physical attributes, increasing by -1 pip for each sleepless night",
            base_difficulty=9,
            count=1,
        ),
        duration=Aspect(format="1 week ", base_difficulty=29, count=1),
        range=Aspect(format="5 meters ", base_difficulty=4, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=4, count=1),
        casting_time=Aspect(format="1 day ", base_difficulty=-25, count=1),
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="11", base_difficulty=0, count=1),
            "Charges": Aspect(format="1 improved charge", base_difficulty=5, count=1),
            "Components": Aspect(
                format="A miniature sheep doll (common); 6 pins silver pins (common, destroyed)",
                base_difficulty=-8,
                count=1,
            ),
            "Focused": Aspect(format="On target", base_difficulty=7, count=1),
            "Gestures": Aspect(
                format="The caster pushes a pin through the sheep doll's head and pushes an additional pin into the doll after every 24 hours (fairly simple)",
                base_difficulty=-2,
                count=1,
            ),
            "Incantations": Aspect(
                format="“Sleep no more.” (phrase)", base_difficulty=-1, count=1
            ),
        },
        notes=dedent("""\
            This spell makes it challenging for the target to sleep. His
            sleeplessness is maddening and dulls his mind and body.
            
            Each night following the end of the casting time, the target
            must make a willpower/mettle roll versus a roll of the caster’s
            willpower/mettle or be stricken with insomnia. He is unable
            to sleep for one full night. In addition to being frustrating,
            the next morning, the victim is mentally drained and physi-
            cally fatigued. He suffers -1 pip to all mental and physical
            attributes. This reduction accumulates for each night the
            character cannot get sleep (by failing to make the roll). Nap-
            ping during the day provides no relief.
            
            No attribute can drop below 1D because of this spell.
            
            The caster can add her result point bonus to the difficulty of
            the willpower/mettle checks needed to shake off the spell.
        """),
        skill="Conjuration",
    ),
    Spell(
        name="Kiss of the Sandman",
        effect=Aspect(
            format="difficulty for target to resist falling asleep",
            base_difficulty=15,
            count=1,
        ),
        duration=Aspect(format="5 minutes ", base_difficulty=13, count=1),
        range=Aspect(format="2.5 meters ", base_difficulty=2, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=2, count=1),
        casting_time=Aspect(format="3.5 seconds ", base_difficulty=-3, count=1),
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="21", base_difficulty=0, count=1),
            "Area of Effect": Aspect(
                format="Cone with height and base radius of 3 meters",
                base_difficulty=10,
                count=1,
            ),
            "Components": Aspect(
                format="Sand (ordinary, destroyed)", base_difficulty=-2, count=1
            ),
            "Focused": Aspect(format="On targets", base_difficulty=5, count=1),
            "Gestures": Aspect(
                format="Grab a handful of sand and blow it at the targets (simple)",
                base_difficulty=-1,
                count=1,
            ),
        },
        notes=dedent("""\
            This spell drives the targets into a magic sleep. The caster
            scoops up a handful of sand and blows upon it, whereupon it
            billows out to create a cone with a tip that begins 2.5 meters
            from the caster. The cone is three meters long and six meters
            wide at its end. The first target hit by the spell must make
            willpower/mettle roll with a difficulty of 15 or fall asleep. Those
            up to one meter behind the first target have difficulty of 14,
            those between one and two meters have a difficulty of 13,
            and those between two and three meters have a difficulty of
            12.  Creatures in combat or some other high-energy situation
            receive a +4 bonus on their willpower/mettle rolls.
            
            Sleeping creatures remain magically asleep and do not
            awaken normally, though other beings can shake them,
            slap them, dump water on their heads, and perform other
            actions in attempts wake them; doing so allows the sleeping
            creature another chance to awake, again with a willpower/
            mettle roll at the same difficulty that put him to sleep. (The
            gamemaster may allow bonuses on this roll depending on
            the vigor with which the characters attempt to awaken the
            victim.) The awakening attempt may be tried once per round
            at most; if one type of action fails, those trying to rose the
            sleeper must find another way.
            
            After the spell’s duration expires, the sleeping creatures
            enter normal sleep and awaken normally (from loud noises,
            being physically jostled, and so on).
            
            The caster can add her result point bonus to the difficulty
            of the willpower/mettle rolls to avoid the spell when other
            people attempt to awaken the victims.
            
            Somniomancers often use this spell as a precursor to other
            spells, such as dream travel, step into sleep, or nightmare.
        """),
        skill="Conjuration",
    ),
    Spell(
        name="Night Terrors",
        effect=Aspect(
            format="difficulty of 18 to resist falling asleep; 5D physical damage, ignores nonmagical armor",
            base_difficulty=41,
            count=1,
        ),
        duration=Aspect(format="1  minute/12 rounds ", base_difficulty=9, count=1),
        range=Aspect(format="60 meters ", base_difficulty=9, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=9, count=1),
        casting_time=Aspect(format="1 round ", base_difficulty=-4, count=1),
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Dreams, folk", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(
                format="30", base_difficulty=0, count=1
            ),  # Should be 35
            "Components": Aspect(
                format="Amber dust (very rare, destroyed)", base_difficulty=-10, count=1
            ),
            "Multiple Targets": Aspect(
                format="Up to 5 targets", base_difficulty=15, count=1
            ),
        },
        notes=dedent("""\
            This spell puts up to five targets to sleep and then ravages
            their minds with lethal nightmares. The targets must each
            make a willpower/mettle roll with a difficulty of 18 or fall
            asleep. This spell then burrows into the sleepers’ subconscious,
            drawing forth their greatest fears and forming them into
            horrific nightmares. They toss and thrash violently, obviously
            distressed and taking 5D of damage per round until dead or
            the duration ends. See kiss of the Sandman  for restrictions
            on waking magically slumbering creatures.
            
            The caster may add her result point bonus to the difficulty
            of the willpower/mettle rolls to resist falling asleep or to the
            damage done each round (not both and chosen once for the
            spell).
        """),
        skill="Conjuration",
    ),
    Spell(
        name="Night Visitation",
        effect=Aspect(format="persuasion of 4D", base_difficulty=12, count=1),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="2.5 kilometers ", base_difficulty=17, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=17, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        other_aspects={
            "Arcane Knowledge": Aspect(format="Dreams", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="23", base_difficulty=0, count=1),
        },
        other_conditions=[
            Aspect(
                format="Touch or name single specific target, who must be asleep",
                base_difficulty=-1,
                count=1,
            )
        ],
        notes=dedent("""\
            This spell allows the caster to deliver messages to sleep -
            ing creatures. The caster names a specific individual and
            formulates an image or series of images, which can be up to
            a minute in length, that appears in the named individual’s
            dream. If the individual is not asleep, the spell fails. The
            images can be anything the caster imagines that’s relatively
            nonfrightening; the caster cannot give the target a nightmare,
            though she may deliver threats and ultimatums. The caster
            can use this dream to persuade the target as if she had 4D
            in the persuasion skill.
            
            The caster chooses whether or not the target remembers
            the dream when he awakes. If the target does not remember
            the dream, the dream may still influence him subconsciously,
            at the gamemaster’s discretion.
            
            In lieu of naming a specific individual, the caster may
            make physical contact with the target (in which case, the
            range is irrelevant).
        """),
        skill="Alteration",
    ),
    Spell(
        name="Nightmare",
        effect=Aspect(
            format="10D physical damage, ignores all armor", base_difficulty=60, count=1
        ),
        duration=Aspect(format="1 round ", base_difficulty=4, count=1),
        range=Aspect(format="Touch ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 second ", base_difficulty=0, count=1),
        other_aspects={
            "Arcane Knowledge": Aspect(format="Dreams", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="32", base_difficulty=0, count=1),
        },
        other_conditions=[
            Aspect(format="Target must be asleep", base_difficulty=-1, count=1)
        ],
        notes=dedent("""\
            The caster touches the creature and  uses this spell to dredge
            up his most feared images from his subconscious, using these
            to create a horrific nightmare. The target thrashes, moans,
            and sweats. He must make a willpower/mettle roll against a
            roll of the caster’s willpower/mettle; if he fails, he dies of fear
            (and cardiac arrest).
            
            If the target is not asleep, this spell fails.
            
            The caster can apply her result point bonus to the difficulty 
            of the willpower/mettle roll the target needs to avoid
            the effect.
        """),
        skill="Alteration",
    ),
    Spell(
        name="Nightshield",
        effect=Aspect(
            format="compare to spell total of spell attempting to influence caster",
            base_difficulty=30,
            count=1,
        ),
        duration=Aspect(format="10 hours ", base_difficulty=23, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1.5 hours ", base_difficulty=-19, count=1),
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="15", base_difficulty=0, count=1),
            "Components": Aspect(
                format="A small shield of beaten silver (rare)",
                base_difficulty=-4,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(format="Awakening disrupts the spell", base_difficulty=-1, count=1)
        ],
        notes=dedent("""\
            The mage places a small silver shield on her chest just
            before she retires for the night, casting a spell that protects
            her dreams from outside influence (such as the machinations
            of another somniomancer). She adds her result point bonus
            to the spell’s effect value. If a another mage casts a spell that
            attempts to access her dreams or detecting whether she’s
            sleeping, the second caster’s  skill roll  for that spell must
            equal or exceed nightshield’s value (30 plus the caster’s result
            point bonus) to affect her.
            
            **Example**: Shannon casts nightshield before she goes to
            sleep because she suspects her somniomantic rival, Bruce,
            is on the prowl. She makes a conjuration roll to cast the spell
            and rolls a total of 19. This roll generates a result point bonus
            of 2, which she adds to nightshield’s effect value of 30, for a
            total of 32. If Bruce shows up and attempts to cast nightmare
            on Shannon, his alteration roll must equal or exceed 32 to
            affect her.        
        """),
        skill="Conjuration",
    ),
    Spell(
        name="Put the “Rest” in “Restoration”",
        effect=Aspect(format="medicine/healing of 9D", base_difficulty=27, count=1),
        duration=Aspect(format="10 hours ", base_difficulty=23, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        other_aspects={
            "Arcane Knowledge": Aspect(format="Time, folk", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="15", base_difficulty=0, count=1),
        },
        other_conditions=[
            Aspect(
                format="Effect may be used once per hour; spell is broken if caster is awakened during the duration",
                base_difficulty=-11,
                count=1,
            )
        ],
        notes=dedent("""\
            The mage casts this spell immediately before going to
            sleep. While she sleeps, her wounds heal at an accelerated
            rate. Each hour, she can heal her physical wounds as if she
            had 9D in the medicine/healing skill.
        """),
        skill="Conjuration",
    ),
    Spell(
        name="Really Comfy Pillow",
        effect=Aspect(
            format="Accelerated Healing (R1), +1D bonus to natural healing attempts, and Arcane Knowledge: Dreams (R1)), +2 to casting of related Magic spells",
            base_difficulty=12,
            count=1,
        ),
        duration=Aspect(format="10 hours ", base_difficulty=23, count=1),
        range=Aspect(format="Touch ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="10 minutes ", base_difficulty=-14, count=1),
        other_aspects={
            "Arcane Knowledge": Aspect(format="magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="16", base_difficulty=0, count=1),
            "Charges": Aspect(format="3 improved charges", base_difficulty=15, count=1),
            "Components": Aspect(
                format="A really comfortable pillow (uncommon)",
                base_difficulty=-3,
                count=1,
            ),
        },
        other_conditions=[
            Aspect(
                format="Target must want to fall asleep; spell is broken if target is awakened during duration",
                base_difficulty=-2,
                count=1,
            )
        ],
        notes=dedent("""\
            The caster touches a pillow, imbuing it with an enchantment
            that functions up to three times. Whenever a creature rests
            on the pillow, whether intending to sleep or merely take a
            short rest, over the course of one minute, the spell puts the
            creature to sleep. The user sleeps deeply and well, untroubled
            by nightmares or anxieties, for 10 hours and awakens feeling
            refreshed and invigorated, providing a +1D bonus to natu -
            ral healing attempts. This sleep is not magical, as it is with
            kiss of the Sandman or night terrors; it’s simply a dreamless,
            refreshing sleep. Loud noises, physical movement, and the
            like awaken the sleeper normally.
            
            The pillow can also aid in the casting of somniomancy
            spells that involve the mage being asleep in order to work.
            Using a really comfy pillow  grants the caster a +2 bonus on
            her appropriate Magic skill checks when she casts spells that
            require her to meditate or sleep.
        """),
        skill="Conjuration",
    ),
    Spell(
        name="Sleep Eternal",
        effect=Aspect(
            format="difficulty to resist falling asleep", base_difficulty=20, count=1
        ),
        duration=Aspect(format="10 years ", base_difficulty=43, count=1),
        range=Aspect(format="10 meters ", base_difficulty=5, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=5, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        other_aspects={
            "Arcane Knowledge": Aspect(format="Dreams", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="41", base_difficulty=0, count=1),
            "Focused": Aspect(format="On target", base_difficulty=12, count=1),
            "Variable Duration": Aspect(format="Off only", base_difficulty=4, count=1),
            "Other Alterant": Aspect(
                format="Puts target in type of sleep the caster chooses",
                base_difficulty=1,
                count=1,
            ),
        },
        notes=dedent("""\
            This spell causes the target to enter an endless sleep, effec-
            tively killing him — or at least, killing him until the caster
            chooses to release the curse.
            
            The target, which must already be asleep, falls even deeper
            into his sleep, so deep that he never awakens. When the caster
            casts this spell, the target can make a willpower/mettle roll
            with a difficulty of 20 to resist its effects; if he succeeds, he
            awakens. If this roll fails, he doesn’t wake up for 10 years.
            However, friends may attempt to bestir him; see kiss of the
            Sandman for details on reviving a magically slumbering
            character. The sleeper must have his nutrition intravenously
            injected if he is to survive.
            
            The caster can choose the nature of the target’s sleep. She
            has three options:
            
            -   The target’s sleep is full of pleasant dreams. He sleeps gently, with a smile upon his lips.
            
            -   The target’s sleep is dreamless. He appears to be in a coma.
            
            -   The target’s sleep is uneasy, filled with vague nightmares. He moans and twitches, obviously distressed.
            
            The caster can end this spell at any time. The only other
            way to awaken the target is to design a spell with the express
            purpose of doing so.
            
            The caster may add her result point bonus to the difficulty
            of the target’s willpower/mettle rolls to resist the spell’s
            effects.
        """),
        skill="Alteration",
    ),
    Spell(
        name="Sleep of Champions",
        effect=Aspect(
            format="+1D to all mental and physical attributes",
            base_difficulty=36,
            count=1,
        ),
        duration=Aspect(format="15 hours ", base_difficulty=24, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="10 hours ", base_difficulty=-23, count=1),
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="25", base_difficulty=0, count=1),
            "Focused": Aspect(format="On caster", base_difficulty=12, count=1),
        },
        notes="The caster spends two hours in preparation, then goes\nto sleep. When she awakens, she feels refreshed. Her mind\nis keen, her muscles flushed with energy, and her reflexes\nat their peak. She receives a +1D bonus on all mental and\nphysical attributes for the next 15 hours.",
        skill="Alteration",
    ),
    Spell(
        name="Sleep Sense",
        effect=Aspect(
            format="search of 8D to locate sleeping creatures",
            base_difficulty=24,
            count=1,
        ),
        duration=Aspect(format="15 hours ", base_difficulty=24, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="15 minutes ", base_difficulty=-15, count=1),
        other_aspects={
            "Arcane Knowledge": Aspect(format="Magic", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="28", base_difficulty=0, count=1),
            "Area of Effect": Aspect(
                format="Divination sphere with radius of 25 meters",
                base_difficulty=21,
                count=1,
            ),
            "Components": Aspect(
                format="Small letter Zs made of gold (very rare, destroyed)",
                base_difficulty=-10,
                count=1,
            ),
            "Focused": Aspect(format="On caster", base_difficulty=9, count=1),
            "Gestures": Aspect(
                format="Toss the Zs into the air (simple)", base_difficulty=-1, count=1
            ),
            "Incantations": Aspect(
                format="“I see you when you’re sleeping.” (complete sentence)",
                base_difficulty=-2,
                count=1,
            ),
            "Variable Movement": Aspect(
                format="Bending/unseen target", base_difficulty=5, count=1
            ),
        },
        notes=dedent("""\
            This spell allows the caster to detect sleeping creatures
            without actively attempting to do so.
            
            Over a 15-minute period, the caster tosses some small gold
            Zs into the air while repeating the incantation. For the spell’s
            duration, the caster always knows the exact locations of all
            sleeping creatures within the area of effect that are the size
            of a cat or larger. Walls and other obstructions do not inhibit
            this spell, though sleep sense does not convey the knowledge
            of how to access the sleepers, merely their locations.
            
            Most somniomancers cast this spell at the beginning of
            the day because it helps them find targets for some of their
            other spells, like step into sleep, nightmare, and dream travel.
        """),
        skill="Divination",
    ),
    Spell(
        name="Sleeping Puppet",
        effect=Aspect(format="Possession: Limited (R1)", base_difficulty=24, count=1),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        other_aspects={
            "Arcane Knowledge": Aspect(format="Dreams", base_difficulty=0, count=1),
            "Difficulty": Aspect(
                format="15", base_difficulty=0, count=1
            ),  # Should be 20
            "Focused": Aspect(format="On caster", base_difficulty=8, count=1),
        },
        other_conditions=[
            Aspect(
                format="Target must be sleeping; target must be sentient",
                base_difficulty=-2,
                count=1,
            )
        ],
        notes=dedent("""\
            It is possible for the caster to enter into the dimension
            of dreams and gain control over another sleep character’s
            mind. The target must be capable of cognitive thought and
            be of similar mind to the caster.
            
            If the spell is successfully cast, then the magic user gets the
            Possession: Limited (R1) Special Ability and must convince
            or command the target to obey The sleeping target cannot
            use willpower/mettle, as she is unaware that her mind is being
            influenced; rather, she can use Presence. If the caster succeeds,
            then the sleeper obeys, providing the command does not go
            against the personal morals of the target. Walking, talking
            and all normal actions can be executed so long as the mage is
            successful. If a failure occurs, the target awakens from what
            is thought to be a dream or nightmare — possibly far from
            where she fell asleep.
        """),
        skill="Alteration",
    ),
    Spell(
        name="Step Into Sleep",
        effect=Aspect(
            format="Possession: Limited (R1) and investigation of 5D",
            base_difficulty=39,
            count=1,
        ),
        duration=Aspect(format="10 minutes ", base_difficulty=14, count=1),
        range=Aspect(format="Touch ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="1 minute ", base_difficulty=-9, count=1),
        other_aspects={
            "Arcane Knowledge": Aspect(format="Dreams", base_difficulty=0, count=1),
            "Difficulty": Aspect(
                format="15", base_difficulty=0, count=1
            ),  # Should be 19
            "Components": Aspect(
                format="An item important to the target (uncommon)", base_difficulty=-4
            ),
            "Incantations": Aspect(
                format='"Open your dreams to me". (phrase)', base_difficulty=-1
            ),
        },
        other_conditions=[Aspect(format="Target must be asleep", base_difficulty=-1)],
        notes=dedent("""\
            This spell allows the caster to become part of the target’s
            dream, delivering messages, showing her power, and perform-
            ing many other actions that lesser spells do not allow.
            
            If the target is not asleep, the spell fails. If he is asleep, the
            caster enters the target’s dream. While in the target’s dreams,
            the caster’s body is rigid and vulnerable, similar to a character
            using the Possession: Limited Special Ability.
            
            While within the dream, the caster can speak, cast spells,
            use skills, and so on, but she cannot affect her surroundings in
            any way. The sleeper continues to dream, and his subconscious
            incorporates the caster into his dreams. The caster cannot
            directly harm the target, but she can deliver messages, disrupt
            his dreams, and so on. Similarly, the target’s dreams pose no
            danger to the caster, though they may be frightening.
            
            Additionally, the mage can observe the dreams, which
            might tell the caster something about the target. Using
            the “Posession Knowledge” chart and the investigation skill
            granted by the spell, the somniomancer can gain informa-
            tion about the target, although it may be couched in dream
            terms.
            
            The caster can add her result point bonus to the investiga-
            tion total.
        """),
        skill="Alteration",
    ),
    Spell(
        name="Timeslip",
        effect=Aspect(
            format="timeslip up to 400 kilograms, caster’s weight plus their alternate self’s weight",
            base_difficulty=13,
            count=1,
        ),
        duration=Aspect(format="1.5 rounds ", base_difficulty=1, count=1),
        range=Aspect(format="150 meters ", base_difficulty=11, count=1),
        speed=Aspect(format="instantaneous ", base_difficulty=11, count=1),
        casting_time=Aspect(format="1 second ", base_difficulty=0, count=1),
        skill="Chronomancy",
        other_aspects={
            "Difficulty": Aspect(
                format="22", base_difficulty=0, count=1
            ),  # Should be 11
            "Components": Aspect(
                format="An ounce of quicksilver (uncommon, destroyed)",
                base_difficulty=-8,
                count=1,
            ),
            "Countenance": Aspect(
                format="Caster sweats profusely and foams at the mouth (noticeable)",
                base_difficulty=-1,
                count=1,
            ),
            "Gestures": Aspect(
                format="The mage points off into the distance and then pulls the visualized target toward them as she leaps forward. (complex, action difficulty 11)",
                base_difficulty=-3,
                count=1,
            ),
            "Incantations": Aspect(
                format="“See ya, wouldn’t want to be ya!” (sentence)",
                base_difficulty=-2,
                count=1,
            ),
        },
        notes=dedent("""\
            In desperate situations, some people are forced into
            taking drastic actions to save their own skin. By invoking
            the power of the timeslip, the caster changes place with a
            counterpart from an alternate reality who returns to their
            proper time when their spell runs its course. When the
            hijacked future relative returns, the caster may choose to
            reappear anywhere up to 150 meters from her previous loca-
            tion. The destination spot must be visible to the caster or at
            the very least known to them (inner sanctum, the home of
            a close friend etc.) when the timeslip is cast. Of course, the
            abducted visitor not think very highly of being so rudely
            abducted and could possibly have the power to revisit their
            alternate self in order to avenge themselves. The payback
            could be brutally painful.
        """),
    ),
    Spell(
        effect=Aspect(
            format="Accelerated Healing (R2), +2D to natural heal - ing rolls",
            base_difficulty=18,
            count=1,
        ),
        duration=Aspect(format="10 hours ", base_difficulty=23, count=1),
        range=Aspect(format="Touch ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="10 minutes ", base_difficulty=-14, count=1),
        name="True Rest",
        other_aspects={
            "Arcane Knowledge": Aspect(
                format="Magic, folk", base_difficulty=0, count=1
            ),
            "Difficulty": Aspect(format="13", base_difficulty=0, count=1),
        },
        other_conditions=[
            Aspect(
                format="Target must be sleeping; awakening target during the duration disrupts the spell",
                base_difficulty=-2,
                count=1,
            )
        ],
        notes="The target, which must be willing and about to go to sleep,\nenters a particularly restful slumber that enhances his natu-\nral healing process. When the target makes natural healing\nroll, he gets +2D on the roll. If the target needs seveal days\nof rest before attempting the natural healing roll, the spell\nshould be cast on the last day of rest, as the effect lasts only\n10 hours.\n\n",
        skill="Alteration",
    ),
    Spell(
        name="Waking Nightmare",
        effect=Aspect(
            format="Fear (R12), +12 to initimidation totals and -12 to combat difficulties against those affected by the fear",
            base_difficulty=24,
            count=1,
        ),
        duration=Aspect(format="1 minute ", base_difficulty=9, count=1),
        range=Aspect(format="5 meters ", base_difficulty=4, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=4, count=1),
        casting_time=Aspect(format="2 rounds ", base_difficulty=-5, count=1),
        other_aspects={
            "Arcane Knowledge": Aspect(format="Dreams", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="22", base_difficulty=0, count=1),
            "Area Effect": Aspect(
                format="Circle with radius of 5 meters", base_difficulty=10, count=1
            ),
            "Concentration": Aspect(
                format="2 rounds with willpower/mettle difficulty of 8",
                base_difficulty=-2,
                count=1,
            ),
            "Focused": Aspect(
                format="On target (nightmare only)", base_difficulty=6, count=1
            ),
            "Unreal Effect": Aspect(
                format="Disbelief difficulty of 13", base_difficulty=-7, count=1
            ),
        },
        notes="A knowledgeable mage can send her mind into the plane of\ndreams and conjure a waking nightmare that can terrifying\nanyone who believes it. If the spell’s conditions are satisfied,\nand it is successfully cast, the mage inspires fear in a solitary\ntarget or a group of creatures that occupy the radius of the\nspell. This fear manifests itself as a walking nightmore to\nthose within the spell’s radius . The dread sight always stays\nwithin the spell’s proximity of those affected by the spell\n— though, if there’s a reason for them to do so, each target\nmay attempt to disbelieve the manifestation (instead of the\nresistance difficulty listed with the Special Ability).",
        skill="Conjuration",
    ),
    Spell(
        name="Walking Dream",
        effect=Aspect(
            format="Psionics: astral projection of 5D+2", base_difficulty=34, count=1
        ),
        duration=Aspect(format="1 hour ", base_difficulty=18, count=1),
        range=Aspect(format="Self ", base_difficulty=0, count=1),
        speed=Aspect(format="Instantaneous ", base_difficulty=0, count=1),
        casting_time=Aspect(format="5 hours ", base_difficulty=-22, count=1),
        other_aspects={
            "Arcane Knowledge": Aspect(format="Dreams", base_difficulty=0, count=1),
            "Difficulty": Aspect(format="12", base_difficulty=0, count=1),
            "Concentration": Aspect(
                format="1 hour with willpower/mettle difficulty of 12",
                base_difficulty=-6,
                count=1,
            ),
        },
        notes="This spell allows the caster’s dreaming consciousness to\nleave her body, roaming the world while she sleeps. The caster\nspends one hour in preparation, meditating and otherwise\npreparing her mind for its journey, then goes to sleep. Four\nhours into her sleep (which counts as part of the casting\ntime), her dreaming consciousness leaves her body for one\nhour, traveling as if the caster has 5D+2 in the Psionics: astral\nprojection skill.\n\n",
        skill="Conjuration",
    ),
]

if __name__ == "__main__":
    detail(spells)


__test__ = {
    "Cleansing Sleep": ">>> spells[0].difficulty\n10",
    "Concentration Lapse": ">>> spells[1].difficulty\n8",
    "Detect Slumber": ">>> spells[2].difficulty\n12",
    "Dream Travel": ">>> spells[3].difficulty\n19",
    "Dream Visions": ">>> spells[4].difficulty\n20",
    "Dreams in Hand": ">>> spells[5].difficulty\n10",
    "Dreamtime": ">>> spells[6].difficulty\n43",
    "Groggy": ">>> spells[7].difficulty\n21",
    "Insomnia": ">>> spells[8].difficulty\n11",
    "Kiss of the Sandman": ">>> spells[9].difficulty\n21",
    "Night Terrors": ">>> spells[10].difficulty\n35",
    "Night Visitation": ">>> spells[11].difficulty\n23",
    "Nightmare": ">>> spells[12].difficulty\n32",
    "Nightshield": ">>> spells[13].difficulty\n15",
    "Put the “Rest” in “Restoration”": ">>> spells[14].difficulty\n15",
    "Really Comfy Pillow": ">>> spells[15].difficulty\n16",
    "Sleep Eternal": ">>> spells[16].difficulty\n41",
    "Sleep of Champions": ">>> spells[17].difficulty\n25",
    "Sleep Sense": ">>> spells[18].difficulty\n28",
    "Sleeping Puppet": ">>> spells[19].difficulty\n20",
    "Step Into Sleep": ">>> spells[20].difficulty\n19",
    "Timeslip": ">>> spells[21].difficulty\n11",
    "True Rest": ">>> spells[22].difficulty\n13",
    "Waking Nightmare": ">>> spells[23].difficulty\n22",
    "Walking Dream": ">>> spells[24].difficulty\n12",
}
