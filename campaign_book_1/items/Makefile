# Items Makefile
.PHONY: items test

vpath %.ipynb ../notebooks

# Create a Python Items module from a Jupyter Notebook with the same name.
%.py : %.ipynb
	python -m opend6_tools.notebook_extract spells --book-variable items $< > $@

# Special cases for swords
keep_lodge_swords.py : keep_lodge_swords.ipynb
	python -m opend6_tools.notebook_extract characters --book-variable swords $< > $@

new_keep_swords.py : new_keep_swords.ipynb
	python -m opend6_tools.notebook_extract characters --book-variable swords $< > $@

eagles_swords.py : eagles_swords.ipynb
	python -m opend6_tools.notebook_extract characters --book-variable swords $< > $@

# Create an RST text file from a Python Spell module with the same name.
%.txt : %.py
	# pytest --doctest-modules $<
	python $< test
	python $< display > $@

# Special cases for swords
keep_lodge_swords.txt : keep_lodge_swords.py
	python $< display --format SHORT > $@

new_keep_swords.txt : new_keep_swords.py
	python $< display --format SHORT > $@

eagles_swords.txt : eagles_swords.py
	python $< display --format SHORT > $@

WORLD_ITEMS = keep_lodge_items.txt keep_lodge_swords.txt \
	new_keep_items.txt new_keep_swords.txt \
	old_keep_items.txt \
	eagles_swords.txt white_water_lightning_rod.txt

items : $(WORLD_ITEMS)


WORLD_MODULES = $(addsuffix .py,$(basename $(WORLD_ITEMS)))
test : $(WORLD_MODULES)
	for mod in $(WORLD_MODULES); do \
 		python $$mod test; \
 	done

.PRECIOUS : %.py
