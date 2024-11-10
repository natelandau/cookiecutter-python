# type: ignore
"""Shared fixtures for tests."""

from pathlib import Path

import pytest
from rich.console import Console

console = Console()


@pytest.fixture
def debug():
    """Print debug information to the console. This is used to debug tests while writing them."""

    def _debug_inner(value: str | Path, label: str = "", stop: bool = False, width: int = 80):
        """Print debug information to the console. This is used to debug tests while writing them.

        Args:
            value (str | Path): The value to print. When this is a path, prints all files in the path.
            label (str, optional): The label to print above the debug information.
            stop (bool, optional): Whether to break after printing. Defaults to False.
            width (int, optional): The width of the console output. Defaults to 80, pytest's default when running without `-s`.

        Returns:
            bool: Whether to break after printing.
        """
        console.rule(label)

        # If a directory is passed, print the contents
        if isinstance(value, Path) and value.is_dir():
            for p in value.rglob("*"):
                console.print(p, width=width)
        else:
            console.print(value, width=width)

        console.rule()

        if stop:
            return pytest.fail("Breakpoint")

        return True

    return _debug_inner
