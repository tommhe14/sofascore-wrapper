# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

src = r'c:\Users\theck\Documents\GitHub\sofascore-wrapper\sofascore_wrapper'
if src not in sys.path:
    sys.path.append(src)

for path in sys.path:
    print(path)

project = 'SofaScore Wrapper'
copyright = '2025, tommhe14 (mane)'
author = 'tommhe14 (mane)'
release = '1.0.4'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',  # Enable autodoc
    'sphinx.ext.viewcode',  # Optional: Add links to source code
    'sphinx.ext.napoleon',  # Optional: For Google-style or NumPy-style docstrings
]
todo_include_todos = True

autodoc_default_options = {
    'members': True,          # Include all functions and methods
    'undoc-members': True,    # Include even those without docstrings
    'show-inheritance': True,
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

autodoc_typehints = "description"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
