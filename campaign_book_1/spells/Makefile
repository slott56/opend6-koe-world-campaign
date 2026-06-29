# Spells Makefile
.PHONY: spells invocations test

vpath %.ipynb ../notebooks

# Create a Python Spell module from a Jupyter Notebook with the same name.
%.py : %.ipynb
	python -m opend6_tools.notebook_extract spells $< > $@

# Create an RST text file from a Python Spell module with the same name.
%.txt : %.py
	# pytest --doctest-modules $<
	python $< test
	python $< display > $@

# Special case for the Keep Spellbook
new_keep_spells.txt : new_keep_spells.py
	python $< display --underline '' > $@

WORLD_SPELLS = xorn_spells.txt bandit_spells.txt new_keep_spells.txt

WORLD_INVOCATIONS = xorn_invocations.txt

spells : $(WORLD_SPELLS) $(WORLD_INVOCATIONS)


WORLD_MODULES = $(addsuffix .py,$(basename $(WORLD_SPELLS) $(WORLD_INVOCATIONS)))
test : $(WORLD_MODULES)
	for mod in $(WORLD_MODULES); do \
 		python $$mod test; \
 	done

.PRECIOUS : %.py
