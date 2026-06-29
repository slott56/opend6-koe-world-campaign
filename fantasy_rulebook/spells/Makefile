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

FANTASY_SPELLS = fantasy_CANTRIPS.txt fantasy_ALTERATION.txt fantasy_APPORTATION.txt fantasy_CONJURATION.txt fantasy_DIVINATION.txt
FANTASY_MIRACLES = fantasy_miracle_DIVINATION.txt fantasy_miracle_FAVOR.txt fantasy_miracle_STRIFE.txt

spells : $(FANTASY_SPELLS) $(FANTASY_MIRACLES)

FANTASY_MODULES = $(addsuffix .py,$(basename $(FANTASY_SPELLS) $(FANTASY_MIRACLES)))
test : $(FANTASY_MODULES)
	for mod in $(FANTASY_MODULES); do \
 		python $$mod test; \
 	done
