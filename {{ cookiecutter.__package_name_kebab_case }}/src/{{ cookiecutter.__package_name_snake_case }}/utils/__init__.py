"""Shared utilities for {{ cookiecutter.package_name }}."""

from .console import console  # isort:skip
from .logging import InterceptHandler, instantiate_logger  # isort:skip

from .config import {{ cookiecutter.__package_name_pascal_case }}Config

__all__ = [
    "InterceptHandler",
    "{{ cookiecutter.__package_name_pascal_case }}Config",
    "console",
    "instantiate_logger",
]
