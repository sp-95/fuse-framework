{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{% if is_open_source %}
.. image:: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug.replace('_', '-') }}/workflows/Tests/badge.svg
    :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug.replace('_', '-') }}/actions?query=workflow%3ATests
    :alt: Tests

.. image:: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug.replace('_', '-') }}/workflows/Documentation/badge.svg
    :target: https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug.replace('_', '-') }}/
    :alt: Documentation

{% if cookiecutter.pypi_deployment|lower == 'y' -%}
.. image:: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug.replace('_', '-') }}/workflows/Release/badge.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug.replace('_', '-') }}
    :alt: Release

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug.replace('_', '-') }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug.replace('_', '-') }}
{%- endif %}
{%- endif %}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug | replace("_", "-") }}/
{% endif %}

Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `sp-95/fuse-framework`_
project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`sp-95/fuse-framework`: https://github.com/sp-95/fuse-framework
