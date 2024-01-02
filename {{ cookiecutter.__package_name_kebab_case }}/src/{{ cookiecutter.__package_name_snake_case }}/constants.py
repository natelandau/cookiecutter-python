"""Constants for {{ cookiecutter.package_name }}."""

from enum import Enum


class LogLevel(str, Enum):
    """Logging levels"""

    TRACE = "trace"
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
