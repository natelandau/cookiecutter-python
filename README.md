[![Test Cruft Create](https://github.com/natelandau/cookiecutter-python/actions/workflows/cruft-test.yml/badge.svg)](https://github.com/natelandau/cookiecutter-python/actions/workflows/cruft-test.yml)

# cookiecutter-python

Personal and opinionated Cookiecutter template for Python projects based largely on the great work from [radix-ai](https://github.com/radix-ai/poetry-cookiecutter) and [inovintell](https://github.com/inovintell/py-template).

## Features

-   Quick and reproducible development environments with VS Code's [Dev Containers](https://code.visualstudio.com/docs/remote/containers)
-   Packaging and dependency management with [Poetry](https://github.com/python-poetry/poetry)
-   Task running with [Poe the Poet](https://github.com/nat-n/poethepoet)
-   Code formatting with [black](https://github.com/psf/black)
-   [pre-commit](https://pre-commit.com/) code linting with
    -   [ruff](https://github.com/charliermarsh/ruff)
    -   [mypy](https://github.com/python/mypy)
    -   [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks)
    -   [shellcheck](https://github.com/koalaman/shellcheck)
-   Follows the [Conventional Commits](https://www.conventionalcommits.org/) standard to automate [Semantic Versioning](https://semver.org/) and [Keep A Changelog](https://keepachangelog.com/) with [Commitizen](https://github.com/commitizen-tools/commitizen)
-   Test coverage with [Coverage.py](https://github.com/nedbat/coveragepy)
-   Scaffolding upgrades with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and [Cruft](https://github.com/cruft/cruft)
-   Automated dependency updating with [Dependabot](https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/about-dependabot-version-updates)
-   Verified commits with [GPG](https://gnupg.org/)
-   Continuous integration with [GitHub Actions](https://docs.github.com/en/actions)

---

## Usage

### 1. Creating a new Python project

To create a new Python project with this template:

1. Install [Cruft](https://cruft.github.io/cruft/) in your [Python environment](https://github.com/pyenv/pyenv-virtualenv) with:
    ```sh
    pip install cruft
    ```
2. Create a new repository and clone it locally.
3. Ensure an ssh key is available to the dev container. [(Link)] (https://code.visualstudio.com/docs/remote/containers#_using-ssh-keys) Or that a [credential helper](https://code.visualstudio.com/docs/remote/containers#_using-ssh-keys) is enabled.
4. Ensure an authorized Github token is available as an `env` variable named `GITHUB_TOKEN`
5. In the **repository's parent directory**, run:
    ```sh
    cruft create -f https://github.com/natelandau/cookiecutter-python.git
    ```
6. If using a pre-existing directory, when asked by Cruft during install, ensure `package_name` is exactly the same as the directory name.

### 2. Updating your Python project

To update your Python project with the latest template:

1. Run `cruft update` within the project folder to update your project with the latest template.
2. If any of the updates failed, resolve them by inspecting the generated `.rej` files.

# Developing

1. Activate the Poetry virtual environment

    ```bash
    poetry shell
    ```

2. Run Cruft against local changes. Note, only changes committed to git are reflected.
    ```sh
    cruft create -f /path/to/local/folder
    ```
