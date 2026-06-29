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

WORLD_SPELLS = fw_cantrips.txt fw_rank2.txt fw_rank3.txt fw_rank4.txt fw_rank5.txt fw_rank6.txt fw_rank8.txt \

WORLD_COPIED_SPELLS = fantasy_CANTRIPS.txt fantasy_ALTERATION.txt fantasy_CONJURATION.txt fantasy_DIVINATION.txt \
	fantasy_miracle_DIVINATION.txt fantasy_miracle_FAVOR.txt fantasy_miracle_STRIFE.txt \
	fantasy_Rank2.txt fantasy_Rank3.txt fantasy_Rank4.txt fantasy_Rank5.txt \
	magic_guide_items.txt system_spells.txt

WORLD_INVOCATIONS = Invocations_Rank2.txt Invocations_Rank3.txt Invocations_Rank4.txt Invocations_Rank5.txt Invocations_Rank6.txt

spells : $(WORLD_SPELLS) $(WORLD_COPIED_SPELLS) $(WORLD_INVOCATIONS)

# Unique Spells -- note the name changes from Notebook to Module.
spells/fw_cantrips.txt : Cantrips\ Workbook.ipynb
	python -m opend6_tools.notebook_extract spells "$<" > $@

spells/fw_rank2.py : Rank2\ Workbook.ipynb
	python -m opend6_tools.notebook_extract spells "$<" > $@

spells/fw_rank3.py : Rank3\ Workbook.ipynb
	python -m opend6_tools.notebook_extract spells "$<" > $@

spells/fw_rank4.py : Rank4\ Workbook.ipynb
	python -m opend6_tools.notebook_extract spells "$<" > $@

spells/fw_rank5.py : Rank5\ Workbook.ipynb
	python -m opend6_tools.notebook_extract spells "$<" > $@

spells/fw_rank6.py : Rank6\ Workbook.ipynb
	python -m opend6_tools.notebook_extract spells "$<" > $@

spells/fw_rank8.py : Rank8\ Workbook.ipynb
	python -m opend6_tools.notebook_extract spells "$<" > $@

WORLD_MODULES = $(addsuffix .py,$(basename $(WORLD_SPELLS) $(WORLD_COPIED_SPELLS) $(WORLD_INVOCATIONS)))
test : $(WORLD_MODULES)
	for mod in $(WORLD_MODULES); do \
 		python $$mod test; \
 	done
