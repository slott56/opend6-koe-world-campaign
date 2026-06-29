# Characters and Creatures Makefile
.phony: characters

vpath %.ipynb ../notebooks

# Create a Python Character or Creature module from a Jupyter Notebook with the same name.
%.py : %.ipynb
	python -m opend6_tools.notebook_extract characters $< > $@

# Create an RST text file from a Python Character or Creature module with the same name.
%.txt : %.py
	python $< test
	python $< display --format SHORT > $@

WORLD_UNIQUE_CHARACTERS = \
	sir_warrant.txt squire_starter.txt squire_angler.txt \
	sir_bond.txt squire_neck.txt oven.txt dredge.txt \
	xorn.txt salamander.txt \
	jackal_high_priest.txt jackal_internal.txt jackal_external.txt jackal_priests.txt \
	bandit_army.txt \
	goblin_horde.txt \
	old_keep_creatures.txt \
	ch_1_bandit_thugs.txt ch_1_allies.txt \
	foxstail_bandit_thugs.txt \
	ch_3_bandit_thugs.txt ch_3_allies.txt ch_3_grifters.txt \
	ch_4_jackal_spymaster.txt ch_4_goblin_assault.txt ch_4_highwaymen.txt \
	ch_5_jackal_spymaster.txt ch_5_jackal_doubleagent.txt wildmare_bandit_thugs.txt \
	ch_7_goblin_guards.txt \


characters : $(WORLD_UNIQUE_CHARACTERS)

.PRECIOUS : %.py
