{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug.replace('_', '-') }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug.replace('_', '-') }}

.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug.replace('_', '-') }}.svg
        :target: https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug.replace('_', '-') }}
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

This package was created with Cookiecutter_ and the `sp-fm/fuse-framework`_
project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`sp-fm/fuse-framework`: https://github.com/sp-fm/fuse-framework
