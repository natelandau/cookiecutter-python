"""Custom errors for {{ cookiecutter.package_name }}."""


class MissingConfigurationError(Exception):
    """Raised when a configuration variable is missing."""

    def __init__(
        self,
        msg: str | None = None,
        e: Exception | None = None,
        *args: str | int,
        **kwargs: int | str | bool,
    ):
        if not msg:
            msg = "A configuration variable is missing."
        else:
            msg = f"A configuration variable is missing: {msg}"

        if e:
            msg += f"\nRaised from: {e.__class__.__name__}: {e}"

        super().__init__(msg, *args, **kwargs)
