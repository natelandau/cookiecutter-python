"""Instantiate {{ cookiecutter.__package_name_pascal_case }}Config class and set default values."""

from typing import ClassVar

from confz import BaseConfig, ConfigSources, FileSource

from {{ cookiecutter.__package_name_snake_case }}.constants import CONFIG_PATH


class {{ cookiecutter.__package_name_pascal_case }}Config(BaseConfig):  # type: ignore [misc]
    """{{ cookiecutter.package_name }} Configuration."""

    # Default values
    key_one: str
    key_two: list[int]
    key_three: tuple[str, ...] = ()

    CONFIG_SOURCES: ClassVar[ConfigSources | None] = FileSource(file=CONFIG_PATH)
