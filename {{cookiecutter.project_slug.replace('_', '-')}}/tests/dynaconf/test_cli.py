#!/usr/bin/env python
"""Tests for `{{ cookiecutter.project_slug }}` package."""
import pytest
from dynaconf.vendor.box.exceptions import BoxKeyError

from {{ cookiecutter.project_slug }}.dynaconf.cli import Main


def test_command_line_interface(caplog):
    """Test the CLI"""

    Main.package_name()
    assert "Package Name: " in caplog.text

    with pytest.raises(BoxKeyError):
        Main.database(key="test")
