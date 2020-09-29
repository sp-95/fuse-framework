Welcome to {{ cookiecutter.project_name }}'s documentation!
==========={% for _ in cookiecutter.project_name %}={% endfor %}=================

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   readme
   installation
   usage

.. toctree::
   :maxdepth: 2
   :caption: Modules

   modules

.. toctree::
   :maxdepth: 2
   :caption: Extra

   contributing
{% if cookiecutter.pypi_deployment == 'y' -%}
   pypi_release_checklist
{%- endif %}
   authors

Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
