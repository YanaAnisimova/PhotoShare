FROM python:3.11-slim-buster

# the python output i.e. the stdout and stderr streams are sent straight to terminal
# (e.g. your container log) without being first buffered and that you can see the output
# of your application (e.g. django logs) in real time. is mainly a concern of getting as much information
# from your running application as fast as possible in the container log and not loosing anything
# in case of a crash.
ENV PYTHONUNBUFFERED 1

# install psycopg dependencies
#RUN apt-get update && apt-get install -y --no-install-recommends  \
#    build-essential  \
#    libpq-dev && \
#    rm -rf /var/lib/apt/lists/*

# installing Poetry
# If Poetry and your project are installed into the same environment,
# Poetry is likely to upgrade or uninstall its own dependencies
ENV POETRY_HOME=/opt/poetry
RUN python3 -m venv $POETRY_HOME && \
    $POETRY_HOME/bin/pip install poetry==1.4.2

# without it calling poetry would be '${POETRY_HOME}/bin/poetry ...', not 'poetry ...'
ENV PATH="${POETRY_HOME}/bin:${PATH}"

# Create a virtual env in home directory.
# Otherwise calling to dependencies would be 'poetry run gunicorn ...', not 'gunicorn ...'
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV VIRTUAL_ENV=/home/.venv
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"

WORKDIR /home

COPY pyproject.toml .
COPY poetry.lock .

# by defaulf installing dependencies in /root/.cache/pypoetry/virtualenvs
RUN poetry install

WORKDIR /app

#COPY entrypoint.sh /entrypoint.sh
## the chmod command is used to change the permissions of files and directories. The x option specifically sets
## the execute permission on a file, allowing it to be run as a program.
#RUN chmod +x /entrypoint.sh
## used to configure the executables that will always run after the container is initiated
#ENTRYPOINT ["/entrypoint.sh"]

