"""Instantiate {{ cookiecutter.hyphenated }}Config class and set default values."""

from typing import ClassVar

from confz import BaseConfig, ConfigSources, EnvSource, FileSource

from {{ cookiecutter.underscored }}.constants import CONFIG_PATH, PROJECT_ROOT_PATH


class {{ cookiecutter.capwords }}Config(BaseConfig):
    """{{ cookiecutter.capwords }} Configuration."""

    # Default values
    key_one: str
    key_two: list[int]
    key_three: tuple[str, ...] = ()

    CONFIG_SOURCES: ClassVar[ConfigSources | None] = [
        EnvSource(prefix="{{ cookiecutter.underscored | upper }}_", file=PROJECT_ROOT_PATH / ".env", allow_all=True),
        EnvSource(prefix="{{ cookiecutter.underscored | upper }}_", file=PROJECT_ROOT_PATH / ".env.secrets", allow_all=True),
        FileSource(file=CONFIG_PATH),
    ]
