# type: ignore
"""Tests for the cookiecutter template."""

import shlex
import subprocess
from pathlib import Path

import pytest

from tests.utils import file_contains_text, run_within_dir


@pytest.mark.parametrize(
    "context",
    [
        {
            "project_name": "my-project",
            "author_name": "Test Author",
        },
        {
            "project_name": "my-project",
            "author_email": "test@example.com",
        },
    ],
)
def test_hooks_dont_pass(cookies, context) -> None:
    """Test that the hooks don't pass with the given context."""
    result = cookies.bake(extra_context=context)
    assert result.exit_code == -1


def test_bake_project(debug, cookies) -> None:
    """Test that the project is created successfully with the given context."""
    # Given: A cookiecutter template
    # When: Baking the project with a custom project name
    result = cookies.bake(
        extra_context={
            "project_name": "my project",
            "author_name": "Test Author",
            "author_email": "test@example.com",
        }
    )

    debug(result.context)

    # Then: Project should be created successfully with the correct name
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "my-project"
    assert result.context == {
        "project_name": "my project",
        "description": "",
        "hyphenated": "my-project",
        "publish_docker_image": "y",
        "publish_to_pypi": "y",
        "underscored": "my_project",
        "include_github_actions": "y",
        "capwords": "MyProject",
        "github_username": "",
        "author_name": "Test Author",
        "author_email": "test@example.com",
        "python_version": "3.13",
    }
    assert result.project_path.is_dir()


def test_installed_project(cookies, tmp_path):
    """Test that the project is installed successfully by installing the virtual environment, running the cli, and running tests."""
    # Given: A temporary directory and cookiecutter template
    with run_within_dir(tmp_path):
        # When: Baking the project with default settings
        result = cookies.bake(
            extra_context={
                "project_name": "my project",
                "author_name": "Test Author",
                "author_email": "test@example.com",
            }
        )

        # Then: Project should be created successfully
        assert result.exit_code == 0
        assert result.exception is None
        assert result.project_path.name == "my-project"
        assert result.project_path.is_dir()
        assert Path(f"{result.project_path}/.github").exists()

        # And: Tests should run successfully in the created project
        with run_within_dir(str(result.project_path)):
            assert subprocess.check_call(shlex.split("uv sync")) == 0
            assert (
                subprocess.check_call(shlex.split("uv run ruff check --no-fix src/ --ignore=F401"))
                == 0
            )
            assert subprocess.check_call(shlex.split("mypy --config-file pyproject.toml src/")) == 0
            assert subprocess.check_call(shlex.split("typos")) == 0
            assert subprocess.check_call(shlex.split("yamllint .")) == 0
            assert subprocess.check_call(shlex.split("uv run pytest tests/")) == 0


def test_not_github_actions(cookies, tmp_path):
    """Test that the github actions files are not created when include_github_actions=n."""
    # Given: A temporary directory and cookiecutter template
    with run_within_dir(tmp_path):
        # When: Baking the project with devcontainer disabled
        result = cookies.bake(
            extra_context={
                "project_name": "my project",
                "author_name": "Test Author",
                "author_email": "test@example.com",
                "include_github_actions": "n",
            }
        )

        # Then: Devcontainer files should not be created
        assert result.exit_code == 0
        assert not Path(f"{result.project_path}/.github").exists()
