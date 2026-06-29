# Character Sheet Makefile
.PHONY: forms

CHARACTERS_PATH = ../characters
vpath %.py $(CHARACTERS_PATH)

CHARACERS_MODULE = $(CHARACTERS_PATH)/template_characters.py

# Create a PDF file from a Python Character in the characters/template_characters.py
%.pdf : $(CHARACERS_MODULE)
	python $(CHARACERS_MODULE) pdf --format LATEX $(basename $@)

NAMES = bard.pdf cleric.pdf gladiator.pdf healer.pdf merchant.pdf monster_slayer.pdf ranger.pdf thief.pdf wanderer.pdf wizard.pdf

forms : $(NAMES)
