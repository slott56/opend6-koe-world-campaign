"""
Template Characters from OpenD6 Fantasy Rulebook.
Used to populate "Templates" chapter
"""
from textwrap import dedent
from opend6_tools.character import *

bard = Character(
    occupation="Bard",
    race="Human",
    agility=Agility(
        2 * D,
        {
            "climbing": 0,
            "dodge": 0,
            "fighting": 0,
            "melee combat": 0,
            "riding": 0,
            "stealth": 0,
        },
    ),
    intellect=Intellect(
        4 * D,
        {
            "cultures": 0,
            "healing": 0,
            "navigation": 0,
            "reading/writing": 0,
            "scholar": 0,
            "speaking": 0,
            "trading": 0,
        },
    ),
    coordination=Coordination(2 * D, {"lockpicking": 0}),
    acumen=Acumen(
        4 * D,
        {
            "artist": 0,
            "disguise": 0,
            "gambling": 0,
            "hide": 0,
            "investigation": 0,
            "know-how": 0,
            "search": 0,
            "streetwise": 0,
            "survival": 0,
        },
    ),
    physique=Physique(2 * D, {"running": 0}),
    charisma=Charisma(
        4 * D, {"bluff": 0, "charm": 0, "intimidation": 0, "mettle": 0, "persuade": 0}
    ),
    # advantages=[],
    disadvantages=[
        Quirk(1, "your muse often overcomes you and inspires you to create a song or story on the spot"),
    ],
    special_abilities=[
        SkillBonus(1, "Eidetic, +1 bonus to speaking, scholar, and investigation totals"),
    ],
    weapons=["dagger (damage +1D)"],
    armor=["leather jerkin (Armor Value +2)"],
    equipment=["paper", "quill and ink", "scroll tube"],
    description=dedent("""\
        Others get ideas for their tales
        second or third hand. You prefer to see the
        really exciting parts of history unfold for yourself."""),
)

cleric = Character(
    occupation="Cleric",
    race="Human",
    agility=Agility(
        2 * D + 1,
        {
            "acrobatics": 0,
            "fighting": 0,
            "melee combat": 0,
            "riding": 0,
        },
    ),
    intellect=Intellect(
        3 * D + 2,
        {
            "cultures": 0,
            "healing": 0,
            "navigation": 0,
            "reading/writing": 0,
            "scholar": 0,
            "speaking": 0,
            "trading": 0,
        },
    ),
    coordination=Coordination(2 * D, {"charioteering": 0, "throwing": 0}),
    acumen=Acumen(
        3 * D,
        {
            "artist": 0,
            "crafting": 0,
            "disguise": 0,
            "investigation": 0,
            "know-how": 0,
            "search": 0,
            "survival": 0,
        },
    ),
    physique=Physique(2 * D, {"lifting": 0, "running": 0, "stamina": 0}),
    charisma=Charisma(
        3 * D,
        {
            "animal handling": 0,
            "bluff": 0,
            "chann": 0,
            "command": 0,
            "intimidation": 0,
            "mettle": 0,
            "persuasion": 0,
        },
    ),
    extranormal=Miracles(2 * D, {"divination": 0, "favor": 0, "strife": 0}),
    advantages="",
    disadvantages=[
        Equipment(1, "armor and weapon"),
    ],
    special_abilities=[
        Devotion(2, "to your religion"),
        Employed(1, "must follow sect's regulations"),
    ],
    weapons=["Mace (damage +1D+1)"],
    armor=["hard leather armor (Armor Value +1D+1)"],
    equipment=[
        "religious symbol",
        "leather pouch",
        "ceremonial cloth"
    ],
    description=dedent("""\
        Being the youngest of a very
        large family, your family sent you away to
        join a religious sect, one that promomoted
        charity and knowledge. Your sect has now sent you
        out to practice what you have been taught
        and help others. Although you will defend
        yourself, you consider indiscriminate violance 
        as stooping to the level of lesser beings."""),
)

