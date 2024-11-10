"""Validate the cookiecutter context."""

import sys

project_name = "{{cookiecutter.project_name}}"
if not project_name:
    print("ERROR: The app name is required")
    sys.exit(1)

author_email = "{{cookiecutter.author_email}}"
if not author_email:
    print("ERROR: The author email is required")
    sys.exit(1)

author_name = "{{cookiecutter.author_name}}"
if not author_name:
    print("ERROR: The author name is required")
    sys.exit(1)
