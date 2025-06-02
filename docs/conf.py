# Configuration file for the Sphinx documentation builder.

import os
import sys

# Incluye la raíz del proyecto (donde están los .md)
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
project = 'Apunts PRO1'
copyright = '2025, Alexandre Gràcia'
author = 'Alexandre Gràcia'
release = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_parser',
]

# Permitir archivos Markdown
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Usa index.md como punto de entrada
master_doc = 'index'

exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
