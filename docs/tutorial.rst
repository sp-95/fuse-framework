Tutorial
========

To start with, you will need a `GitHub account`_ and an account on `PyPI`_.
Create these before you get started on this tutorial. If you are new to Git and
GitHub, you should probably spend a few minutes on some of the tutorials at the
top of the page at `GitHub Help`_.

.. _`GitHub account`: https://github.com/
.. _`PyPI`: https://pypi.python.org/pypi
.. _`GitHub Help`: https://help.github.com/


Step 1: Install Cookiecutter
----------------------------

Install cookiecutter:

    .. code-block:: bash

        pip install --user cookiecutter


Step 2: Generate Your Package
-----------------------------

Now it's time to generate your Python package.

Use cookiecutter, pointing it at the fuse-standard repo:

    .. code-block:: bash

        cookiecutter https://github.com/sp-fm/fuse-standard.git

You'll be asked to enter a bunch of values to set the package up. If you don't
know what to enter, stick with the defaults.


Step 3: Setup Virtual Environment
---------------------------------

    .. code-block:: bash

        pip install --user poetry

If you want to install prerelease versions, you can do so by passing --pre
option.

    .. code-block:: bash

        pip install --user poetry --pre

Activate your environment:

    .. code-block:: bash

        cd mypackage
        poetry shell

Here, ``mypackage`` is the name of the package that you'll create.


Step 4: Create a GitHub Repo
----------------------------

Go to your GitHub account and create a new repo named ``mypackage``, where
``mypackage`` matches the ``[project_slug]`` from your answers to running
cookiecutter. This is so that Travis CI can find it when we get to Step 5.

You will find one folder named after the ``[project_slug]``. Move into this
folder, and then setup git to use your GitHub repo and upload the code:

    .. code-block:: bash

        git init .
        git add .
        git commit -m "Initial skeleton."
        git remote add origin git@github.com:myusername/mypackage.git
        git push -u origin master

Where ``myusername`` and ``mypackage`` are adjusted for your username and
package name.

You'll need an ssh key to push the repo. You can `Generate`_ a key or `Add`_ an
existing one.

.. _`Generate`: https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/
.. _`Add`: https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/


Step 5: Install Dev Requirements
--------------------------------

You should still be in the folder containing the ``pyproject.toml`` file.

Your virtualenv should still be activated. If it isn't, activate it now. Install
the new project's local development requirements:

    .. code-block:: bash

        poetry install


Step 6: Set Up Travis CI
------------------------

`Travis CI org`_ [*]_ is a continuous integration tool used to prevent
integration problems. Every commit to the master branch will trigger automated
builds of the application.

Log in using your Github credentials. It may take a few minutes for Travis CI to
load up a list of all your GitHub repos. They will be listed with boxes to the
left of the repo name, where the boxes have an ``X`` in them, meaning it is not
connected to Travis CI.

Add the public repo to your Travis CI account by clicking the ``X`` to switch it
"on" in the box next to the ``mypackage`` repo.

.. [*] For private projects go to `Travis CI com`_

.. _`Travis CI org`: https://travis-ci.org/
.. _`Travis CI com`: https://travis-ci.com/


Step 7: Set Up the Docs
--------------------------

`Sphinx`_ is a tool that makes it easy to create intelligent and beautiful
documentation.

Sphinx uses `reStructuredText`_ as its markup language and many of its
strengths come from the power and straightforwardness of reStructuredText and
its parsing and translating suite, the `Docutils`_.

We are making use of `Read the Docs Sphinx Theme`_. This Sphinx theme was
designed to provide a great reader experience for documentation users on both
desktop and mobile devices. This theme is used primarily on `Read the Docs`_ but
can work with any Sphinx project.

These have already been set up for you. You can generate the docs for your
project using the command:

    .. code-block:: bash

        make docs

`GitHub Pages`_ is a static site hosting service that takes HTML, CSS, and
JavaScript files straight from a repository on GitHub optionally runs the files
through a build process, and publishes a website.

You can host your site on GitHub's ``github.io`` domain or your custom
domain.

`GitHub Pages Deployment using Travis CI`_ has already been set up for you.

.. _Sphinx: https://www.sphinx-doc.org/en/master/
.. _reStructuredText: https://docutils.sourceforge.io/rst.html
.. _Docutils: https://docutils.sourceforge.io/
.. _Read the Docs Sphinx Theme: https://github.com/readthedocs/sphinx_rtd_theme
.. _Read the Docs: https://readthedocs.org/
.. _GitHub Pages: https://docs.github.com/en/github/working-with-github-pages/about-github-pages
.. _GitHub Pages Deployment using Travis CI: https://docs.travis-ci.com/user/deployment/pages/


Step 8: Release on PyPI
-----------------------

The Python Package Index or `PyPI`_ is the official third-party software
repository for the Python programming language. Python developers intend it to
be a comprehensive catalog of all open-source Python packages.

When you are ready, you can release your package using poetry.

See :ref:`pypi-setup` for more information.

Here's a release checklist you can use: :ref:`pypi-release-checklist`


Having problems?
----------------

Visit our :ref:`troubleshooting` page for help. If that doesn't help, go to our
`Issues`_ page and create a new Issue. Be sure to give as much information as
possible.

.. _`Issues`: https://github.com/sp-fm/fuse-standard/issues

.. note:: Did you find any of these instructions confusing? `Edit this file`_
          and submit a pull request with your improvements!

.. _`Edit this file`: https://github.com/sp-fm/fuse-standard/blob/master/docs/tutorial.rst
