=============================
Fusemachines Python Framework
=============================

.. image:: https://travis-ci.com/sp-fm/fuse-framework.svg?branch=fuse
    :target: https://travis-ci.com/github/sp-fm/fuse-framework
    :alt: Travis CI Build Status

Cookiecutter_ template for Fusemachines Python Framework.

* GitHub repo: https://github.com/sp-fm/fuse-framework
* Documentation: https://sp-fm.github.io/fuse-framework/
* Free software: BSD license

Features
--------

* `Editor Config`_: Maintains Code Consistency
* poetry_: Dependency Management
* loguru_: Logging
* fire_: Command-line Interface
* dynaconf_: Configuration Management
* pre_commit_hooks_: Git hooks
* pytest_ and coverage_: Python Testing and Code Coverage
* black_ and flake8_: Linting
* mypy_: Type Hinting
* Sphinx_: Generates documents automatically
* Tox_: Automated and Standardized testing
* GitHub issue templates
* `Travis CI`_: Continuous Integration
* `GitHub Pages`_: Documentation Hosting
* PyPi_: Auto-release when you push a new tag to master (optional)

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher):

.. code-block:: console

    $ pip install -U cookiecutter

Install the prerelease version of poetry

.. code-block:: console

    $ pip install -U poetry --pre

Generate a Python package project:

.. code-block:: console

    $ cookiecutter https://github.com/sp-fm/fuse-framework.git

Go to the generated project and run the initialization process:

.. code-block:: console

    $ cd mypackage
    $ make init

where ``mypackage`` is the name of the project that was generated.

Then:

* Create a repo and put it there.
* Add the repo to your `Travis CI`_ account.
* Generate the docs by pushing your first commit to master.
* Release your package by pushing a new tag to master.

For more details, see the `fuse-framework tutorial`_.

Acknowledgment
---------------

This package is a modified duplicate of the `audreyr/cookiecutter-pypackage`_
project template

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter
.. _Editor Config: https://editorconfig.org/
.. _poetry: https://python-poetry.org/docs/
.. _loguru: https://loguru.readthedocs.io/en/stable/
.. _fire: https://google.github.io/python-fire/guide/
.. _dynaconf: https://www.dynaconf.com/
.. _pre_commit_hooks: https://github.com/pre-commit/pre-commit-hooks
.. _pytest: https://docs.pytest.org/en/stable/
.. _coverage: https://coverage.readthedocs.io/en/coverage-5.3/
.. _black: https://black.readthedocs.io/en/stable/
.. _flake8: https://pypi.org/project/flake8/
.. _mypy: http://mypy-lang.org/
.. _Sphinx: http://sphinx-doc.org/
.. _Tox: http://testrun.org/tox/
.. _Travis CI: http://travis-ci.org/
.. _GitHub Pages: https://docs.github.com/en/free-pro-team@latest/github/working-with-github-pages
.. _PyPi: https://pypi.python.org/pypi
.. _`fuse-framework tutorial`: https://sp-fm.github.io/fuse-framework/tutorial.html
.. _audreyr/cookiecutter-pypackage: https://github.com/audreyfeldroy/cookiecutter-pypackage
