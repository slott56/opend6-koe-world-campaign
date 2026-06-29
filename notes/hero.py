"""
Tools to parse a Hero character description
and emit a seed OpenD6 description for a similar character.

Two forms:

- long has 1 characteristic per line.

- Short has 5 characteristics per line.
"""

from collections import deque, defaultdict
from dataclasses import dataclass
import re

from sphinx.addnodes import desc

from opend6_tools.character import Physique, Agility, Coordination, Intellect, Acumen, Charisma, DieCode

@dataclass
class Characteristic:
    value: int
    name: str
    cost: int | None = None
    @classmethod
    def from_text(cls, text: str) -> "Characteristic":
        fields = text.split('\t')
        if len(fields) == 3:
            # Long form: value\tname\tcost
            val_text, name, cost_text = text.split('\t')
            yield cls(int(val_text), name.strip(), int(cost_text))
        elif len(fields) == 5:
            # Short form: name:value\t...
            parsed = [f.split(':') for f in fields]
            yield from (cls(int(val_text), name) for name, val_text in parsed)
        elif len(fields) == 1:
            # Short form extra item (usually swimming:whatever)
            parsed = [f.split(':') for f in fields]
            yield from (cls(int(val_text), name) for name, val_text in parsed)
        else:
            raise SyntaxError(f"confusing characteristic {text!r}")

@dataclass
class SkillAbility:
    roll: str | list[str] = ""
    description: str = ""
    cost: int | None = None
    def astuple(self):
        if self.cost is None:
            cost = ""
        else:
            cost = str(self.cost)
        if isinstance(self.roll, str):
            roll = self.roll
            description = self.description
        elif len(self.roll) == 1:
            roll = self.roll[0]
            description = self.description
        else:
            roll = ""
            description =  ' '.join([self.description] + self.roll)
        return cost, description, roll
    @classmethod
    def from_text(cls, text: str) -> "SkillAbility":
        fields = text.split('\t')
        if len(fields) == 1:
            # Short form: label \d+-,... or sometimes only label,...
            parsed = [skill.split(' ') for skill in text.split(',')]
            yield from (
                cls(description=description, roll=roll) for description, *roll in parsed
            )
        elif len(fields) == 2:
            # Long form 1: cost\tdescription
            cost_text, description = fields
            yield cls(cost=int(cost_text), description=description.strip())
        elif len(fields) == 3:
            # Long form 1: cost\tdescription\troll
            cost_text, description, roll = fields
            yield cls(cost=int(cost_text), description=description.strip(), roll=roll)
        else:
            raise SyntaxError(f"confusing skill/ability {fields!r}")

@dataclass
class Disadvantage:
    description: str = ""
    cost: int | None = None
    @classmethod
    def from_text(cls, text: str) -> "Disadvantage":
        fields = text.split('\t')
        if len(fields) == 1:
            # Short form: label: details;...
            parsed = text.split(';')
            yield from (
                cls(description=description) for description in parsed
            )
        elif len(fields) == 2:
            # Long form 1: cost\tlabel: details
            cost_text, description = fields
            yield cls(cost=int(cost_text), description=description.strip())

        else:
            raise SyntaxError(f"confusing disadvantage {fields!r}")

@dataclass
class Description:
    label: str
    value: str
    @classmethod
    def from_text(cls, text: str) -> "Description":
        label, _, value = text.partition(":")
        yield cls(label.strip(), value.strip())

