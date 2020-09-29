Tutorial
========

To start with, you will need a `GitHub account`_ and an account on `PyPI`_ (optional).
Create these before you get started on this tutorial. If you are new to Git and
GitHub, you should probably spend a few minutes on some of the tutorials at the
top of the page at `GitHub Help`_.

.. _GitHub account: https://github.com/
.. _PyPI: https://pypi.python.org/pypi
.. _GitHub Help: https://help.github.com/


Step 1: Install Cookiecutter
----------------------------

Install cookiecutter.

.. code-block:: console

    $ pip install --user cookiecutter


Step 2: Generate Your Package
-----------------------------

Now it's time to generate your Python package.

Use cookiecutter, pointing it at the fuse-framework repo.

.. code-block:: console

    $ cookiecutter https://github.com/sp-fm/fuse-framework.git

You'll be asked to enter a bunch of values to set the package up. If you don't
know what to enter, stick with the defaults.


Step 3: Setup Virtual Environment
---------------------------------

.. code-block:: console

    $ pip install -U poetry

If you want to install prerelease versions, you can do so by passing --pre
option.

.. code-block:: console

    $ pip install -U poetry --pre

Activate your environment.

.. code-block:: console

    $ cd mypackage
    $ poetry shell

Here, ``mypackage`` is the name of the package that you'll create.


Step 4: Install Dev Requirements
--------------------------------

You should still be in the folder containing the ``pyproject.toml`` file.

Your virtualenv should still be activated. If it isn't, activate it now. Install
the new project's local development requirements.

.. code-block:: console

    $ poetry install


Step 5: Initialize Git
----------------------

Create an empty Git repository.

.. code-block:: console

    $ git init


Step 6: Pre-commit Installation
-------------------------------

Git hook scripts are useful for identifying simple issues before submission to
code review. We run our hooks on every commit to automatically point out issues
in code such as trailing whitespace, and debug statements. By pointing these
issues out before code review, this allows a code reviewer to focus on the
architecture of a change while not wasting time with trivial style nitpicks.

Before you can run hooks, you need to have the pre-commit_ package manager
installed.

Install pre-commit if it is not present in the dependencies.

.. code-block:: console

    $ poetry add pre-commit --dev
    $ pre-commit --version

You can change your pre-commit configurations in the ``.pre-commit-config.yaml``
file. This is the list of `hooks supported`_ by pre-commit.

Set up the git hook scripts.

.. code-block:: console

    $ pre-commit install

Now pre-commit will run automatically on ``git commit``!

.. _pre-commit: https://pre-commit.com/
.. _hooks supported: https://pre-commit.com/hooks.html


Step 7: Create a GitHub Repo
----------------------------

Go to your GitHub account and create a new repo named ``mypackage``, where
``mypackage`` matches the ``[project_slug]`` from your answers to running
cookiecutter.

You will find one folder named after the ``[project_slug]``. Move into this
folder, and then setup git to use your GitHub repo and upload the code.

.. code-block:: console

    $ git add .
    $ git commit -m "first commit"
    $ git branch -M master
    $ git remote add origin git@github.com:myusername/mypackage.git
    $ git push -u origin master

Where ``myusername`` and ``mypackage`` are adjusted for your username and
package name.

You'll need an ssh key to push the repo. You can `Generate`_ a key or `Add`_ an
existing one.

.. _Generate: https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/
.. _Add: https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/


Step 8: Set Up GitHub Actions
-----------------------------

Automate, customize, and execute your software development workflows right in your
repository with `GitHub Actions`_. You can discover, create, and share actions to
perform any job you'd like, including CI/CD, and combine actions in a completely
customized workflow.

You only need an existing GitHub repository to create and run a GitHub Actions workflow.
Your workflow configurations are stored in `.github/workflows` directory.

.. _GitHub Actions: https://docs.github.com/en/free-pro-team@latest/actions

Step 9: Set Up the Docs
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

`GitHub Pages`_ is a static site hosting service that takes HTML, CSS, and
JavaScript files straight from a repository on GitHub optionally runs the files
through a build process, and publishes a website.

You can host your site on GitHub's ``github.io`` domain or your custom
domain. You can automatically host to `GitHub Pages using Using GitHub Actions`_.

Setup Deploy Keys
~~~~~~~~~~~~~~~~~

#. Generate your deploy key with the following command

   .. code-block:: console

        $ ssh-keygen -t rsa -b 4096 -C "$(git config user.email)" -f ~/.ssh/gh-pages -N ""

   You will get 2 files:

   * gh-pages.pub (public key)
   * gh-pages     (private key)

#. Install ``xclip`` if you haven't done so already

   .. code-block:: console

        $ sudo apt install xclip -y

#. Copy your public key

   .. code-block:: console

        $ xclip -sel clip < ~/.ssh/gh-pages.pub

#. Next, Go to **Repository Settings**.

   Go to **Deploy Keys** and add your public key with the **Allow write access**

#. Copy your private key

   .. code-block:: console

        $ xclip -sel clip < ~/.ssh/gh-pages

#. Go to **Secrets** and add your private key as `ACTIONS_DEPLOY_KEY`

.. _Sphinx: https://www.sphinx-doc.org/en/master/
.. _reStructuredText: https://docutils.sourceforge.io/rst.html
.. _Docutils: https://docutils.sourceforge.io/
.. _Read the Docs Sphinx Theme: https://github.com/readthedocs/sphinx_rtd_theme
.. _Read the Docs: https://readthedocs.org/
.. _GitHub Pages: https://docs.github.com/en/github/working-with-github-pages/about-github-pages
.. _GitHub Pages using Using GitHub Actions: https://github.com/marketplace/actions/github-pages-action


Step 10: Release on PyPI
------------------------

The Python Package Index or `PyPI`_ is the official third-party software
repository for the Python programming language. Python developers intend it to
be a comprehensive catalog of all open-source Python packages.

When you are ready, you can release your package using poetry.

See :ref:`pypi-setup` for more information.


Having problems?
----------------

Visit our :ref:`troubleshooting` page for help. If that doesn't help, go to our
`Issues`_ page and create a new Issue. Be sure to give as much information as
possible.

.. _Issues: https://github.com/sp-fm/fuse-framework/issues

.. note:: Did you find any of these instructions confusing? `Edit this file`_
          and submit a pull request with your improvements!

.. _Edit this file: https://github.com/sp-fm/fuse-framework/blob/master/docs/tutorial.rst
