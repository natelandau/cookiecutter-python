"""Test CLI."""

from typer.testing import CliRunner

from {{ cookiecutter.underscored }}.cli import app
from {{ cookiecutter.underscored }}.constants import VERSION

def test_version() -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert f"{{ cookiecutter.underscored }} version: {VERSION}" in result.output
