# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "OpenD6 Magic Guide"
copyright = "2004, Purgatory Publishing, Inc."
author = "WestEndGames"
release = "1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.intersphinx",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store",
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

# -- Options for intersphinx ------

intersphinx_mapping = {
    "system": (
        "../../../system_book/_build/html/",
        ("../system_book/_build/html/objects.inv", None),
    ),
    "fantasy_rulebook": (
        "../../../fantasy_rulebook/_build/html/",
        ("../fantasy_rulebook/_build/html/objects.inv", None),
    ),
    "magic_guide": (
        "../../../magic_guide/_build/html/",
        ("../magic_guide/_build/html/objects.inv", None),
    ),
}
