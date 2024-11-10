"""{{ cookiecutter.description or cookiecutter.hyphenated }} CLI."""

import shutil
from pathlib import Path
from typing import Annotated, Optional

import typer
from confz import validate_all_configs
from loguru import logger
from pydantic import ValidationError

from {{ cookiecutter.underscored }}.constants import CONFIG_PATH, STATE_DIR, VERSION
from {{ cookiecutter.underscored }}.utils import console, instantiate_logger

app = typer.Typer(
    add_completion=False,
    no_args_is_help=True,
    rich_markup_mode="rich",
    context_settings={"help_option_names": ["-h", "--help"]},
)
typer.rich_utils.STYLE_HELPTEXT = ""


def version_callback(value: bool) -> None:
    """Print version and exit."""
    if value:
        console.print(f"{__package__} version: {VERSION}")
        raise typer.Exit()

def create_config_callback(value: bool) -> None:
    """Create a default configuration file and exit."""
    if value:
        if not CONFIG_PATH.exists():
            CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
            default_config_file = Path(__file__).parent.resolve() / "default_config.toml"
            shutil.copy(default_config_file, CONFIG_PATH)
            logger.info(f"Created default configuration file: {CONFIG_PATH}")
        else:
            logger.error(f"Configuration file already exists: {CONFIG_PATH}")
            raise typer.Exit(code=1)

        raise typer.Exit()

@app.command()
def main(
    dry_run: Annotated[
        bool,
        typer.Option(
            "--dry-run",
            "-n",
            help="Run all brew commands with the --dry-run flag",
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
    ] = STATE_DIR / f"{__package__}.log",
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
    create_config: Annotated[  # noqa: ARG001
        Optional[bool],
        typer.Option(
            "--create-config",
            is_eager=True,
            callback=create_config_callback,
            help="Create a default configuration file",
        ),
    ] = None,
) -> None:
    """Add application documentation here."""
    instantiate_logger(verbosity, log_file, log_to_file)

    # ##########################
    # Uncomment this if you want to use a configuration file
    # ##########################
    # try: # noqa: ERA001
    #     validate_all_configs() # noqa: ERA001
    # except ValidationError as e: # noqa: ERA001
    #     logger.error(f"Invalid configuration file: {CONFIG_PATH}") # noqa: ERA001
    #     for error in e.errors():
    #         console.print(f"           [red]{error['loc'][0]}: {error['msg']}[/red]") # noqa: ERA001
    #     raise typer.Exit(code=1) from e # noqa: ERA001

    # ##########################
    # Uncomment this if you want to use custom data sources in the config
    # ##########################
    # Add cli arguments to the configuration
    # new_config_data = {} # noqa: ERA001
    # with {{ cookiecutter.capwords }}Config.change_config_sources([FileSource(file=CONFIG_PATH), DataSource(data={})]):
    #     console.print({{ cookiecutter.capwords }}Config()) # noqa: ERA001

    if dry_run:
        logger.log("DRYRUN", "Dry run enabled")

    logger.debug("Should only see this if verbosity is 2 or more")
    console.print(f"Starting {__package__} version: {VERSION}")


if __name__ == "__main__":
    app()
