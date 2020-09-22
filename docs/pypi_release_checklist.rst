.. _pypi-release-checklist:

PyPI Release Checklist
======================

For Every Release
-------------------

#. Update CHANGELOG.rst

#. Commit the changes:

    .. code-block:: bash

        git add CHANGELOG.rst
        git commit -m "Changelog for upcoming release 0.1.1."

#. Update version number (can also be patch or major)

    .. code-block:: bash

        poetry version minor

#. Install the package again for local development, but with the new version number:

    .. code-block:: bash

        poetry install

#. Run the tests:

    .. code-block:: bash

        tox

#. Push the commit:

    .. code-block:: bash

        git push

#. Push the tags, creating the new release on both GitHub and PyPI:

    .. code-block:: bash

        git push --tags

#. Check the PyPI listing page to make sure that the README, release notes, and roadmap display properly. If not, try one of these:

    #. Copy and paste the RestructuredText into http://rst.ninjs.org/ to find out what broke the formatting.

    #. Check your long_description locally:

        .. code-block:: bash

            pip install readme_renderer
            # Replace PROBLEM.rst with the name of the file you are having trouble with
            python -m readme_renderer PROBLEM.rst >/dev/null

#. Edit the release on GitHub (e.g. https://github.com/audreyr/cookiecutter/releases). Paste the release notes into the release's release page, and come up with a title for the release.
