# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'OpenD6 Fantasy Locations'
copyright = "2005, Purgatory Publishing, Inc."
author = "WestEndGames"
release = '1.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.todo",
]

templates_path = ['_templates']
exclude_patterns = [
    '_build', 'Thumbs.db', '.DS_Store',
    'D6_Fantasy_Locations_v1.1_weg51020OGL.rst',
    "LICENSE*",
    "make.bat",
    "Makefile",
    "conf.py",
    "un.lock",
    "pyproject.toml",
    "*.tex",
    "*.ods",
    ".venv",
]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]

html_sidebars = {
    "**": [
        "about.html",
        "searchfield.html",
        "navigation.html",
        "relations.html",
    ]
}

html_theme_options = {
    "show_related": True,
    "extra_nav_links": {"Home": "../../../home_page/index.html"},
}