gladiator = Character(
    occupation="Gladiator",
    race="Human",
    agility=Agility(
        4 * D,
        {
            "acrobatics": 0,
            "climbing": 0,
            "dodge": 0,
            "fighting": 0,
            "jumping": 0,
            "melee combat": 0,
            "riding": 0,
            "stealth": 0,
        },
    ),
    intellect=Intellect(
        2 * D,
        {
            "healing": 0,
        },
    ),
    coordination=Coordination(
        3 * D, {"charioteering": 0, "marksmanship": 0, "throwing": 0}
    ),
    acumen=Acumen(
        3 * D,
        {"crafting": 0, "gambling": 0, "know-how": 0, "streetwise": 0, "survival": 0},
    ),
    physique=Physique(
        4 * D,
        {
            "lifting": 0,
            "running": 0,
            "stamina": 0,
            "swimming": 0,
        },
    ),
    charisma=Charisma(
        2 * D,
        {
            "command": 0,
            "intimidation": 0,
            "mettle": 0,
            "persuasion": 0,
        },
    ),
    advantages=[
        TrademarkSpecialization(1, "gain +2D when using one weapon (your choice) plus you may be recognized by those watching"),
    ],
    disadvantages=[
        Devotion(1,"to fighting"),
    ],
    special_abilities=[],
    weapons=["Short sword (damage +1D+2)"],
    armor=["hard leather armor (armor value +1D+1)", "small shield (armor value +2D)"],
    equipment=[],
    description=dedent("""\
        You have so focused yourself onb battle
        that you find it hard to resist a 
        fight when you have the opportunity.
        From your time in the arena circuit, you've become
        famous for the use of a particular weapon."""),
)

healer = Character(
    occupation="Healer",
    race="Human",
    agility=Agility(
        2 * D + 2,
        {
            "climbing": 0,
            "dodge": 0,
            "melee combat": 0,
            "riding": 0,
        },
    ),
    intellect=Intellect(
        4 * D,
        {
            "cultures": 0,
            "healing": 0,
            "readi11g/writing": 0,
            "scholar": 0,
            "speaking": 0,
            "trading": 0,
        },
    ),
    coordination=Coordination(
        2 * D,
        {
            "sleight of hand": 0,
            "throwing": 0,
        },
    ),
    acumen=Acumen(
        3 * D + 2,
        {
            "artist": 0,
            "hide": 0,
            "investigation": 0,
            "know-how": 0,
            "search": 0,
            "survival": 0,
        },
    ),
    physique=Physique(
        2 * D + 1,
        {
            "lifting": 0,
            "running": 0,
            "stamina": 0,
            "swimming": 0,
        },
    ),
    charisma=Charisma(
        3 * D + 1,
        {
            "animal handling": 0,
            "charm": 0,
            "command": 0,
            "mettle": 0,
            "persuasion": 0,
        },
    ),
    advantages=[],
    disadvantages=[
        Quirk(1, "Stutter, whenever you fail a skill check, you become flustered and stutter, getting a +3 to all interaction difficulties, until you get a Critical Success on a roll"),
    ],
    special_abilities=[
        SkillBonus(1, "Naturally Soothing, +1 bonus to animal handling, charm and healing rolls"),
    ],
    armor=[],
    weapons=["Knife (damage +1D)"],
    equipment=[
        "3 candles, tinderbox",
        "pouch of herbs (+1 bonus to healing totals, six uses)"
    ],
    description=dedent("""\
        You've always had a prediliction
        toward caring for others. Except when
        you get nervous and stutter, people like to 
        be around you."""),
)

