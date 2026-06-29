# Creates the OpenD6 Fantasy Worldbook: Kingdom of the East, and
# all of the OpenD6 books with supporting details.

# Requires the https://github.com/slott56/opend6-tools project is installed.
# When the two projects are adjacent, the following will install from a sibling directory.
# uv add ../opend6-tools --active --upgrade
# More usefully, it can be installed from GitHub with
# uv add git+https://github.com/slott56/opend6-tools --upgrade

# The collection of HTML-based books and book-like material created by Sphinx.
BOOKS = world_book campaign_book_1 \
        fantasy_locations fantasy_rulebook magic_guide system_book \
        home_page gm_ref player_guide
# Other play-aids not created by Sphinx.
AIDS = forms

.PHONY: help all $(BOOKS) $(AIDS)
PWD = $(shell pwd)

help :
	@echo all test "$(BOOKS)" "$(AIDS)"

# All HTML sites in a single target
book_sites = $(addsuffix /_build/index.html,$(BOOKS))
all: $(book_sites) forms/char_sheet.pdf

# Some shared tables and forms...
# Not part of the $(all) list
shared/die_code.csv :
	python -m opend6_tools.die_simplification > $@

shared/spell_measure.csv :
	python -m opend6_tools.spell_measure > $@

shared/blank_character.txt :
	# pytest --doctest-modules $<
	python $< test
	python $< > $@

SHARED = $(wildcard shared/*)

# The centerpiece: the Kingdom of the East Worldbook.
world_book : world_book/_build/index.html
world_book/_build/index.html :
	@echo world_book
	$(MAKE) -C world_book html

# The centerpiece: The Bandit King Campaign.
campaign_book_1 : campaign_book_1/_build/index.html
campaign_book_1/_build/index.html :
	@echo campaign_book_1
	$(MAKE) -C campaign_book_1 html

# The Home Page document
home_page : home_page/_build/index.html
home_page/_build/index.html :
	@echo home_page
	$(MAKE) -C home_page html

# The Gamemaster's Reference document
gm_ref : gm_ref/_build/index.html
gm_ref/_build/index.html :
	@echo gm_ref
	$(MAKE) -C gm_ref html

# The Player's Guide document
player_guide : player_guide/_build/index.html
player_guide/_build/index.html :
	@echo player_guide
	$(MAKE) -C player_guide html

# The LaTeX-based paper forms.
forms : forms/char_sheet.pdf
forms/char_sheet.pdf : forms/char_sheet.tex forms/fastasy_character.tex
	@echo forms
	cd forms && pdflatex char_sheet.tex

# Books from West-End Games, reproduced here.

system_book : system_book/_build/index.html
system_book/_build/index.html :
	@echo system_book
	$(MAKE) -C system_book html

fantasy_rulebook : fantasy_rulebook/_build/index.html
fantasy_rulebook/_build/index.html :
	@echo fantasy_rulebook
	$(MAKE) -C fantasy_rulebook html

fantasy_locations : fantasy_locations/_build/index.html
fantasy_locations/_build/index.html :
	@echo fantasy_locations
	$(MAKE) -C fantasy_locations html

magic_guide : magic_guide/_build/index.html
magic_guide/_build/index.html :
	@echo magic_guide
	$(MAKE) -C magic_guide html

# Other targets

.PHONY : test_spells test_characters doctest

# Do the spells all execute properly?
ALL_SPELLS = $(foreach b,$(BOOKS),$(wildcard $(b)/spells/*.py))
test_spells : $(ALL_SPELLS)
	set -e; for mod in $(ALL_SPELLS); do python $${mod} debug '*' > /dev/null; done

# Do the characters all execute properly?
ALL_CHARACTERS = $(foreach b,$(BOOKS),$(wildcard $(b)/characters/*.py))
test_characters : $(ALL_CHARACTERS)
	set -e; for mod in $(ALL_CHARACTERS); do python $${mod} debug '*' > /dev/null; done

# Do the spells (and characters) pass the doctest examples (if any)?
# Not all modules have doctest examples.
doctest :
	set -e; for mod in $(ALL_CHARACTERS) $(ALL_SPELLS); do python $${mod} test; done
