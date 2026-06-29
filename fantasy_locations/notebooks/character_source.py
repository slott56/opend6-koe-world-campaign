"""
The character_source data model.

This is for characters extracted from source documents as text.
"""
from collections.abc import Iterator
from dataclasses import dataclass, field, asdict
from difflib import get_close_matches
from typing import Any, ClassVar

import opend6_tools.character as od6

class ClassMatcher:
    def __init__(self, base_cls: type) -> None:
        self.class_map = {
            c.__name__: c
            for c in self.subclass_closure(base_cls)
        }
        self.suffix = ""

    @staticmethod
    def subclass_closure(cls: type) -> Iterator[type]:
        yield cls
        for sub in cls.__subclasses__():
            yield from ClassMatcher.subclass_closure(sub)

    def closest_match(self, name: str) -> type:
        """
        Sometimes the ability name includes a ":".
        Sometimes, the words after the ":" are clarification.
        There's no easy way to tell, so we do multiple lookups.

        Side-Effect: This also sets suffix to any suffix after the ":"
        that was not part of the match.
        """
        if ":" in name:
            full_matches = get_close_matches(name.strip(), self.class_map.keys(), n=1, cutoff=0.8)
            prefix, self.suffix = name.split(":")
            partial_matches = get_close_matches(prefix.strip(), self.class_map.keys(), n=1, cutoff=0.8)
            if full_matches:
                self.suffix = ""
                return self.class_map[full_matches[0]]
            elif partial_matches:
                return self.class_map[partial_matches[0]]
            else:
                raise ValueError(f"no class is close to {name}")
        else:
            self.suffix = ""
            matches = get_close_matches(name.strip(), self.class_map.keys(), n=1, cutoff=0.8)
            if matches:
                return self.class_map[matches[0]]
            raise ValueError(f"no class is close to {name}")

attribute_class_matcher = ClassMatcher(od6.Attribute)
option_class_matcher = ClassMatcher(od6.CharacterOption)

@dataclass
class Skill:
    label: str
    dice: str

    @classmethod
    def from_dict(cls, tomldict: dict[str, Any]) -> "Skill":
        return cls(**tomldict)

    def d6obj(self):
        pass

@dataclass
class Attribute:
    label: str
    dice: str
    skills: list[Skill]

    @classmethod
    def from_dict(cls, tomldict: dict[str, Any]) -> "Attribute":
        return cls(tomldict['label'], tomldict['dice'], list(map(Skill.from_dict, tomldict['skills'])))

    def d6obj(self):
        pass

    def pycode(self):
        cls = attribute_class_matcher.closest_match(self.label)
        skills = {
            skl.label: skl.dice for skl in self.skills
        }
        return f"{cls.__name__}({self.dice!r}, {skills!r})"

@dataclass
class OtherAttribute:
    label: str
    value: str
    suffix: str

    @classmethod
    def from_dict(cls, tomldict: dict[str, Any]) -> "OtherAttribute":
        return cls(**tomldict)

    def d6obj(self):
        pass

    def pycode(self):
        return repr(f"{self.value}, {self.suffix}")


@dataclass
class Ability:
    label: str
    rank: str
    details: str

    @classmethod
    def from_dict(cls, tomldict: dict[str, Any]) -> "Ability":
        return cls(**tomldict)

    def d6obj(self):
        if self.rank:
            cls = option_class_matcher.closest_match(self.label)
            return cls(self.rank, self.details)
        else:
            return od6.NaturalAbility(self.label)

    def pycode(self):
        if self.rank:
            cls = option_class_matcher.closest_match(self.label)
            return f"{cls.__name__}({self.details!r}, {self.rank})"
        else:
            return f"NaturalAbility({self.label!r})"