@dataclass
class HeroCharacter:
    characteristics: dict[str, Characteristic]
    skills_abilities: dict[str, SkillAbility]
    disadvantages: list[Disadvantage]
    description: dict[str, Description]

    @classmethod
    def from_text(cls, block) -> "HeroCharacter":
        r"""Special lines that change mode:
        "Characteristics:", "Skills & Abilities:",
        "\d+\+ Disadvantage", "Costs: char skills total disadv base",
        "Powers and Skills:",

        Also, "\d+ \+ \d+ = \d+ = \d+ \+ \d+", "Cost: \d+", "Background:" and "Quote:" become Descriptions.
        """
        special = re.compile(
            r"Characteristics:"
            r"|Skills\s&\sAbilities:"
            r"|\d+\+ Disadvantage"
            r"|\d+ \+ \d+ = \d+ = \d+ \+ \d+"
            r"|Cost: \d+"
            r"|Costs: [\w\s]+"
            r"|Powers and Skills:"
            r"|Background:"
            r"|Quote:"
        )
        def parse(source: deque[str]) -> defaultdict[str, list[str]]:
            subsections = defaultdict(list[str])
            mode: type = Description
            while source:
                line = source.popleft()
                if not line:
                    continue
                if special.match(line):
                    if line.startswith("Charac"):
                        mode = Characteristic
                        continue
                    elif line.startswith("Skills"):
                        mode = SkillAbility
                        continue
                    elif "Disadvantage" in line:
                        mode = Disadvantage
                        continue
                    elif line.startswith("Powers and"):
                        mode = SkillAbility
                        header, _, details = line.partition(':')
                        subsections[mode].extend(mode.from_text(details.strip()))
                        continue
                    elif line.startswith("Backgr") or line.startswith("Quote"):
                        mode = Description
                        subsections[mode].extend(mode.from_text(line))
                        continue
                    elif "=" in line or line.startswith("Cost:") or line.startswith("Costs:"):
                        mode = Description
                        subsections[mode].extend(mode.from_text(line))
                        continue
                    else:
                        raise RuntimeError
                else:
                    try:
                        subsections[mode].extend(mode.from_text(line))
                    except Exception:
                        print(mode, repr(line))
                        raise
            return subsections
        subsects = parse(deque(line.strip() for line in block.splitlines()))
        return cls(
            characteristics = {c.name: c for c in subsects[Characteristic]},
            skills_abilities = {s.description: s for s in subsects[SkillAbility]},
            disadvantages = subsects[Disadvantage],
            description = {d.label: d for d in subsects[Description]}
        )

def to_dieCode(value: int):
    return DieCode.from_pips(9+value/5)

def opend6_seed(hc: HeroCharacter):
    print("Character(")
    print(f"    name={hc.description['Name'].value!r},")
    if 'Background' in hc.description:
        print(f"    description={hc.description['Background'].value!r},")
    if 'Quote' in hc.description:
        print(f"    other_notes=\"Quote: {hc.description['Quote'].value!r}\",")
    print(f"    physique={Physique(to_dieCode(hc.characteristics['STR'].value), {'stamina': hc.characteristics['CON'].value})},")  # plus REC and END if cost > 0?
    print(f"    agility={Agility(to_dieCode(hc.characteristics['DEX'].value), {'fighting': hc.characteristics['SPD'].value})},")
    print(f"    coordination={Coordination(to_dieCode(hc.characteristics['DEX'].value))},")
    print(f"    intellect={Intellect(to_dieCode(hc.characteristics['INT'].value))},")
    print(f"    acumen={Acumen(to_dieCode(hc.characteristics['EGO'].value))},")
    print(f"    charisma={Charisma(to_dieCode(hc.characteristics['COM'].value), {'intimidation': hc.characteristics['PRE'].value})},")
    print(f"    body={hc.characteristics['BODY'].value*2},")
    print(f"    move={hc.characteristics['Running'].value * 10 / 6},")
    print(")")
    print(f"| {'cost':4s} | {'description':40s} | {'roll':20s} |")
    print(f"|-{'-'*4:4s}-|-{'-'*40:40s}-|-{'-'*20:20s}-|")
    for sa in hc.skills_abilities.values():
        cost, description, roll = sa.astuple()
        print(f"| {cost:>4s} | {description:40s} | {roll:20s} |")
    print()
    for d in hc.disadvantages:
        print(d.description)
    print()
