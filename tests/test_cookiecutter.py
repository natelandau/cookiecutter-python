# type: ignore
"""Tests for the cookiecutter template."""

from __future__ import annotations

import shlex
import subprocess

import pytest

from tests.utils import file_contains_text, run_within_dir


@pytest.mark.parametrize(
    "context",
    [
        {
            "app_name": "my-project",
            "author_name": "Test Author",
        },
        {
            "app_name": "my-project",
            "author_email": "test@example.com",
        },
    ],
)
def test_hooks_dont_pass(cookies, context) -> None:
    """Test that the hooks don't pass with the given context."""
    result = cookies.bake(extra_context=context)
    assert result.exit_code == -1


def test_bake_project(debug, cookies) -> None:  # noqa: ARG001
    """Test that the project is created successfully with the given context."""
    # Given: A cookiecutter template
    # When: Baking the project with a custom project name
    result = cookies.bake(
        extra_context={
            "app_name": "my project",
            "author_name": "Test Author",
            "author_email": "test@example.com",
        }
    )

    # Then: Project should be created successfully with the correct name
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "my-project"
    assert result.context == {
        "app_name": "my project",
        "description": "",
        "hyphenated": "my-project",
        "publish_docker_image": "y",
        "publish_to_pypi": "y",
        "underscored": "my_project",
        "capwords": "MyProject",
        "github_username": "",
        "author_name": "Test Author",
        "author_email": "test@example.com",
        "python_version": "3.13",
    }
    assert result.project_path.is_dir()


def test_venv_and_lint(cookies, tmp_path):
    """Test that the venv and linting tools run successfully in the created project."""
    # Given: A temporary directory and cookiecutter template
    with run_within_dir(tmp_path):
        # When: Baking the project with default settings
        result = cookies.bake(
            extra_context={
                "app_name": "my project",
                "author_name": "Test Author",
                "author_email": "test@example.com",
            }
        )

        # Then: Project should be created successfully
        assert result.exit_code == 0
        assert result.exception is None
        assert result.project_path.name == "my-project"
        assert result.project_path.is_dir()
        # assert is_valid_yaml(result.project_path / ".github" / "workflows" / "main.yml")

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


def test_pytest(cookies, tmp_path):
    """Test that pytest runs successfully in the created project."""
    # Given: A temporary directory and cookiecutter template
    with run_within_dir(tmp_path):
        # When: Baking the project with default settings
        result = cookies.bake(
            extra_context={
                "app_name": "my project",
                "author_name": "Test Author",
                "author_email": "test@example.com",
            }
        )

        # Then: Project should be created successfully
        assert result.exit_code == 0
        assert result.exception is None
        assert result.project_path.name == "my-project"
        assert result.project_path.is_dir()
        # assert is_valid_yaml(result.project_path / ".github" / "workflows" / "main.yml")

        # And: Tests should run successfully in the created project
        with run_within_dir(str(result.project_path)):
            assert subprocess.check_call(shlex.split("uv sync")) == 0
            assert subprocess.check_call(shlex.split("uv run pytest tests/")) == 0


# def test_devcontainer(cookies, tmp_path):
#     """Test that the devcontainer files are created when devcontainer=y"""
#     # Given: A temporary directory and cookiecutter template
#     with run_within_dir(tmp_path):
#         # When: Baking the project with devcontainer enabled
#         result = cookies.bake(extra_context={"devcontainer": "y"})

#         # Then: Devcontainer files should be created
#         assert result.exit_code == 0
#         assert os.path.isfile(f"{result.project_path}/.devcontainer/devcontainer.json")
#         assert os.path.isfile(f"{result.project_path}/.devcontainer/postCreateCommand.sh")


# def test_not_devcontainer(cookies, tmp_path):
#     """Test that the devcontainer files are not created when devcontainer=n"""
#     # Given: A temporary directory and cookiecutter template
#     with run_within_dir(tmp_path):
#         # When: Baking the project with devcontainer disabled
#         result = cookies.bake(extra_context={"devcontainer": "n"})

#         # Then: Devcontainer files should not be created
#         assert result.exit_code == 0
#         assert not os.path.isfile(f"{result.project_path}/.devcontainer/devcontainer.json")
#         assert not os.path.isfile(f"{result.project_path}/.devcontainer/postCreateCommand.sh")


# def test_cicd_contains_pypi_secrets(cookies, tmp_path):
#     # Given: A temporary directory and cookiecutter template
#     with run_within_dir(tmp_path):
#         # When: Baking the project with publish_to_pypi enabled
#         result = cookies.bake(extra_context={"publish_to_pypi": "y"})

#         # Then: CICD files should contain pypi secrets
#         assert result.exit_code == 0
#         assert is_valid_yaml(result.project_path / ".github" / "workflows" / "on-release-main.yml")
#         assert file_contains_text(f"{result.project_path}/.github/workflows/on-release-main.yml", "PYPI_TOKEN")
#         assert file_contains_text(f"{result.project_path}/Makefile", "build-and-publish")


# def test_dont_publish(cookies, tmp_path):
#     # Given: A temporary directory and cookiecutter template
#     with run_within_dir(tmp_path):
#         # When: Baking the project with publish_to_pypi disabled
#         result = cookies.bake(extra_context={"publish_to_pypi": "n"})