@dataclass
class Option:
    label: str
    details: list[Ability]

    @classmethod
    def from_dict(cls, tomldict: dict[str, Any]) -> "Option":
        return cls(tomldict['label'], list(map(Ability.from_dict, tomldict['details'])))

    def d6obj(self):
        return [dtl.dsl() for dtl in self.details]

    def pycode(self):
        details = ", ".join(
            dtl.pycode() for dtl in self.details
        )
        return f"[{details}]"

@dataclass
class Item:
    description: str
    features: str

    @classmethod
    def from_dict(cls, tomldict: dict[str, Any]) -> "Item":
        return cls(**tomldict)

    def d6obj(self):
        return f"{self.description} {self.features}"

    def pycode(self):
        return repr(f"{self.description} {self.features}")

@dataclass
class Equipment:
    items: list[Item]
    label: str = "Equipment"

    @classmethod
    def from_dict(cls, tomldict: dict[str, Any]) -> "Equipment":
        return cls(list(map(Item.from_dict, tomldict['items'])))

    def d6obj(self):
        return ", ".join(
            item.d6obj() for item in self.items
        )

    def pycode(self):
        items = ", ".join(
            item.pycode() for item in self.items
        )
        return items

@dataclass
class Character:
    name: str
    details: dict[str, Attribute | OtherAttribute | Ability | Equipment]

    base_attributes: ClassVar[str] = {
        "Agility", "Coordination", "Physique", "Charisma",
        "Intellect", "Acumen", "Magic", "Miracles"
    }
    other_attributes: ClassVar[str] = {
        "Strength Damage", "Move", "Fate Points",
        "Character Points", "Body Points", "Wound levels"
    }
    options: ClassVar[str] = {
        "Disadvantages", "Advantages", "Special", "Natural"
    }

    @classmethod
    def from_dict(cls, tomldict: dict[str, Any]) -> "Character":
        details = {}
        for label, detail in tomldict['details'].items():
            if label in cls.base_attributes:
                attr = Attribute.from_dict(detail)
            elif label in cls.other_attributes:
                attr = OtherAttribute.from_dict(detail)
            elif label in cls.options:
                attr = Option.from_dict(detail)
            elif label == "Equipment":
                attr = Equipment.from_dict(detail)
            else:
                raise RuntimeError(f"unknown {detail}")
            details[label] = attr
        return cls(tomldict['name'], details)

    def d6obj(self) -> od6.Character:
        """..todo:: Finish this??"""
        if 'Natural' in self.details:
            cls = od6.Creature
            extra_fields = {
                'natural_abilities': self.details['Natural'].dsl()
            }
        else:
            cls = od6.Character
            extra_fields = {}

        # NOTEBOOK EXTRACT NEEDS TEXT!
        # NOT THE FINAL OBJECT.
        # THE OBJECT IS NICE -- IT CONFIRMS THINGS -- BUT IT'S NOT THE GOAL

        return cls(
            name=self.name,
            disadvantages=(self.details['Disadvantages'].dsl() if 'Disadvantages' in self.details else []),
            advantages=(self.details['Advantages'].dsl() if 'Advantages' in self.details else []),
            special_abilities=(self.details['Special'].dsl() if 'Special' in self.details else []),
            equipment=(self.details['Equipment'].dsl() if 'Equipment' in self.details else ''),
            **extra_fields
        )

    def pycode(self) -> tuple[str, str]:
        if 'Natural' in self.details:
            cls = od6.Creature
            extra_fields = {
                'natural_abilities': self.details['Natural'].pycode()
            }
        else:
            cls = od6.Character
            extra_fields = {}

        fields = {
            'name': repr(self.name)
        } | {
            dtl.label.lower().replace(" ", "_"):  dtl.pycode()
            for label, dtl in self.details.items()
        } | extra_fields

        name_slug = self.name.lower().replace(" ", "_").replace(",", "")

        args = ",\n    ".join(f"{name}={value}" for name, value in fields.items())
        return name_slug, f"{cls.__name__}(\n    {args}\n)"
