sl29.games.maze
===============
Une implémentation d'un labyrinthe à des fins éducatives.

.. _readme-vue-d-ensemble:

📦 Vue d’ensemble
-----------------

L'objectif de ce projet est de :

- Créer un labyrinthe en utilisant le principe de diviser pour régner
- Utiliser les graphes
- Empaqueter correctement avec les conventions **PEP 621** (`pyproject.toml`)
- Écrire et exécuter des **tests unitaires** avec `pytest`
- Générer automatiquement de la **documentation** en utilisant `Sphinx`

.. _readme-installation:

🧩 Installation
---------------

Il est recommandé de travailler dans un **environnement virtuel** pour éviter les conflits de dépendances.

🔧 Créer et activer un environnement virtuel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sur Linux/Mac :

.. code-block:: bash

   python3 -m venv maze
   source maze/bin/activate

Sur Windows :

.. code-block:: bash

   python -m venv maze
   maze\Scripts\activate

Installer en mode développement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pour le développement, les tests et la documentation :

.. code-block:: bash

   pip install -e .[dev,test,doc]

Cela installera :

- Le package lui-même et ses dépendances;
- Les outils de développement (par exemple Jupyter, linters);
- Les dépendances de test (pytest, pytest-cov);
- Les outils de documentation (Sphinx, sphinx-rtd-theme, etc.).

Installation en production
~~~~~~~~~~~~~~~~~~~~~~~~~~

Pour installer le package comme un package Python standard :

.. code-block:: bash

   pip install -e .

ou construire et installer depuis une wheel :

.. code-block:: bash

   python -m build
   pip install dist/sl29.games.maze-*.whl

.. _readme-exemple-d-utilisation:

Exécuter les tests
------------------

Exécuter tous les tests :

.. code-block:: bash

   pytest

Exécuter les tests avec couverture :

.. code-block:: bash

   pytest --cov=sl29.games.maze

Générer un rapport de couverture HTML :

.. code-block:: bash

   pytest --cov=sl29.games.maze --cov-report=html

Le rapport HTML sera généré dans le répertoire `htmlcov/`. Ouvrez `htmlcov/index.html` dans votre navigateur web pour voir les détails de couverture.

.. _readme-construire-la-documentation:

Construire la documentation
---------------------------

La documentation est construite avec Sphinx et suppose que vous avez installé les dépendances optionnelles de doc.

Sur Linux/Mac :

.. code-block:: bash

   cd doc
   make html

Sur Windows :

.. code-block:: bash

   cd doc
   make.bat html

Ou alternativement sur tous les systèmes :

.. code-block:: bash

   sphinx-build doc _build/html

Les fichiers HTML générés seront dans `doc/_build/html/index.html`. Ouvrez ce fichier dans votre navigateur web pour voir la documentation.
