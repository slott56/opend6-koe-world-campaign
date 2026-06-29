# Artifacts and Holy Items Makefile
.PHONY : items

vpath %.ipynb ../../notebooks


# Create a Python Items module for a notebook that doesn't match the common pattern.
unique_sword_relics.py : unique_sword_relics.ipynb
	python -m opend6_tools.notebook_extract characters --book-variable swords $< > $@

unique_swords.py : unique_swords.ipynb
	python -m opend6_tools.notebook_extract characters --book-variable swords $< > $@

# Create a Python Items module from a Jupyter Notebook with the same name.
%.py : %.ipynb
	python -m opend6_tools.notebook_extract spells --book-variable items $< > $@


unique_sword_relics.txt : unique_sword_relics.py
	python $< display --format SHORT > $@

unique_swords.txt : unique_swords.py
	python $< display --format SHORT > $@

# Create an RST text file from a Python Items module with the same name.
%.txt : %.py
	# pytest --doctest-modules $<
	python $< test
	python $< display > $@


WORLD_COPIED_ITEMS = fantasy_items.txt fantasy_holy_items.txt
WORLD_UNIQUE_ITEMS = unique_rings.txt unique_wands_staves.txt unique_cups.txt unique_swords.txt unique_sword_relics.txt unique_potions.txt unique_armor.txt

items : $(WORLD_UNIQUE_ITEMS) $(WORLD_COPIED_ITEMS)

.PRECIOUS : %.py
