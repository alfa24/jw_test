FROM python:3.9

WORKDIR /var/app

ENV FETCH_PACKAGES="wget gnupg2" \
    BUILD_PACKAGES="build-essential autoconf libtool pkg-config \
    gcc linux-headers-amd64 libffi-dev libgeos-c1v5 libpq-dev libssl-dev python3-dev libgnutls28-dev" \
    PACKAGES="postgresql-client" \
    POETRY_VIRTUALENVS_CREATE="false"

RUN apt update && \
    apt install -y ${FETCH_PACKAGES}

RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main" > /etc/apt/sources.list.d/pgdg.list && \
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

RUN apt update && \
    apt upgrade -y && \
    apt install -y --no-install-recommends ${BUILD_PACKAGES} ${PACKAGES} && \
    pip install poetry && \
    rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock entrypoint.sh ./
RUN poetry install --no-interaction --no-ansi --no-dev

ADD src/ /var/app

RUN ["chmod", "+x", "./entrypoint.sh"]
ENTRYPOINT ["/var/app/entrypoint.sh"]
