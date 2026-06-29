# Characters and Creatures Makefile
.PHONY: characters

vpath %.ipynb ../../notebooks

# Create a Python Character or Creature module from a Jupyter Notebook with the same name.
%.py : %.ipynb
	python -m opend6_tools.notebook_extract characters $< > $@

# Create an RST text file from a Python Character or Creature module with the same name.
%.txt : %.py
	# pytest --doctest-modules $<
	python $< test
	python $< display --format SHORT > $@

CASTLES = aaroth.txt kinzo_mimoto.txt labor.txt lord_urdane.txt miroko_yhukiini.txt sir_warrock.txt taszor_the_wise.txt thufer.txt wrekyon_the_strong.txt

OTHER = fang.txt giant_eel.txt master_ota.txt miner.txt minotaur.txt monks.txt precursor.txt shadohowl.txt summer_blossom.txt temple_clerics.txt variana.txt

SETTLEMENTS = acolyte.txt ascara.txt balam_mis.txt bede_trowbryde.txt betha_etain.txt cachamwri_cabry.txt cernay_avers.txt cire.txt \
	dock_worker.txt fane.txt garvin_helot.txt gladiator.txt guild_member.txt healfdene.txt jirair_shan.txt jurin_coram.txt kasen.txt \
	ladira_almer.txt library_guard.txt lighthouse_guard.txt mayan_priest.txt morcades.txt mukhtar.txt namo.txt nevest.txt ori_swifthand.txt \
	philosopher.txt phylo_duran.txt sofronius.txt tiu_mali.txt viking_warrior.txt

FANTASY_LOCATION_CHARACTERS = $(CASTLES) $(OTHER) $(SETTLEMENTS)

characters : $(FANTASY_LOCATION_CHARACTERS)
