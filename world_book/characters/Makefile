# Characters and Creatures Makefile
.phony: characters creatures

vpath %.ipynb ../../notebooks

# Create a Python Character or Creature module from a Jupyter Notebook with the same name.
%.py : %.ipynb
	python -m opend6_tools.notebook_extract characters $< > $@

# Special case for a single notebook with all realms
Creatures_aelvishcavesandearth.py Creatures_aelvishmountainsandforests.py Creatures_brightfire.py Creatures_brightsandandwind.py Creatures_brighttowersandcities.py Creatures_darkcoldandmist.py Creatures_darksmokeandash.py Creatures_unknownrealm.py : creatures.ipynb
	python -m opend6_tools.notebook_extract characters --groupby realm --output "Creatures.py" $<

# Create an RST text file from a Python Character or Creature module with the same name.
%.txt : %.py
	python $< test
	python $< display --format SHORT > $@

WORLD_COPIED_CHARS = generic_people.txt generic_animals.txt generic_monsters.txt
WORLD_UNIQUE_CHARACTERS = Creatures_aelvishcavesandearth.txt Creatures_aelvishmountainsandforests.txt Creatures_brightfire.txt Creatures_brightsandandwind.txt Creatures_brighttowersandcities.txt Creatures_darkcoldandmist.txt Creatures_darksmokeandash.txt Creatures_unknownrealm.txt

# Special formats for the non-human races section.
fantasy_dwarf.txt : fantasy_dwarf.py
	python $< display --format LONG2 > $@
fantasy_elf.txt : fantasy_elf.py
	python $< display --format LONG2 > $@
fantasy_gnome.txt : fantasy_gnome.py
	python $< display --format LONG2 > $@
fantasy_reptile_man.txt : fantasy_reptile_man.py
	python $< display --format LONG2 > $@

characters : $(WORLD_UNIQUE_CHARACTERS) $(WORLD_COPIED_CHARS)

creatures : characters
