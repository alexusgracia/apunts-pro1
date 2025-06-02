import os
import sys

# Añadir raíz del proyecto al path
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
project = 'Apunts PRO1'
copyright = '2025, Alexandre Gràcia'
author = 'Alexandre Gràcia'
release = '1.0'

# -- General configuration ---------------------------------------------------
extensions = ['myst_parser']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

master_doc = 'index'
exclude_patterns = []

# -- HTML output -------------------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
