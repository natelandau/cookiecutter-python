"""Utility functions for {{ cookiecutter.hyphenated }}."""

from .config import {{ cookiecutter.capwords }}Config
from .logging import console, instantiate_logger

__all__ = ["console", "instantiate_logger", "{{ cookiecutter.capwords }}Config"]