merchant = Character(
    occupation="Merchant",
    race="Human",
    agility=Agility(
        2 * D + 2,
        {
            "dodge": 0,
            "fighting": 0,
            "melee combat": 0,
            "riding": 0,
        },
    ),
    intellect=Intellect(
        4 * D,
        {
            "cultures": 0,
            "healing": 0,
            "navigation": 0,
            "readi11g/writing": 0,
            "scholar": 0,
            "speaking": 0,
            "lTading": 0,
        },
    ),
    coordination=Coordination(
        2 * D,
        {
            "charioteering": 0,
            "lockpicking": 0,
            "sleightofhand": 0,
        },
    ),
    acumen=Acumen(
        3 * D,
        {
            "artist": 0,
            "crafting": 0,
            "disguise": 0,
            "gambling": 0,
            "hide": 0,
            "investigation": 0,
            "know-how": 0,
            "search": 0,
            "streetwise": 0,
        },
    ),
    physique=Physique(
        2 * D + 1,
        {
            "lifting": 0,
            "running": 0,
        },
    ),
    charisma=Charisma(
        4 * D,
        {
            "animal handling": 0,
            "bluff": 0,
            "charm": 0,
            "command": 0,
            "intimidation": 0,
            "mettle": 0,
            "persuasion": 0,
        },
    ),
    funds=5 * D,
    advantages=[
        Wealth(1," +2 to Funds roll / 10 silver coins"),
    ],
    disadvantages=[
        Quirk(1, "always looking for a way to make a profit -- always"),
    ],
    special_abilities=[],
    armor=["fine garments with a heavy brocade vesat (Armor value +1)"],
    weapons=["Staff (damage +1D+2)"],
    equipment=["leather bag filled with a handful of small gold and silver coins and small jewels"],
    description=dedent("""\
        You've made your fortune several 
        times over (and lost some of it on other schemes.)
        You're looking for a new town that could use your services."""),
)


monster_slayer = Character(
    occupation="Monster Slayer",
    race="Human",
    agility=Agility(
        3 * D + 2,
        {
            "acrobatics": 0,
            "climbing": 0,
            "dodge": 0,
            "fighting": 0,
            "jumping": 0,
            "melee combat": 0,
            "stealth": 0,
        },
    ),
    intellect=Intellect(
        2 * D,
        {
            "healing": 0,
            "traps": 0,
        },
    ),
    coordination=Coordination(
        3 * D + 1,
        {
            "marksmanship": 0,
            "throwing": 0,
        },
    ),
    acumen=Acumen(
        3 * D + 1,
        {
            "gambling": 0,
            "crafting": 0,
            "hide": 0,
            "investigation": 0,
            "search": 0,
            "streetwise": 0,
            "survival": 0,
            "tracking": 0,
        },
    ),
    physique=Physique(
        3 * D + 2,
        {
            "lifting": 0,
            "running": 0,
            "stamina": 0,
            "swimming": 0,
        },
    ),
    charisma=Charisma(
        2 * D,
        {
            "animal handling": 0,
            "command": 0,
            "intimidation": 0,
            "mettle": 0,
            "persuasion": 0,
        },
    ),
    advantages=[],
    disadvantages=[
        Age(1, "you are slightly younger than typical, so people don't always take you seriously. Devotion (R1), to protecting ordinary people from extraordinary fiends"),
    ],
    special_abilities=[
        AttackResistance(1, "Nonenchanted Weapons, +1D to your damage resistance totalled against such weapons"),
    ],
    armor=["Leather pants (armor value +2 to legs only)"],
    weapons=["Battle Axe (damage +3D)"],
    equipment=[],
    description=dedent("""\
    After a band of monsters killed those you loved, you've been wandering the
    world, seeking to rid it of such diabolical creatures.  A priest blessed your cause, giving
    you a resistance to certain kinds of physical harm."""),
)

