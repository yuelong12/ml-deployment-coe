# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'ML Deployment COE'
copyright = '2022, Blend360'
author = 'Blned360.LLC'

release = '0.0'
version = '0.0.0'

"""
Imports the system and the 
theme the project is using to the project.
"""

import sys, os

"""
Adds path to the folder ext, where extensions are stored.
"""

sys.path.append(os.path.abspath('ext'))
sys.path.append('.')


# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
