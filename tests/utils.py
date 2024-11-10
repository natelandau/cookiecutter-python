"""Utility functions for tests."""

from __future__ import annotations

import os
from contextlib import contextmanager
from pathlib import Path
from typing import TYPE_CHECKING

import yaml

if TYPE_CHECKING:
    from collections.abc import Generator


def is_valid_yaml(path: str | Path) -> bool:
    """Validate if a file contains valid YAML syntax.

    Args:
        path: File path to validate, either as string or Path object.

    Returns:
        True if file exists and contains valid YAML, False otherwise.
    """
    path = Path(path)

    if not path.is_file():
        print(f"File does not exist: {path}")  # noqa: T201
        return False

    try:
        with path.open("r") as file:
            yaml.safe_load(file)
    except yaml.YAMLError as e:
        print(f"Invalid YAML file: {path} - Error: {e}")  # noqa: T201
        return False
    except OSError as e:
        print(f"Error reading file: {path} - Error: {e}")  # noqa: T201
        return False

    return True


@contextmanager
def run_within_dir(path: str) -> Generator[None, None, None]:
    """Temporarily change working directory within a context.

    Args:
        path: Directory path to temporarily change to.

    Yields:
        None

    Example:
        ```python
        with run_within_dir("/tmp"):
            # Code here runs in /tmp
        # Back to original directory
        ```
    """
    oldpwd = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(oldpwd)


def file_contains_text(file: str, text: str) -> bool:
    """Search for text within a file.

    Args:
        file: Path to file to search in.
        text: String to search for.

    Returns:
        True if text is found in file, False otherwise.
    """
    with Path(file).open("r") as f:
        return f.read().find(text) != -1
