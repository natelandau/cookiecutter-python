"""Logging utilities."""

import contextlib
import logging
import sys
from collections import defaultdict
from enum import Enum
from pathlib import Path

from loguru import logger
from rich.console import Console

console = Console()


class LogLevel(Enum):
    """Log levels."""

    INFO = 0
    DEBUG = 1
    TRACE = 2
    WARNING = 3
    ERROR = 4


def log_formatter(record: dict) -> str:
    """Use rich to style log messages."""
    color_map = defaultdict(
        lambda: "bold",
        {
            "TRACE": "turquoise4",
            "DEBUG": "cyan",
            "DRYRUN": "bold blue",
            "INFO": "",
            "SUCCESS": "bold green",
            "WARNING": "bold yellow",
            "ERROR": "bold red",
            "CRITICAL": "bold white on red",
            "SECONDARY": "dim",
        },
    )
    line_start_map = defaultdict(
        lambda: "{name: <8} | ",
        {
            "INFO": "",
            "DEBUG": "DEBUG | 🐞 ",
            "DRYRUN": "DRYRUN| 👉 ",
            "TRACE": "TRACE | 🔧 ",
            "WARNING": "⚠️ ",
            "SUCCESS": "✅ ",
            "ERROR": "❌ ",
            "CRITICAL": "💀 ",
            "EXCEPTION": "",
            "SECONDARY": "",
        },
    )

    name = record["level"].name
    lvl_color = color_map[name]
    line_start = line_start_map[name].format(name=name)

    msg = (
        f"[{lvl_color}]{line_start}{{ '{{' }}message}}[/{lvl_color}]"
        if lvl_color
        else f"{line_start}{{ '{{' }}message}}"
    )
    func_trace = f"[#c5c5c5]({record['name']}:{record['function']}:{record['line']})[/#c5c5c5]"

    return f"{msg} {func_trace}" if name == "TRACE" else msg


def instantiate_logger(verbosity: int, log_file: Path, log_to_file: bool) -> None:
    """Instantiate the Loguru logger."""
    level = min(verbosity, 2)

    logger.remove()

    with contextlib.suppress(
        TypeError
    ):  # Suppress error if DRYRUN is already defined (typically in tests)
        logger.level("DRYRUN", no=20, color="<blue>", icon="👉")
        logger.level("SECONDARY", no=20, color="<blue>", icon="👉")

    logger.add(
        console.print,
        level=LogLevel(level).name,
        colorize=True,
        format=log_formatter,
    )
    if log_to_file:
        logger.add(
            log_file,
            level=LogLevel(level).name,
            format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {message} ({name}:{function}:{line})",
            rotation="50 MB",
            retention=2,
            compression="zip",
        )

    if verbosity > 2:  # noqa: PLR2004
        # logging.getLogger("peewee").setLevel(level="DEBUG") # Example of how to set a specific logger level  # noqa: ERA001
        logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)


class InterceptHandler(logging.Handler):  # pragma: no cover
    """Intercepts standard logging and redirects to Loguru."""

    @staticmethod
    def emit(record: logging.LogRecord) -> None:
        """Intercepts standard logging and redirects to Loguru.

        Args:
            record: A logging.LogRecord object representing the logging message.
        """
        # Get corresponding Loguru level if it exists.
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message.
        frame, depth = sys._getframe(6), 6  # noqa: SLF001
        while frame and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())
