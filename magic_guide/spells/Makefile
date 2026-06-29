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

MG_SPELLS = \
	Chronomancy.txt         Elemental.txt           Necromancy.txt          Peregrination.txt       Photomancy.txt          Somniomancy.txt         Technomancy.txt         Vitomancy.txt           Wizardry.txt            sample_spells.txt	magic_guide_items.txt

spells : $(MG_SPELLS)

MG_MODULES = $(addsuffix .py,$(basename $(MG_SPELLS)))
test : $(MG_MODULES)
	for mod in $(MG_MODULES); do \
 		python $$mod test; \
 	done
