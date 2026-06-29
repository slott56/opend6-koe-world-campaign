# Characters and Creatures Makefile
.PHONY: characters

vpath %.ipynb ../../notebooks

# Create a Python Character or Creature module from a Jupyter Notebook with the same name.
# NOTE: Not all characters are defined in notebooks. Some are only defined in modules.
%.py : %.ipynb
	python -m opend6_tools.notebook_extract characters $< > $@

# Create an RST text file from a Python Character or Creature module with the same name.
%.txt : %.py
	# pytest --doctest-modules $<
	python $< test
	python $< display --format SHORT > $@

FANTASY_CHARACTERS = intro_character.txt template_characters.txt generic_people.txt generic_animals.txt generic_monsters.txt
FANTASY_NON_NUMAN = fantasy_dwarf.txt fantasy_elf.txt fantasy_gnome.txt fantasy_reptile_man.txt

# Special formats for the non-human races section.
fantasy_dwarf.txt : fantasy_dwarf.py
	python $< display --format LONG2 > $@
fantasy_elf.txt : fantasy_elf.py
	python $< display --format LONG2 > $@
fantasy_gnome.txt : fantasy_gnome.py
	python $< display --format LONG2 > $@
fantasy_reptile_man.txt : fantasy_reptile_man.py
	python $< display --format LONG2 > $@

characters : $(FANTASY_CHARACTERS) $(FANTASY_NON_NUMAN)
