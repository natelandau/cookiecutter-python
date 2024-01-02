"""Constants for {{ cookiecutter.package_name }}."""

from enum import Enum
from pathlib import Path

import typer

class LogLevel(Enum):
    """Log levels for {{ cookiecutter.package_name }}."""

    INFO = 0
    DEBUG = 1
    TRACE = 2
    WARNING = 3
    ERROR = 4

APP_DIR = Path(typer.get_app_dir("{{ cookiecutter.__package_name_kebab_case }}"))