ranger = Character(
    occupation="Ranger",
    race="Human",
    agility=Agility(
        3 * D + 1,
        {
            "climbing": 0,
            "dodge": 0,
            "fighting": 0,
            "jumping": 0,
            "melee combat": 0,
            "riding": 0,
            "stealth": 0,
        },
    ),
    intellect=Intellect(
        2 * D + 2,
        {
            "healing": 0,
            "navigation": 0,
            "scholar": 0,
            "speaking": 0,
            "traps": 0,
        },
    ),
    coordination=Coordination(
        3 * D + 1,
        {
            "marksmanship": 0,
            "throwing": 0,
        },
    ),
    acumen=Acumen(
        2 * D + 2,
        {
            "crafting": 0,
            "hide": 0,
            "investigation": 0,
            "know-how": 0,
            "search": 0,
            "survival": 0,
            "tracking ": 0,
        },
    ),
    physique=Physique(
        3 * D,
        {
            "lifting": 0,
            "running": 0,
            "stamina": 0,
            "swimming": 0,
        },
    ),
    charisma=Charisma(
        3 * D,
        {
            "animal handling": 0,
            "charm": 0,
            "command": 0,
            "intimidation": 0,
            "mettle": 0,
            "persuasion": 0,
        },
    ),
    advantages=[
        Contacts(1, "you've helped a lot of people, many of whom would be willing to return to the favor"),
    ],
    disadvantages=[
        Devotion(2, "fierclu devoted to protecting wilderness areas and their inhabitants"),
    ],
    special_abilities=[
        SkillBonus(1, "Keen Eye, +1 bonus to marksmanship, search, and tracking"),
    ],
    armor=["Leather jerkin (armor value +2)"],
    weapons=["long bow, and quiver of arrows (damage +3D+2)"],
    equipment=["Cloak"],
    description=dedent("""\
    You grew up in forests and you've traveled through a lot of wilderness.
    You firstly seek to protect the land, plants, and animals, and secondly, any travelers."""),
)

thief = Character(
    occupation="Thief",
    race="Human",
    agility=Agility(
        3 * D,
        {
            "acrobatics": 0,
            "climbing": 0,
            "contortion": 0,
            "dodge": 0,
            "fighting": 0,
            "jumping": 0,
            "melee combat": 0,
            "stealth": 0,
        },
    ),
    intellect=Intellect(
        2 * D + 1,
        {
            "cultures": 0,
            "reading/writing": 0,
            "trading": 0,
            "traps": 0,
        },
    ),
    coordination=Coordination(
        4 * D,
        {
            "lockpickjng": 0,
            "sleight of hand": 0,
            "throwing": 0,
        },
    ),
    acumen=Acumen(
        2 * D + 2,
        {
            "artist": 0,
            "crafting": 0,
            "disguise": 0,
            "gambling": 0,
            "hide": 0,
            "investigation": 0,
            "search": 0,
            "streetwise": 0,
            "survival": 0,
        },
    ),
    physique=Physique(
        3 * D,
        {
            "lifting": 0,
            "running": 0,
        },
    ),
    charisma=Charisma(
        3 * D,
        {
            "bluff": 0,
            "charm": 0,
            "mettle": 0,
            "persuasion": 0,
        },
    ),
    advantages=[],
    disadvantages=[
        Enemy(1, "someone caught you while you were stealing -- though you managed to escape, you now have someone after you"),
    ],
    special_abilities=[
        SkillBonus(1, "Nimble Fingers, +1 bpnus to lockpicking, sleight of hand, and gambling"),
    ],
    armor=[],
    weapons=["Dagger (damage +1D)"],
    equipment=["cloak", "rope", "sack", "a few tools to spring traps"],
    description=dedent("""\
    Some people farm or fight professionally to earn a living.
    You prefer to test your wits against the awareness of a household.
    If you win, you get to keep something."""),
)


