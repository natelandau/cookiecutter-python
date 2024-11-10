# Cookiecutter Python CLI Template

[![Automated Tests](https://github.com/natelandau/cookiecutter-python/actions/workflows/main.yml/badge.svg)](https://github.com/natelandau/cookiecutter-python/actions/workflows/main.yml) [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://github.com/natelandau/cookiecutter-python/blob/master/LICENSE) [![Changelog](https://img.shields.io/github/v/release/natelandau/cookiecutter-python?include_prereleases&label=changelog)](https://github.com/natelandau/cookiecutter-python/releases)

Personal and opinionated [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for creating Python CLI applications with [Typer](https://typer.tiangolo.com/) and [uv](https://github.com/astral-sh/uv).

## Features

-   Packaging and dependency management with [uv](https://github.com/astral-sh/uv)
-   Task running with [Poe the Poet](https://github.com/nat-n/poethepoet)
-   Linting and code formatting with [ruff](https://github.com/charliermarsh/ruff)
-   [pre-commit](https://pre-commit.com/) code linting with
    -   [ruff](https://github.com/charliermarsh/ruff)
    -   [mypy](https://github.com/python/mypy)
    -   [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks)
    -   [shellcheck](https://github.com/koalaman/shellcheck)
    -   [typos](https://github.com/crate-ci/typos)
-   Follows the [Conventional Commits](https://www.conventionalcommits.org/) standard to automate [Semantic Versioning](https://semver.org/) and [Keep A Changelog](https://keepachangelog.com/) with [Commitizen](https://github.com/commitizen-tools/commitizen)
-   Automated dependency updating with [Dependabot](https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/about-dependabot-version-updates)
-   Continuous integration with [GitHub Actions](https://docs.github.com/en/actions)

---

## Usage

To create a new Python project with this template:

```bash
uvx cookiecutter https://github.com/natelandau/cookiecutter-python.git
```

If you don't have uv installed, then run the following two commands.

```bash
pip install cookiecutter
cookiecutter https://github.com/natelandau/cookiecutter-python.git
```

Then run the following to install the project dependencies and activate the virtual environment:

```bash
uv sync
source .venv/bin/activate
```

Enjoy!
