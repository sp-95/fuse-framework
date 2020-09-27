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

* Dependency tracking using poetry_
* Logging with loguru_
* Command-line interface using fire_
* dynaconf_ for Configuration Management
* Git hooks by pre_commit_hooks_
* Testing setup with ``pytest``
* Linting provided by flake8_ [executed by Tox]
* Sphinx_ docs: Documentation ready for generation with, for example, `Read the Docs`_
* Tox_ testing: Setup to easily test for Python 3.7 and 3.8
* Travis-CI_: Ready for Travis Continuous Integration testing
* Auto-release to PyPI_ when you push a new tag to master (optional)
* GitHub issue templates

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
* Add the repo to your Travis-CI_ account.
* Generate the docs by pushing your first commit to master.
* Release your package by pushing a new tag to master.

For more details, see the `fuse-framework tutorial`_.

Acknowledgment
---------------

This package is a modified duplicate of the `audreyr/cookiecutter-pypackage`_
project template

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter
.. _poetry: https://python-poetry.org/docs/
.. _loguru: https://loguru.readthedocs.io/en/stable/
.. _fire: https://google.github.io/python-fire/guide/
.. _dynaconf: https://www.dynaconf.com/
.. _pre_commit_hooks: https://github.com/pre-commit/pre-commit-hooks
.. _flake8: https://pypi.org/project/flake8/
.. _Sphinx: http://sphinx-doc.org/
.. _Read the Docs: https://readthedocs.io/
.. _Tox: http://testrun.org/tox/
.. _Travis-CI: http://travis-ci.org/
.. _PyPi: https://pypi.python.org/pypi
.. _`fuse-framework tutorial`: https://sp-fm.github.io/fuse-framework/tutorial.html
.. _audreyr/cookiecutter-pypackage: https://github.com/audreyfeldroy/cookiecutter-pypackage
