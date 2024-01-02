"""Shared utilities for {{ cookiecutter.package_name }}."""

from .console import console
from .logging import InterceptHandler, instantiate_logger

__all__ = [
    "console",
    "InterceptHandler",
    "instantiate_logger"
]
