# type: ignore
"""Test {{ cookiecutter.__package_name_kebab_case}} CLI."""

import re

from typer.testing import CliRunner

from {{ cookiecutter.__package_name_snake_case }}.cli import app
from tests.helpers import strip_ansi

runner = CliRunner()


def test_version():
    """Test printing version and then exiting."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert re.match(r"{{ cookiecutter.__package_name_snake_case }} version: \d+\.\d+\.\d+", strip_ansi(result.output))
