# type: ignore
"""Shared fixtures for tests."""

from pathlib import Path

import pytest
from confz import DataSource, FileSource

from {{ cookiecutter.__package_name_snake_case }}.config import {{ cookiecutter.__package_name_pascal_case }}Config
from {{ cookiecutter.__package_name_snake_case }}.utils import console


@pytest.fixture()
def debug():
    """Print debug information to the console. This is used to debug tests while writing them."""

    def _debug_inner(label: str, value: str | Path, breakpoint: bool = False):
        """Print debug information to the console. This is used to debug tests while writing them.

        Args:
            label (str): The label to print above the debug information.
            value (str | Path): The value to print. When this is a path, prints all files in the path.
            breakpoint (bool, optional): Whether to break after printing. Defaults to False.

        Returns:
            bool: Whether to break after printing.
        """
        console.rule(label)
        if not isinstance(value, Path) or not value.is_dir():
            console.print(value)
        else:
            for p in value.rglob("*"):
                console.print(p)

        console.rule()

        if breakpoint:
            return pytest.fail("Breakpoint")

        return True

    return _debug_inner


@pytest.fixture()
def config_data():
    """Mock specific configuration data for use in tests."""

    def _inner(
        key_one: str | None = None,
        key_two: list[int] | None = None,
        key_three: tuple[str, ...] | None = None,
    ):
        override_data = {}
        if key_one:
            override_data["key_one"] = key_one
        if key_two:
            override_data["key_two"] = key_two
        if key_three:
            override_data["key_three"] = key_three

        mock_config_file = Path(__file__).resolve().parent / "fixtures/default_config.toml"

        return [
            FileSource(mock_config_file),
            DataSource(data=override_data),
        ]

    return _inner


@pytest.fixture()
def mock_config():  # noqa: PT004
    """Override configuration file with mock configuration for use in tests. To override a default use the `config_data` fixture.

    Returns:
        {{ cookiecutter.__package_name_pascal_case }}Config: The mock configuration.
    """
    mock_config_file = Path(__file__).resolve().parent / "fixtures/default_config.toml"

    with {{ cookiecutter.__package_name_pascal_case }}Config.change_config_sources(FileSource(mock_config_file)):
        yield
