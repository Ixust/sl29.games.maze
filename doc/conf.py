# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
from pathlib import Path
import toml  # Utilisez `tomllib` si vous êtes en Python 3.11+

# -- Chemins et configuration ------------------------------------------------

# Chemin vers le répertoire racine du projet (remonte de deux niveaux)
project_root = Path(__file__).resolve().parent.parent

# Ajoute le chemin du projet pour importer les modules
sys.path.insert(0, str(project_root / "src"))

# -- Lecture des informations depuis pyproject.toml -------------------------

# Chemin vers le fichier pyproject.toml
pyproject_path = project_root / "pyproject.toml"

# Charge le fichier pyproject.toml
with open(pyproject_path, "r", encoding="utf-8") as f:
    pyproject_data = toml.load(f)

# Extrait les informations du projet
project_info = pyproject_data["project"]



# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = project_info["name"]
author = project_info["authors"][0]["name"]
copyright = f"2025, {author}"
release = project_info["version"]


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # Génère la documentation à partir des docstrings
    "sphinx.ext.viewcode",  # Ajoute des liens vers le code source
    "sphinx_rtd_theme",  # Active le thème ReadTheDocs
    "sphinx_autodoc_typehints",  # Support des annotations de type
    'sphinx.ext.napoleon',      # Pour prendre en charge les docstrings au format Google ou NumPy
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"  # Utilise le thème ReadTheDocs
html_static_path = ['_static']

source_suffix = '.rst'
