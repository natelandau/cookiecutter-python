"""{{ cookiecutter.package_name }} CLI."""

from pathlib import Path
from typing import Annotated, Optional

import typer
from loguru import logger

from {{ cookiecutter.__package_name_snake_case }}.__version__ import __version__
from {{ cookiecutter.__package_name_snake_case }}.constants import APP_DIR
from {{ cookiecutter.__package_name_snake_case }}.utils import console, edit_config, instantiate_logger, validate_config

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
    edit_configuration: Annotated[
        bool,
        typer.Option(
            "--edit-config",
            help="Edit the configuration file",
            show_default=True,
        ),
    ] = False,
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

    if edit_configuration:
        edit_config()
        raise typer.Exit(0)

    validate_config()

    logger.debug("Debugging enabled")
    console.print(f"Starting {__package__} version: {__version__}")


if __name__ == "__main__":
    app()
