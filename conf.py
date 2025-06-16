# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example: sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Activate Peacock TV'
copyright = '2025, NBCUniversal'
author = 'Peacock TV Support Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings.
extensions = []

# Paths that contain templates, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files/directories to ignore.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Title shown in the browser tab and at the top of HTML pages
html_title = "Activate Peacock TV at peacocktv.com/tv – Complete Guide"

# Optional short title for navbar
html_short_title = "Peacock TV Activation"

# Custom favicon (place in root or _static)
html_favicon = 'favicon.ico'

# HTML theme (uncomment if needed)
# html_theme = 'sphinx_rtd_theme'

# Hide the “View page source” link
html_show_sourcelink = False

# Allow raw HTML blocks in reStructuredText files
html_allow_unsafe = True

# Theme customization options
html_theme_options = {
    'show_powered_by': False,
}

# Static path for custom styles, scripts, etc.
# html_static_path = ['_static']  # Uncomment if needed
