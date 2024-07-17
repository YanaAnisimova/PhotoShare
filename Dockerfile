FROM python:3.11-slim-buster

    # to make Python avoid to write .pyc files on the import of source modules
ENV PYTHONDONTWRITEBYTECODE=1 \
    # allows for log messages to be immediately dumped to the stream instead of being buffered.
    # This is useful for receiving timely log messages and avoiding situations where the application
    # crashes without emitting a relevant message due to the message being "stuck" in a buffer.
    PYTHONUNBUFFERED=1 \
    \
    # Poetry
    # make poetry install to this location
    POETRY_HOME="/opt/poetry" \
    # Create a virtual env in the project's root ($PYSETUP_PATH) it gets named `.venv`.
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    \
    # paths
    # this is where our requirements + virtual environment will live
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# adding poetry and venv to PATH,
# without it calling poetry would be '${POETRY_HOME}/bin/poetry ...', not 'poetry ...', and dependencies - 'poetry run gunicorn ...', not 'gunicorn ...'
ENV PATH="${VENV_PATH}/bin:${POETRY_HOME}/bin:${PATH}"


# installing Poetry
# If you install Poetry via pip, ensure you have Poetry installed into an isolated environment
# that is not the same as the target environment managed by Poetry.
# Otherwise, Poetry is likely to upgrade or uninstall its own dependencies
RUN python3 -m venv $POETRY_HOME && \
    $POETRY_HOME/bin/pip install poetry==1.4.2


WORKDIR $PYSETUP_PATH

COPY poetry.lock pyproject.toml ./

# by defaulf installing dependencies in /root/.cache/pypoetry/virtualenvs
RUN poetry install

WORKDIR /app




#####################################################################
#COPY entrypoint.sh /entrypoint.sh
## the chmod command is used to change the permissions of files and directories. The x option specifically sets
## the execute permission on a file, allowing it to be run as a program.
#RUN chmod +x /entrypoint.sh
## used to configure the executables that will always run after the container is initiated
#ENTRYPOINT ["/entrypoint.sh"]


# install psycopg dependencies
#RUN apt-get update && apt-get install -y --no-install-recommends  \
#    build-essential  \
#    libpq-dev && \
#    rm -rf /var/lib/apt/lists/*

