"""{{ cookiecutter.package_name }} CLI."""

import sys
from pathlib import Path
from typing import Optional
from loguru import logger

import typer

from {{ cookiecutter.__package_name_snake_case }}.__version__ import __version__
from {{ cookiecutter.__package_name_snake_case }}.config import Config
from {{ cookiecutter.__package_name_snake_case }}.constants import APP_DIR
from {{ cookiecutter.__package_name_snake_case }}.utils import console
from {{ cookiecutter.__package_name_snake_case }}.utils import instantiate_logger


app = typer.Typer(add_completion=False, no_args_is_help=True, rich_markup_mode="rich")
app_dir = typer.get_app_dir("{{ cookiecutter.__package_name_snake_case }}")
config = Config(config_path=APP_DIR / "config.toml")

typer.rich_utils.STYLE_HELPTEXT = ""


def version_callback(value: bool) -> None:
    """Print version and exit."""
    if value:
        console.print(f"{__package__} version: {__version__}")
        raise typer.Exit()


@app.command()
def main(
    log_file: Path = typer.Option(
        config.get("log_file", default=f"{APP_DIR}/{{ cookiecutter.__package_name_snake_case }}.log"),
        help="Path to log file",
        show_default=True,
        dir_okay=False,
        file_okay=True,
        exists=False,
    ),
    log_to_file: bool = typer.Option(
        config.get("log_to_file", default=False),
        "--log-to-file",
        help="Log to file",
        show_default=True,
    ),
    verbosity: int = typer.Option(
        0,
        "-v",
        "--verbose",
        show_default=True,
        help="""Set verbosity level(0=INFO, 1=DEBUG, 2=TRACE)""",
        count=True,
    ),
    version: Optional[bool] = typer.Option(  # noqa: ARG001
        None, "--version", help="Print version and exit", callback=version_callback, is_eager=True
    ),
) -> None:
    """Add application documentation here."""
    # Instantiate Logging
    instantiate_logger(verbosity, log_file, log_to_file)
    logger.info(f"Starting {__package__} version: {__version__}")

if __name__ == "__main__":
    app()
