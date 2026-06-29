# Spells Makefile
.PHONY: spells test

vpath %.ipynb ../../notebooks

# Create a Python Spell module from a Jupyter Notebook with the same name.
%.py : %.ipynb
	python -m opend6_tools.notebook_extract spells $< > $@

# Create an RST text file from a Python Spell module with the same name.
%.txt : %.py
	# pytest --doctest-modules $<
	python $< test
	python $< display > $@

FANTASY_LOCATION_SPELLS = wizard_tower.txt

spells : $(FANTASY_LOCATION_SPELLS)

FANTASY_LOCATION_MODULES = $(addsuffix .py,$(basename $(FANTASY_LOCATION_SPELLS)))
test : $(FANTASY_LOCATION_MODULES)
	for mod in $(FANTASY_LOCATION_MODULES); do \
 		python $$mod test; \
 	done
