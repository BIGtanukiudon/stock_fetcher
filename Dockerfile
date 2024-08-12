FROM python:3.12-slim

RUN apt-get update &&\
    apt-get -y install locales curl &&\
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN pip install --upgrade pip
RUN curl -sSL https://install.python-poetry.org | python -

ENV PATH /root/.local/bin:$PATH

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
COPY ./src/ /app/src/

# COPY main.py pyproject.toml poetry.lock scripts/ /app/
# RUN poetry install --no-dev