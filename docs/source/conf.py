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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import warnings
from sphinx_gallery.sorting import FileNameSortKey


# -- Project information -----------------------------------------------------

project = 'pyrtlib'
copyright = '2021, CNR-IMAA'
author = 'Salvatore Larosa'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    # 'sphinx.ext.doctest',
    # 'sphinx_toggleprompt',
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
    'nbsphinx',
    'sphinx_gallery.gen_gallery',
    # 'rst2pdf.pdfbuilder',
]

# pdf_documents = [('index', u'rst2pdf', project + u'Documentation', u'Salvatore Larosa'),]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_logo = "../../resources/logo/logo_white_large.png"
html_theme_options = {
    'logo_only': False,
    'display_version': True,
}

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

autosummary_generate = True

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'pyrtlib', 'pyrtlib Documentation',
     ['Andrew Collette and contributors'], 1)
]

# If true, show URL addresses after external links.
# man_show_urls = False

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index', 'pyrtlib.tex', 'pyrtlib Documentation',
     'Salvatore Larosa and contributors', 'manual'),
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'pyrtlib', 'pyrtlib Documentation',
     'Salvatore Larosa and contributors', 'pyrtlib', 'One line description of project.',
     'Miscellaneous'),
]

# # == Disable search functionality for html
# def on_builder_inited(app):
#     if app.builder.name == 'html':
#         app.builder.search = False

# # Register custom CSS files.
# def setup(app):
#    app.add_css_file("custom.css")
#    # == disable search functionality for html
#    app.connect('builder-inited', on_builder_inited)

# suppress "WARNING: Footnote [1] is not referenced." messages
# https://github.com/pvlib/pvlib-python/issues/837
suppress_warnings = ['ref.footnote']

# settings for sphinx-gallery
sphinx_gallery_conf = {
    'examples_dirs': ['../examples'],  # location of gallery scripts
    'gallery_dirs': ['auto_examples'],  # location of generated output
    # sphinx-gallery only shows plots from plot_*.py files by default:
    # 'filename_pattern': '*.py',
    'within_subsection_order': FileNameSortKey,

    # directory where function/class granular galleries are stored
    'backreferences_dir': 'generated/gallery_backreferences',

    # Modules for which function/class level galleries are created. In
    # this case only pyrtlib, could include others though.  must be tuple of str
    'doc_module': ('pyrtlib','numpy'),
}
# supress warnings in gallery output
# https://sphinx-gallery.github.io/stable/configuration.html
warnings.filterwarnings("ignore", category=UserWarning,
                        message='Matplotlib is currently using agg, which is a'
                                ' non-GUI backend, so cannot show the figure.')

import os
import sys

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme

    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
else:
    html_theme = 'default'

# add sourcecode to path
sys.path.insert(0, os.path.abspath('../../'))

############################
# SETUP THE RTD LOWER-LEFT #
############################

# The master toctree document.
master_doc = 'index'

try:
    html_context
except NameError:
    html_context = dict()
html_context['display_lower_left'] = True

if 'REPO_NAME' in os.environ:
    REPO_NAME = os.environ['REPO_NAME']
else:
    REPO_NAME = ''

# SET CURRENT_LANGUAGE
if 'current_language' in os.environ:
    # get the current_language env var set by buildDocs.sh
    current_language = os.environ['current_language']
else:
    # the user is probably doing `make html`
    # set this build's current language to english
    current_language = 'en'

# tell the theme which language to we're currently building
html_context['current_language'] = 'en'

# SET CURRENT_VERSION
from git import Repo

repo = Repo(search_parent_directories=True)

if 'current_version' in os.environ:
    # get the current_version env var set by buildDocs.sh
    current_version = os.environ['current_version']
else:
    # the user is probably doing `make html`
    # set this build's current version by looking at the branch
    current_version = repo.active_branch.name

# tell the theme which version we're currently on ('current_version' affects
# the lower-left rtd menu and 'version' affects the logo-area version)
html_context['current_version'] = current_version
html_context['version'] = current_version

