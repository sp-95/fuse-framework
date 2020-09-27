.. _console-script-setup:


Console Script Setup
====================

Your package includes a console script using ``fire``.

How It Works
------------

Cookiecutter will add a file 'cli.py' in the module ``dynaconf`` in the project_slug
subdirectory. An entry point is added to pyproject.toml that points to the main function
in 'cli.py'.

Usage
------------
To use the console script in development:

.. code-block:: console

    $ poetry install

'projectdir' should be the top level project directory with the pyproject.toml file

The script will be generated with output for no arguments and --help.

--help
    show help menu and exit

More Details
------------

You can read more about fire at:
https://google.github.io/python-fire/
