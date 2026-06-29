# Artifacts and Holy Items Makefile
.PHONY : items

vpath %.ipynb ../../notebooks


# Create a Python Items module from a Jupyter Notebook with the same name.
%.py : %.ipynb
	python -m opend6_tools.notebook_extract spells --book-variable items $< > $@


# Create an RST text file from a Python Items module with the same name.
%.txt : %.py
	# pytest --doctest-modules $<
	python $< test
	python $< display > $@

# Unique formatting requirement
mirror_of_the_highest_sun.txt : mirror_of_the_highest_sun.py
	python $< test
	python $< display --underline='' > $@

FANTASY_LOCATION_ITEMS = mirror_of_the_highest_sun.txt kasens_potions.txt morcades_potions.txt singing_sword.txt

items : $(FANTASY_LOCATION_ITEMS)

.PRECIOUS : %.py
