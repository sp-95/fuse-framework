.. _pypi-setup:

PyPI Setup
=================

Optionally, your package can automatically be released on PyPI whenever you
push a new tag to the master branch.

Configuring PyPi Credentials
----------------------------

To publish to PyPI, you can set your credentials for the repository named pypi.

Note that it is recommended to use API tokens when uploading packages to PyPI. Once you
have created a new token, you can tell Poetry to use it:

.. code-block:: console

    $ poetry config pypi-token.pypi my-token

If you still want to use your username and password, you can do so with the following
call to config.

.. code-block:: console

    $ poetry config http-basic.pypi username password

Packaging
---------

Before you can publish your library, you will need to package it.

.. code-block:: console

    $ poetry build

This command will package your library in two different formats: sdist which is the
source format, and wheel which is a compiled package.

Once that's done you are ready to publish your library

Publishing to PyPI
------------------

Alright, so now you can publish packages.

Poetry will publish to PyPI by default. Anything that is published to PyPI is available
automatically through Poetry.

If we wanted to share a package with the Python community, we would publish on PyPI as
well. Doing so is easy.

.. code-block:: console

    $ poetry publish

This will package and publish the library to PyPI, at the condition that you are a
registered user and you have configured your credentials properly.

The publish command does not execute build by default.

If you want to build and publish your packages together, just pass the --build option.

.. code-block:: console

    $ poetry publish --build

Once this is done, your library will be available to anyone.

GitHub Actions Setup
--------------------

Github Actions can automatically release your Python package to PyPI after a successful
build.

For a minimal configuration, generate a PyPI API token and add it to the Secrets tab in
your project settings in GitHub.

.. code-block:: YAML

    name: Release

    jobs:
        deploy:
            runs-on: ubuntu-latest

            steps:
                - uses: actions/checkout@v2

                - name: Set up Python
                  uses: actions/setup-python@v2
                  with:
                      python-version: "3.x"

                - name: Install and set up Poetry
                  run: |
                      python -m pip install --upgrade pip
                      pip install --upgrade poetry --pre
                      poetry config virtualenvs.in-project true

                - name: Install dependencies
                  run: poetry install

                - name: Build and publish
                  env:
                      PYPI_TOKEN: ${{ secrets.PYPI_TOKEN }}
                  run: |
                      poetry config pypi-token.pypi $PYPI_TOKEN
                      poetry publish --build

It is also possible, but not recommended, to use PyPI user and password, instead of a
token.

Deploying tags
--------------

Most likely, you would only want to deploy to PyPI when a new version of your package is
cut. To do this, you can tell GitHub Actions to only deploy on tagged commits, like so:

.. code-block:: YAML

    on:
        release:
            types: [created]

If you tag a commit locally, remember to run ``git push --tags`` to ensure that your
tags are uploaded to GitHub.

Your Release Process
--------------------

If you are using this feature, this is how you would do a patch release:

.. code-block:: console

    $ poetry version patch
    $ git tag `poetry version -s`
    $ git push --tags

This will result in:

* mypackage 0.1.1 showing up in your GitHub tags/releases page
* mypackage 0.1.1 getting released on PyPI

You can also replace the patch with `minor` or `major`.

References
------------

* `Configuring PyPi Credentials`_
* `Publishing to PyPi`_
* `Building Python packages with GitHub Actions`_
* `Poetry GitHub Actions workflow`_

.. _Configuring PyPi Credentials: https://python-poetry.org/docs/repositories/
.. _Publishing to PyPi: https://python-poetry.org/docs/libraries/
.. _Building Python packages with GitHub Actions: https://docs.github.com/en/free-pro-team@latest/actions/guides/building-and-testing-python
.. _Poetry GitHub Actions workflow: https://github.com/python-poetry/poetry/actions/runs/30094511/workflow
