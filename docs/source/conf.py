import os
import sys

# Ensure Sphinx can find your package
sys.path.insert(0, os.path.abspath('../../'))

# Project information
project = 'sofascore_wrapper'
copyright = '2025, tommhe14'
author = 'tommhe14'
release = '1.0.0'

# Enable necessary extensions
extensions = [
    'sphinx.ext.autodoc',   # Extracts docstrings from your code
    'sphinx.ext.napoleon',  # Supports Google and NumPy-style docstrings
]

# Tell Sphinx to document imported members
autodoc_default_options = {
    'members': True,          # Include all functions and methods
    'undoc-members': True,    # Include even those without docstrings
    'show-inheritance': True,
}

# If your module has type hints, this will include them
autodoc_typehints = "description"

html_theme = 'sphinx_rtd_theme'  # Or 'sphinx_rtd_theme' for ReadTheDocs theme
html_static_path = ['_static']  # Ensure this folder exists