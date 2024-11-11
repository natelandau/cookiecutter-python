# {{cookiecutter.project_name}}

{% if cookiecutter.publish_to_pypi == "y" %}[![PyPI](https://badge.fury.io/py/{{ cookiecutter.hyphenated }}.svg)](https://badge.fury.io/py/{{ cookiecutter.hyphenated }}) ![Python Versions](https://img.shields.io/pypi/pyversions/{{ cookiecutter.hyphenated }}){% endif %}{% if cookiecutter.github_username %} [![Changelog](https://img.shields.io/github/v/release/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated }}?include_prereleases&label=changelog)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated }}/releases) [![Tests](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated }}/actions/workflows/tests.yml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated }}/actions/workflows/tests.yml) [License](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated }}/blob/master/LICENSE){% endif %}

{{cookiecutter.description}}

# Installation

Note: {{cookiecutter.project_name}} requires Python {{cookiecutter.python_version}} or higher.

Recommended installation with [pipx](https://pipx.pypa.io/)

```bash
pipx install {{cookiecutter.project_name}}
```

If pipx is not an option, you can install {{cookiecutter.project_name}} in your Python user directory.

```bash
python -m pip install --user {{cookiecutter.project_name}}
```

# Usage

```bash
{{cookiecutter.project_name}} --help
```

# Contributing

## Setup

1. Install [uv](https://docs.astral.sh/uv/)
2. Clone this repository `git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}.git`
3. Install dependencies `uv sync`
4. Activate pre-commit hooks `uv run pre-commit install`

## Development

-   Run the development version of the project `uv run {{cookiecutter.project_name}}`
-   Run tests `uv run poe test`
-   Run linting `uv run poe lint`
-   Enter the virtual environment with `source .venv/bin/activate`
-   Add or remove dependencies with `uv add/remove <package>`
-   Upgrade dependencies with `uv run poe upgrade`
