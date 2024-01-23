"""Constants for {{ cookiecutter.package_name }}."""

from pathlib import Path

import typer

APP_DIR = Path(typer.get_app_dir("{{ cookiecutter.__package_name_kebab_case }}"))
CONFIG_PATH = APP_DIR / "config.toml"
