## v0.4.0 (2023-01-21)

### Feat

- **workflows**: add autorelease github action
- **actions**: bump harden security to 2.1.0

### Fix

- add pypi release workflow
- remove unnecessary `src` prefix in imports
- **extensions**: use `Chouzz.vscode-better-align` extension
- venvs in project
- add package name to --version

## v0.3.0 (2022-12-19)

### Feat

- migrate from flake8 to ruff
- **linters**: improve linting
- **dev_container**: add Gitlens extension

### Fix

- remove duplicate key
- **pre-commit**: revert flake8 changes. run only on changed files
- **git**: lint when updating dependencies

## v0.2.0 (2022-11-18)

### Feat

- Major update for devcontainers and preferred cli options

### Fix

- add cruft v2.11.0
- remove cruft to allow using typer 0.6.1
- remove typed.py
- **improve-accessing-cli-apps-with-docker-compose**: Can now run 'docker compose run --rm cli'

## v0.1.1 (2022-07-28)

### Fix

- **ci**: fix minor bugs keeping Github CI from succeeding
- fix test file import
- rename code directory to 'src/'
- use src/ as base code dir
- **CI**: fix Github test workflow

## v0.1.0 (2022-07-27)

### Fix

- pass linting

### Refactor

- Fix VSCode dev container
- Add CLI dependencies
- bugfix json
- remove unused options

### Feat

- initial commit
