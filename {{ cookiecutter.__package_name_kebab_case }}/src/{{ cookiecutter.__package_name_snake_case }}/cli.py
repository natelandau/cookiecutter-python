"""{{ cookiecutter.package_name }} CLI."""

import shutil
from pathlib import Path
from typing import Annotated, Optional

import typer
from confz import validate_all_configs
from loguru import logger
from pydantic import ValidationError

from {{ cookiecutter.__package_name_snake_case }}.__version__ import __version__
from {{ cookiecutter.__package_name_snake_case }}.constants import APP_DIR, CONFIG_PATH
from {{ cookiecutter.__package_name_snake_case }}.utils import console, instantiate_logger

app = typer.Typer(add_completion=False, no_args_is_help=True, rich_markup_mode="rich")
app_dir = typer.get_app_dir("{{ cookiecutter.__package_name_snake_case }}")
typer.rich_utils.STYLE_HELPTEXT = ""


def version_callback(value: bool) -> None:
    """Print version and exit."""
    if value:
        console.print(f"{__package__} version: {__version__}")
        raise typer.Exit()


@app.command()
def main(
    log_file: Annotated[
        Path,
        typer.Option(
            help="Path to log file",
            show_default=True,
            dir_okay=False,
            file_okay=True,
            exists=False,
        ),
    ] = Path(f"{APP_DIR}/{{ cookiecutter.__package_name_snake_case }}.log"),
    log_to_file: Annotated[
        bool,
        typer.Option(
            "--log-to-file",
            help="Log to file",
            show_default=True,
        ),
    ] = False,
    verbosity: Annotated[
        int,
        typer.Option(
            "-v",
            "--verbose",
            show_default=True,
            help="""Set verbosity level(0=INFO, 1=DEBUG, 2=TRACE)""",
            count=True,
        ),
    ] = 0,
    version: Annotated[  # noqa: ARG001
        Optional[bool],
        typer.Option(
            "--version",
            is_eager=True,
            callback=version_callback,
            help="Print version and exit",
        ),
    ] = None,
) -> None:
    """Add application documentation here."""
    # Instantiate Logging
    instantiate_logger(verbosity, log_file, log_to_file)

    # Create a default configuration file if one does not exist
    if not CONFIG_PATH.exists():
        CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
        default_config_file = Path(__file__).parent.resolve() / "default_config.toml"
        shutil.copy(default_config_file, CONFIG_PATH)
        logger.info(f"Created default configuration file: {CONFIG_PATH}")

    # Load and validate configuration
    try:
        validate_all_configs()
    except ValidationError as e:
        logger.error(f"Invalid configuration file: {CONFIG_PATH}")
        for error in e.errors():
            console.print(f"           [red]{error['loc'][0]}: {error['msg']}[/red]")
        raise typer.Exit(code=1) from e

    logger.debug("Debugging enabled")
    console.print(f"Starting {__package__} version: {__version__}")


if __name__ == "__main__":
    app()
