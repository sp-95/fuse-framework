.. _pypi-release-checklist:

PyPI Release Checklist
======================

For Every Release
-------------------

#. Update CHANGELOG.rst

#. Commit the changes:

   .. code-block:: console

        $ git add CHANGELOG.rst
        $ git commit -m "Changelog for upcoming release 0.1.1."

#. Update version number (can also be patch or major)

   .. code-block:: console

        $ poetry version minor

#. Install the package again for local development, but with the new version number:

   .. code-block:: console

        $ poetry install

#. Run the tests:

   .. code-block:: console

        $ tox

#. Push the commit:

   .. code-block:: console

        $ git push

#. Push the tags, creating the new release on both GitHub and PyPI:

   .. code-block:: console

        $ git push --tags

#. Check the PyPI listing page to make sure that the README, release notes, and roadmap display properly. If not, try one of these:

    #. Copy and paste the RestructuredText into http://rst.ninjs.org/ to find out what broke the formatting.

    #. Check your long_description locally:

       .. code-block:: console

            $ pip install readme_renderer
            $ python -m readme_renderer PROBLEM.rst >/dev/null

       Replace PROBLEM.rst with the name of the file you are having trouble with

#. Edit the release on GitHub (e.g. https://github.com/audreyr/cookiecutter/releases). Paste the release notes into the release's release page, and come up with a title for the release.
