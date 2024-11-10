"""Utility functions for tests."""

import os
from collections.abc import Generator
from contextlib import contextmanager
from pathlib import Path


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
