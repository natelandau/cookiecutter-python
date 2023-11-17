"""Constants for {{ cookiecutter.package_name }}."""

from enum import Enum


class LogLevel(str, Enum):
    """Log levels for video-transcode."""

    TRACE = "trace"
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
