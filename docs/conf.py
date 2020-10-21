# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join('.','..', '../docs', '../src/examples')))
#sys.path.insert(0, os.path.abspath('.'))
#sys.path.append(os.path.abspath('exts'))


# -- Project information -----------------------------------------------------

project = 'AWS Neuron'
copyright = '2020, Amazon Web Services'
author = 'Maen Suleiman'
master_doc = 'index'

# The full version, including alpha/beta/rc tags
release = '1.8.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinxcontrib.contentui','nbsphinx']

#extensions = ['sphinxcontrib.contentui','ipykernel','nbsphinx']
#extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon','nbsphinx','recommonmark']
#extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon','sphinxcontrib.contentui','nbsphinx']
#extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon','nbsphinx','sphinx.ext.autosectionlabel','recommonmark']
#extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']
#extensions = [ ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
#exclude_patterns = []
exclude_patterns = ['_build', '**.ipynb_checkpoints',
                    'neuron-guide/pytorch-neuron/tutorials/*.ipynb',
                    'neuron-guide/pytorch-neuron/tutorials/bert_tutorial/*.ipynb']

html_logo = 'images/Site-Merch_Neuron-ML-SDK_Editorial.jpg'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

