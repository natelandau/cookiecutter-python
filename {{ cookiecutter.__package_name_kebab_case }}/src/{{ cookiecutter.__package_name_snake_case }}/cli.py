"""{{ cookiecutter.package_name }} CLI."""

import sys
from pathlib import Path
from typing import Optional
from loguru import logger

import typer

from {{ cookiecutter.__package_name_snake_case }}.__version__ import __version__
from {{ cookiecutter.__package_name_snake_case }}.config import Config
from {{ cookiecutter.__package_name_snake_case }}.constants import LogLevel
from {{ cookiecutter.__package_name_snake_case }}.utils.console import console


app = typer.Typer(add_completion=False, no_args_is_help=True, rich_markup_mode="rich")

typer.rich_utils.STYLE_HELPTEXT = ""


def version_callback(value: bool) -> None:
    """Print version and exit."""
    if value:
        console.print(f"{__package__} version: {__version__}")
        raise typer.Exit()



@app.command()
def main(
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        "-n",
        help="Dry run - don't actually change anything",
    ),
    config_file: Path = typer.Option(
        Path(Path.home() / f".{__package__}/{__package__}.toml"),
        help="Specify a custom path to configuration file.",
        show_default=False,
        dir_okay=False,
        file_okay=True,
    ),
    log_file: Path = typer.Option(
        Path(Path.home() / "logs" / f"{__package__}.log"),
        help="Path to log file",
        show_default=True,
        dir_okay=False,
        file_okay=True,
        exists=False,
    ),
    log_to_file: bool = typer.Option(
        False,
        "--log-to-file",
        help="Log to file",
        show_default=True,
    ),
    log_level: LogLevel = typer.Option(
        LogLevel.INFO,
        help="Log level",
        show_default=False,
        case_sensitive=False,
    ),
    version: Optional[bool] = typer.Option(  # noqa: ARG001
        None, "--version", help="Print version and exit", callback=version_callback, is_eager=True
    ),
) -> None:
    """Say a message."""
    logger.remove()
    logger.add(
        sys.stdout,
        level=log_level.name,
        colorize=True,
        format="<level>{level: <8}</level> | <level>{message}</level> <fg #c5c5c5>({name}:{function}:{line})</fg #c5c5c5>"
        if log_level in {log_level.DEBUG, log_level.TRACE}
        else "<level>{level: <8}</level> | <level>{message}</level>",
        enqueue=True,
    )
    if log_to_file:
        logger.add(
            log_file,
            level=log_level.name,
            format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {message} ({name})",
            rotation="50 MB",
            retention=2,
            compression="zip",
            enqueue=True,
        )

    logger.info("Starting {name} version: {version}", name=__package__, version=__version__)

    config = Config(config_file, context={"dry_run": dry_run})
