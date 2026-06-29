"""
Extract Characters from ``creatures.ipynb realm dark smoke and ash characters``.
Created by V2026.5.7.dev1 opend6-tools, ``opend6_tools.notebook_extract`` 


When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the Characters.

With "display" argument, generates .RST-formatted short-form of all the Characters.

With "debug" argument, writes debugging details for selected Characters.

"""

from opend6_tools.character import *



giant = Creature(
    name='Giant',
    description="These are huge creatures, often weighing over one thousand kg.",
    agility=Agility(3*D, {'fighting': 4*D, 'melee combat': 4*D}),
    coordination=Coordination(1*D, {'throwing': 4*D}),
    physique=Physique(5*D, {'lifting': 6*D, 'running': 6*D+2}),
    intellect=Intellect(3*D, {'navigation': 1*D}),
    acumen=Acumen(1*D, {'tracking': 2*D}),
    charisma=Charisma(1*D, {'intimidation': 6*D}),
    move=10,
    advantages=[Size(3, 'Huge, scale value 8')],
    # disadvantages=[],
    special_abilities=[
        Hypermovement(2, '+4 to Move'),
        IncreasedAttribute(3, 'Physique, +3 to all Physique totals'),
        Fear(2, "+2D to intimidation and +2D to combat defense"),
    ],
    equipment='Large club (damage +2D); armor (defense +2D)',
    realm="dark smoke and ash",
)

troll = Creature(
    name='Troll',
    description="These are large creatures, often weighing several hundred kg. They prefer to hide and tunnel and build traps.",
    agility=Agility(3*D, {'fighting': 2*D, 'melee combat': 2*D}),
    coordination=Coordination(3*D, {'throwing': 1*D}),
    physique=Physique(4*D, {'lifting': 4*D, 'stamina': 1*D}),
    intellect=Intellect(3*D, {'healing': 1*D, 'traps': 3*D}),
    acumen=Acumen(2*D, {'hide': 2*D, 'know-how': 2*D}),
    charisma=Charisma(1*D, {'intimidation': 6*D}),
    move=10,
    advantages=[Size(1, 'Large, scale value 3')],
    disadvantages=[AchillesHeel(3, "Vulnerability to Fire: does double damage"),],
    special_abilities=[
        AcceleratedHealing(3, "+3D to Physique for natural healing"),
        AttackResistance(2, "+1D for extranormal, and non-enchanted weapons"),
    ],
    equipment='Often armed with war hammer (+1D+2), bone and hide armor (+1D), small shield (+2D)',
    realm="dark smoke and ash",
)

ogre = Creature(
    name="Ogre",
    description="These are large creatures. They are clever and magic use, but terrified of water.",
    agility=Agility(3*D, {'fighting': 2*D, 'melee combat': 2*D}),
    coordination=Coordination(3*D, {'throwing': 1*D}),
    physique=Physique(2*D, {'lifting': 2*D, 'stamina': 2*D}),
    intellect=Intellect(3*D, {'healing': 1*D, 'scholar': 3*D}),
    acumen=Acumen(3*D, {'disguise': 2*D, 'know-how': 2*D}),
    charisma=Charisma(1*D, {'intimidation': 6*D}),
    extranormal=Magic(3*D, {'apportation': 2*D}),
    advantages=[Size(1, 'Large, scale value 3')],
    disadvantages=[AchillesHeel(3, "Vulnerability to Water, takes +1D damage from a bucket-full"),],
    special_abilities=[
        AttackResistance(2, "+1D for extranormal, and non-enchanted weapons"),
    ],
    realm="dark smoke and ash",
)

giant_spider = Creature(
    name="Giant Spider",
    description="A spider with a 1-2 meter long body and 2-3 meter legs, a surprisingly tough hide, and a vicious poison in the fangs inside the mouth",
    agility=Agility(3 * D),
    coordination=Coordination(3 * D),
    physique=Physique(2 * D,
                      {'stamina': 3 * D}),
    intellect=Intellect(2 * D),
    acumen=Acumen(3 * D, {"tracking": D}),
    charisma=Charisma(3 * D, {'intimidation': 2 * D}),
    advantages=[
    ],
    disadvantages=[
    ],
    special_abilities=[
        NaturalHandWeapon(3, "Poison in the mouth fangs"),
        NaturalArmor(2, "tough chitonous hide")
    ],
    natural_abilities=[
        InfravisionUltravision(2),
    ],
    realm="dark smoke and ash",
)
characters = [ 
    giant, troll, ogre, giant_spider, 
]

__test__ = {
    
    'todo': """>>> note = 'Run the module with ``tests --make`` to create a template.'\n>>> pass"""
    
}


if __name__ == "__main__":
    app = build_app(characters)
    app()

