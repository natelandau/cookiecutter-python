# Cookiecutter Python CLI Template

[![Automated Tests](https://github.com/natelandau/cookiecutter-python/actions/workflows/main.yml/badge.svg)](https://github.com/natelandau/cookiecutter-python/actions/workflows/main.yml) [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://github.com/natelandau/cookiecutter-python/blob/master/LICENSE) [![Changelog](https://img.shields.io/github/v/tag/natelandau/cookiecutter-python)](https://github.com/natelandau/cookiecutter-python/tags)

Opinionated [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for creating Python CLI applications with [Typer](https://typer.tiangolo.com/) and [uv](https://github.com/astral-sh/uv).

## Features

-   Packaging and dependency management with [uv](https://github.com/astral-sh/uv)
-   Task running with [Poe the Poet](https://github.com/nat-n/poethepoet)
-   Linting and code formatting with [ruff](https://github.com/charliermarsh/ruff)
-   Type checking with [mypy](https://github.com/python/mypy)
-   Spell checking with [typos](https://github.com/crate-ci/typos)
-   Pre-commit hooks with [pre-commit](https://pre-commit.com/)
-   Automated testing with [GitHub Actions](https://docs.github.com/en/actions)
-   Code coverage with [codecov](https://about.codecov.io/)
-   Optional publishing as a package to PyPI and a Docker image to GitHub Container Registry via GitHub Actions
-   Follows the [Conventional Commits](https://www.conventionalcommits.org/) standard to automate [Semantic Versioning](https://semver.org/) and [Keep A Changelog](https://keepachangelog.com/) with [Commitizen](https://github.com/commitizen-tools/commitizen)
-   Automated dependency updating with [Dependabot](https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/about-dependabot-version-updates)

---

## Usage

To create a new Python project with this template:

```bash
uvx cookiecutter https://github.com/natelandau/cookiecutter-python.git
```

If you don't have [uv](https://github.com/astral-sh/uv) or [Cookiecutter](https://github.com/cookiecutter/cookiecutter) installed, then run the following two commands.

```bash
pip install cookiecutter
cookiecutter https://github.com/natelandau/cookiecutter-python.git
```

Once installed, run the following to install the project dependencies and activate the virtual environment:

```bash
uv sync
source .venv/bin/activate
```

Enjoy!
