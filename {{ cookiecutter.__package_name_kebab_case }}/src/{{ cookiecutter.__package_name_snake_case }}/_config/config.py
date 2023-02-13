"""Instantiate Configuration class and set default values."""

import shutil
from pathlib import Path
from typing import Any

import rich.repr
import typer

from {{ cookiecutter.__package_name_snake_case }}._utils import alerts
from {{ cookiecutter.__package_name_snake_case }}._utils.alerts import logger as log

{%- if cookiecutter.python_version.split(".")[1] | int  <= 10 %}
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib  # type: ignore [no-redef]
{%- else %}
import tomllib
{%- endif %}

PATH_CONFIG_DEFAULT = Path(__file__).parent / "default_config.toml"


@rich.repr.auto
class Config:
    """Representation of a configuration file."""

    def __init__(self, config_path: Path = None) -> None:
        """Initialize configuration file."""
        self.config_path = config_path.expanduser().resolve()
        if not self.config_path.exists():
            self._create_config()

        self.dict = self._load_config()
        self._validate_config()

    def __rich_repr__(self) -> rich.repr.Result:
        """Return the representation of the configuration file."""
        yield "config_path", self.config_path
        yield "dict", self.dict

    def _load_config(self) -> dict[str, Any]:
        """Load the configuration file."""
        log.debug(f"Loading configuration from {self.config_path}")
        with self.config_path.open("rb") as f:
            try:
                return tomllib.load(f)
            except tomllib.TOMLDecodeError as e:
                log.exception(f"Could not parse '{self.config_path}'")
                raise typer.Exit(code=1) from e

    def _create_config(self) -> None:
        """Create a configuration file from the default when it does not exist."""
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(PATH_CONFIG_DEFAULT, self.config_path)
        alerts.success(f"Created default configuration file at {self.config_path}")
        alerts.notice(f"Please edit {self.config_path} before continuing")
        raise typer.Exit(code=1)

    def _validate_config(self) -> None:
        """Validate the configuration file."""
        if self.dict == {}:
            log.error(f"Configuration file '{self.config_path}' is empty or malformed")
            raise typer.Exit(code=1)
