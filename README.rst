=====================
FuseMachines Standard
=====================

.. image:: https://travis-ci.com/sp-fm/fuse-standard.svg?branch=fuse
    :target: https://travis-ci.com/github/sp-fm/fuse-standard
    :alt: Travis CI Build Status

Cookiecutter_ template for a standard FuseMachines Python package.

* GitHub repo: https://github.com/sp-fm/fuse-standard
* Documentation: https://sp-fm.github.io/fuse-standard/
* Free software: BSD license

Features
--------

* Testing setup with ``pytest``
* Travis-CI_: Ready for Travis Continuous Integration testing
* Tox_ testing: Setup to easily test for Python 3.7, 3.8
* Sphinx_ docs: Documentation ready for generation with, for example, `Read the Docs`_
* Command line interface using Click
* Auto-release to PyPI_ when you push a new tag to master (optional)
* Dependency tracking using poetry_
* Linting provided by flake8_ [executed by Tox]
* Git hooks by pre_commit_hooks_

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher):

.. code-block:: console

    $ pip install -U cookiecutter

Generate a Python package project:

.. code-block:: console

    $ cookiecutter https://github.com/sp-fm/fuse-standard.git

Then:

* Create a repo and put it there.
* Add the repo to your Travis-CI_ account.
* Install the dev requirements into a virtualenv. (``poetry install``)
* Release your package by pushing a new tag to master.

For more details, see the `fuse-standard tutorial`_.

Acknowledgement
---------------

This package is a modified duplicate of the `audreyr/cookiecutter-pypackage`_
project template

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter
.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _Read the Docs: https://readthedocs.io/
.. _PyPi: https://pypi.python.org/pypi
.. _poetry: https://python-poetry.org/docs/
.. _flake8: https://pypi.org/project/flake8/
.. _pre_commit_hooks: https://github.com/pre-commit/pre-commit-hooks
.. _`fuse-standard tutorial`: https://sp-fm.github.io/fuse-standard/tutorial.html
.. _audreyr/cookiecutter-pypackage: https://github.com/audreyfeldroy/cookiecutter-pypackage
