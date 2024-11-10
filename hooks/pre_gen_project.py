"""Validate the cookiecutter context."""

import sys

app_name = "{{cookiecutter.app_name}}"
if not app_name:
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