wanderer = Character(
    occupation="Wanderer",
    race="Human",
    agility=Agility(
        3 * D,
        {
            "acrobatics": 0,
            "climbing": 0,
            "contortion": 0,
            "dodge": 0,
            "fighting": 0,
            "jumping": 0,
            "melee combat": 0,
            "riding": 0,
            "stealth": 0,
        },
    ),
    intellect=Intellect(
        3 * D,
        {
            "cultures": 0,
            "devices": 0,
            "healing": 0,
            "readi11g/writing": 0,
            "navigation": 0,
            "scholar": 0,
            "speaking": 0,
            "trading": 0,
            "traps": 0,
        },
    ),
    coordination=Coordination(
        3 * D,
        {
            "charioteering": 0,
            "lockpicking": 0,
            "marksmamhip": 0,
            "pilotry": 0,
            "sleight of hand": 0,
            "throwing": 0,
        },
    ),
    acumen=Acumen(
        3 * D,
        {
            "crafting": 0,
            "artist": 0,
            "disguise": 0,
            "gambling": 0,
            "hide": 0,
            "investigation": 0,
            "know-how": 0,
            "search": 0,
            "streetwise": 0,
            "survival": 0,
            "tracking": 0,
        },
    ),
    physique=Physique(
        3 * D,
        {
            "lifting": 0,
            "running": 0,
            "stamina": 0,
            "swimming": 0,
        },
    ),
    charisma=Charisma(
        3 * D,
        {
            "animal handling": 0,
            "bluff": 0,
            "charm": 0,
            "command": 0,
            "intimidation": 0,
            "mettle": 0,
            "persuasion": 0,
        },
    ),
    advantages=[
        Cultures(1, "you have a knack for drawing parallels between known and unusual cultures"),
    ],
    disadvantages=[
        Hindrance(1, "Trick Shoulder, +1 to climbing, melee combat, and throwing difficulties"),
    ],
    special_abilities=[],
    weapons=["Studded Staff (damage +2D)"],
    equipment=["cloak", "sack", "water skin"],
    description=dedent("""\
    You seek to learn about new cultures.  Whan you've had your fill of one, you move on."""),
)


wizard = Character(
    occupation="Wizard",
    race="Human",
    agility=Agility(
        2 * D + 1,
        {
            "acrobatics": 0,
            "fighting": 0,
            "riding": 0,
            "stealth": 0,
        },
    ),
    intellect=Intellect(
        3 * D + 1,
        {
            "cultures": 0,
            "devices": 0,
            "healing": 0,
            "navigation": 0,
            "reading/writing": 0,
            "scholar": 0,
            "speaking": 0,
            "trading": 0,
            "traps": 0,
        },
    ),
    coordination=Coordination(
        2 * D,
        {
            "charioteering": 0,
            "marksmanship": 0,
            "sleight of hand": 0,
            "throwing": 0,
        },
    ),
    acumen=Acumen(
        3 * D + 1,
        {
            "artist": 0,
            "crafting": 0,
            "disguise": 0,
            "gambling": 0,
            "hide": 0,
            "investigation": 0,
            "know-how": 0,
            "search": 0,
            "streetwise": 0,
            "survival": 0,
        },
    ),
    physique=Physique(
        2 * D,
        {
            "lifting": 0,
            "running": 0,
        },
    ),
    charisma=Charisma(
        2 * D + 2,
        {
            "animal handling": 0,
            "bluff": 0,
            "charm": 0,
            "command": 0,
            "intimidation": 0,
            "mettle": 0,
            "persuasion": 0,
        },
    ),
    extranormal=Magic(
        2 * D + 1,
        {
            "alteration": 0,
            "apportation": 0,
            "conjuration": 0,
            "divination": 0,
        },
    ),
    advantages=[],
    disadvantages=[
        Prejudice(2, "the wizard cult you belonged to has a bad reputation, and you find many people shun you"),
    ],
    special_abilities=[
        LuckGood(1),
    ],
    armor=["soft leather jerkin and pants (Armor Value +2)"],
    weapons=["Small knife (damage +2)"],
    equipment=["paper, quill, and kin", "a few small spell components", "a few spells on scrolls"],
    description=dedent("""\
    Though the art of spell design fascinates you, the idea of staying locked in a
    stuffy library doesn't. You've taken  to adventuring to find inspiration for new
    spells, lost sources of mystical energy, and forgotten ancient artifacts."""),
)


all_characters = {
    "Bard": bard,
    "Cleric": cleric,
    "Gladiator": gladiator,
    "Healer": healer,
    "Merchant": merchant,
    "Monster Slayer": monster_slayer,
    "Ranger": ranger,
    "Thief": thief,
    "Wanderer": wanderer,
    "Wizard": wizard,
}


if __name__ == "__main__":
    app = build_app(all_characters)
    app()

__test__ = {
    "pass": ">>> pass\n"
}
