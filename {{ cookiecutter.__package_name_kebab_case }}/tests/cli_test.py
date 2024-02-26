# type: ignore
"""Test {{ cookiecutter.__package_name_kebab_case }} CLI."""

from typer.testing import CliRunner

from {{ cookiecutter.__package_name_snake_case }}.cli import app
from {{ cookiecutter.__package_name_snake_case }}.constants import VERSION
from {{ cookiecutter.__package_name_snake_case }}.utils import {{ cookiecutter.__package_name_pascal_case }}Config
from tests.helpers import strip_ansi

runner = CliRunner()


def test_version():
    """Test printing version and then exiting."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert f"{{ cookiecutter.__package_name_snake_case }} version: {VERSION}" in strip_ansi(result.output)


def test_default_output(mock_config):
    """Test printing version and then exiting."""
    with {{ cookiecutter.__package_name_pascal_case }}Config.change_config_sources(mock_config(key_one="edited")):
        result = runner.invoke(app)
        assert result.exit_code == 0
        assert f"Starting {{ cookiecutter.__package_name_snake_case }} version: {VERSION}" in strip_ansi(result.output)
