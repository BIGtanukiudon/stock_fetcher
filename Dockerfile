FROM python:3.12-slim

RUN apt-get update &&\
    apt-get -y install locales curl &&\
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm
ENV BUF_PREFIX /usr/local
ENV BUF_VERSION 1.36.0

RUN pip install --upgrade pip
RUN curl -sSL https://install.python-poetry.org | python -

ENV PATH /root/.local/bin:$PATH

# buf cli install
RUN curl -sSL \
"https://github.com/bufbuild/buf/releases/download/v${BUF_VERSION}/buf-$(uname -s)-$(uname -m).tar.gz" | \
tar -xvzf - -C "${BUF_PREFIX}" --strip-components 1

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
COPY ./src/ /app/src/

# COPY main.py pyproject.toml poetry.lock scripts/ /app/
# RUN poetry install --no-dev