# type: ignore
"""Test {{ cookiecutter.__package_name_kebab_case }} CLI."""

import re

from typer.testing import CliRunner

from {{ cookiecutter.__package_name_snake_case }}.cli import app
from {{ cookiecutter.__package_name_snake_case }}.config import {{ cookiecutter.__package_name_pascal_case }}Config
from tests.helpers import strip_ansi

runner = CliRunner()


def test_version():
    """Test printing version and then exiting."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert re.match(r"{{ cookiecutter.__package_name_snake_case }} version: \d+\.\d+\.\d+", strip_ansi(result.output))

def test_default_output(config_data):
    """Test printing version and then exiting."""
    with {{ cookiecutter.__package_name_pascal_case }}Config.change_config_sources(config_data(key_one="edited")):
        result = runner.invoke(app)
        assert result.exit_code == 0
        assert re.match(r"Starting {{ cookiecutter.__package_name_snake_case }} version: \d+\.\d+\.\d+", strip_ansi(result.output))


def test_default_output_2(mock_config, debug):  # noqa: ARG001
    """Test printing version and then exiting."""
    result = runner.invoke(app)
    assert result.exit_code == 1
    assert "Configuration file is using default values" in strip_ansi(result.output)
