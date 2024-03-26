# Use the official Python base image
FROM python:{{ cookiecutter.python_version }}

# Install Apt Packages
# RUN apt-get update && apt-get install -y XXXXXXX

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Poetry
RUN pip install poetry

# Install dependencies and script
RUN poetry install --without dev,test

# Set the entrypoint to run the script
ENTRYPOINT ["poetry", "run", "{{ cookiecutter.__package_name_kebab_case }}"]
