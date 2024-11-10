"""Constants for {{ cookiecutter.hyphenated }}."""

import os
from pathlib import Path

VERSION = "0.1.0"
CONFIG_DIR = (
    Path(os.getenv("XDG_CONFIG_HOME", "~/.config")).expanduser().absolute()
    / __package__
)
DATA_DIR = (
    Path(os.getenv("XDG_DATA_HOME", "~/.local/share")).expanduser().absolute()
    / __package__
)
STATE_DIR = (
    Path(os.getenv("XDG_STATE_HOME", "~/.local/state")).expanduser().absolute()
    / __package__
)
CACHE_DIR = (
    Path(os.getenv("XDG_CACHE_HOME", "~/.cache")).expanduser().absolute() / __package__
)
PROJECT_ROOT_PATH = Path(__file__).parents[2].absolute()
CONFIG_PATH = CONFIG_DIR / "config.toml"
