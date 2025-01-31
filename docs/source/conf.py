import os
import sys
import sphinx_rtd_theme

# Ensure Sphinx can find your package
sys.path.insert(0, os.path.abspath('../../'))
for path in sys.path:
    print(path)

# Project information
project = 'sofascore_wrapper'
copyright = '2025, tommhe14'
author = 'tommhe14'
release = '1.0.0'

# Enable necessary extensions
extensions = [
    'sphinx.ext.autodoc',  # Enable autodoc
    'sphinx.ext.viewcode',  # Optional: Add links to source code
    'sphinx.ext.napoleon',  # Optional: For Google-style or NumPy-style docstrings
]

# Tell Sphinx to document imported members
autodoc_default_options = {
    'members': True,          # Include all functions and methods
    'undoc-members': True,    # Include even those without docstrings
    'show-inheritance': True,
}

# If your module has type hints, this will include them
autodoc_typehints = "description"
html_css_files = [
    'css/alabaster.css',  # or your preferred CSS file
    'css/basic.css'
]

html_theme = 'sphinx_rtd_theme'  # Or 'sphinx_rtd_theme' for ReadTheDocs theme
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']
