"""Shared utilities."""

from {{ cookiecutter.__package_name_snake_case }}._utils import alerts
from {{ cookiecutter.__package_name_snake_case }}._utils.alerts import LoggerManager


__all__ = [
    "alerts",
    "LoggerManager",
]
