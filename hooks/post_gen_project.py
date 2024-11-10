"""Post-generation hooks for the cookiecutter template."""

import os
import shutil
from pathlib import Path

PROJECT_DIRECTORY = Path(os.path.realpath(os.path.curdir))


def remove_file(filepath: str) -> None:
    """Remove a file from the project directory.

    Args:
        filepath: Relative path to the file to remove
    """
    (PROJECT_DIRECTORY / filepath).unlink()


def remove_dir(filepath: str) -> None:
    """Remove a directory and all its contents from the project directory.

    Args:
        filepath: Relative path to the directory to remove
    """
    shutil.rmtree(PROJECT_DIRECTORY / filepath)


if __name__ == "__main__":
    if "{{cookiecutter.include_github_actions}}" != "y":  # noqa: PLR0133
        remove_dir(".github")
