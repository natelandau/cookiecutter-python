# Use a Python image with uv pre-installed
FROM ghcr.io/astral-sh/uv:python{{ cookiecutter.python_version }}-bookworm-slim

# Set labels
{%- if cookiecutter.github_username %}
LABEL org.opencontainers.image.source=https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated }}
LABEL org.opencontainers.image.description="{{ cookiecutter.description or "" }}"
LABEL org.opencontainers.image.licenses=Apache-2.0
LABEL org.opencontainers.image.url=https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated }}
LABEL org.opencontainers.image.title="{{ cookiecutter.hyphenated }}"
{%- endif %}

# Install the project into `/app`
WORKDIR /app

# Install git and tzdata
RUN apt-get update && apt-get install -y git tzdata

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy

# Install the project's dependencies using the lockfile and settings
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

# Then, add the rest of the project source code and install it
# Installing separately from its dependencies allows optimal layer caching
COPY . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

# Reset the entrypoint, don't invoke `uv`
ENTRYPOINT []

# Run the valentina by default
CMD ["uv", "run", "{{ cookiecutter.hyphenated }}"]
