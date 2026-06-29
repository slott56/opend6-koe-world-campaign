#######################################
 OpenD6 Fantasy -- Kingdom of the East
#######################################

This is all the source material for the *Kingdom of the East* world.

- An OpenD6 Fantasy Worldbook for the *Kingdom of the East*.
- The "Bandit King" Campaign, set in the *Kingdom of the East*.

Additionally, as background, some additional material is available here in easy-to-edit text form.

- OpenD6 Fantasy Rulebook
- OpenD6 Fantasy: Locations
- OpenD6 Player's Guide
- OpenD6 GM Reference
- OpenD6 Magic Guidebook
- OpenD6 System Book (some selected snippets)

Additionally, some material has been duplicated from the OpenD6 Project web site.

Other useful material includes these two items, which are not (currently) extracted from the PDF sources.

- OpenD6 Fantasy: Creatures

Making Changes
===============

The entire suite of documents has been prepared using Python and the Sphinx tool.
See https://www.sphinx-doc.org/en/master/ for more on Sphinx.
See https://www.python.org for more on Python.

The "bookkeeping" aspect of the OpenD6 system is relatively small, but important.
This is a separate project, https://github.com/slott56/opend6-tools.
The tools helps with computations of difficulty, and confirming the budget of dice has been adhered to.
These also help with formatting the complicated spell and character summmaries for publication.

The workflow is this.

1.  Spells, characters, and monsters are defined in Jupyter Notebooks in a common ``notebooks`` directory.

2.  An individual book will have a ``characters`` and ``spells`` directory.
    It may also have ``items``, and ``creatures``.
    These directories each have a ``Makefile`` to do two things:

    a. Extract Python modules from the central notebooks, leaving a ``.py`` file in the local directory.

    b. Create a ``.txt`` file from the Python module with the character, spell, item, or creature file.

3.  The various book chapters use the ``.. include::`` directive to incorporate the details.
    For example, ``..  include:: characters/<whatever>.txt``.

4.  The top-level book ``Makefile`` runs a recursive **make** in the sub-directories for characters, spells, etc.
    This is done prior to running the **sphinx-build** step to assemble the final book.

In some cases, common material is in a ``shared`` directory.
The idea is to avoid copy-and-paste editing.
The core principle here is **DRY**, Don't Repeat Yourself.

A master ``Makefile`` rebuilds the document library of books.
This is a recursive make of each book.

Getting Started
===============

You must have two developer tools: **git** and **make**.

It helps to have the **uv** tool to work with Python. https://docs.astral.sh/uv/

1.  Use `uv python install` to install Python.

2.  Fork this repository and clone it to your local computer.

    ..  code-block:: bash

        git clone URL-FOR-THIS-PROJECT
        cd opend6

3.  Create a virtual environment and synchronize the needed tools libraries.

    ..  code-block:: bash

        uv venv
        uv sync

Each time you want to do some work, you'll need to activate the Python virtual environment:

..  code-block:: bash

    source .venv/bin/activate

For Windows with PowerShell, use this:

..  code-block:: bash

    .venv\Scripts\Activate.ps1

To update the document suite after making a change:

..  code-block:: bash

    make all

