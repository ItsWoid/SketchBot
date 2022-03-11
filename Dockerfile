FROM --platform=linux/amd64 python:3.10-slim

ENV PIP_NO_CACHE_DIR=false \
    POETRY_VIRTUALENVS_CREATE=false

RUN pip install -U poetry

WORKDIR /bot

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev

COPY . .

ENTRYPOINT ["python3"]
CMD ["-m", "bot"]