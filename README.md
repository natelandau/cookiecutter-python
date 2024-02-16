[![Automated Tests](https://github.com/natelandau/cookiecutter-python/actions/workflows/cookiecutter_test.yml/badge.svg)](https://github.com/natelandau/cookiecutter-python/actions/workflows/cookiecutter_test.yml)

# cookiecutter-python

Personal and opinionated Cookiecutter template for Python CLIs and libraries.

## Features

-   Packaging and dependency management with [Poetry](https://github.com/python-poetry/poetry)
-   Task running with [Poe the Poet](https://github.com/nat-n/poethepoet)
-   Linting and code formatting with [ruff](https://github.com/charliermarsh/ruff)
-   [pre-commit](https://pre-commit.com/) code linting with
    -   [ruff](https://github.com/charliermarsh/ruff)
    -   [mypy](https://github.com/python/mypy)
    -   [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks)
    -   [shellcheck](https://github.com/koalaman/shellcheck)
    -   [typos](https://github.com/crate-ci/typos)
-   Follows the [Conventional Commits](https://www.conventionalcommits.org/) standard to automate [Semantic Versioning](https://semver.org/) and [Keep A Changelog](https://keepachangelog.com/) with [Commitizen](https://github.com/commitizen-tools/commitizen)
-   Test coverage with [Coverage.py](https://github.com/nedbat/coveragepy)
-   Automated dependency updating with [Dependabot](https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/about-dependabot-version-updates)
-   Continuous integration with [GitHub Actions](https://docs.github.com/en/actions)

---

## Usage

### 1. Creating a new Python project

To create a new Python project with this template:

1. Install [Cookiecutter](https://cookiecutter.readthedocs.io/) in your [Python environment](https://github.com/pyenv/pyenv-virtualenv) with:
    ```sh
    pipx install cookiecutter
    ```
2. Create a new project with the following command:
    ```sh
    cookiecutter https://github.com/natelandau/cookiecutter-python.git
    ```
3. Initialize a new git repository in the project folder:
    ```sh
    git init
    ```
4. Go develop your project!

### Developing

1. Install project dependencies

    ```bash
    poetry install
    ```

2. Activate the Poetry virtual environment

    ```bash
    poetry shell
    ```