# POPULATE LINKS TO OTHER LANGUAGES
html_context['languages'] = [('en', '/' + REPO_NAME + '/en/' + current_version + '/')]

# languages = [lang.name for lang in os.scandir('locales') if lang.is_dir()]
# for lang in languages:
#    html_context['languages'].append( (lang, '/' +REPO_NAME+ '/' +lang+ '/' +current_version+ '/') )

# POPULATE LINKS TO OTHER VERSIONS
html_context['versions'] = list()

versions = [branch.name for branch in repo.branches]
for version in versions:
    if version != 'gh-pages':
        html_context['versions'].append((version, '/' + REPO_NAME + '/' + current_language + '/' + version + '/'))

# settings for creating PDF with rinoh
# rinoh_documents = [(
#  master_doc,
#  'target',
#  project+ ' Documentation',
#  '© ' +copyright,
# )]
# today_fmt = "%B %d, %Y"

# settings for EPUB
epub_basename = project

html_context['downloads'] = list()
html_context['downloads'].append(('pdf',
                                  '/' + REPO_NAME + '/' + current_language + '/' + current_version + '/' + project + '-docs_' + current_language + '_' + current_version + '.pdf'))

html_context['downloads'].append(('epub',
                                  '/' + REPO_NAME + '/' + current_language + '/' + current_version + '/' + project + '-docs_' + current_language + '_' + current_version + '.epub'))

html_context['display_github'] = True
html_context['github_user'] = 'slarosa'
html_context['github_repo'] = 'pyrtlib'
html_context['github_version'] = 'main/docs/'

# Napoleon stuff
#
napoleon_use_admonition_for_examples = True
napoleon_google_docstring = True
# napoleon_use_rtype = False  # group rtype on same line together with return

# todo extension
todo_include_todos = True

# def make_github_url(pagename):
#     """
#     Generate the appropriate GH link for a given docs page.  This function
#     is intended for use in sphinx template files.
#     The target URL is built differently based on the type of page.  Sphinx
#     provides templates with a built-in `pagename` variable that is the path
#     at the end of the URL, without the extension.  For instance,
#     https://pvlib-python.rtfd.org/en/stable/auto_examples/plot_singlediode.html
#     will have pagename = "auto_examples/plot_singlediode".
#     """

#     URL_BASE = "https://github.com/pyrtlib/pyrtlib/blob/main/"

#     # is it a gallery page?
#     if any(d in pagename for d in sphinx_gallery_conf['gallery_dirs']):
#         if pagename.split("/")[-1] == "index":
#             example_file = "README.rst"
#         else:
#             example_file = pagename.split("/")[-1] + ".py"
#         target_url = URL_BASE + "docs/examples/" + example_file

#     # is it an API autogen page?
#     elif "generated" in pagename:
#         # pagename looks like "generated/pvlib.location.Location"
#         qualname = pagename.split("/")[-1]
#         obj, module = get_obj_module(qualname)
#         path = module.__name__.replace(".", "/") + ".py"
#         target_url = URL_BASE + path
#         # add line numbers if possible:
#         start, end = get_linenos(obj)
#         if start and end:
#             target_url += f'#L{start}-L{end}'

#     # Just a normal source RST page
#     else:
#         target_url = URL_BASE + "docs/sphinx/source/" + pagename + ".rst"

#     return target_url


# # variables to pass into the HTML templating engine; these are accessible from
# # _templates/breadcrumbs.html
# html_context = {
#     'make_github_url': make_github_url,
# }
html_last_updated_fmt = '%d/%m/%Y'

# configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/{.major}'.format(sys.version_info), None),
    'matplotlib': ('https://matplotlib.org/', None),
    'pandas': ('http://pandas.pydata.org/pandas-docs/stable/', None),
    'numpy': ('http://docs.scipy.org/doc/numpy', None),
}

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'default'
highlight_language = 'python3'