#         # Then: CICD files should not contain pypi secrets
#         assert result.exit_code == 0
#         assert is_valid_yaml(result.project_path / ".github" / "workflows" / "on-release-main.yml")
#         assert not file_contains_text(
#             f"{result.project_path}/.github/workflows/on-release-main.yml", "make build-and-publish"
#         )


# def test_mkdocs(cookies, tmp_path):
#     # Given: A temporary directory and cookiecutter template
#     with run_within_dir(tmp_path):
#         # When: Baking the project with mkdocs enabled
#         result = cookies.bake(extra_context={"mkdocs": "y"})

#         # Then: Documentation files should be created
#         assert result.exit_code == 0
#         assert is_valid_yaml(result.project_path / ".github" / "workflows" / "main.yml")
#         assert is_valid_yaml(result.project_path / ".github" / "workflows" / "on-release-main.yml")
#         assert file_contains_text(f"{result.project_path}/.github/workflows/on-release-main.yml", "mkdocs gh-deploy")
#         assert file_contains_text(f"{result.project_path}/Makefile", "docs:")
#         assert os.path.isdir(f"{result.project_path}/docs")


# def test_not_mkdocs(cookies, tmp_path):
#     # Given: A temporary directory and cookiecutter template
#     with run_within_dir(tmp_path):
#         # When: Baking the project with mkdocs disabled
#         result = cookies.bake(extra_context={"mkdocs": "n"})

#         # Then: Documentation files should not be created
#         assert result.exit_code == 0
#         assert is_valid_yaml(result.project_path / ".github" / "workflows" / "main.yml")
#         assert is_valid_yaml(result.project_path / ".github" / "workflows" / "on-release-main.yml")
#         assert not file_contains_text(
#             f"{result.project_path}/.github/workflows/on-release-main.yml", "mkdocs gh-deploy"
#         )
#         assert not file_contains_text(f"{result.project_path}/Makefile", "docs:")
#         assert not os.path.isdir(f"{result.project_path}/docs")


# def test_tox(cookies, tmp_path):
#     # Given: A temporary directory and cookiecutter template
#     with run_within_dir(tmp_path):
#         # When: Baking the project
#         result = cookies.bake()

#         # Then: tox.ini should be created
#         assert result.exit_code == 0
#         assert os.path.isfile(f"{result.project_path}/tox.ini")
#         assert file_contains_text(f"{result.project_path}/tox.ini", "[tox]")


# def test_dockerfile(cookies, tmp_path):
#     # Given: A temporary directory and cookiecutter template
#     with run_within_dir(tmp_path):
#         # When: Baking the project with dockerfile enabled
#         result = cookies.bake(extra_context={"dockerfile": "y"})

#         # Then: Dockerfile should be created
#         assert result.exit_code == 0
#         assert os.path.isfile(f"{result.project_path}/Dockerfile")


# def test_not_dockerfile(cookies, tmp_path):
#     # Given: A temporary directory and cookiecutter template
#     with run_within_dir(tmp_path):
#         # When: Baking the project with dockerfile disabled
#         result = cookies.bake(extra_context={"dockerfile": "n"})

#         # Then: Dockerfile should not be created
#         assert result.exit_code == 0
#         assert not os.path.isfile(f"{result.project_path}/Dockerfile")


# def test_codecov(cookies, tmp_path):
#     # Given: A temporary directory and cookiecutter template
#     with run_within_dir(tmp_path):
#         # When: Baking the project
#         result = cookies.bake()

#         # Then: codecov.yaml should be created
#         assert result.exit_code == 0
#         assert is_valid_yaml(result.project_path / ".github" / "workflows" / "main.yml")
#         assert os.path.isfile(f"{result.project_path}/codecov.yaml")
#         assert os.path.isfile(f"{result.project_path}/.github/workflows/validate-codecov-config.yml")


# def test_not_codecov(cookies, tmp_path):
#     # Given: A temporary directory and cookiecutter template
#     with run_within_dir(tmp_path):
#         # When: Baking the project with codecov disabled
#         result = cookies.bake(extra_context={"codecov": "n"})

#         # Then: codecov.yaml should not be created
#         assert result.exit_code == 0
#         assert is_valid_yaml(result.project_path / ".github" / "workflows" / "main.yml")
#         assert not os.path.isfile(f"{result.project_path}/codecov.yaml")
#         assert not os.path.isfile(f"{result.project_path}/.github/workflows/validate-codecov-config.yml")


# def test_remove_release_workflow(cookies, tmp_path):
#     # Given: A temporary directory and cookiecutter template
#     with run_within_dir(tmp_path):
#         # When: Baking the project with publish_to_pypi disabled and mkdocs enabled
#         result = cookies.bake(extra_context={"publish_to_pypi": "n", "mkdocs": "y"})

#         # Then: on-release-main.yml should be created
#         assert result.exit_code == 0
#         assert os.path.isfile(f"{result.project_path}/.github/workflows/on-release-main.yml")

#         # And: When baking the project with publish_to_pypi disabled and mkdocs disabled
#         result = cookies.bake(extra_context={"publish_to_pypi": "n", "mkdocs": "n"})

#         # Then: on-release-main.yml should not be created
#         assert result.exit_code == 0
#         assert not os.path.isfile(f"{result.project_path}/.github/workflows/on-release-main.yml")
